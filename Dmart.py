import warnings
warnings.filterwarnings('ignore')
from selenium import webdriver
import time 
import pandas as pd 
import sys 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import numpy as np
import re 
from datetime import datetime

# Record the start time
start_time = time.time()
options = Options()
options.add_experimental_option('excludeSwitches',['enable-logging'])

################################################################################################################################################
chrome_drive = r"chromedriver.exe"
filter_title = []
################################################################################################################################################

wd = webdriver.Chrome(chrome_drive,chrome_options=options)
wd.maximize_window()

def has_page_scrolled():
    return wd.execute_script("return window.pageYOffset;")
items = {
    "Grocery": 'https://www.dmart.in/category/grocery-aesc-grocerycore',
    'Dairy' : 'https://www.dmart.in/category/dairy---beverages-aesc-dairyandbeveragescore',
    'Dmart_Grocery' : 'https://www.dmart.in/category/dmart-grocery-aesc-dmartgrocerycore',
    'Packed_food' : 'https://www.dmart.in/category/packaged-food-aesc-packagedfoodcore',
    'Fruits_vegetables' : 'https://www.dmart.in/category/fruits---vegetables-aesc-fruitsandvegetablescore',
    'Baby_care' : 'https://www.dmart.in/category/baby---kids-aesc-babyandkidscore',
    'Cosmetics' : 'https://www.dmart.in/category/beauty---cosmetics',
    'Home_Kitchen' : 'https://www.dmart.in/category/home---kitchen-aesc-homeandkitchencore',
    'Personal_care' : 'https://www.dmart.in/category/personal-care-aesc-personalcarecore',
    'Footwear' : 'https://www.dmart.in/category/aesc--footwear',
    'Schoolsupply' : 'https://www.dmart.in/category/school-supplies',
    'Electric_Appliance' : 'https://www.dmart.in/category/appliances-aesc-appliancescore',
    'Clothing' : 'https://www.dmart.in/category/clothing-accessories-aesc-clothingaccessories',
    'Special' : 'https://www.dmart.in/category/specials-aesc-specialscore',   
}


final_df = pd.DataFrame({'Date','Item','Sale Price'})

#url = 'https://www.dmart.in/category/dairy-aesc-dairy'
custom_scroll_count = 1
for item, url in items.items():
    date = []
    product_name = []
    product_price = []
    product_qty = []
    product_link = []
    print(f"{item}")

    try:
        wd.get(url)
        time.sleep(1)
        for _ in range(custom_scroll_count):
            wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
        type_lists = wd.find_element_by_class_name('product-grid_gridContainerDiv__9KSkq')
        product_lists = wd.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/div[2]/div/div/div[3]')
        lists = product_lists.find_elements(By.TAG_NAME, "div")
        #__next > div.layout_container__ojOIi > main > div > div > div.common_content-container__CoI4k > div > div > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-1.mui-style-tuxzvu
        #__next > div.layout_container__ojOIi > main > div > div > div.common_content-container__CoI4k > div > div > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-1.mui-style-tuxzvu > div:nth-child(1)
        #__next > div.layout_container__ojOIi > main > div > div > div.common_content-container__CoI4k > div > div > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-1.mui-style-tuxzvu > div:nth-child(2)
        
        for list in lists:
            # mrp_element = list.find_element(By.XPATH, './/p[contains(text(), "MRP")]/following-sibling::p[@class="vertical-card_value__HM5of"]/span[@class="vertical-card_amount__muVeb"]')
            # dmart_price_element = list.find_element(By.XPATH, './/p[contains(text(), "DMart")]/following-sibling::p[@class="vertical-card_value__HM5of"]/span[@class="vertical-card_amount__muVeb"]')
            # product_name_element = list.find_element(By.XPATH, './/div[@class="vertical-card_title__awihj"]')

            current_date = datetime.now().date()
            date.append(current_date)
            try:
                product_name0 = list.find_element(By.XPATH, './/div[@class="vertical-card_title__awihj"]').text
                product_name.append(product_name0)
                
            except:
                product_name.append('')
                pass
            try:
                product_price0 = list.find_element(By.XPATH, './/p[contains(text(), "DMart")]/following-sibling::p[@class="vertical-card_value__HM5of"]/span[@class="vertical-card_amount__muVeb"]').text
                product_price0 = product_price0.upper().replace('₹','').replace('DMART','').strip()
                product_price.append(product_price0)
            except:
                product_price.append('')
                pass
            # try:
            #     mrp_price0 = list.find_element(By.XPATH, './/p[contains(text(), "DMart")]/following-sibling::p[@class="vertical-card_value__HM5of"]/span[@class="vertical-card_amount__muVeb"]').text
            #     mrp_price0 = product_price0.upper().replace('₹','').replace('DMART','').strip()
            #     mrp_price.append(mrp_price0)
            # except:
            #     mrp_price.append('')
            #     pass
            
        dmart = pd.DataFrame({'Date': date,'Item': product_name,'Sale Price': product_price})
        final_df = pd.concat([final_df, dmart ], ignore_index=True)


    except Exception as e:
        print(e)


final_df.to_csv(f"D_mart.csv_{item}", index=False)
wd.close()
# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print("Elapsed time:", elapsed_time, "seconds")
print('Extraction Completed!!!')

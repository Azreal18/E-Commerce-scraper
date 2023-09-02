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
    "Grocery": 'https://www.jiomart.com/c/groceries/2',
    'Premium_fruits' : 'https://www.jiomart.com/c/premiumfruits/6047',
    'Home_kitchen' : 'https://www.jiomart.com/c/homeandkitchen/8582',
    'Fashion' : 'https://www.jiomart.com/c/fashion/3',
    'Electronics' : 'https://www.jiomart.com/c/electronics/4',
    'Cosmetics' : 'https://www.jiomart.com/c/beauty/5',
    'Home' : 'https://www.jiomart.com/c/homeimprovement/8583',
    'Toys_etc' : 'https://www.jiomart.com/c/sportstoysluggage/8584',
    
}
final_df = pd.DataFrame({'Date','Item','QTY & price','Price','Link'})

# url = 'https://www.jiomart.com/c/groceries/dairy-bakery/61?prod_mart_groceries_products_popularity%5Bpage%5D=84'
custom_scroll_count = 25    #3 products in a line so accordingly change it 
for item, url in items.items():
    date = []
    product_name = []
    product_price = []
    product_link = []
    print(f"{item}")
    finaldf = pd.DataFrame(columns =['Date','Item','QTY & price','Price','Link'])

    try:
        wd.get(url)
        # Wait for the 'Show more results' button to be visible
        time.sleep(2)

        for _ in range(custom_scroll_count):
            print(_)
            wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3) 
        prod_list = wd.find_element_by_class_name('ais-InfiniteHits')
        product_lists = prod_list.find_element_by_css_selector('#algolia_hits > div > div > ol')
        lists = product_lists.find_elements_by_tag_name("li")
        for product in lists: 
            current_date = datetime.now().date()
            date.append(current_date)
            try:
                product_name0 = product.find_element_by_css_selector("div.plp-card-container > div.plp-card-details-wrapper > div > div.plp-card-details-name.line-clamp.jm-body-xs.jm-fc-primary-grey-80").text
            except:
                product_name0 =''
            product_name.append(product_name0)

            try:
                product_price0 = product.find_element_by_class_name('plp-card-details-price').text
                product_price01 = product_price0.split(' ')
                if product_price01:
                    product_price0 = product_price01[0]

                else:
                    product_price0
                product_price0 = product_price0.replace('₹','').strip()
            except:
                product_price0 = ''
            product_price.append(product_price0)


            product_link0 = product.find_element_by_css_selector('a').get_attribute('href')
            product_link.append(product_link0)

        jio_mart = pd.DataFrame({'Date': date,'Item': product_name,'Price': product_price,'Link': product_link})
        final_df = pd.concat([final_df, jio_mart], ignore_index=True)


    except Exception as e:
        print(e)



final_df.to_csv(f"Jio_Mart.csv", index=False)
wd.close()
# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print("Elapsed time:", elapsed_time, "seconds")
print('Extraction Completed!!!')

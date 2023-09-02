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
# excel = r""
# state = "Bengaluru"
# role = "Data Scientist"
filter_title = []
################################################################################################################################################

wd = webdriver.Chrome(chrome_drive,chrome_options=options)
wd.maximize_window()
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

#9*4 per page 
page = 1
# url = f"https://www.bigbasket.com/pc/fruits-vegetables/fresh-vegetables/?page={page}"
url = f'https://www.bigbasket.com/pc/bakery-cakes-dairy/dairy/?nc=nb?page={page}'
items = {
    "Fruits": f'https://www.bigbasket.com/cl/fruits-vegetables/?nc=nb&page={page}',
    "Grains": f"https://www.bigbasket.com/cl/foodgrains-oil-masala/?nc=nb&page={page}",
    "Dairy": f'https://www.bigbasket.com/cl/bakery-cakes-dairy/?nc=nb&page={page}',
    "Beverage": f'https://www.bigbasket.com/cl/beverages/?nc=nb&page={page}',
    "Snack": f'https://www.bigbasket.com/cl/snacks-branded-foods/?nc=nb&page={page}',
    "Beauty": f'https://www.bigbasket.com/cl/beauty-hygiene/?nc=nb&page={page}',
    "Cleaning" : f'https://www.bigbasket.com/cl/cleaning-household/?nc=nb&page={page}',
    'Biscuits' :f'https://www.bigbasket.com/cl/kitchen-garden-pets/?nc=nb&page={page}',
    'Eggs' : f'https://www.bigbasket.com/cl/eggs-meat-fish/?nc=nb&page={page}',
    'Gourment' : f'https://www.bigbasket.com/cl/gourmet-world-food/?nc=nb&page={page}',
    'Baby care' : f'https://www.bigbasket.com/cl/baby-care/?nc=nb&page={page}'
}
final_df =  pd.DataFrame({'Date','Item','QTY & price','Price','Link'})

def keep_only_numbers(input_string):
    regex_pattern = r'\d+'
    numbers_only = ''.join(re.findall(regex_pattern, input_string))
    return numbers_only
i = 1
for item, url in items.items():
    print(item)
    try:
        date = []
        product_name = []
        product_price = []
        product_qty = []
        product_link = []
        wd.get(url)
        # times = wd.find_element_by_xpath('//*[@id="jserp-filters"]/ul/li[1]/div/div/button')
        # wd.execute_script("arguments[0].click();", times)
        time.sleep

        try:
            no_jobs = wd.find_element_by_css_selector('#dynamicDirective > product-deck > section > div.col-md-9.wid-fix.clearfix.pl-wrap > div.col-xs-12.product-deck-container.pad-0 > div.ng-isolate-scope > div > div > div:nth-child(2) > div')
        except:
            time.sleep(5)
        finally:
            no_jobs = wd.find_element_by_css_selector('#dynamicDirective > product-deck > section > div.col-md-9.wid-fix.clearfix.pl-wrap > div.col-xs-12.product-deck-container.pad-0 > div.ng-isolate-scope > div > div > div:nth-child(2) > div')
        
        no = wd.find_element_by_xpath('//*[@id="deck"]/div[2]/div/h2').text
        no = keep_only_numbers(no)
        print(f'Total products = {no}')
        con = int(int(no)/36)+1
        print(f'Scroll count = {con}')
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        while i <= con:
            i = i + 1
            
            more = wd.find_element_by_xpath('//*[@id="dynamicDirective"]/product-deck/section/div[2]/div[4]/div[3]/button')
            wd.execute_script("arguments[0].scrollIntoView();", more)
            try:
                more.click()
            except:
                pass
            # print(i)
            time.sleep(3)
        product_lists = wd.find_element_by_class_name('items')
        lists = product_lists.find_elements_by_xpath("//div[@qa='product']")
        for product in lists: 
            current_date = datetime.now().date()
            date.append(current_date)

            product_name0 = product.find_element_by_css_selector("product-template > div > div:nth-child(4) > div.col-sm-12.col-xs-7.prod-name").text
            product_name0 = product_name0.replace('Fresho','').strip()
            product_name.append(product_name0)
            #dynamicDirective > product-deck > section > div.col-md-9.wid-fix.clearfix.pl-wrap > div.col-xs-12.product-deck-container.pad-0 > div.ng-isolate-scope > div > div > div:nth-child(2) > div > div:nth-child(2) > product-template > div > div:nth-child(4) > div.col-sm-12.col-xs-7.prod-name
            
            wait_time = 1
            dropdown_button_locator = (By.XPATH, "//div[@class='btn-group btn-input clearfix ng-scope']")
            dropdown_button = WebDriverWait(wd, wait_time).until(EC.visibility_of_element_located(dropdown_button_locator))
            default_text = dropdown_button.text.strip()
            product_qty.append(default_text)

            
            product_price0 = product.find_element_by_css_selector("div.col-sm-12.col-xs-12.add-bskt > div > div.po-markup > h4 > span.discnt-price").text
            product_price.append(product_price0)

            product_link0 = product.find_element_by_css_selector('a').get_attribute('href')
            product_link.append(product_link0)

        big_basket = pd.DataFrame({'Date': date,'Item': product_name,'QTY & price': product_qty,'Price': product_price,'Link': product_link})
        final_df = pd.concat([final_df, big_basket], ignore_index=True)





    except Exception as e:
        print(e)
final_df.to_csv(f"Bigbasket_.csv", index=False)

wd.close()
# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print("Elapsed time:", elapsed_time, "seconds")
print('Extraction Completed!!!')

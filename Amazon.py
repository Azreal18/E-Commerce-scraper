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

options = Options()
options.add_experimental_option('excludeSwitches',['enable-logging'])

################################################################################################################################################
chrome_drive = r"chromedriver.exe"
filter_title = []
################################################################################################################################################

wd = webdriver.Chrome(chrome_drive,chrome_options=options)
wd.maximize_window()

url = 'https://www.amazon.in/alm/category/ref=s9_acss_ot_cg_SBCT14_3c1_w?almBrandId=ctnow&node=16984555031&ref=fs_dsk_sn_dairybread&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=alm-storefront-desktop-dram-top-1&pf_rd_r=4NKGRZR82RYRE6Y0MS6Q&pf_rd_t=0&pf_rd_p=11c9a545-5512-471d-961b-a0d9adf4adc3&pf_rd_i=FMCDummyValue'
wa
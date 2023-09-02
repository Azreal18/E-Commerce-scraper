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

def has_page_scrolled():
    return wd.execute_script("return window.pageYOffset;")
import time

# Record the start time
start_time = time.time()


items = {
    "DAL": 'https://www.flipkart.com/grocery/staples/dals-pulses/pr?sid=73z,bpe,3uv&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_377b9267-df57-4248-beab-8b38f5d00e75_2_G211C67CJ4GB_MC.O1V4G01H9SMV&otracker=clp_rich_navigation_1_2.navigationCard.RICH_NAVIGATION_Staples~Dals%2B%2526%2BPulses~All_grocery-supermart-store_O1V4G01H9SMV&otracker1=clp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L2_view-all&cid=O1V4G01H9SMV',
    "DAIRY": "https://www.flipkart.com/grocery/staples/ghee-oils/pr?sid=73z,bpe,4wu&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_377b9267-df57-4248-beab-8b38f5d00e75_2_G211C67CJ4GB_MC.QW9A7WPEBLP6&otracker=clp_rich_navigation_2_2.navigationCard.RICH_NAVIGATION_Staples~Ghee%2B%2526%2BOils_grocery-supermart-store_QW9A7WPEBLP6&otracker1=clp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L1_view-all&cid=QW9A7WPEBLP6",
    "Flour": 'https://www.flipkart.com/grocery/staples/atta-flours/pr?sid=73z,bpe,9da&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_10705c0f-0ffe-4362-87ff-af99afb6ff07_2_G211C67CJ4GB_MC.ZWBFCX62G9LP&otracker=clp_rich_navigation_3_2.navigationCard.RICH_NAVIGATION_Staples~Atta%2B%2526%2BFlours_grocery-supermart-store_ZWBFCX62G9LP&otracker1=clp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L1_view-all&cid=ZWBFCX62G9LP',
    "RICE": 'https://www.flipkart.com/grocery/staples/rice-rice-products/pr?sid=73z,bpe,zwp&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_dae8e699-823b-409f-bb51-7484d413f2b6_2_G211C67CJ4GB_MC.GQEJYG9UMBCO&otracker=clp_rich_navigation_5_2.navigationCard.RICH_NAVIGATION_Staples~Rice%2B%2526%2BRice%2BProducts_grocery-supermart-store_GQEJYG9UMBCO&otracker1=clp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_5_L1_view-all&cid=GQEJYG9UMBCO',
    "Spices": 'https://www.flipkart.com/grocery/staples/masalas-spices/pr?sid=73z,bpe,a6m&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_d4d19340-ba22-4baa-8ebc-3820433e9613_2_G211C67CJ4GB_MC.QFQ3Q4E8ZB2I&otracker=dynamic_rich_navigation_4_2.navigationCard.RICH_NAVIGATION_Staples~Masalas%2B%2526%2BSpices_QFQ3Q4E8ZB2I&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_4_L1_view-all&cid=QFQ3Q4E8ZB2I',
    "DRY Fruits": 'https://www.flipkart.com/grocery/staples/dry-fruits-nuts-seeds/pr?sid=73z,bpe,dtp&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_baff499e-60be-4324-bd6a-eff1d6c705e1_2_G211C67CJ4GB_MC.X697907L5MB0&otracker=dynamic_rich_navigation_6_2.navigationCard.RICH_NAVIGATION_Staples~Dry%2BFruits%252C%2BNuts%2B%2526%2BSeeds_X697907L5MB0&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_6_L1_view-all&cid=X697907L5MB0',
    "SUGAR" : 'https://www.flipkart.com/grocery/staples/sugar-jaggery-salt/pr?sid=73z,bpe,fdl&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_3daa32c1-f826-4fcb-9032-228341e3b1b6_2_G211C67CJ4GB_MC.XI6TQHBVLUGF&otracker=dynamic_rich_navigation_7_2.navigationCard.RICH_NAVIGATION_Staples~Sugar%252C%2BJaggery%2B%2526%2BSalt_XI6TQHBVLUGF&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_7_L1_view-all&cid=XI6TQHBVLUGF',
    'Biscuits' : 'https://www.flipkart.com/grocery/snacks-beverages/biscuits/pr?sid=73z,ujs,eb9&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_44d24d64-60e8-4558-84a5-c3f6fc2b7be0_2_G211C67CJ4GB_MC.AZ9TH6KGXIQX&otracker=dynamic_rich_navigation_1_2.navigationCard.RICH_NAVIGATION_Snacks%2B%2526%2BBeverages~Biscuits_AZ9TH6KGXIQX&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L1_view-all&cid=AZ9TH6KGXIQX',
    'Namkeen' : 'https://www.flipkart.com/grocery/snacks-beverages/chipsnamkeen-snacks/pr?sid=73z,ujs,dd9&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_a82cb6bd-020a-482d-bfd7-a3a3c97ef81f_2_G211C67CJ4GB_MC.ZTW4LDXW99L4&otracker=dynamic_rich_navigation_2_2.navigationCard.RICH_NAVIGATION_Snacks%2B%2526%2BBeverages~Chips%252CNamkeen%2B%2526%2BSnacks_ZTW4LDXW99L4&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L1_view-all&cid=ZTW4LDXW99L4',
    'Tea' : 'https://www.flipkart.com/grocery/snacks-beverages/tea/pr?sid=73z,ujs,amr&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_0e03a6c7-88ae-4f4a-b393-c1426e66979c_2_G211C67CJ4GB_MC.WGRAZWGDPE1W&otracker=dynamic_rich_navigation_3_2.navigationCard.RICH_NAVIGATION_Snacks%2B%2526%2BBeverages~Tea_WGRAZWGDPE1W&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L1_view-all&cid=WGRAZWGDPE1W',
    'Coffee' : 'https://www.flipkart.com/grocery/snacks-beverages/coffee/pr?sid=73z,ujs,t7k&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_5105f4d9-0bdc-4cb7-aca3-a9ca2ce9871a_2_G211C67CJ4GB_MC.098FWDWWR6ZV&otracker=dynamic_rich_navigation_4_2.navigationCard.RICH_NAVIGATION_Snacks%2B%2526%2BBeverages~Coffee_098FWDWWR6ZV&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_4_L1_view-all&cid=098FWDWWR6ZV',
    'Juices' : 'https://www.flipkart.com/grocery/snacks-beverages/juices/pr?sid=73z,ujs,afd&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_926dc29f-e493-4c45-a478-a043fcada111_2_G211C67CJ4GB_MC.W5PUVK1VCI95&otracker=dynamic_rich_navigation_5_2.navigationCard.RICH_NAVIGATION_Snacks%2B%2526%2BBeverages~Juices_W5PUVK1VCI95&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_5_L1_view-all&cid=W5PUVK1VCI95',
    'Bornvita' : 'https://www.flipkart.com/grocery/snacks-beverages/health-drink-mix/pr?sid=73z,ujs,vnq&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_9ec7afc2-254d-4e99-aa4a-af0629970a84_2_G211C67CJ4GB_MC.0UDCKV2OVSBR&otracker=dynamic_rich_navigation_6_2.navigationCard.RICH_NAVIGATION_Snacks%2B%2526%2BBeverages~Health%2BDrink%2BMix_0UDCKV2OVSBR&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_6_L1_view-all&cid=0UDCKV2OVSBR',
    'Soft_Drinks' : 'https://www.flipkart.com/grocery/snacks-beverages/soft-drinks/pr?sid=73z,ujs,dfw&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_73009128-d8bc-433f-b0d0-d7514d548e86_2_G211C67CJ4GB_MC.L6I5OTOPKRJ0&otracker=dynamic_rich_navigation_7_2.navigationCard.RICH_NAVIGATION_Snacks%2B%2526%2BBeverages~Soft%2BDrinks_L6I5OTOPKRJ0&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_7_L1_view-all&cid=L6I5OTOPKRJ0',
    'Syrups' : 'https://www.flipkart.com/grocery/snacks-beverages/squash-syrups/pr?sid=73z,ujs,iau&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_bdc84131-7ade-45e8-98eb-a9a91e8da560_2_G211C67CJ4GB_MC.X92O1TC1W20T&otracker=dynamic_rich_navigation_8_2.navigationCard.RICH_NAVIGATION_Snacks%2B%2526%2BBeverages~Instant%2BDrink%2BMixes%252C%2BSquash%2B%2526%2BSyrups_X92O1TC1W20T&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=X92O1TC1W20T',
    'Cereal' : 'https://www.flipkart.com/grocery/packaged-food/breakfast-cereals/pr?sid=73z,u0u,bx9&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_a0c2cf06-c747-47ff-a306-86e0f51acb9a_2_G211C67CJ4GB_MC.NXLSWOZVU3Q0&otracker=dynamic_rich_navigation_1_2.navigationCard.RICH_NAVIGATION_Packaged%2BFood~Breakfast%2BCereals_NXLSWOZVU3Q0&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L1_view-all&cid=NXLSWOZVU3Q0',
    'Noodle_pasta' :"https://www.flipkart.com/grocery/packaged-food/noodles-pasta/pr?sid=73z,u0u,ltz&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_ebbef467-ce40-4824-8653-5e9f4101dad3_2_G211C67CJ4GB_MC.GOSA97N625VX&otracker=dynamic_rich_navigation_2_2.navigationCard.RICH_NAVIGATION_Packaged%2BFood~Noodles%2B%2526%2BPasta_GOSA97N625VX&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L1_view-all&cid=GOSA97N625VX",
    'Ketchup' : 'https://www.flipkart.com/grocery/packaged-food/ketchups-spreads/pr?sid=73z,u0u,0tl&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_4435c1a5-7f8a-45e5-b28b-95873f5a26a6_2_G211C67CJ4GB_MC.Y2HU0NO6WEWM&otracker=dynamic_rich_navigation_3_2.navigationCard.RICH_NAVIGATION_Packaged%2BFood~Ketchups%2B%2526%2BSpreads_Y2HU0NO6WEWM&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L1_view-all&cid=Y2HU0NO6WEWM',
    'Chocolate' : 'https://www.flipkart.com/grocery/packaged-food/chocolates-sweets/pr?sid=73z,u0u,7o6&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_48edda1c-f75e-4435-b0d1-cf1e43fb41f2_2_G211C67CJ4GB_MC.XDTF6QJ4BWBW&otracker=dynamic_rich_navigation_4_2.navigationCard.RICH_NAVIGATION_Packaged%2BFood~Chocolates%2B%2526%2BSweets_XDTF6QJ4BWBW&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_4_L1_view-all&cid=XDTF6QJ4BWBW',
    'Jams_honey' : 'https://www.flipkart.com/grocery/packaged-food/jams-honey/pr?sid=73z,u0u,j4e&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_6a209413-0861-4bf1-8e73-42f4b7482fb4_2_G211C67CJ4GB_MC.NOMWVMJOO0PM&otracker=dynamic_rich_navigation_5_2.navigationCard.RICH_NAVIGATION_Packaged%2BFood~Jams%2B%2526%2BHoney_NOMWVMJOO0PM&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_5_L1_view-all&cid=NOMWVMJOO0PM',
    'Pickles' : 'https://www.flipkart.com/grocery/packaged-food/pickles-chutney/pr?sid=73z,u0u,03x&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_70375593-10fd-4079-a9f4-e3d316cb9bcb_2_G211C67CJ4GB_MC.SYSHNZJX28YU&otracker=dynamic_rich_navigation_6_2.navigationCard.RICH_NAVIGATION_Packaged%2BFood~Pickles%2B%2526%2BChutney_SYSHNZJX28YU&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_6_L1_view-all&cid=SYSHNZJX28YU',
    'Instant' : 'https://www.flipkart.com/grocery/packaged-food/ready-to-cook/pr?sid=73z,u0u,0gv&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_1de17c15-2c4c-4527-b774-722d4032712d_2_G211C67CJ4GB_MC.N8BWXHWL92JS&otracker=dynamic_rich_navigation_7_2.navigationCard.RICH_NAVIGATION_Packaged%2BFood~Ready%2BTo%2BCook_N8BWXHWL92JS&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_7_L1_view-all&cid=N8BWXHWL92JS',
    'Sauces' : 'https://www.flipkart.com/grocery/packaged-food/cooking-sauces-vinegar/pr?sid=73z,u0u,wd7&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_03634680-483b-43f4-b683-698df229b82c_2_G211C67CJ4GB_MC.VV2FEO6GLPZD&otracker=dynamic_rich_navigation_8_2.navigationCard.RICH_NAVIGATION_Packaged%2BFood~Cooking%2BSauces%2B%2526%2BVinegar_VV2FEO6GLPZD&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=VV2FEO6GLPZD',
    'Baking'  : 'https://www.flipkart.com/grocery/packaged-food/baking/pr?sid=73z,u0u,td1&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_0d5a8590-1b90-4aa3-819e-c54978632ba7_2_G211C67CJ4GB_MC.BL6HT50QLUZU&otracker=dynamic_rich_navigation_9_2.navigationCard.RICH_NAVIGATION_Packaged%2BFood~Baking_BL6HT50QLUZU&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_9_L1_view-all&cid=BL6HT50QLUZU',
    'Soaps' : 'https://www.flipkart.com/grocery/personal-baby-care/soaps-body-wash/pr?sid=73z,njl,sn6&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_e47f333d-fdc1-4a11-a1c1-c65c16058c9d_2_G211C67CJ4GB_MC.7F0DETGHROTO&otracker=dynamic_rich_navigation_1_2.navigationCard.RICH_NAVIGATION_Personal%2B%2526%2B%2BBaby%2BCare~Soaps%2B%2526%2BBody%2BWash_7F0DETGHROTO&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L1_view-all&cid=7F0DETGHROTO',
    'Hair' : 'https://www.flipkart.com/grocery/personal-baby-care/hair-care/pr?sid=73z,njl,vpw&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_4e78cf89-a53f-4fba-84b9-15c216904375_2_G211C67CJ4GB_MC.R7ZRVFUBRXPF&otracker=dynamic_rich_navigation_2_2.navigationCard.RICH_NAVIGATION_Personal%2B%2526%2B%2BBaby%2BCare~Hair%2BCare_R7ZRVFUBRXPF&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L1_view-all&cid=R7ZRVFUBRXPF',
    'Teeth' : 'https://www.flipkart.com/grocery/personal-baby-care/oral-care/pr?sid=73z,njl,2s3&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_4de96eef-07b2-4b06-9c5c-871a2af3d2da_2_G211C67CJ4GB_MC.VW3OLXAN704N&otracker=dynamic_rich_navigation_3_2.navigationCard.RICH_NAVIGATION_Personal%2B%2526%2B%2BBaby%2BCare~Oral%2BCare_VW3OLXAN704N&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L1_view-all&cid=VW3OLXAN704N',
    'Parfum' : 'https://www.flipkart.com/grocery/personal-baby-care/deos-perfumes-talc/pr?sid=73z,njl,np3&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_df8c391d-30b6-48af-aade-4a40f93f7032_2_G211C67CJ4GB_MC.RJC3FQD7ABJ2&otracker=dynamic_rich_navigation_4_2.navigationCard.RICH_NAVIGATION_Personal%2B%2526%2B%2BBaby%2BCare~Deos%252C%2BPerfumes%2B%2526%2BTalc_RJC3FQD7ABJ2&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_4_L1_view-all&cid=RJC3FQD7ABJ2',
    'Loation' : 'https://www.flipkart.com/grocery/personal-baby-care/creams-lotions-skin-care/pr?sid=73z,njl,n3m&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_82a8cc48-da7a-4892-a2a5-e0367359af35_2_G211C67CJ4GB_MC.WTZJ5WJG7PHA&otracker=dynamic_rich_navigation_5_2.navigationCard.RICH_NAVIGATION_Personal%2B%2526%2B%2BBaby%2BCare~Creams%252C%2BLotions%252C%2BSkin%2BCare_WTZJ5WJG7PHA&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_5_L1_view-all&cid=WTZJ5WJG7PHA',
    'Makeup' : 'https://www.flipkart.com/grocery/personal-baby-care/kajal-makeup/pr?sid=73z,njl,lzq&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_e7a29595-4bde-4cfb-997b-7b9c20f86d89_2_G211C67CJ4GB_MC.MZ33JOUJEQ4M&otracker=dynamic_rich_navigation_6_2.navigationCard.RICH_NAVIGATION_Personal%2B%2526%2B%2BBaby%2BCare~Kajal%2B%2526%2BMakeup_MZ33JOUJEQ4M&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_6_L1_view-all&cid=MZ33JOUJEQ4M',
    'Sanitary' :'https://www.flipkart.com/grocery/personal-baby-care/sanitary-needs/pr?sid=73z,njl,tlj&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_6c20dd71-1b06-432b-851d-9ebb29390954_2_G211C67CJ4GB_MC.Z0TGVHD7I91A&otracker=dynamic_rich_navigation_7_2.navigationCard.RICH_NAVIGATION_Personal%2B%2526%2B%2BBaby%2BCare~Sanitary%2BNeeds_Z0TGVHD7I91A&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_7_L1_view-all&cid=Z0TGVHD7I91A',
    'Detol' : 'https://www.flipkart.com/grocery/personal-baby-care/wellness-common-pharma/pr?sid=73z,njl,07d&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_ecc9e8a6-854d-42e2-bfe4-2bc6cc98346f_2_G211C67CJ4GB_MC.2Y1DUHDVM8UF&otracker=dynamic_rich_navigation_8_2.navigationCard.RICH_NAVIGATION_Personal%2B%2526%2B%2BBaby%2BCare~Wellness%2B%2526%2BCommon%2BPharma_2Y1DUHDVM8UF&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=2Y1DUHDVM8UF',
    'Shaving' : 'https://www.flipkart.com/grocery/personal-baby-care/shaving-needs/pr?sid=73z,njl,nw3&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_d0ad18e1-35b8-46fb-abb1-490dc6461b39_2_G211C67CJ4GB_MC.I7MGHRBTU853&otracker=dynamic_rich_navigation_9_2.navigationCard.RICH_NAVIGATION_Personal%2B%2526%2B%2BBaby%2BCare~Shaving%2BNeeds_I7MGHRBTU853&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_9_L1_view-all&cid=I7MGHRBTU853',
    'Daipers' : 'https://www.flipkart.com/grocery/personal-baby-care/diapers-wipes/pr?sid=73z,njl,smb&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_01f43d75-ba2d-4c60-bc57-b76a23eba970_2_G211C67CJ4GB_MC.UGJV25JFCWSR&otracker=dynamic_rich_navigation_10_2.navigationCard.RICH_NAVIGATION_Personal%2B%2526%2B%2BBaby%2BCare~Diapers%2B%2526%2BWipes_UGJV25JFCWSR&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_10_L1_view-all&cid=UGJV25JFCWSR',
    'Baby_food' : 'https://www.flipkart.com/grocery/personal-baby-care/baby-foods/pr?sid=73z,njl,2jj&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_d9d0fb66-a230-43d3-9003-daa03563d4c9_2_G211C67CJ4GB_MC.5HNYYGGUGK4A&otracker=dynamic_rich_navigation_11_2.navigationCard.RICH_NAVIGATION_Personal%2B%2526%2B%2BBaby%2BCare~Baby%2BFoods_5HNYYGGUGK4A&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_11_L1_view-all&cid=5HNYYGGUGK4A',
    'Baby_bath' : 'https://www.flipkart.com/grocery/personal-baby-care/baby-bath-skin-care/pr?sid=73z,njl,m1f&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_2d584ca6-3517-4899-b421-04a254b17ca2_2_G211C67CJ4GB_MC.KS27G12L39SU&otracker=dynamic_rich_navigation_12_2.navigationCard.RICH_NAVIGATION_Personal%2B%2526%2B%2BBaby%2BCare~Baby%2BBath%2B%2526%2BSkin%2BCare_KS27G12L39SU&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_12_L1_view-all&cid=KS27G12L39SU',
    'Detergent' :'https://www.flipkart.com/grocery/household-care/detergents-laundry/pr?sid=73z,cwl,2z2&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_20fe60e9-493c-4302-ba6e-da7b7e95bf87_2_G211C67CJ4GB_MC.8NV4Z62U9QS3&otracker=dynamic_rich_navigation_1_2.navigationCard.RICH_NAVIGATION_Household%2BCare~Detergents%2B%2526%2BLaundry_8NV4Z62U9QS3&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L1_view-all&cid=8NV4Z62U9QS3',
    'Dish_soap' : 'https://www.flipkart.com/grocery/household-care/utensil-cleaners/pr?sid=73z,cwl,bdc&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_0f922e2e-c599-44a1-95cd-26cbaafe9921_2_G211C67CJ4GB_MC.WBQVNZTUYITO&otracker=dynamic_rich_navigation_2_2.navigationCard.RICH_NAVIGATION_Household%2BCare~Utensil%2BCleaners_WBQVNZTUYITO&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L1_view-all&cid=WBQVNZTUYITO',
    'Floor_soap' : 'https://www.flipkart.com/grocery/household-care/floor-other-cleaners/pr?sid=73z,cwl,u3c&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_82b53b2c-2952-4c73-a809-5deca8cd05cb_2_G211C67CJ4GB_MC.L8H68E76OXNJ&otracker=dynamic_rich_navigation_3_2.navigationCard.RICH_NAVIGATION_Household%2BCare~Floor%2B%2526%2BOther%2BCleaners_L8H68E76OXNJ&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L1_view-all&cid=L8H68E76OXNJ',
    'Freshner' : 'https://www.flipkart.com/grocery/household-care/repellants-fresheners/pr?sid=73z,cwl,qz9&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_ac6dae05-ea7d-4399-be13-03dd1fdd0d01_2_G211C67CJ4GB_MC.BHLX1BPW8BFY&otracker=dynamic_rich_navigation_4_2.navigationCard.RICH_NAVIGATION_Household%2BCare~Repellants%2B%2526%2BFresheners_BHLX1BPW8BFY&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_4_L1_view-all&cid=BHLX1BPW8BFY',
    'Paper' : 'https://www.flipkart.com/grocery/household-care/paper-disposables/pr?sid=73z,cwl,2wc&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_2eb84698-84f4-40cc-9d24-8cffab829f1b_2_G211C67CJ4GB_MC.1JRSLDRSO719&otracker=dynamic_rich_navigation_5_2.navigationCard.RICH_NAVIGATION_Household%2BCare~Paper%2B%2526%2BDisposables_1JRSLDRSO719&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_5_L1_view-all&cid=1JRSLDRSO719',
    'Batteries' : 'https://www.flipkart.com/grocery/household-care/basic-electricals/pr?sid=73z,cwl,0s4&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_9122d821-4e6a-4c5c-ba51-d1c07d77ed4b_2_G211C67CJ4GB_MC.HP4FWSHM4NN9&otracker=dynamic_rich_navigation_6_2.navigationCard.RICH_NAVIGATION_Household%2BCare~Basic%2BElectricals_HP4FWSHM4NN9&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_6_L1_view-all&cid=HP4FWSHM4NN9',
    'Pooja' : 'https://www.flipkart.com/grocery/household-care/pooja-needs/pr?sid=73z,cwl,u64&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_c71fef12-5875-4f30-bc40-618e7b39ca75_2_G211C67CJ4GB_MC.2L6HN2TIPCK6&otracker=dynamic_rich_navigation_7_2.navigationCard.RICH_NAVIGATION_Household%2BCare~Pooja%2BNeeds_2L6HN2TIPCK6&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_7_L1_view-all&cid=2L6HN2TIPCK6',
    'Pet' : 'https://www.flipkart.com/grocery/household-care/pet-food/pr?sid=73z,cwl,m92&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_caee73f5-6a4b-47c5-ab06-7d652e7bdd9c_2_G211C67CJ4GB_MC.Y9ZFDE0JI0AM&otracker=dynamic_rich_navigation_8_2.navigationCard.RICH_NAVIGATION_Household%2BCare~Pet%2BFood_Y9ZFDE0JI0AM&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=Y9ZFDE0JI0AM',
    'Shoe_care' : 'https://www.flipkart.com/grocery/household-care/shoe-care/pr?sid=73z%2Ccwl%2C5mx&marketplace=GROCERY&pageUID=1579679877380&fm=neo%2Fmerchandising&iid=M_a26c60b3-92b4-4deb-9608-cb2680d17764_2_G211C67CJ4GB_MC.DVUQ5GFL88IF&otracker=dynamic_rich_navigation_9_2.navigationCard.RICH_NAVIGATION_Household%2BCare~Shoe%2BCare_DVUQ5GFL88IF&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_9_L1_view-all&cid=DVUQ5GFL88IF',
    'Storage' : 'https://www.flipkart.com/grocery/~cs-2ifk48xg9a/pr?sid=73z&marketplace=GROCERY&collection-tab-name=Containers+and+bottles&param=11111&fm=neo%2Fmerchandising&iid=M_80e000b1-8fef-4ab4-9aca-c0a0ffa07c85_2_G211C67CJ4GB_MC.F5ZKXCCR1WH2&otracker=dynamic_rich_navigation_1_2.navigationCard.RICH_NAVIGATION_Home%2B%2526%2BKitchen~Storage%2B%2526%2BContainers~All_F5ZKXCCR1WH2&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L2_view-all&cid=F5ZKXCCR1WH2',
    'kitchen_tool' : 'https://www.flipkart.com/grocery/~cs-cq6mm6u2d9/pr?sid=73z&marketplace=GROCERY&collection-tab-name=Kitchen+tools&p%5B%5D=facets.discount_range_v1%255B%255D%3D10%2525%2Bor%2Bmore&fm=neo%2Fmerchandising&iid=M_bd843996-8b7a-408a-bf84-9068cc18a81e_2_G211C67CJ4GB_MC.W18YJL3ZPA2C&otracker=dynamic_rich_navigation_2_2.navigationCard.RICH_NAVIGATION_Home%2B%2526%2BKitchen~Kitchen%2BTools_W18YJL3ZPA2C&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L1_view-all&cid=W18YJL3ZPA2C',
    'Fruits': 'https://www.flipkart.com/grocery/~cs-czmflnl4er/pr?sid=73z&marketplace=GROCERY&collection-tab-name=All+Fruits+and+Vegetables&fm=neo%2Fmerchandising&iid=M_fd0ea56d-dec9-429e-ac4b-e4ee4f3f0f52_2_G211C67CJ4GB_MC.EG1QZHPQIGJQ&otracker=dynamic_rich_navigation_2_2.navigationCard.RICH_NAVIGATION_Fruits%2B%2526%2BVegetables~Fruits%2B%2526%2BVegetables~Fruits%2B%2526%2BVegetables_EG1QZHPQIGJQ&otracker1=dynamic_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all&cid=EG1QZHPQIGJQ'

}
finaldf = pd.DataFrame({'Date','Item','QTY & price','Price','Link'})
#dairy = f'https://www.flipkart.com/grocery/dairy-eggs/dairy/pr?sid=73z,esa,dt6&otracker=categorytree&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_7b379817-4c00-4619-9e70-87266f879939_2_G211C67CJ4GB_MC.OWYMNIINR533&otracker=clp_rich_navigation_1_2.navigationCard.RICH_NAVIGATION_Dairy%2B%2526%2BEggs~Dairy~All_grocery-supermart-store_OWYMNIINR533&otracker1=clp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L2_view-all&cid=OWYMNIINR533'
# custom_scroll_count = 20    
for item, url in items.items():
    date = []
    product_name = []
    product_price = []
    product_qty = []
    product_link = []
    zip_code = 400070
    print(f"{item}")
    
    try:
        wd.get(url)
        # Wait for the 'Show more results' button to be visible
        time.sleep(2)

        try:
            input_element = wd.find_element_by_css_selector('input[name="pincode"]')

            # Enter the zip code from the variable into the input field
            input_element.send_keys(zip_code)
            verify_button = wd.find_element_by_css_selector('.E9Z0B8._209xbS button[type="button"]')
            verify_button.click()
            element_present = EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-id]'))
            WebDriverWait(wd,20).until(element_present)
        except:
            pass


        count = wd.find_element_by_css_selector('#container > div > div._36fx1h._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div:nth-child(2) > div > div:nth-child(12) > div > div > span:nth-child(1)').text
        count = count.split('of', 1)[1].strip()
        count = int(count)

        prod = wd.find_element_by_css_selector('#container > div > div._36fx1h._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div:nth-child(2)')
        prod_page = prod.find_element_by_css_selector('div')
    
        prod_list = prod_page.find_elements_by_css_selector('div')
        prod_test = prod_page.find_elements_by_class_name('_1AtVbE col-12-12')
        current_page = 1
        while True:
            product_containers = wd.find_elements_by_css_selector('div[data-id]')
            for product in product_containers:
                current_date = datetime.now().date()
                date.append(current_date)

                try:
                    name_element = product.find_element_by_css_selector('a[title]')
                    product_name.append(name_element.get_attribute('title'))
                except :
                    product_name.append('Name not available')

                # Extract product quantity
                try:
                    qty_element = product.find_element_by_css_selector('div._1qE-1H')
                    product_qty.append(qty_element.text)
                except:
                    product_qty.append('Quantity not available')

                # Extract product price
                try:
                    price_element = product.find_element_by_css_selector('div._30jeq3')
                    price_element0 = price_element.text
                    price_element0 = price_element0.replace('₹','').strip()
                    product_price.append(price_element0)
                except:
                    product_price.append('Price not available')

                # Extract product link (href)
                try:
                    link_element = product.find_element_by_css_selector('div._2gX9pM a')
                    product_link.append(link_element.get_attribute('href'))
                except :
                    product_link.append('Link not available')
            
            flipkartdf = pd.DataFrame({'Date': date,'Item': product_name,'QTY & price': product_qty,'Price': product_price,'Link': product_link})
            finaldf = pd.concat([finaldf, flipkartdf], ignore_index=True)
            
            if current_page == 1:
                next_page_button = wd.find_elements_by_css_selector('#container > div > div._36fx1h._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div:nth-child(2) > div > div:nth-child(12) > div > div > nav > a._1LKTO3')
            else:
                next_page_button = wd.find_elements_by_css_selector(f'#container > div > div._36fx1h._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div:nth-child(2) > div > div:nth-child(12) > div > div > nav > a:nth-child({current_page + 1})')

            if not next_page_button:
                # If the button is not found, exit the loop and stop the extraction
                print("Extraction from pages completed!")
                break

            # Click the "Next Page" button
            next_page_button[0].click()
            current_page += 1
            # Wait for the page to load
            WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-id]')))




    except Exception as e:
        print(e)



finaldf.to_csv(f"Flipkart.csv", index=False)
wd.close()
# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print('Extraction Completed!!!')


print("Elapsed time:", elapsed_time, "seconds")
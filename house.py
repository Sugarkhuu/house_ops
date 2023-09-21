
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

chrome_options = Options()

# to run in the background or without opening chrome GUI
chrome_options.add_argument("--headless")

# open chrome, name the object as driver
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://www.unegui.mn/l-hdlh/l-hdlh-zarna/oron-suuts-zarna/")
driver.find_element(By.XPATH, "//*[@id='trait_fields']/div[2]/div[2]/div[2]").click()


driver.find_element(By.PARTIAL_LINK_TEXT,"2 өрөө").click()


listing = driver.find_elements(By.XPATH,"//*[@id='listing']/section/div[2]/div[1]/div[2]/ul/li")

price_list = []

for i in range(len(listing[:10])):
    desc = listing[i].find_element(By.XPATH,"div[1]/div[2]/div/a").text
    price = listing[i].find_element(By.XPATH,"div[1]/div[3]/div").text
    print(desc,price)
    price_list.append([desc,price])

df = pd.DataFrame(price_list, columns = ["Тайлбар","Үнэ"])

df.to_csv("results/unegui.csv",index=False,encoding = "utf-8-sig")



from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup 
players= {"diaby" : "https://www.futbin.com/24/player/87/moussa-diaby","martinelli": "https://www.futbin.com/24/player/2527/gabriel-martinelli"}
prices=[]

for name, link in players.items():
  print(name)

  driver = webdriver.Chrome()
  driver.implicitly_wait(0.5)


  driver.get(link)

  m = driver.find_element(By.CLASS_NAME,"price_big_right")
  mm= m.find_element(By.ID, 'ps-lowest-1')
  price = mm.get_attribute('data-price')
  driver.close()

  prices.append(price)


  df = pd.DataFrame({'name':name,'Price':prices}) 
  
df.to_csv('products.csv', index=False, encoding='utf-8')


#scrapp all gold players in one page


from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup 

prices=[]

driver = webdriver.Chrome()
driver.implicitly_wait(0.5)

driver.get('https://www.futbin.com/players?page=1&version=gold&pos_type=all')


#mixed_list = driver.find_elements(By.CLASS_NAME,"d-inline pt-2 pl-3")
#mixed = mixed_list.find_elements(By.CLASS_NAME,"d-inline pt-2 pl-3")

#print(len(mixed_list))

mixed_list = driver.find_elements(By.CLASS_NAME,"font-weight-bold")

for i in mixed_list:
	item = i.text
	if item[0].isdigit():  # Check if the item is a numeric string
		if item.endswith('K'):
			result = item.replace(".", "")
			prices.append(int(result[:-1]+ '000'))
		elif item.endswith('M'):
			result_int = item.replace(".", "")
			prices.append(int(result_int[:-1]+'000000'))
		else: 
			prices.append(int(item))

print(prices)

driver.close()

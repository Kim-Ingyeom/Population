import time
import selenium
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://superkts.com/population/sum_sido/?o=2')

time.sleep(1)

test=driver.find_elements_by_tag_name("td")
count=0
new_list_x =[]
new_list_y =[]

for i in test[0:20]:
    if count%4 ==1:
         new_list_x.append(i.text)
    elif count%4 == 2:
         new_list_y.append(i.text)
    count+=1


print(new_list_x)
print(new_list_y)

driver.get('https://superkts.com/population/sum_sido/?o=3')

time.sleep(1)

test=driver.find_elements_by_tag_name("td")
count=0
new_list_x =[]
new_list_y =[]

for i in test[0:20]:
    if count%4 ==1:
         new_list_x.append(i.text)
    elif count%4 == 2:
         new_list_y.append(i.text)
    count+=1


print(new_list_x)
print(new_list_y)
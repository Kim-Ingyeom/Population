
import time
import selenium
from selenium import webdriver
import matplotlib.pyplot as plt\




driver = webdriver.Chrome()

driver.get('https://superkts.com/population/sum_sido/?o=2')

time.sleep(1)

test=driver.find_elements_by_tag_name("td")
count=0
new_list_x_1 =[]
new_list_y_1 =[]
list_y_1=[]
for i in test[0:20]:
    if count%4 == 1:
         new_list_x_1.append(i.text)
    elif count%4 == 2:

        list_y_1.append(i.text)
    count+=1

for i in list_y_1:
    i = int(i.replace(',',''))
    new_list_y_1.append(i)

x=[1,2,3,4,5]

print('인구 많은 순')
print(new_list_x_1)
print(new_list_y_1)

plt.figure(figsize=(10,5))
plt.plot(x, new_list_y_1)
plt.xticks(x,new_list_x_1)
plt.show()

time.sleep(3)

driver.get('https://superkts.com/population/sum_sido/?o=3')

time.sleep(1)

test=driver.find_elements_by_tag_name("td")
count=0
new_list_x =[]
new_list_y =[]
list_y=[]
for i in test[0:20]:
    if count%4 == 1:
         new_list_x.append(i.text)
    elif count%4 == 2:

        list_y.append(i.text)
    count+=1

for i in list_y:
    i = int(i.replace(',',''))
    new_list_y.append(i)

x=[1,2,3,4,5]

print('인구 적은순')
print(new_list_x)
print(new_list_y)

plt.figure(figsize=(10,5))
plt.plot(x, new_list_y)
plt.xticks(x,new_list_x)
plt.show()

driver.close()
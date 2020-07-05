from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

input('Scan the QR code for authentication and then press "Enter" ')

name_of_recipient = input('Name of Recipient:')
user = driver.find_element_by_xpath(f'//span[@title = "{name_of_recipient}"]')
user.click()
count = 0
am = 'am'
while True:
    x = time.strftime(f"%H:%M {am}, %d/%m/%Y")
    if x[:2] == '00':
        x.replace(x[:2], str(int(x[:2]) + 12))
    y = x.split(',')
    z = y[0].split(':')
    z
    z[0] = int(z[0])
    if z[0] > 12:
        z[0] -= 12
        z[1] = z[1].replace('am', 'pm')
        z[0] = str(z[0])
    z = (':').join(z)
    y[0] = z
    x = (',').join(y)
    msg_1 = driver.find_element_by_xpath(f'//div[@tabindex = "0" or  @class = "_2hqOq message-in focusable-list-item"]').text #for fetching the time
    print(msg_1)  # of the type string

    print(type(msg_1))

    msg_from = driver.find_element_by_class_name('eRacY').text
    #print(msg_from)
    count += 1
    if count == 1:
        break

'''
#Mom♥️

#message details  is saved in this format : [7:36 pm, 03/07/2020] Mom♥️:

data-pre-plain-text
class name : class="copyable-text"

time class : _18lLQ 

import time
am='am'
pm='pm'
x=time.strftime(f"%H:%M:%S {am}, %d/%m/%Y")
if x[:2]=='00':
	x.replace(x[:2],str(int(x[:2])+12))
elif int(x[:2])>12:
	x.replace(x[:2],str(int(x[:2])-12))
	x.replace('am','pm')
x
[5:13 pm, 04/07/2020] Mom♥️: 
'''
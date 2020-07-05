from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

input('Scan the QR code and then press "Enter"')
dp = driver.find_element_by_class_name('_1BjNO') #opens the dp
dp.click()

pic = driver.find_element_by_class_name('Ao0On') #clicks on the dp
time.sleep(2)
pic.click()

time.sleep(3) #sleeps for 3 sec

upload_pic = driver.find_element_by_xpath('//div[@title = "Upload photo"]') #for uploading a new dp
upload_pic.click()
time.sleep(2)









#upload_pic.send_keys('C:/Users/91884/Desktop/IMG_20190206_110652_758.jpg')

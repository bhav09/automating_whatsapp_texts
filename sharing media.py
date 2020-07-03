#sharing image with the same
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
input('Scan the QR and then proceed by pressing "Enter" ')

name_of_recipient = input('Name of recipient:')

user = driver.find_element_by_xpath(f'//span[@title = "{name_of_recipient}"]') #finding the user
user.click()
file_path = 'C:/Users/91884/PycharmProjects/whatsapp_texting/Music-Between-Us.webp'  #file that is to be shared

attachment = driver.find_element_by_xpath('//div[@title = "Attach"]')  #the media attachment clip
attachment.click() #clicks the clip

time.sleep(2) #waits for 2 second

media = driver.find_element_by_xpath('//input[@accept = "image/*,video/mp4,video/3gpp,video/quicktime"]') #accepts video and images
media.send_keys(file_path) #gives them the file location

time.sleep(3)

msg_in_media = 'Automation via Py script'

msg = driver.find_element_by_class_name('_2FVVk')
msg.send_keys(msg_in_media)

send = driver.find_element_by_xpath('//span[@data-icon = "send"]') #send button to share the media
send.click()

#driver.quit()

#_3WjMU _1C-hz

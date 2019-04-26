from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from RBC_Credentials import username, password

import time


browser = webdriver.Ie("C:\\Users\\amanser\\Documents\\IEDriverServer.exe")

browser.get("https://infoworks.rbc.com")

print (browser.title)

# If Infoworks takes you to a login page, enter the username and password
if browser.find_element_by_name("username"):

    print ("username field found")

    browser.find_element_by_name("username").send_keys(username)

if browser.find_element_by_name("password"):

    print ("password field found")

    browser.find_element_by_name("password").send_keys(password)

    time.sleep(1)

    browser.find_element_by_id("submitButton").click()


# Open ClientSource
time.sleep(2)

# browser.find_element_by_id("infoworks-workstation-tools-2-portal-link-text").click()

# browser.find_element_by_id("infoworks-workstation-tools-2-portal-link-text").key_down(Keys.LEFT_CONTROL).click()

# browser.find_element_by_tag_name('body').send_keys(Keys.LEFT_CONTROL + 't')

time.sleep(2)

# browser.find_element_by_tag_name('body').send_keys(Keys.LEFT_CONTROL + 't')


time.sleep(4)

# browser.find_element_by_tag_name('body').send_keys(Keys.LEFT_CONTROL + Keys.TAB)

# time.sleep(2)

print(browser.window_handles)

# time.sleep(2)

# browser.switch_to.window(browser.window_handles[1])

# time.sleep(2)

browser.get("https://infoworks.rbc.com/launchapp/45/550")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webelement import FirefoxWebElement

driver = webdriver.Firefox()
driver.get("https://google.co.in")
Title = driver.title
driver.maximize_window()
print("Current url is :",driver.current_url)
print("Title of the page is", driver.title)

source_code = driver.page_source
print(source_code)
file_write = open("movius.txt",'a')


links = driver.find_elements_by_xpath("//a")
print(len(links))

for link in links:
    url = (link.get_attribute("href"))
    print(url)
file_write.write(driver.page_source)
'''
if 'Google' in Title:
    print("Title is matched")
else :
    print("Title is not matched")
'''
Login = driver.find_element_by_xpath("/html/body/button")
Login.click()



#driver.close()
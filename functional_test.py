import time
from selenium import webdriver

driver = webdriver.Chrome('/Users/wedaren/Downloads/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.baidu.com/xhtml');
# time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
time.sleep(3) # Let the user actually see something!
driver.quit()

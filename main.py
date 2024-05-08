import sys
import os

from dotenv import load_dotenv
load_dotenv(override=True)
from selenium.webdriver.common.by import By
from selenium import webdriver
USERNAME,PASSWORD = os.environ["USERNAME"], os.environ["PASSWORD"]
driver = webdriver.Firefox()
n = len(sys.argv)
if n == 1:
    sys.argv.append("events")
URL = {}
URL['cn'] = "https://eduserver.nitc.ac.in/course/view.php?id=5985"
URL['nl'] = "https://eduserver.nitc.ac.in/course/view.php?id=5987"
URL['se'] = "https://eduserver.nitc.ac.in/course/view.php?id=5983"
URL['cd'] = "https://eduserver.nitc.ac.in/course/view.php?id=5984"
URL['dash'] = "https://eduserver.nitc.ac.in/my/"
URL["events"] = URL['dash']
driver.get(URL[sys.argv[1]])
# else:
    # element = driver.find_elements_by_class_name("btn btn-primary")
driver.find_element(by=By.ID, value="username").send_keys(USERNAME) 
driver.find_element(by=By.ID, value="password").send_keys(PASSWORD) 
print(USERNAME,PASSWORD)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # print(len(element),element)

# if sys.argv[1] == "events":
#     elements = driver.find_element(By.PARTIAL_LINK_TEXT, "calendar")
#     # elements = driver.find_element_by_class_name("event")
#     print(len(elements), elements)

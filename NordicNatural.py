import requests
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# Invoking chrome browser and getting Nordic naturals site also maximising it!!
driver=  Chrome(ChromeDriverManager().install())
driver.get("https://www.nordicnaturals.com/consumers/")
driver.maximize_window()

# In case the above code does not work and throughs google version issue please UNCommment this code and run (Commment above one) and put desired
# execuatble path of google chrome.
# driver= webdriver.Chrome(executable_path="/Users/shivanigambhir/Downloads/chromedriver 3")
# driver.get("https://www.nordicnaturals.com/consumers/")
# driver.maximize_window()

#Clicking on Accept Cookies button and getting all links on page and checking the length of links on the page
driver.find_element_by_id("onetrust-accept-btn-handler").click()
links = driver.find_elements_by_css_selector("a")
print("Total no of links ",len(links))

#Iterating through each link from all links and checking if status code is 200 it is active and working and if 404 it's not working etc
try:
    for link in links:
        r = requests.head(link.get_attribute('href'))
        if r.status_code >= 400:
            print(link.get_attribute('href')," Broken Link --Not working")
        else:
            print(link.get_attribute('href'), "Active and working")
except:
    print (link.get_attribute('href'), "Link does not work")
finally:
    driver.quit()

#This code is working absolutely fine at my end please let me know in case if you face any issue
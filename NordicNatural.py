import requests
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

# Invoking chrome browser and getting Nordic naturals site also maximising it!!
driver=  Chrome(ChromeDriverManager().install())
driver.get("https://www.nordicnaturals.com/consumers/")
driver.maximize_window()

#Clicking on Accept Cookies button and getting all links on page and checking the length of links on the page
driver.find_element_by_id("onetrust-accept-btn-handler").click()
links = driver.find_elements_by_css_selector("a")
print("Total no of links ",len(links))

#Iterating through each link from all links and checking if status code is 200 it is active and working and if 404 it's not working etc
# try:
for link in links:
    r = requests.head(link.get_attribute('href'))
    if r.status_code == 200:
        print(r, "Active and working")
    elif r.status_code == 201:
        print(r, "Active and working")
    elif r.status_code == 404:
        print(r ," Nordic Internal 404 error --Not working")
    elif r.status_code == 500:
        print(r, "500 Sever error")
driver.close()

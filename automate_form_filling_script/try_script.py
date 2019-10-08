#to search anything on any website
#importing importing modules
from selenium import webdriver #to get the browser webdriver
from selenium.webdriver.common.keys import Keys #common keys module use to enter some special keys like alt,ctrl etc

#this is giving the path of webdriver of the specific browser
driver=webdriver.Chrome(executable_path="D:\python scripts\Whatsapp send messages\chromedriver.exe")
driver.get("https://ctazuresmartenterprise.azurewebsites.net/") #the website on which we have to search

#assert "Python" in driver.title #to check that the title is having Python as their name
ex=driver.find_element_by_id('CustomerName') # now to find get the search tab by the name (q)
#click on the search tab and after clicking right click on the search tab and inspect the element 
ex.clear() #to remove any pre written word on the tab

ex.send_keys("Abhishek Varshney") #now to search what we have to search
ex.send_keys(Keys.RETURN) #to search we have to click RETURN key by this
#assert "no result found" not in driver.page_source #if the search not found then output would be this

ee=input("enter any thing to close")
driver.quit()  #this will close the whole browser
#driver.close() #this will close only the tab on which the website is running


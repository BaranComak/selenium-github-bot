from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from githubUserinfo import username,password

class Github:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome() 
        self.username = username
        self.password = password
        self.followers = []


    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(3)
        self.browser.find_element(By.XPATH, "//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element(By.XPATH, "//*[@id='password']").send_keys(self.password)
        time.sleep(2)
        self.browser.find_element(By.XPATH, "//*[@id='login']/div[4]/form/div/input[11]").send_keys(Keys.ENTER)
        time.sleep(2)
    
    def loadFollowers(self):
        items = self.browser.find_elements(By.CSS_SELECTOR, ".d-inline-block.no-underline.mb-1")
        for i in items:
            i.find_elements(By.CSS_SELECTOR, ".f4.Link--primary")
            self.followers.append(i.text)  

    def getFollowers(self):
        self.browser.get("") # Followers Control
        time.sleep(2)
        self.loadFollowers()
        while True:
            links = self.browser.find_element(By.CLASS_NAME, "pagination").find_elements(By.TAG_NAME, ("a"))
            if len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(3)
                    self.loadFollowers()
                    
                else:
                    break
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(3)                        
                        self.loadFollowers()

                    else:
                        continue

github = Github(username,password)
github.signIn()
github.getFollowers()
github.loadFollowers()
print(len(github.followers))
print(github.followers)











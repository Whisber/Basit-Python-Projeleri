#İnstagram takipci sayisi ögrenme , python selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self):
        self.browser = webdriver.Firefox(executable_path=r'/home/emirhan/Masaüstü/projeler/geckodriver')
        self.username = "username"
        self.password = "pass"
        self.followers = []
        self.instapage = "instaurl"
        self.numberFollowers = 0
    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(4)
        email = self.browser.find_element_by_name("username")
        passw = self.browser.find_element_by_name("password")
        email.send_keys(self.username)
        passw.send_keys(self.password)
        time.sleep(4)
        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div").click()
    def getFollowers(self):
        self.browser.get(self.instapage)
        time.sleep(2)
        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
        time.sleep(2)
        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followerCount = len(dialog.find_elements_by_css_selector("li"))
        print(f'ilk yüklendigindeki takipciler {followerCount}')

        action = webdriver.ActionChains(self.browser) #browser'a istedigimiz tuşları göndeririz.
        dialog.click()
        while True:
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            newCount = len(dialog.find_elements_by_css_selector("li"))
            if followerCount != newCount:
                followerCount = newCount
                print(f'Anlık takipci : {newCount}')
                time.sleep(1)
            else:
                break

        followers = dialog.find_elements_by_css_selector("li")
        for users in followers:
            link = users.find_element_by_css_selector("a").get_attribute("href")
            split = link.replace("https://www.instagram.com","").replace("/","")
            self.followers.append(split)
insta = Instagram()
insta.signIn()
time.sleep(4)
insta.getFollowers()
insta.numberFollowers = len(insta.followers)
print(f'Toplam takipçi sayısı: {insta.numberFollowers}')
time.sleep(2)
for users in insta.followers:
    print(users)

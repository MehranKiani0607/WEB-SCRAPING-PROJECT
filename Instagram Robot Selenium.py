from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time


class Bot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
    def log_in(self):
        self.driver.get("https://www.instagram.com/")
        self.driver.maximize_window()
        name = self.driver.find_element_by_name("username").send_keys(self.username)
        pass_ = self.driver.find_element_by_name("password").send_keys(self.password)
        button_1 = self.driver.find_element_by_css_selector("button[type='submit']").click()
        time.sleep(5)
        button_2 = self.driver.find_element_by_xpath("//button[@type='button']").click()
        time.sleep(5)
        button_3 = self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm").click()

    def comment(self):
        self.driver.get("https://www.instagram.com/juventus/")
        post = self.driver.find_element_by_css_selector("a[href='/p/COS0tKzMNeb/']").click()
        i = 1
        while i<=5:
            time.sleep(5)
            waits = WebDriverWait(self.driver, 10)
            text = waits.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "Ypffh"))).click()
            text = waits.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "Ypffh"))).send_keys("Hi Guys"+Keys.ENTER)
            time.sleep(5)
            next = self.driver.find_element_by_link_text("Next").click()
            i += 1
        self.driver.get("https://www.instagram.com/juventus/")

    def follow(self):
        self.driver.get("https://www.instagram.com/juventus/")
        waits = WebDriverWait(self.driver, 10)
        follow_1 = waits.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/juventus/followers/']"))).click()
        time.sleep(5)
        for i in range(1, 7):
            follow_2 = self.driver.find_element_by_xpath(f"/html/body/div[4]/div/div/div[2]/ul/div/li[{i}]/div/div[3]/button").click()
            time.sleep(4)

user_name = "mehrankiani0607"
password = "###"
test = Bot(user_name, password)
test.log_in()
test.follow()
# test.comment()
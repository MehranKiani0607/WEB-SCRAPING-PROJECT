from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select

# driver = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Chrome('C:/Users/DaryaSystem/.wdm/drivers/chromedriver/win32/91.0.4472.101/chromedriver.exe')
driver.get("https://www.google.com/")
driver.maximize_window()


waits = WebDriverWait(driver, 10)
x_1 = waits.until(expected_conditions.element_to_be_clickable((By.NAME, "q")))
x_1.send_keys("تست روانشناسی"+Keys.ENTER)


x_2 = waits.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                   "a[href='https://esanj.ir/tag/psychology-test']"))).click()
x_3 = waits.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT,
                   "تست شخصیت شناسی مایرز - بریگز | آنلاین (تست MBTI) - ای سنج"))).click()
x_4 = waits.until(expected_conditions.element_to_be_clickable((By.XPATH,
                   "/html/body/section[2]/div/div[3]/div[2]/a[1]"))).click()
x_5 = waits.until(expected_conditions.element_to_be_clickable((By.XPATH,
                   "//select[@name='sex']")))

sel_1 = Select(x_5).select_by_value("male")
x_6 = waits.until(expected_conditions.element_to_be_clickable((By.XPATH, "//select[@name='year_birth']")))
sel_2 = Select(x_6).select_by_value("1374")
x_7 = waits.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

i = 1
while i <= 10:
    if i%2==0:
        x_8 = waits.until(expected_conditions.element_to_be_clickable((By.XPATH, "//label[@for='answer-1']"))).click()
    else:
        x_9 = waits.until(expected_conditions.element_to_be_clickable((By.XPATH, "//label[@for='answer-2']"))).click()
    i += 1
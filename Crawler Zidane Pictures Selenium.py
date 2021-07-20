from selenium import webdriver
import time
import requests
import random


driver = webdriver.Chrome('C:/Users/DaryaSystem/.wdm/drivers/chromedriver/win32/91.0.4472.101/chromedriver.exe')
driver.get("https://lenz.varzesh3.com/account/280/%D8%B2%DB%8C%D8%AF%D8%A7%D9%86")
driver.maximize_window()
time.sleep(3)


end_of_scroll = driver.execute_script("return document.body.scrollHeight")
my_image = []


while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(5)
    my_scroll = driver.execute_script("return document.body.scrollHeight")
    if my_scroll == end_of_scroll:
        break
    end_of_scroll = my_scroll


images = driver.find_elements_by_css_selector("div.inner-img-hld img")
for img in images:
    post = img.get_attribute("src")
    my_image.append(post)


for pic in my_image:
    name = random.randrange(1,50)
    with requests.get(pic, stream=True) as r:
        with open(str(name)+".jpg", "wb") as f:
            for data in r.iter_content(chunk_size=1024):
                f.write(data)

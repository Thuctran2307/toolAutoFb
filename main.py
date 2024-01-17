import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
username = 'tranduythuc2003@gmail.com'
password = '23070603'
image_list = ["D:\\Code\\python\\toolAutoFb\\rs_image\\1.jpg", "D:\\Code\\python\\toolAutoFb\\rs_image\\2.jpg", "D:\\Code\\python\\toolAutoFb\\rs_image\\3.jpg", "D:\\Code\\python\\toolAutoFb\\rs_image\\4.jpg"
              "D:\\Code\\python\\toolAutoFb\\rs_image\\5.jpg","D:\\Code\\python\\toolAutoFb\\rs_image\\6.jpg"]
def post_to_group(text, link_groups, driver):
    for link_group in link_groups:
        driver.get(link_group)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Bạn viết gì đi...']"))).click()
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]"))).send_keys(text)
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]"))).click()
        time.sleep(5)
        # for image in image_list:
        #     try:
        #         driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("D:\\Code\\python\\toolAutoFb\\rs_image\\1.jpg")
        #         time.sleep(8)
        #     except:
        #         pass
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("D:\\Code\\python\\toolAutoFb\\rs_image\\new.jpg")
        time.sleep(10)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]"))).click()
        time.sleep(20)
        

option = Options()
# Working with the 'add_argument' Method to modify Driver Default Notification
option.add_argument('--disable-notifications')
option.add_argument("--lang=en")

# Khởi tạo trình duyệt
driver = webdriver.Chrome(service=Service(executable_path=r"D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"), options=option)

# Mở trang web của Facebook
driver.get('https://www.facebook.com')

username_field = driver.find_element(By.ID, 'email')
password_field = driver.find_element(By.ID, 'pass')

username_field.send_keys(username)
password_field.send_keys(password)


password_field.send_keys(Keys.RETURN)

time.sleep(5)  # Thời gian để trang đăng nhập

groups_link = ["https://www.facebook.com/groups/669225251946228","https://www.facebook.com/groups/kiemtienonlinemienphi1", "https://www.facebook.com/groups/kiemtienonline147"
               ,"https://www.facebook.com/groups/985536349314165", "https://www.facebook.com/groups/359563819672220"]

message= "Bạn nào đủ 18t ib mình hướng dẫn đăng ký ngân hàng nhận #100k free, rút được hết nhé mn. Sự kiện đến cuối tháng 12 mn tranh thủ nha."

post_to_group(message, groups_link, driver)

driver.quit()

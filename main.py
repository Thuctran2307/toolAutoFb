import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


option = Options()

# Working with the 'add_argument' Method to modify Driver Default Notification
option.add_argument('--disable-notifications')
option.add_argument("--lang=en")

# Khởi tạo trình duyệt
driver = webdriver.Chrome(service=Service(executable_path=r"C:\Users\vytra\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"), options=option)

# Mở trang web của Facebook
driver.get('https://www.facebook.com')

# Nhập thông tin đăng nhập
username = 'tranduythuc2003@gmail.com'
password = '06032307'

username_field = driver.find_element(By.ID, 'email')
password_field = driver.find_element(By.ID, 'pass')

username_field.send_keys(username)
password_field.send_keys(password)

# Submit để đăng nhập
password_field.send_keys(Keys.RETURN)

# Chờ trang đăng nhập xong
time.sleep(5)  # Thời gian để trang đăng nhập

# Mở đường link cụ thể tới bài viết
post_url = 'https://www.facebook.com/nsth.plus/posts/pfbid0bsBMPfHdaa9n1WUhxnEwvXK3osWSddZdYfyf7FQDGgsp7QNkLvbkkN1u7vXcQcwkl'  # Thay thế URL của bài viết cần like vào đây
driver.get(post_url)

# Đợi cho trang bài viết được tải hoàn chỉnh
time.sleep(10)  # Thời gian chờ cho trang bài viết

# Thử tìm và ấn nút Like (cần thay đổi theo HTML của trang web)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Thích']"))).click()
time.sleep(10)
# Đóng trình duyệt sau khi hoàn thành
driver.quit()

# importing required modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import sys

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("--disable-software-rasterizer")
#opt.add_argument("--headless") # 不要開啟瀏覽器
#opt.add_argument('--disable-gpu') #關閉GPU 避免某些系統或是網頁出錯

#opt.add_argument("window-size=1920,1080") # 設定瀏覽器大小

# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 2, 
"profile.default_content_setting_values.media_stream_camera": 2,
"profile.default_content_setting_values.geolocation": 2, 
"profile.default_content_setting_values.notifications": 2 
})

print("Please type your email account for google meet")
account = input()
print("Please type your email password")
password = input()
# Your Google meet URL
meet_url = 'https://meet.google.com/jrc-fbyg-srj?authuser=0&hs=179'

#初始化selenium driver時傳入option參數
#driver = webdriver.Chrome(chrome_options = options)
#driver = webdriver.Chrome(chrome_options = opt)
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),chrome_options=opt)
# Due to security reasons google has blocked Sign In from automated or third-party applications.
# To login your google account enable less secure apps in your Google settings.
# After this you can do the login manually or by writing two more lines in the same code. 
# (I am not writing code for log in because when you try on your own you learn many new things.)
def Login_meet():
    driver.get('https://gmail.com')
    #type_account = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
    type_account = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='identifier']")))
    
    type_account.send_keys(account,Keys.ENTER)
    # going to the meet URL after login.
    time.sleep(1)
    type_password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')))
    #type_password = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
    ActionChains(driver).move_to_element(type_password)
    type_password.send_keys(password,Keys.ENTER)

    driver.get(meet_url)
    time.sleep(1)
    driver.refresh()
    time.sleep(2)
    btn_dismiss = driver.find_element(By.XPATH,"/html/body/div/div[3]/div[2]/div/div[2]/button/span")
    btn_dismiss.click()
    time.sleep(2)
    #print("join_click")
    btn_join = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div[1]/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/button/span')))
    btn_join.click()
    time.sleep(5)
    print("successfully login classroom")


def Sign_in():
    
    
    try: 
        # finding the text box to type message in text box.
        x_path = '/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[4]/div[2]/div[2]/div/div[5]/div/label/textarea'
        t_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path)))
        # sending messages.
        message = '150905 鄭恆安'
        t_box.send_keys(message,Keys.ENTER)
    except:
        # getting the message button in google meet.
        xpath_btn = '/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[3]/div/div/div[3]/span/button/i[1]'
        btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_btn)))
        btn.click()
        time.sleep(1)
        # finding the text box to type message in text box.
        x_path = '/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[4]/div[2]/div[2]/div/div[5]/div/label/textarea'
        t_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path)))
        # sending messages.
        message = '150905 鄭恆安'
        t_box.send_keys(message,Keys.ENTER)
    #'''

now = datetime.datetime.now()
current_time = now.strftime("%H:%M / %A")
# %A is to get the name of the Day!
justtime = now.strftime("%H:%M")

Login_meet()

while True:
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M / %A")
    # %A is to get the name of the Day!
    justtime = now.strftime("%H:%M")
    print (current_time)
    classtime=['08:12','09:03','09:12','10:02','10:13','11:00','11:11','13:02','13:51','14:03','14:51','15:11','16:00']
    while justtime not in classtime:
        time.sleep(20)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M / %A")
        justtime = now.strftime("%H:%M")
        print(justtime)
    Sign_in()
    time.sleep(60)
    print("alive")
'''
while True:
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M / %A")
    # %A is to get the name of the Day!
    justtime = now.strftime("%H:%M")
    print (current_time)
    classtime=['21:49','21:50','21:36','21:37','21:38','21:40','18:54','18:51','18:52','18:53']
    while justtime not in classtime:
        time.sleep(20)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M / %A")
        justtime = now.strftime("%H:%M")
        print(justtime)
    Sign_in()
    time.sleep(60)
    print("alive")
'''
    


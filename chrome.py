from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains


from selenium.webdriver.chrome.options import Options
import time
from dotenv import load_dotenv
import os

import pickle
import sys

opts = Options()

opts.binary_location = '/usr/lib/chromium/chromium'
opts.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2,     # 1:allow, 2:block 
    "profile.default_content_setting_values.media_stream_camera": 2,  # 1:allow, 2:block 
    "profile.default_content_setting_values.geolocation": 2,          # 1:allow, 2:block 
    "profile.default_content_setting_values.notifications": 2         # 1:allow, 2:block 
  })
driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver',chrome_options=opts)


load_dotenv()




def signin():
    # def NCookie():
    #     if os.path.exists("jar.pkl"):
    #         wCookie()
    #     else:
    #         open("jar.pkl","wb")
    #         print("""file did not existed !!!
    #         and it is created now 
    #         repeat the process to handle the file""")
    #         wCookie()

    # def wCookie():
        # if os.path.getsize("jar.pkl")==0:
    driver.get("https://accounts.google.com")
    enames = ['identifier','Email']
    for name in enames:
      try:
        mail = driver.find_element_by_name(name)
        if mail:
          mail.clear()
          mail.send_keys(os.getenv("USERNAME"))
          mail.send_keys(Keys.RETURN)
      except Exception as err:
        print(err)

    pnames = ['Passwd','password']
    for name in pnames:
      try:
        paswd = WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.NAME,"password")))
        if paswd:
          paswd.clear()
          paswd.send_keys(os.getenv("PASSWORD"))
          paswd.send_keys(Keys.RETURN)
          time.sleep(6)
      except Exception as err:
        print(err)

    
    # mail.clear()
    # mail.send_keys(os.getenv("USERNAME"))
    # mail.send_keys(Keys.RETURN)
    
           
def join():
   
    MEETING_CODE = "otc-vshm-vww"
    MEETING_URL = "https://meet.google.com/"+ MEETING_CODE 
    driver.get(MEETING_URL)
    time.sleep(10)
    print('loooool')
    dissmis = "document.getElementsByClassName('U26fgb O0WRkf oG5Srb HQ8yf C0oVfc kHssdc HvOprf DEhM1b M9Bg4d')[0].click()"
    driver.execute_script(dissmis)
    print('loool2')
    print('joining .....')
    time.sleep(10)
    command = 'document.getElementsByClassName("l4V7wb Fxmcue")[0].click();'
    driver.execute_script(command)

    def screenshot():
      #WHILE NOT CUrrunt time + 1h:30
      time.strftime("%H:%M:%S",time.localtime())
      while True:
        t  = time.strftime("%H.%M",time.localtime())
        while float(time.strftime("%H.%M",time.localtime())) != float(t)+0.06:
          print('not yet')
          driver.get_screenshot_as_png()
          print('getting pic...')
          pic = "pic_number"
          driver.save_screenshot(f"{pic}{time.localtime().tm_min} m.png")
          time.sleep(62)
    screenshot()
    

        

    
    
    
    


signin()
join()
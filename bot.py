from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from secrets import username_, password_
import requests
import shutil
import pyfiglet 
import random
import keyboard


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\\webdrivers\\chromedriver.exe")
    
    def login(self):
        self.driver.get('https://tinder.com/')
        time.sleep(3)
        #accept_terms_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        #accept_terms_btn.click()
        sign_in_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button')
        sign_in_btn.click()
        go_sign_in_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button')
        go_sign_in_btn.click()

        # #Switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        email_in = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_in.send_keys(username_)
        next_btn = self.driver.find_element_by_xpath('//*[@id="identifierNext"]')
        next_btn.click()
        time.sleep(1)
        self.driver.switch_to_window(self.driver.window_handles[1])
        pass_in = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        pass_in.send_keys('alvarado3105452037')
        next_btn = self.driver.find_element_by_xpath('//*[@id="passwordNext"]')
        next_btn.click()
        time.sleep(10)

        # #Switch to main window
        self.driver.switch_to_window(base_window)
        # Acept location sharing
        allow_loc_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_loc_btn.click()

    def get_pp_img(self):
        img_elmt = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div/div') 
        img_elmnt_div = img_elmt.find_elements_by_tag_name('div')[-1]
        style_attr = img_elmnt_div.get_attribute('style') 
        style_attr_split = style_attr.split('"')
        img_url = style_attr_split[1]

        filename = img_url.split("/")[-1]
        #Open the url image, set stream to True, this will return the stream content
        r = requests.get(img_url, stream=True)

        #Check if the image was retrieved successfully
        if r.status_code == 200:
            #Set decode_content value to True, otherwise the downloaded image file's size will be zero
            r.raw.decode_content = True

            #Open a local file with wb (write binary) permission
            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            
            print('Image successfully Downloaded: ', filename)
        else:
            print('Image Couldn\'t be retreived')

#//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[1]/div/div[4]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[3]/div[2]/div/div/div/div/form/div[2]/div/div/div/div/div/div

    
    def like(self):
        #Write thise function for swapping
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()
        result = pyfiglet.figlet_format("You liked it") 
        print(result)
    
    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()     
        result = pyfiglet.figlet_format("Oh, Next time!") 
        print(result)  
    
    def auto_swipe(self):
        choice = [True, False]
        while True:
            time.sleep(0.5)
            if random.choice(choice) or keyboard.is_pressed('q'):
                self.like()
            else:
                self.dislike()


        


    def free_navigate(self):
        self.driver.get('https://www.tinder.com/')
        time.sleep(3)
        self.driver.get('https://www.wikipedia.com/')
        time.sleep(3)
        self.driver.get('https://www.edx.org/')
        

element_ = "k4urcfbm dp1hu0rb d2edcug0 cbu4d94t j83agx80 bp9cbjyn"


class FacebookBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\\webdrivers\\chromedriver.exe")
    
    def login(self):
        self.driver.get('https://facebook.com/')
        time.sleep(3)
        # accept_terms_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        # accept_terms_btn.click()
        
        # sign_in_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button')
        # sign_in_btn.click()
        # go_sign_in_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button')
        # go_sign_in_btn.click()
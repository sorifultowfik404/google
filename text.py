import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import sys

import time
import random
driver = uc.Chrome('C:\\Users\\Md Alamin Hossain\\Desktop\\chromedriver.exe')
time.sleep(2)
login = 'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmyaccount.google.com%2Fsigninoptions%2Frescuephone&osid=1&rart=ANgoxcfbj5MICImsby3i6E4WliB4NiCObSuRKGTYLSt03bQVr5EN0ekxnuxLrRGkyz5DKW13ZqMxZkUoZn1oMKAXz3u6m-8mXw&service=accountsettings&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
driver.get(login)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as exp_con
from reCaptchaBypasser import reCaptchaV2Scraper
from time import sleep

driver = webdriver.Firefox(executable_path=r"./geckodriver")

driver.get("https://google.com/recaptcha/api2/demo")

captcha_bypasser = reCaptchaV2Scraper(driver, 4)
res = captcha_bypasser.reCaptchaGoogleV2()
if res != None:
    if res["Status"] == True:
        print(f"Bypassed !!! | rCaptcha Audio Text : {res['reCaptchaText']}")
        sleep(2)
        submit_btn = WebDriverWait(driver, timeout=4).until(exp_con.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
        submit_btn.click()
        print("Submited !!!")
    elif res["Status"] == False:
        print("Cannot Bypass reCaptcha !!!")

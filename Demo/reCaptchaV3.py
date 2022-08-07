#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reCaptchaBypasser import reCaptchaV3Scraper
from requests import post


recaptcha_url = "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfB5_IbAAAAAMCtsjEHEHKqcB9iQocwwxTiihJu&co=aHR0cHM6Ly8yY2FwdGNoYS5jb206NDQz&hl=en&v=gWN_U6xTIPevg0vuq7g1hct0&size=invisible&cb=lkowcryvrtab"
site_key = "6LfB5_IbAAAAAMCtsjEHEHKqcB9iQocwwxTiihJu"
captcha_bypasser = reCaptchaV3Scraper(recaptcha_url)
res = captcha_bypasser.reCaptchaGoogleV3()
if res != None:
    if res["Status"] == True:
        res = res["reCaptchaResponse"]
        site_res = post(
                         url = "https://2captcha.com/api/v1/captcha-demo/recaptcha/verify",
                         json = {
                                 "siteKey":site_key,
                                 "answer":res
                                },
                         headers = {
                                     "Host": "2captcha.com",
                                     "User-Agent": "", 
                                     "Accept": "*/*",
                                     "Accept-Language": "en-US,en;q=0.5",
                                     "Content-Type": "application/json",
                                     "Origin": "https://2captcha.com",
                                     "Connection": "keep-alive",
                                     "Referer": "https://2captcha.com/demo/recaptcha-v3",
                                     "Sec-Fetch-Dest": "empty",
                                     "Sec-Fetch-Mode": "cors",
                                     "Sec-Fetch-Site": "same-origin"
                                   }
                       )
        if site_res.status_code == 200:
            site_res = site_res.json()
            if site_res["success"] == True:
                print(f"Bypassed !!! , reCaptcha Version 3 Response :\n\n{res}\n\nSite Result :\n\n{site_res}")
            else:
                print("Cannot Bypass reCaptcha Version 3 !!!")
        else:
            print("Cannot Bypass reCaptcha Version 3 !!!")
    else:
        print("Cannot Bypass reCaptcha Version 3 !!!")


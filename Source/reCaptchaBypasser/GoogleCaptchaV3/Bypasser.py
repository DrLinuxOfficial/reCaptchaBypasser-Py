#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =================================================== #
# reCaptchaBypasser Library v1.4                      #
#                                                     #
# Class File Of Bypass Google reCaptcha Version 3 .   #
# =================================================== #
# ========================================================================= #
#                                                                           #
# GitHub Link ==> https://github.com/DrLinuxOfficial/reCaptchaBypasser-Py   #
#                                                                           #
# PyPi Link ==> https://pypi.org/project/reCaptchaBypasser/                 #
#                                                                           #
# ========================================================================= #
# =================================================== #
#                                                     #
# Created By : Dr.Linux .                             #
# Copyright 2021 - 2022 Dr.Linux .                    #
#                                                     #
# =================================================== #


#== Import Required Packages ==#


from bs4 import BeautifulSoup as BS
from requests import Session
from random import choice
import re


#== Class Of Bypass Google reCaptcha Version 3 ==#


class reCaptchaV3Scraper:
    """
        reCaptcha Version 3 Bypasser Class .
        ====================================
        Arguments :
             url :
                   string | Anchor URL Of reCaptcha Version 3 .
             =====================
    """
    def __init__(self, url: str):
        self.url = url
        self.session_req = Session()
        self.url_data = self.__GetURLData__()
        self.user_agent = (self.__GetUserAgent__())
        self.captcha_response_post_data = "v={}&reason=q&c={}&k={}&co={}&hl=en&size=invisible&chr=%5B89%2C64%2C27%5D&vh=13599012192&bg=!q62grYxHRvVxjUIjSFNd0mlvrZ-iCgIHAAAB6FcAAAANnAkBySdqTJGFRK7SirleWAwPVhv9-XwP8ugGSTJJgQ46-0IMBKN8HUnfPqm4sCefwxOOEURND35prc9DJYG0pbmg_jD18qC0c-lQzuPsOtUhHTtfv3--SVCcRvJWZ0V3cia65HGfUys0e1K-IZoArlxM9qZfUMXJKAFuWqZiBn-Qi8VnDqI2rRnAQcIB8Wra6xWzmFbRR2NZqF7lDPKZ0_SZBEc99_49j07ISW4X65sMHL139EARIOipdsj5js5JyM19a2TCZJtAu4XL1h0ZLfomM8KDHkcl_b0L-jW9cvAe2K2uQXKRPzruAvtjdhMdODzVWU5VawKhpmi2NCKAiCRUlJW5lToYkR_X-07AqFLY6qi4ZbJ_sSrD7fCNNYFKmLfAaxPwPmp5Dgei7KKvEQmeUEZwTQAS1p2gaBmt6SCOgId3QBfF_robIkJMcXFzj7R0G-s8rwGUSc8EQzT_DCe9SZsJyobu3Ps0-YK-W3MPWk6a69o618zPSIIQtSCor9w_oUYTLiptaBAEY03NWINhc1mmiYu2Yz5apkW_KbAp3HD3G0bhzcCIYZOGZxyJ44HdGsCJ-7ZFTcEAUST-aLbS-YN1AyuC7ClFO86CMICVDg6aIDyCJyIcaJXiN-bN5xQD_NixaXatJy9Mx1XEnU4Q7E_KISDJfKUhDktK5LMqBJa-x1EIOcY99E-eyry7crf3-Hax3Uj-e-euzRwLxn2VB1Uki8nqJQVYUgcjlVXQhj1X7tx4jzUb0yB1TPU9uMBtZLRvMCRKvFdnn77HgYs5bwOo2mRECiFButgigKXaaJup6NM4KRUevhaDtnD6aJ8ZWQZTXz_OJ74a_OvPK9eD1_5pTG2tUyYNSyz-alhvHdMt5_MAdI3op4ZmcvBQBV9VC2JLjphDuTW8eW_nuK9hN17zin6vjEL8YIm_MekB_dIUK3T1Nbyqmyzigy-Lg8tRL6jSinzdwOTc9hS5SCsPjMeiblc65aJC8AKmA5i80f-6Eg4BT305UeXKI3QwhI3ZJyyQAJTata41FoOXl3EF9Pyy8diYFK2G-CS8lxEpV7jcRYduz4tEPeCpBxU4O_KtM2iv4STkwO4Z_-c-fMLlYu9H7jiFnk6Yh8XlPE__3q0FHIBFf15zVSZ3qroshYiHBMxM5BVQBOExbjoEdYKx4-m9c23K3suA2sCkxHytptG-6yhHJR3EyWwSRTY7OpX_yvhbFri0vgchw7U6ujyoXeCXS9N4oOoGYpS5OyFyRPLxJH7yjXOG2Play5HJ91LL6J6qg1iY8MIq9XQtiVZHadVpZVlz3iKcX4vXcQ3rv_qQwhntObGXPAGJWEel5OiJ1App7mWy961q3mPg9aDEp9VLKU5yDDw1xf6tOFMwg2Q-PNDaKXAyP_FOkxOjnu8dPhuKGut6cJr449BKDwbnA9BOomcVSztEzHGU6HPXXyNdZbfA6D12f5lWxX2B_pobw3a1gFLnO6mWaNRuK1zfzZcfGTYMATf6d7sj9RcKNS230XPHWGaMlLmNxsgXkEN7a9PwsSVwcKdHg_HU4vYdRX6vkEauOIwVPs4dS7yZXmtvbDaX1zOU4ZYWg0T42sT3nIIl9M2EeFS5Rqms_YzNp8J-YtRz1h5RhtTTNcA5jX4N-xDEVx-vD36bZVzfoMSL2k85PKv7pQGLH-0a3DsR0pePCTBWNORK0g_RZCU_H898-nT1syGzNKWGoPCstWPRvpL9cnHRPM1ZKemRn0nPVm9Bgo0ksuUijgXc5yyrf5K49UU2J5JgFYpSp7aMGOUb1ibrj2sr-D63d61DtzFJ2mwrLm_KHBiN_ECpVhDsRvHe5iOx_APHtImevOUxghtkj-8RJruPgkTVaML2MEDOdL_UYaldeo-5ckZo3VHss7IpLArGOMTEd0bSH8tA8CL8RLQQeSokOMZ79Haxj8yE0EAVZ-k9-O72mmu5I0wH5IPgapNvExeX6O1l3mC4MqLhKPdOZOnTiEBlSrV4ZDH_9fhLUahe5ocZXvXqrud9QGNeTpZsSPeIYubeOC0sOsuqk10sWB7NP-lhifWeDob-IK1JWcgFTytVc99RkZTjUcdG9t8prPlKAagZIsDr1TiX3dy8sXKZ7d9EXQF5P_rHJ8xvmUtCWqbc3V5jL-qe8ANypwHsuva75Q6dtqoBR8vCE5xWgfwB0GzR3Xi_l7KDTsYAQIrDZVyY1UxdzWBwJCrvDrtrNsnt0S7BhBJ4ATCrW5VFPqXyXRiLxHCIv9zgo-NdBZQ4hEXXxMtbem3KgYUB1Rals1bbi8X8MsmselnHfY5LdOseyXWIR2QcrANSAypQUAhwVpsModw7HMdXgV9Uc-HwCMWafOChhBr88tOowqVHttPtwYorYrzriXNRt9LkigESMy1bEDx79CJguitwjQ9IyIEu8quEQb_-7AEXrfDzl_FKgASnnZLrAfZMtgyyddIhBpgAvgR_c8a8Nuro-RGV0aNuunVg8NjL8binz9kgmZvOS38QaP5anf2vgzJ9wC0ZKDg2Ad77dPjBCiCRtVe_dqm7FDA_cS97DkAwVfFawgce1wfWqsrjZvu4k6x3PAUH1UNzQUxVgOGUbqJsaFs3GZIMiI8O6-tZktz8i8oqpr0RjkfUhw_I2szHF3LM20_bFwhtINwg0rZxRTrg4il-_q7jDnVOTqQ7fdgHgiJHZw_OOB7JWoRW6ZlJmx3La8oV93fl1wMGNrpojSR0b6pc8SThsKCUgoY6zajWWa3CesX1ZLUtE7Pfk9eDey3stIWf2acKolZ9fU-gspeACUCN20EhGT-HvBtNBGr_xWk1zVJBgNG29olXCpF26eXNKNCCovsILNDgH06vulDUG_vR5RrGe5LsXksIoTMYsCUitLz4HEehUOd9mWCmLCl00eGRCkwr9EB557lyr7mBK2KPgJkXhNmmPSbDy6hPaQ057zfAd5s_43UBCMtI-aAs5NN4TXHd6IlLwynwc1zsYOQ6z_HARlcMpCV9ac-8eOKsaepgjOAX4YHfg3NekrxA2ynrvwk9U-gCtpxMJ4f1cVx3jExNlIX5LxE46FYIhQ"

    def __GetUserAgent__(self):
        """
             Get Random User Agent Function .
             ====================================
             Arguments :
                 self :
                       reCaptcha Version 3 Bypasser , Class Object .
                 =====================
             
        """
        user_agent_list = [
                            "Mozilla/5.0 (Windows 95; sl-SI; rv:1.9.1.20) Gecko/20180427 Firefox/37.0",
                            "Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/535.41.5 (KHTML, like Gecko) Version/5.0 Safari/535.41.5",
                            "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8 rv:5.0) Gecko/20190815 Firefox/36.0",
                            "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/5341 (KHTML, like Gecko) Chrome/39.0.800.0 Mobile Safari/5341",
                            "Opera/9.79 (X11; Linux x86_64; sl-SI) Presto/2.12.225 Version/12.00",
                            "Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/531.5.3 (KHTML, like Gecko) Version/4.0.4 Safari/531.5.3",
                            "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/5360 (KHTML, like Gecko) Chrome/38.0.821.0 Mobile Safari/5360"
                          ]
        return (choice(user_agent_list))

    def __GetURLData__(self):
        """
             Get Data Of Anchor URL Function .
             ====================================
             Arguments :
                 self :
                       reCaptcha Version 3 Bypasser , Class Object .
                 =====================
             
        """
        return {"EndPoints":((self.url).split("/")[4]), "Arguments":(((self.url).split("/")[5]).replace("anchor?", "").strip())}

    def __ArgToDict__(self):
        """
             Convert Arguments Data Of Anchor URL To Dict Function .
             ====================================
             Arguments :
                 self :
                       reCaptcha Version 3 Bypasser , Class Object .
                 =====================
             
        """
        return (dict((i.split("=")) for i in ((self.url_data["Arguments"]).split("&"))))

    def __Get_reCaptcha_Chalange_Token__(self):
        """
             Get reCaptcha Version 3 Chalange Token Function .
             ====================================
             Arguments :
                 self :
                       reCaptcha Version 3 Bypasser , Class Object .
                 =====================
             
        """
        res = self.session_req.get(
                                    url=("https://www.google.com/recaptcha/" + ((self.url_data["EndPoints"]) + "/anchor")),
                                    params=(self.url_data["Arguments"]),
                                    headers={
                                              "Host":"www.google.com",
                                              "User-Agent":(self.user_agent),
                                              "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                                              "Accpet-Language":"en-US,en;q=0.5",
                                              "Alt-Used":"www.google.com"
                                            }
                              )
        if res.status_code == 200:
            res = res.text
            res = BS(res, "html.parser")
            res = res.find("input").attrs["value"]
            return res
        else:
            return False

    def __Get_reCaptcha_Response__(self, captcha_token: str):
        """
             Get reCaptcha Version 3 Answer Response Function .
             ====================================
             Arguments :
                 self :
                       reCaptcha Version 3 Bypasser , Class Object .
                 =====================
                 captcha_token :
                                 string | reCaptcha Version 3 Chalange Token .
                 =====================
        """
        url_arg_data = self.__ArgToDict__()
        res = self.session_req.post(
                                      url=("https://www.google.com/recaptcha/" + ((self.url_data["EndPoints"]) + "/reload")),
                                      data=(self.captcha_response_post_data.format(
                                            (url_arg_data["v"]),
                                            captcha_token,
                                            (url_arg_data["k"]),
                                            (url_arg_data["co"])
                                            )),
                                      params=("k=" + url_arg_data["k"]),
                                      headers={
                                                "Host":"www.google.com",
                                                "User-Agent":(self.user_agent),
                                                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                                                "Accpet-Language":"en-US,en;q=0.5",
                                                "Alt-Used":"www.google.com",
                                                "Content-Type":"application/x-www-form-urlencoded"
                                              }
                               )
        if res.status_code == 200:
            res = res.text
            res = (re.findall(r'"rresp","(.*?)"', res))[0]
            return res
        else:
            return False

    def reCaptchaGoogleV3(self):
        """
             Main reCaptcha Version 3 Bypasser Function .
             ====================================
             Arguments :
                 self :
                       reCaptcha Version 3 Bypasser , Class Object .
                 =====================
        """
        captcha_token = self.__Get_reCaptcha_Chalange_Token__()
        if captcha_token != False:
            captcha_response = self.__Get_reCaptcha_Response__(captcha_token)
            if captcha_response != False:
                return {"Status":True, "reCaptchaResponse":captcha_response}
            else:
                print("Cannot Get reCaptcha Version 3 Response From Chalange Token .")
                return {"Status":False}
        else:
            print("Check Anchor URL !!! , Cannot Get reCaptcha Version 3 Chalange Token .")
            return None

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =================================================== #
# reCaptchaBypasser Library v1.4                      #
#                                                     #
# Class File Of Bypass Google reCaptcha Version 2 .   #
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


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as exp_con
import speech_recognition as Speech
from pydub import AudioSegment
from pydub.silence import split_on_silence
from time import sleep
import os
import wave
import requests


#== Class Of Bypass Google reCaptcha Version 2 ==#


class reCaptchaV2Scraper:
    """
        reCaptcha Version 2 Bypasser Class .
        ====================================
        Arguments :
             Driver :
                     webdriver variable
             =====================
             SearchElementTime :
                                integer | Searching Elements Wait Time(s).
             =====================
    """
    def __init__(self, Driver, SearchElementTime: int = 2):
        self.driver = Driver
        self.sleep = SearchElementTime

    def __Get_reCaptcha_Button__(self):
        """
             Find reCaptcha Button And Click On It Function .
             ================================================
             Arguments :
                 self :
                       reCaptcha Version 2 Bypasser , Class Object .
                 =====================
        """
        self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME, "iframe"))
        Button = WebDriverWait(self.driver, self.sleep).until(exp_con.presence_of_element_located((By.CSS_SELECTOR ,".recaptcha-checkbox-border")))
        Button.click()
        self.driver.switch_to.default_content()

    def __Get_reCaptcha_Audio_Button__(self):
        """
             Find reCaptcha Audio Button And Click On It Function .
             ================================================
             Arguments :
                 self :
                       reCaptcha Version 2 Bypasser , Class Object .
                 =====================
        """
        self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME, "iframe")[2])
        AudioButton = WebDriverWait(self.driver, self.sleep).until(exp_con.presence_of_element_located((By.CSS_SELECTOR ,"#recaptcha-audio-button")))
        AudioButton.click()
        self.driver.switch_to.default_content()

    def __Get_reCaptcha_Audio_Link__(self):
        """
             Find reCaptcha Audio Link Function .
             ================================================
             Arguments :
                 self :
                       reCaptcha Version 2 Bypasser , Class Object .
                 =====================
        """
        AudioLink  = self.driver.find_elements(By.TAG_NAME, "iframe")[2]
        self.driver.switch_to.frame(AudioLink)
        DownloadButton = WebDriverWait(self.driver, self.sleep).until(exp_con.presence_of_element_located((By.CSS_SELECTOR ,".rc-audiochallenge-tdownload-link")))
        Audio_Link = DownloadButton.get_attribute("href")
        return Audio_Link

    def __Send_reCaptcha_Audio_Text__(self, Text: str):
        """
             Write reCaptcha Audio Answer On Text Fild Function .
             ================================================
             Arguments :
                 self :
                       reCaptcha Version 2 Bypasser , Class Object .
                 =====================
                 Text :
                     string | reCaptcha Answer .
                 =====================
        """
        text_field = WebDriverWait(self.driver, self.sleep).until(exp_con.presence_of_element_located((By.CSS_SELECTOR ,"#audio-response")))
        text_field.send_keys(Text , Keys.ENTER)
        self.driver.switch_to.default_content()

    def __Check_reCaptcha_Status__(self):
        """
             Check reCaptcha Bypass Status Function .
             ================================================
             Arguments :
                 self :
                       reCaptcha Version 2 Bypasser , Class Object .
                 =====================
        """
        self.driver.switch_to.frame(WebDriverWait(self.driver, self.sleep).until(exp_con.presence_of_element_located((By.CSS_SELECTOR, "iframe[name^=a]"))))
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-checkmark")
            self.driver.switch_to.default_content()
            return True
        except Exception:
            self.driver.switch_to.default_content()
            return False

    def __Audio_Downloader__(self, Link):
        """
             reCaptcha Audio Downloader Function .
             ================================================
             Arguments :
                 self :
                       reCaptcha Version 2 Bypasser , Class Object .
                 =====================
                 Link :
                     string | reCaptcha Audio Link .
                 =====================
        """
        try:
            res = requests.get(Link)
        except Exception:
            print("Trying To Get reCaptcha Audio Data ...")
            sleep(0.4)
            self.__Downloader__(Link)
        else:
            try:
                os.path("Audio-Captcha").remove("audio.mp3")
            except Exception:
                pass
            audio_file = open("Audio-Captcha/audio.mp3", "wb")
            audio_file.write(res.content)
            audio_file.close()

    def __Get_reCaptcha_Audio__(self):
        """
             reCaptcha Audio Noise Remover And ,
             Adjust The Speed Of reCaptcha Audio Function .
             ================================================
             Arguments :
                 self :
                       reCaptcha Version 2 Bypasser , Class Object .
                 =====================
        """
        if not os.path.isdir("Audio-Captcha"):
            os.mkdir("Audio-Captcha")

        Link = self.__Get_reCaptcha_Audio_Link__()
        self.__Audio_Downloader__(Link)
        Sound = AudioSegment.from_mp3("Audio-Captcha/audio.mp3")
        GenVoice = split_on_silence(
                                  Sound,
                                  min_silence_len = 1200,
                                  silence_thresh = Sound.dBFS,
                                  keep_silence = 500
                                  )
        
        try:
            os.path("Audio-Captcha").remove("audio.wav")
        except Exception:
            pass
        File_Name = os.path.join("Audio-Captcha", "audio.wav")
        for Audio_Out in GenVoice:
            Audio_Out.export(File_Name, format="wav")  
        Audio_File = wave.open(File_Name, "rb")
        Audio_Rate = Audio_File.getframerate()
        Audio_Frame = Audio_File.readframes(-1)
        os.remove(File_Name)
        Audio_Out = wave.open(File_Name, "wb")
        Audio_Out.setnchannels(2)
        Audio_Out.setsampwidth(2)
        Audio_Out.setframerate(Audio_Rate - 5400)
        Audio_Out.writeframes(Audio_Frame)
        Audio_Out.close()

    def __Get_reCaptcha_Audio_Text__(self):
        """
             Get reCaptcha Audio Text Function .
             ================================================
             Arguments :
                 self :
                       reCaptcha Version 2 Bypasser , Class Object .
                 =====================
        """
        recog = Speech.Recognizer()
        Audio_File = Speech.AudioFile(r"Audio-Captcha/audio.wav")
        with Audio_File as SoundAudio:
            Audio = recog.record(SoundAudio)
        try:
            Text_Audio = recog.recognize_google(Audio)
        except Exception:
            try:
                Text_Audio = recog.recognize_google(Audio)
            except Exception:
                try:
                    Text_Audio = recog.recognize_google(Audio)
                except Exception:
                    return False
        return Text_Audio

    def reCaptchaGoogleV2(self):
        """
             Main Function Of reCaptcha Version 2 Bypasser Class .
             ================================================
             Arguments :
                 self :
                       reCaptcha Version 2 Bypasser , Class Object .
                 =====================
        """
        self.__Get_reCaptcha_Button__()
        sleep(1)
        self.__Get_reCaptcha_Audio_Button__()
        sleep(1)
        self.__Get_reCaptcha_Audio__()
        captcha_answer = self.__Get_reCaptcha_Audio_Text__()
        if captcha_answer != False:
            self.__Send_reCaptcha_Audio_Text__(captcha_answer)
            sleep(1)
            captcha_status = self.__Check_reCaptcha_Status__()
            if captcha_status == True:
                return {"Status":captcha_status, "reCaptchaText":captcha_answer}
            elif captcha_status == False:
                return {"Status":captcha_status}
        else:
            print("Cannot Get reCaptcha Audio Text .")
            return None

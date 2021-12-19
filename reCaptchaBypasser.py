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


class reCaptchaScraper:

    def __init__(self, Drivers):
        self.driver = Drivers
    
    def __reCaptchaButton__(self):
        self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME, "iframe"))
        Button = WebDriverWait(self.driver, 10).until(exp_con.presence_of_element_located((By.CSS_SELECTOR ,"#recaptcha-anchor")))
        Button.click()
        self.driver.switch_to.default_content()
    
    def __reCaptchaAudioButton__(self):
        self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME, "iframe")[2])
        AudioButton = WebDriverWait(self.driver, 10).until(exp_con.presence_of_element_located((By.CSS_SELECTOR ,"#recaptcha-audio-button")))
        AudioButton.click()
        self.driver.switch_to.default_content()

    def __reCaptchaAudioLink__(self):
        AudioLink  = self.driver.find_elements(By.TAG_NAME, "iframe")[2]
        self.driver.switch_to.frame(AudioLink)
        DownloadButton = WebDriverWait(self.driver, 10).until(exp_con.presence_of_element_located((By.CSS_SELECTOR ,".rc-audiochallenge-tdownload-link")))
        Audio_Link = DownloadButton.get_attribute('href')
        return Audio_Link

    def __reCaptchaTextFild__(self, Text):
        text_field = WebDriverWait(self.driver, 10).until(exp_con.presence_of_element_located((By.CSS_SELECTOR ,"#audio-response")))
        text_field.send_keys(Text , Keys.ENTER)
        self.driver.switch_to.default_content()

    def __reCaptchaChecked__(self):
        self.driver.switch_to.frame(WebDriverWait(self.driver, 10).until(exp_con.presence_of_element_located((By.CSS_SELECTOR, 'iframe[name^=a]'))))
        try:
            self.driver.find_element(By.CSS_SELECTOR, '.recaptcha-checkbox-checked')
            self.driver.switch_to.default_content()
            return True
        except Exception:
            self.driver.switch_to.default_content()
            return False
    
    def __Downloader__(self, Links):
        res = requests.get(Links)
        try:
            os.path("Audio-Captcha").remove("audio.mp3")
        except Exception:
            audio_file = open("Audio-Captcha/audio.mp3", "wb")
            audio_file.write(res.content)
            audio_file.close()
        else:
            audio_file = open("Audio-Captcha/audio.mp3", "wb")
            audio_file.write(res.content)
            audio_file.close()
    
    def __SoundCaptcha__(self):
        
        if not os.path.isdir("Audio-Captcha"):
            os.mkdir("Audio-Captcha")
        
        Link = self.__reCaptchaAudioLink__()
        sleep(2)
        self.__Downloader__(Links=Link)
        sleep(2)
        Sound = AudioSegment.from_mp3("Audio-Captcha/audio.mp3")
        GenVoice = split_on_silence(
                                  Sound,
                                  min_silence_len = 1200,
                                  silence_thresh = Sound.dBFS,
                                  keep_silence = 500
                                  )
        
        try:
            os.path("Audio-Captcha").remove("Voice.wav")
        except Exception:
            File_Name = os.path.join("Audio-Captcha", "Voice.wav")
            for Audio_Out in GenVoice:
                Audio_Out.export(File_Name, format="wav")
        else:
            File_Name = os.path.join("Audio-Captcha", "Voice.wav")
            for Audio_Out in GenVoice:
                Audio_Out.export(File_Name, format="wav")
            sleep(3)        
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
            
                    
                    
    def __SoundText__(self):
        
        recog = Speech.Recognizer()
        Audio_File = Speech.AudioFile(r"Audio-Captcha/Voice.wav")
        with Audio_File as SoundAudio:
            Audio = recog.record(SoundAudio)
        sleep(4)
        try:
            Text_Audio = recog.recognize_google(Audio)
        except Exception:
            try:
                Text_Audio = recog.recognize_google(Audio)
            except Exception:
                try:
                    Text_Audio = recog.recognize_google(Audio)
                except Exception:
                    False
                else:
                    return Text_Audio
            else:
                return Text_Audio
        else:
            return Text_Audio
        
    
    def reCaptchaGoogleV2(self):
        self.__reCaptchaButton__()
        sleep(2)
        self.__reCaptchaAudioButton__()
        sleep(2)
        self.__SoundCaptcha__()
        Key_Text = self.__SoundText__()
        self.__reCaptchaTextFild__(Text=Key_Text)
        sleep(4)
        reCaptchaResponse = self.__reCaptchaChecked__()
        return reCaptchaResponse

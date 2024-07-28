from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class speechify:

    def __init__(self, driver, language='persian', new_description=""):
        '''
        languages:
        persian, spanish, french, german, afrikaans, arabic
        '''
        self.driver = driver
        self.new_description = new_description
        self.language = language

    def check_popup(self):
        try:
            popup = self.driver.find_element(By.CSS_SELECTOR, '.modal.fade.ttso-signup-modal.show')
            if popup:
                close_button = popup.find_element(By.CSS_SELECTOR, 'button.btn-close')
                close_button.click()
                print("Popup closed.")
                return True
        except Exception as e:
            print("Not find POPUP windows !!!!!!!!")
            return False

    def paste_text(self, check=""):
        content_div = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea#article")))
        if check == "check":
            print("CHECK PASTE FANC")
            if content_div:
                time.sleep(1)
                entered_text = content_div.get_attribute('value')
                print(f"PRINT GPT RESPONSE: {self.new_description}")
                if entered_text != self.new_description:
                    print("Try paste respons.")
                    self.paste_text()
            else:
                print("Not find text AREA in check mode!")
                time.sleep(2)
                self.paste_text("check")
        else:
            if content_div:
                content_div.click()
                time.sleep(1)
                content_div.click()
            else:
                print("Not find text AREA !")
                time.sleep(2)
                self.paste_text()

            # Clear
            print("Clear with ctrl A")
            content_div.send_keys(Keys.CONTROL, 'a')
            content_div.send_keys(Keys.DELETE)
            time.sleep(2)
            # Input the desired text into the div
            content_div.send_keys(self.new_description)
            print("TEXT PASTE ... ")

            time.sleep(1)
            entered_text = content_div.get_attribute('value')
            if entered_text != self.new_description:
                print("Try paste respons.")
                self.paste_text()

    def text2speech(self, new_description):
        self.new_description = new_description
        print("New: ", self.new_description)
        self.driver.get(f'https://speechify.com/text-to-speech-online/{self.language}/')
        time.sleep(10)
        self.paste_text()
        time.sleep(2)
        self.play_text()

    def check_progress_bar(self):
        time.sleep(4)
        width_percentage = 0
        print("Wait for play text.")
        while width_percentage <= 90:
            progress_bar = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.progress-bar')))
            if progress_bar:
                style_attribute = progress_bar.get_attribute('style')
                width_percentage = int(style_attribute.split('width: ')[1].replace('%', '').replace(';', ''))
                print("progress bar : ", width_percentage)
            else:
                return False
        print("text PLAY!")
        return True

    def play_text(self):
        self.paste_text("check")
        play_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#page > main > div.ttso-iframe.text-to-speech-online.ttso-iframe-v3 > div.ttso-iframe-html > div.ttso-iframe-head.fixed-top > div.container.d-flex.align-items-center.justify-content-between > div.ttso-iframe-player.d-flex.align-items-center > div.ttso-iframe-center > button.ttso-iframe-play")))
        if play_button:
            play_button.click()
        else:
            self.check_popup()
            time.sleep(1)
            self.play_text("check")

        self.check_popup()
        if self.check_progress_bar() == False:
            self.check_popup()
            self.play_text()

from selenium import webdriver
import time


class SingleAccountBot():
    
    insta_url = 'https://www.instagram.com/'
    username = ''
    password = ''
    driver = ''
    path = ''
    options = webdriver.ChromeOptions()
    # options.add_experimental_option('prefs',  { "download.default_directory": "/run/media/maximiliank/Daten/Development/Projekte/instabot/download" } )

    def __init__(self, username="", password="", path=""):
        self.path = path
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path=self.path, chrome_options=self.options)

        self.driver.get('https://www.instagram.com/accounts/login/')

        time.sleep(3)
        username_field = self.driver.find_element_by_name('username')
        pw_field = self.driver.find_element_by_name('password')
        username_field.send_keys(self.username)
        pw_field.send_keys(self.password)
        pw_field.submit()

        print("Logged in as " + self.username)


    def open_profile(self, username=""):
        self.driver.get(self.insta_url + username + "/")

    
    def open_activity(self):
        self.driver.get("https://www.instagram.com/accounts/activity/")

    
    def open_followlist(self):
        self.driver.get("https://www.instagram.com/accounts/activity/?followRequests=1")


    def accept_follows(self):
        followlist_btns = self.driver.find_elements_by_xpath("//div/div/div/div/button")
        for btn in followlist_btns:
            if btn.text == 'Bestätigen':
                btn.click()
                print("accepted follow")


    def follow(self):
        follow_btn = self.driver.find_element_by_xpath("//header//section//button[1]")
        follow_btn.click()


    def open_ownprofile(self):
        self.open_profile(self.username)

    
    def close(self):
        settings_btn = self.driver.find_element_by_xpath("//header//section//div//button/span[@aria-label='Optionen']")
        settings_btn.click()
        logout_btn = self.driver.find_element_by_xpath("//body/div/div/div/div/button[last()-1]")
        logout_btn.click()
        self.driver.quit()


class NoAccountBot():

    insta_url = 'https://www.instagram.com/'
    driver = ''
    path = ''
    options = webdriver.ChromeOptions()
    # options.add_experimental_option('prefs',  { "download.default_directory": "/run/media/maximiliank/Daten/Development/Projekte/instabot/download" } )

    def __init__(self, path=""):
        self.path = path
        self.driver = webdriver.Chrome(executable_path=self.path, chrome_options=self.options)

        self.driver.get('https://www.instagram.com/')

        print("NoAccountBot started")

    def open_profile(self, username=""):
        self.driver.get(self.insta_url + username + "/")

    def check_existenz(self):
        try:
            error_headline = self.driver.find_element_by_xpath("//body/div/div/div/div/h2")
            if error_headline.text == 'Diese Seite ist leider nicht verfügbar.':
                return False
        except:
            return True
        return True

    def edit_profile(self):
        self.driver.get(self.insta_url + "accounts/edit/")

    def change_username(self, name):
        username_field = self.driver.find_element_by_id('pepUsername')
        username_field.clear()
        username_field.send_keys(name)
        time.sleep(1)
        submit_btn = self.driver.find_element_by_xpath("//body/div/section/main/div/article/form/div/div/div/button[1]")
        submit_btn.click()
        time.sleep(2)
        status = self.driver.find_element_by_xpath("//body/div/div/div/div/p")
        print(status.text)
        # Username not available
        if status.text == 'Dieser Benutzername ist nicht verfügbar. Bitte probiere einen anderen aus.':
            return 0
        # Username changed
        if status.text == 'Profil gespeichert.':
            return 1
        # Request rejected
        if status.text == 'Beim Speichern deines Profils ist ein Fehler aufgetreten.':
            return 2

        try:
            error_popup = self.driver.find_element_by_xpath("//body/div/div/div/button")
            if error_popup.text == 'Nochmal versuchen':
                return False
        except:
            return True
        return True

    def close(self):
        self.driver.quit()
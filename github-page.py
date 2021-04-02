# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options
import sys, fitz

from github import Github
from dotenv import load_dotenv
import unittest
import time
import re
import sys
import os
# import img2pdf

load_dotenv()
github_account = os.getenv('GITHUB_USERNAME')
github_passwd = os.getenv('GITHUB_PASSWORD')
g = Github(os.getenv('GITHUB_TOKEN'))
repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))
contents = repo.get_contents(os.getenv('GITHUB_REPOSITORY_FILE'))

class GithubLogin(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        self.driver.implicitly_wait(30)
        self.base_url = "https://github.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_github_login(self):
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_id("login_field").clear()
        driver.find_element_by_id("login_field").send_keys(github_account)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(github_passwd)
        driver.find_element_by_name("commit").click()
        driver.get(contents.html_url)
        time.sleep(3)
        page_height = driver.execute_script("return document.scrollingElement.scrollHeight;")
        driver.set_window_size(1366, page_height)
        time.sleep(2)
        driver.save_screenshot("saved_screenshots/page1.png")
        imglist=['saved_screenshots/page1.png']
        doc = fitz.open()
        for i, f in enumerate(imglist):
            img = fitz.open(f)
            rect = img[0].rect
            pdfbytes = img.convertToPDF()
            img.close()
            imgPDF = fitz.open("pdf", pdfbytes)
            page = doc.newPage(width = rect.width,
                            height = rect.height)
            page.showPDFpage(rect, imgPDF, 0) 
        doc.save("converted_pdfs/page1.pdf")
        # with open("converted_pdfs/page1.pdf","wb") as f:
	    #     f.write(img2pdf.convert('saved_screenshots/page1.png'))
        # el = driver.find_element_by_tag_name('body')
        # el.screenshot('here.png')

        driver.quit()

if __name__ == "__main__":
    unittest.main()

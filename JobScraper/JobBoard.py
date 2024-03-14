import math
import time
import numpy as np
import pandas as pd
from .Nav import nav
#from .Config import *
import pyautogui as gui
from random import random
from datetime import date
from splinter import Browser
from bs4 import BeautifulSoup as soup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class JobBoard:
    def __init__(self, JobTitle, JobLocation, DaysAgo):
        self.job_title = JobTitle
        self.job_location = JobLocation
        self.days_ago = DaysAgo
        self.browser = Browser('chrome')

    def __clear__(self, xpath):
        if self.browser.find_by_xpath(xpath).value!="":
        	try:
        	    self.__fill__(xpath, Keys.BACKSPACE)
        	    time.sleep(random()/4)
        	    self.__clear__(xpath)
        	except:
        	    print("cant delete")
    # Click a browsers tag based on the xpath
    def __click__(self, xpath):
        self.browser.find_by_xpath(xpath).click()    
        
    # Fill a browsers textbox
    def __fill__(self, xpath, filler):
        self.browser.find_by_xpath(xpath).fill(filler)

    # Scroll Css selector by pixel 
    def __scroll__(self, csSelect, start, end):
        self.browser.execute_script(
        f"document.querySelector('{csSelect}').scroll({start}, {end})") 
        
    def __pageScroll__(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        
    # Select the correct Date Bin For Filtering
    def __minDateBin__(self, date_bins):
        for day, label in date_bins:
            if self.days_ago<=day:
                return label
        return "Nope"
            
    # For DataFrame Storage
    def __fillSchema__(self, tag, ls, conv):
        if conv == "title":
            ls.append(np.nan) if tag == None\
            else ls.append(tag.get_text())
        elif conv == "txt":
            ls.append(np.nan) if tag == None\
            else ls.append(tag.get_text())
        elif conv == "href":
            ls.append(np.nan) if tag == None\
            else ls.append(tag.get('href'))
        else:
            raise Exception("Imporoper Conversion Tag Selected")
            
def noSeniors(df):
    return df.loc[(df["job_title"].str.contains("Senior") == False)]

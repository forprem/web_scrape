from .JobBoard import *

class Google(JobBoard):
    def __init__(self, JobTitle, JobLocation, DaysAgo):
        super().__init__(JobTitle, JobLocation, DaysAgo)
        
        # Visit Google
        self.browser.visit("http://www.google.com")
        
        # Fill Job Parameters
        self.browser.fill("textarea", self.job_title+" jobs in "+self.job_location)
        #Seach Google
        self.__click__(nav["Google"]["click1"])
        # Open Job Listings
        self.__click__(nav["Google"]["click2"])
        # Click On Locations
        self.__click__(nav["Google"]["click3"])
        # Adjust 30 miles Near Location
        self.__click__(nav["Google"]["click4"])
        # Click On Date Range 
        self.__click__(nav["Google"]["click5"])

        # VV EWWWWW VV
        # Select Date Range
        if self.days_ago>30:
            self.__click__(nav["Google"]["click6"][""])
        elif self.days_ago<=1:
            self.__click__(nav["Google"]["click6"][""])
        elif self.days_ago<=3:
            self.__click__(nav["Google"]["click6"][""])
        elif self.days_ago<=7:
            time.sleep(5)
            self.__click__(nav["Google"]["click6"][""])
        else:
            time.sleep(5)
            self.__click__(nav["Google"]["click6"][""])
            
        self.job_soup = soup(self.browser.html, 'html.parser')

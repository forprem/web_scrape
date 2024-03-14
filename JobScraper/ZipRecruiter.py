from .JobBoard import *

class ZipRecruiter(JobBoard):
    # Want to initialize in parrallel 
    def bottChallenge(self):
        x, y = (350, 440)
        try:
            time.sleep(random()*2+2)
            gui.moveTo(x, y, duration=random()*3/2)
            gui.click(x, y, 
                clicks=1, interval=2, 
                button='left')
            x -= 10
            time.sleep(random()*3)
            gui.moveTo(random()*x, random()*y, duration=random()) 
            self.bottChallenge()
        except:
            print("Failed Bott Check")
            self.bottChallenge()
                

    def __init__(self, JobTitle, JobLocation, DaysAgo):
        super().__init__(JobTitle, JobLocation, DaysAgo)
       
 
        # Define homepage navigations 
        def navigation():
            self.browser.visit("http://www.ziprecruiter.com")
            time.sleep(random()*2+1)
            self.__fill__(nav["ZipRecruiter"]["jobfill"], self.job_title)
            time.sleep(random()*2+1)
            self.__clear__(nav["ZipRecruiter"]["locfill"])
            self.__fill__(nav["ZipRecruiter"]["locfill"], self.job_location)
            time.sleep(random()*2+1)
            self.__click__(nav["ZipRecruiter"]["search"])
        # Manually Filter Displayed Jobs
        def filtered():
            1/self.browser.is_element_present_by_xpath(nav["ZipRecruiter"]["click1"])
            time.sleep(random()*4+2)
            # Click Past Userfill
            gui.click( x=500, y=400, 
                clicks=1, interval=2, 
                button='left')
            # Widden the radius for local job searches
            if self.job_location.lower()!="remote":
                self.__click__(nav["ZipRecruiter"]["radius1"])
                self.__click__(nav["ZipRecruiter"]["radius2"])
                time.sleep(random()*2+1)
            # Get Minimum date bucket 
            self.__click__(nav["ZipRecruiter"]["click1"])
            date_range = self.__minDateBin__([(1, "within_1_day"),
                                              (5, "within_5_day"),
                                              (10, "within_10_day"),
                                              (30, "within_30_day")])
            # Select Date Bucket, If dates' bounded
            if date_range != "Nope":
                time.sleep(random()*2+1)
                self.__click__(nav["ZipRecruiter"]["click2"][date_range])
            time.sleep(random()*2)
        # Add jobs to DataFrame
        def addJobs(available_jobs):
            time.sleep(random()*2+1)
            raw = soup(self.browser.html, 'html.parser').html
            for job in raw.find_all("div", class_="flex flex-col gap-24 md:gap-36"):
                available_jobs["job_search"].append(self.job_title)
                available_jobs["company"].append(job.find("a", class_="relative").get_text())
                available_jobs["job_title"].append(job.find("a").get_text())
                available_jobs["location"].append(job.find_all("a")[2].get_text())
                available_jobs["date_range"].append(date_range)
                available_jobs["link"].append(job.find("a").get("href"))
            return pd.DataFrame(available_jobs)
        
        
        navigation()
        try:
            filtered()
        except ZeroDivisionError:
            print("Running Bott Check")
            self.bottChallenge()
            filtered() 
       	except:
            print("Filter Failed for Some Reason")
         
        ## Add Jobs
        available_jobs = {"job_title": [], "company": [], "job_search": [],
                          "location": [], "date_range": [], "link": []}
        self.available_jobs = addJobs(available_jobs)

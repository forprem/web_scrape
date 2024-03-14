from .JobBoard import *

class Indeed(JobBoard):
    # Select the correct Date Bin For Filtering
    def __minDateBin__(self, date_bins):
        for i in range(len(date_bins)):
            if self.days_ago<=date_bins[i][0]:
                return i
        return "Nope"
    
    def __init__(self, JobTitle, JobLocation, DaysAgo):
        super().__init__(JobTitle, JobLocation, DaysAgo)
        
        
        def fillLocation():
            time.sleep(random()*2+1)
            # Fill Job's Location
            loc_tag = self.browser.find_by_css("#text-input-where")[0]
            loc_tag.clear()
            print("loc Tag", loc_tag.value)
            if (loc_tag.value==""):
                time.sleep(random()*2+1)
                # Will paste default value infront.., need to manually "type" into search bar
                loc_tag.fill(self.job_location)
            else:
                fillLocation()
        def addJobs(available_jobs):
            raw = soup(self.browser.html, 'html.parser').html
            raw.find_all("li", class_="css-5lfssm")
            try:
                for job in raw.find_all("div", class_="cardOutline"):
                    available_jobs["job_title"].append(job.find("span").get_text())
                    available_jobs["company"].append(job.find("span", class_="css-1x7z1ps eu4oa1w0").get_text())
                    available_jobs["location"].append(job.find("div", class_="css-t4u72d eu4oa1w0").get_text())
                    available_jobs["job_search"].append(self.job_title)
                    available_jobs["date_range"].append(self.days_ago)
            except:
                "No Jobs Available"
            return pd.DataFrame(available_jobs)

        
        ## Navigation
        # Visit Dice
        self.browser.visit("http://www.indeed.com") 
        time.sleep(random()+2)
        # Fill Job
        self.browser.find_by_css("#text-input-what").fill(self.job_title)
        time.sleep(random()+2)
        # Fill Location
#         fillLocation()
        # Click on Search
        self.__click__(nav["Indeed"]["click1"])
        
        
        ## Filter Jobs
        # Select Date Range
        time.sleep(random()*3+2)
        self.browser.find_by_id("filter-dateposted").click()
        date_range = self.__minDateBin__([(1, "last_24_hours"),
                                          (3, "last_3_days"),
                                          (7, "last_7_days"),
                                          (14, "last_14_days")])
        if date_range != "Nope":
            time.sleep(random()*2+1)
            date_selections=self.browser\
                .find_by_css(".is-dropdownOpen")[0]\
                .find_by_css("li")
            date_selections[date_range].click()
    
    
        ## Add Jobs
        available_jobs = {"job_title": [], "company": [],  "location": [], "job_search": [], 
                          "date_range": []}
        self.available_jobs = addJobs(available_jobs)

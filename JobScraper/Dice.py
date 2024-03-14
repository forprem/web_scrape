from .JobBoard import *

class Dice(JobBoard):
    def __init__(self, JobTitle, JobLocation, DaysAgo):
        super().__init__(JobTitle, JobLocation, DaysAgo)

            
        ## Scroll Pages and add Available Jobs List
        def getJobs(available_jobs):
            more = True
            time.sleep(random()*2+1)
            # Collect Unique Jobs as a Tile
            def addJobs(available_jobs):
                raw = soup(self.browser.html, 'html.parser').html
                for job in raw.find_all("dhi-search-card"):
                    available_jobs["company"].append(job.find("a", class_="ng-star-inserted").get_text())
                    available_jobs["job_title"].append(job.find("a", class_="card-title-link normal").get_text())
                    available_jobs["description"].append(job.find("div", class_="card-description").get_text())
                return available_jobs
            new_jobs = addJobs(available_jobs)
            # If on last page terminate loop
            try:
                self.browser\
                    .find_by_css("li[class='pagination-next page-item ng-star-inserted disabled']")\
                    .is_visible()
                more = False
            except:
                # Else Navigate to next page and get pages' jobs
                time.sleep(random()*2); self.__pageScroll__()
                self.browser.find_by_css(".pagination > li")[-1].click()
            return getJobs(new_jobs) if more else new_jobs
        
        
        ## Navigation
        # Visit Dice
        self.browser.visit("http://www.dice.com/jobs") 
        # Fill Job
        self.__fill__(nav["Dice"]["fill1"], self.job_title)
        # Fill Job's Location
        self.__fill__(nav["Dice"]["fill2"], self.job_location)
        # Click on Search
        self.__click__(nav["Dice"]["search"])

        
        ## Filter Results
        # Select in Person- If non remote else
        if self.job_location.lower()=="remote":
            self.__click__(nav["Dice"]["location"]["remote"])
        else:
            self.__click__(nav["Dice"]["location"]["in-person"]) 
        # Select Date Range
        date_bin = self.__minDateBin__([(0, "last_day"),(1, "last_3"),(6, "last_7")])
        if date_bin != "Nope":
            self.__click__(nav["Dice"]["click3"][date_bin])
#         # Show 100 Jobs/Page
#         self.browser.select("pageSize_2")
    
    
        ## Add Jobs
        available_jobs = {"company": [], "job_title": [], "description": []}            
        self.available_jobs = pd.DataFrame(getJobs(available_jobs))

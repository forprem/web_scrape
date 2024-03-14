from .JobBoard import *

class Monster(JobBoard):
    def __init__(self, JobTitle, JobLocation, DaysAgo):
        super().__init__(JobTitle, JobLocation, DaysAgo)  
 

        def clicker():
            print("Trying Filter Click...")
            time.sleep(random()*3+2); self.__click__(nav["Monster"]["click2"])
            if self.browser.is_element_present_by_xpath(nav["Monster"]["click3"]):
                print("Filter Clicked"); return
            clicker()
            
        # Scroll and Collect All Available Jobs
        def addJobs(start, available_jobs, date_range):
            time.sleep(random()*3)
            # Load all Jobs
            def loadMore(acc):
                # Are There Any Results?
                condition = self.browser\
                    .find_by_css('.job-search-resultsstyle__LoadMoreContainer-sc-1wpt60k-0')\
                    .value != "No More Results"
                # Any More Results?
                if condition:
                    # Scroll Side-Bar to Bottom then up a Little
                    self.__scroll__('#card-scroll-container', acc, (acc + 300)); time.sleep(random()*1.5)
                    self.__scroll__('#card-scroll-container', (acc + 300), (acc + 290))
                    time.sleep(random()*.7); loadMore(acc + 1000)              
            loadMore(0); return parseJob(available_jobs, date_range)
        # Parse all Jobs on the page
        def parseJob(available_jobs, date_range):
            job_soup = soup(self.browser.html, 'html.parser').html.find_all("li", class_="sc-blKGMR")
            for i in range(len(job_soup)-2):
                x = job_soup[i].find("a").get("href")
                self.__fillSchema__(job_soup[i].find("a"), available_jobs["job_title"], "title")
                self.__fillSchema__(job_soup[i].find("span", class_="sc-kufkCr"), available_jobs["company"], "txt")
                self.__fillSchema__(job_soup[i].find("span", class_="sc-fICZUB"), available_jobs["location"], "txt")
                self.__fillSchema__(job_soup[i].find("a"), available_jobs["link"], "href")
                available_jobs["job_search"].append(self.job_title)
                available_jobs["date_range"].append(date_range)
            return pd.DataFrame(available_jobs)

        ## Navigation
        start = time.perf_counter()
        # Visit Dice
        self.browser.visit("http://www.monster.com") 
        # Fill Job
        self.browser.find_by_css("#horizontal-input-one-undefined").fill(self.job_title)
        # Fill Job's Location
        self.browser.find_by_css("#horizontal-input-two-undefined").fill(self.job_location)
        # Click on Search
        self.__click__(nav["Monster"]["click1"])
         
        
        ## Filter Results
        clicker()
        # Select In-Person (If Non-Remote)
        if self.job_location.lower()=="remote":
            self.__click__(nav["Monster"]["click3"])
        # Select Date Range
        date_range = self.__minDateBin__([(0, "today"),(1, "last_2"),(6, "last_week"),
                                    (13, "last_2_weeks"),(29, "last_month")])
        if date_range != "Nope":
            self.__click__(nav["Monster"]["click4"][date_range])
        # Confirm Filters
        self.__click__(nav["Monster"]["click5"])
        time.sleep(random()*4)
    
    
        ## Add Jobs
        available_jobs = {"company": [], "job_title": [], "job_search": [], "location": [], 
                          "date_range": [], "link": []}
        try:
            self.available_jobs = addJobs(start, available_jobs, date_range) 
        except:
            print("Failed to Scroll")
            self.available_jobs = parseJob(available_jobs, date_range)

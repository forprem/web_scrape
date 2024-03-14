from .JobBoard import *

class LinkedIn(JobBoard):
    def __init__(self, JobTitle,  JobLocation, DaysAgo):
        super().__init__(JobTitle, JobLocation, DaysAgo)


 #        # Scroll to bottom of component and click to final page
 #        def loadMore(page):
 #            try:
 #                self.__scroll__('.jobs-search-results-list', acc, (acc + 2100)); time.sleep(random()*1.5)
 #                addJobs()
 #                self.browser.find_by_css('.artdeco-pagination__pages')[page].click()
 #            except:
 #                "On The Last Page"
        # Parse Job and add too available jobs
        def addJobs(available_jobs):
            time.sleep(random()*2+1)
            raw = soup(self.browser.html, 'html.parser').html
            tags = raw.find("ul", class_="scaffold-layout__list-container").find_all("li", class_="ember-view")
            for i in range(len(tags)):
                try:
                    available_jobs["job_title"].append(tags[i].find("a").get_text().split("\n")[1][20:])
                    available_jobs["link"].append(tags[i].find("a").get("href"))
                    available_jobs["location"].append(self.job_location+" | Remote")
                    available_jobs["company"].append(
                        tags[i].find("span", class_="job-card-container__primary-description")\
                        .get_text().split("\n")[1])
                    available_jobs["date_range"].append(self.days_ago)
                    available_jobs["job_search"].append(self.job_title)
                except:
                    "Tag doesn't have a Job"
            return pd.DataFrame(available_jobs)
        
        
        ## Navigation
        # Visit Linkedin
        self.browser.visit("https://www.linkedin.com")
        # If First Time
        self.__fill__(nav["LinkedIn"]["userfill"], username)
        self.__fill__(nav["LinkedIn"]["passfill"], password)
        self.__click__(nav["LinkedIn"]["clickloggin"])
        self.browser.visit("https://www.linkedin.com/jobs/?") 
        search = self.browser.find_by_css("input")
        search[0].fill(self.job_title)
        search[3].fill(self.job_location+Keys.ENTER)
        
        
        ## Filter Jobs
        # Widden Search Radius
        time.sleep(random()*2+1)
        try:
            self.browser.find_by_css(".search-reusables__primary-filter")[1].find_by_css(".artdeco-pill").click()
        except:
            self.__click__(nav["LinkedIn"]["radius1"])	
        time.sleep(random()*2)
        touch = self.browser.find_by_id("distance-filter-bar-slider")
        gui.click(
            x=350, 
            y=300,
            clicks=1, 
            interval=2, 
            button='left')
        time.sleep(random()*2)
        gui.click(
            x=600, 
            y=1200,
            clicks=1, 
            interval=2, 
            button='left')
        # Select Date Range
        time.sleep(random()*4+2)
	# Want to integrating __click__ with both xpath and default gui click
        self.__click__(nav["LinkedIn"]["click1"])
        date_range = self.__minDateBin__([(1, "past_24_hours"),
                                          (7, "past_week"),
                                          (30, "past_month")])
        if date_range != "Nope":
            time.sleep(random()*2+1)
            self.__click__(nav["LinkedIn"]["click2"][date_range])
        time.sleep(random()*2)
        self.__click__(nav["LinkedIn"]["click3"])

        
        ## Add Jobs
        available_jobs = {"company": [], "job_title": [], "job_search": [],
                          "location": [], "date_range": [], "link": []}
        self.available_jobs = addJobs(available_jobs)

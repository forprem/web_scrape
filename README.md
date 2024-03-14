# Job Scraper
## Overview
This python package automates the collection of this job data from the top 6 search engines, LinkedIn, ZipRecruiter, Indeed, Monster, Dice, and Google.

### Purpose
Using selenium, beautifulSoup, and pyautogui this python-based webscraper has three main functions.

It first navigates a job board's homepage and searches for the user's specified job title/location.

Then, it will filter the results (in the website) by widening the search radius (to within 100 miles), excluding remote positions (if not remote), and 
eliminating jobs outside the search window's timeframe.

Finally, it writes each dataframe to its respective subdirectory with the date and whether the search was remote.
## 
### Abstract Class - JobBoard.py
To Define a new Jobboard- regardless of type- they must have
- JobTitle: Whats the Job
- JobLocation: Wheres the Job
- DaysAgo: How old is the Job Listing

In return, an instantiated object will have an attribute browser that will let you manually interact
with Chrome WebDriver.
        
Available Methods for New Class Extensions:
- \__clear__(self, xpath): Manually delete each character if WebDriver clear fails.
- \__click__(self, xpath): Click a browsers tag based on the xpath
- \__fill__(self, xpath, filler): Fill a browsers textbox
- \__scroll__(self, csSelect, start, end): Scroll Css selector by pixel 
- \__pageScroll__(self): Scroll to the Bottom
- \__minDateBin__(self, date_bins): Select the correct Date Bin For Filtering
- \__fillSchema__(self, tag, ls, conv): For DataFrame Storage

*Example 1*:

"Get all Data Engineer Jobs from Indeed in the last week from Centennial Colorado"

    python3> Indeed("Data Engineer", "Centennial Colorado", 7)

*Example 2*: 

Reference `scraper.py` for a more complex query.

## Required Libraries
setuptools, numpy, pandas, pyautogui, splinter, beautifulsoup4, selenium

## Summary
This package allows for easy automation of scraping job data. Using a scheduler like chron, one can set and leave this script- only considering the aggregated job's data.

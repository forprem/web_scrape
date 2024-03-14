from JobScraper import *
from datetime import date


def __main__(days_ago, location):
	todays_date = str(date.today()) if (location.lower() != "remote") else "remote_"+str(date.today())

	def clean(df):
		grouped = df\
                    .groupby(["job_title", "company"]).sum()\
                    .reset_index()\
                    .sort_values("job_title"); return noSeniors(grouped)

 #	# Dice Listings
 #	dice_listings = pd.concat([
 #		Dice("SQL Analyst", location, days_ago).available_jobs,\
 #		Dice("Data Analyst", location, days_ago).available_jobs,\
 #		Dice("Data Scientist", location, days_ago).available_jobs,\
 #		Dice("Data Engineer", location, days_ago).available_jobs],
 #                ignore_index = True)
 #	clean(dice_listings).to_csv("Listings/Dice/"+todays_date+".csv")
 #
 #	# Indeed Listings
 #	indeed_listings = pd.concat([
 #		Indeed("SQL Analyst", location, days_ago).available_jobs,\
 #		Indeed("Data Analyst", location, days_ago).available_jobs,\
 #		Indeed("Data Scientist", location, days_ago).available_jobs,\
 #		Indeed("Data Engineer", location, days_ago).available_jobs],
 #                ignore_index = True)
 #	clean(indeed_listings).to_csv("Listings/Indeed/"+todays_date+".csv")
 #
	# LinkedIn Listings
	linkedin_jobs = pd.concat([
		LinkedIn("SQL Analyst", location, days_ago).available_jobs,\
		LinkedIn("Data Analyst", location, days_ago).available_jobs,\
		LinkedIn("Data Scientist", location, days_ago).available_jobs,\
		LinkedIn("Data Engineer", location, days_ago).available_jobs],
                ignore_index = True)
	clean(linkedin_jobs).to_csv("Listings/LinkedIn/"+todays_date+".csv")
 #
 #	# Zip Recruiter Listings
 #	zip_listings = pd.concat([
 #		ZipRecruiter("SQL Analyst", location, days_ago).available_jobs,\
 #		ZipRecruiter("Data Analyst", location, days_ago).available_jobs,\
 #		ZipRecruiter("Data Scientist", location, days_ago).available_jobs,\
 #		ZipRecruiter("Data Engineer", location, days_ago).available_jobs],
 #                ignore_index = True)
 #	clean(zip_listings).to_csv("Listings/ZipRecruiter/"+todays_date+".csv")
 #
 #	# Monster Listings
 #	monster_listings =  pd.concat([
 #		Monster("SQL Analyst", location, days_ago).available_jobs,\
 #		Monster("Data Analyst", location, days_ago).available_jobs,\
 #		Monster("Data Scientist", location, days_ago).available_jobs,\
 #		Monster("Data Engineer", location, days_ago).available_jobs],
 #                ignore_index = True)
 #	clean(monster_listings).to_csv("Listings/Monster/"+todays_date+".csv")


__main__(0, "Centennial, Colorado")
__main__(0, "remote")

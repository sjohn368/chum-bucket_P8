#import beautifulsoup and request here
import urllib.request
import bs4
import json


def displayJobDetails():
    print("Display job details")

#function to get job list from url 'https://www.indeed.com/jobs?q={role}&l={location}'
def getJobList(role,location):
    url = 'https://www.indeed.com/jobs?q={role}&l={location}'
    # Complete the missing part of this function here 
    jobURL = urllib.request.urlopen('https://www.indeed.com/jobs?q={role}&l={location}')
    jobData = jobURL.read()
    print(jobData)
    
#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    print("Saving data to JSON")

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    # Complete the missing part of this function here
    print("Enter the Location to search")
    location = input()
    
if __name__ == '__main__':
    main()

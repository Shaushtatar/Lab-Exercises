import requests
import json
import csv
endpoint  = "https://newsapi.org/v2/top-headlines"
params = {
    #"q" : "upstate new york",
    "language" : "en", 
    "country" : "us",
    "from" : "2024-09-12T01:30:31",
    "to" : "2024-09-19T01:30:31", 
    "apiKey" : "d2570b7a57944f93b45f3440ec57aff4" #this is my API key
}

stories = requests.get(endpoint, params = params)
json_news = stories.json()
print(json_news)

#For some reason, adding search query filtered all of the results
#I got rid of everything else, and I know query is causing it
#I tried different queries and I know it is not due to this specific one
#So I am just going to do the program with top US headlines in general

csv_file = open("storydata.csv", "w", newline = "", encoding = "utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Title", "Author", "Outlet", "URL"])

for i in json_news["articles"]:
    csv_writer.writerow([i["title"], i["author"], i["source"]["name"], i["url"]])

csv_file.close()
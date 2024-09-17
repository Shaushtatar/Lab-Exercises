import requests
key = "ca700e695888301850ac59bc05f8c1370bef368b"
url = f"https://api.census.gov/data/2019/pep/charagegroups?get=NAME,POP&HISP=2&for=state" #:*&key={key}
request = requests.get(url)
#we used the URL given to us by the census bureau  https://api.census.gov/data/2019/pep/charagegroups?get=NAME,POP&HISP=2&for=state:*
#and then added &key={key}
#& in URL means 
census_dict = {}
jsonlist = request.json()
for i in jsonlist:
    census_dict[i[0]] = i[1]


print(census_dict)



'''Use a predicate clause starting with an ampersand (&) to separate it
 from your get clause and then a for followed by an in clause, if needed; 
 e.g., &for=state:. Because we are looking for information in all the states,
   add a wildcard (*) to indicate all values; e.g.,  state:*.'''

#?get is the query, it is calling for information. This tends to be the function of the question mark


#Let's try our own
url2 = "http://api.census.gov/data/2020/cps/voting/nov?get="
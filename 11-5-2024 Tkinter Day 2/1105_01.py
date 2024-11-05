#Let's try accessing our weather API using tkinter buttons, and showing it in a window
import requests
import json
import tkinter as tk
#latitude = "42.098701"
#longitude = "-75.912537"
label = []
def get_weather(lat, lon):
    weather = requests.get(f"https://api.weather.gov/points/{lat},{lon}")
    json_weather = weather.json()
    isolated_forecast = json_weather["properties"]["forecast"]
    forecast = requests.get(isolated_forecast).json()

    for section in forecast["properties"]["periods"]:
        
        day = section["name"]
        temp = section["temperature"]
        detail = section["detailedForecast"] #all of this is copied from our 9/19 classwork
        label = tk.Label(root, text=f"{day}: {temp} \n -----") #we can reuse these labels because we pack them right after
        label.pack()
def close_window():
    root.destroy()

root = tk.Tk()
root.title("Dropdown practice")
root.geometry("400x700") 

'''
Tkinter doesn't let us use our Python variables, we have to use specific Tkinter variables 
Our options are: BooleanVar(), StringVar(), IntVar(), DoubleVar()
You do two things with these:
set() - sets the default value
get() - retrieves a value 

So have to tie the tkinter objects we get from doing stuff in tkinter to python variables

'''

lat = tk.StringVar() 
lat.set("")
lon = tk.StringVar()
lon.set("")

entry_lat = tk.Entry(root, textvariable = lat) #it is better to separate labels from entries, even though entries have built in labels
latlabel = tk.Label(root, text = "Latitude")
entry_lon = tk.Entry(root, textvariable = lon)
lonlabel = tk.Label(root, text = "Longitude:")


button = tk.Button(root, text="Get Forecast", font = 24, command=lambda: get_weather(lat.get(), lon.get()))
#the lambda function is an "anonymous function" that allows us to pass functions with arguments in buttons
#font changes font size. This just makes it bigger or smaller -- in this case, bigger.
exit = tk.Button(root, text = " X ", bg = "red2", command = close_window)
#https://www.geeksforgeeks.org/change-color-of-button-in-python-tkinter/
exit.pack()
latlabel.pack()
entry_lat.pack()
lonlabel.pack()
entry_lon.pack()
button.pack(pady = 50) #pad y -- creates buffer space between the button and everything else with respect to the y-axis

root.mainloop()
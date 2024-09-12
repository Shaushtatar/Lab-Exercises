from PIL import Image
import os
import csv
import random
path = "C:\\Users\\billy\\OneDrive\\Documents\\GitHub\\Lab-Exercises\\Lab 3\\Rorschach Images"
    #This list will be used by writerow for our column names
csv_file = open("Rorschach_responses.csv", "w",newline = "", encoding = "utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Name", "RorNum", "Response"])
x=0
while x != 1:
    answer = ""
    while answer != "Y" and answer != "N":
        answer = input("Would you like to take the test? (Y/N)")
        if answer.upper() != "Y" and answer != "N":
            print("Please input a valid answer.")
    if answer == "Y":
        name = input("What is your name?") #goes before for loop b/c it'd be tedious to re-enter name 5 times
        for j in range(5):
            num = random.randint(0,31)
            image = Image.open(f"{path}\\Ror{str(num)}.png")
            image.show()
            resp = input("What do you see in this picture?")
            csv_writer.writerow([name, num, resp])
    else:
        x = 1
csv_file.close()


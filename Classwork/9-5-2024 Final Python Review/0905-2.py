import csv
import random
import names
csv_file = open("csv_for_loop_ex.csv", "w", newline = "", encoding = "utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Name", "Age"])

#let's try using a for loop to fill out the csv

for i in range(10):
    name = names.get_full_name()
    age = random.randint(1,100)
    csv_writer.writerow([name, age])

csv_file.close()
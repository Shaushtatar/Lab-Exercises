#csv creation and opening
import csv
csv_file = open("FILENAME.csv", "w",newline = "", encoding = "utf-8")
#this creates a csv file with name "FILENAME.csv", w means write, and newline is blank
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["COLUMN NAME", "COLUMN NAME"])

csv_file.close()

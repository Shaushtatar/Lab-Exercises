import random
file_path = "C:\\Users\\billy\\OneDrive\\Documents\\Python Scripts\\sowpods.txt"
with open(file_path, "r", encoding="utf8") as f:
    #the with line is the same as this below:
    #f = open(filename, "r", encoding="utf8")
    words = f.readlines()
    f.close()

word = random.choice(words).strip()
print(word)
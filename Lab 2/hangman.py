from PIL import Image
word = "teaching"
file_path = "C:\\Users\\billy\\OneDrive\\Documents\\Python Scripts\\png images"
stage = [Image.open(f"{file_path}\\one_limb.png"), Image.open(f"{file_path}\\two_limbs.png"),
         Image.open(f"{file_path}\\three_limbs.png"), Image.open(f"{file_path}\\four_limbs.png"),
         Image.open(f"{file_path}\\five_limbs.png"), Image.open(f"{file_path}\\six_limbs.png")]
letterlist = []
blank_list = []

for letter in word:
  letterlist.append(letter)
  blank_list.append("_")

def lettersearch(letter):
  for x in letterlist:
    if letter == x:
      position = letterlist.index(x)
      blank_list[position] = x


def hangman():
  attempts = 0
  while attempts < 6:
    for x in letterlist:
      if letter == x:
        position = letterlist.index(x)
        blank_list[position] = x

      if letter == x:
        position = letterlist.index(x)
        blank_list[position] = x

      if letter == x:
        position = letterlist.index(x)
        blank_list[position] = x


def hangman():
  attempts = 0
  while attempts < 6:
    print(" ")
    guess = input("please guess one letter: ")
    if guess in letterlist:
      print(" ")
      print("You guessed correctly!")
      lettersearch(guess)
      print(blank_list)
    else:
      attempts += 1
      print(" ")
      print(f"Wrong. {6 - attempts} attempts left.")
      stage[attempts-1].show()
    if blank_list == letterlist:
      print(" ")
      print("You won!")
      break
  if attempts == 6:
    print(" ")
    print("You lose, sorry!")
hangman()
#resources used:
#https://shorturl.at/7kkYU -- how to use .index()
#Partner: Emma Sainovic
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
         ]

USERS = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

titledWords = 0
upperWords = 0
lowerWords = 0
numericWords = 0
sumOfNumbers = 0
textCount = len(TEXTS)

print("-" * 65)
print("Welcome to TextApp. Please log in.")
print("-" * 65)
username = input("Username: ")
password = input("Password: ")
if (username not in USERS.keys()) or (password != USERS[username]):
    print("Username or password is not correct!")
    exit()

print("-" * 65)
print(f"We have {textCount} texts to be analyzed.")
try:
    textNumber = int(input(f"Enter a number between 1 and {textCount} to select: ")) - 1
except:
    print(f"You did not enter a number.")
    exit()

if textNumber < 1:
    print(f"OK, this should work, but I asked you for a number between 1 and {textCount}.")
    exit()

print("-" * 65)

try:
    splittedTexts = TEXTS[textNumber].split()
except:
    print(f"The number is not between 1 and {textCount}.")
    exit()

wordsCount = len(splittedTexts)

for word in splittedTexts:
    if word.istitle():
        titledWords += 1
    elif word.isupper():
        upperWords += 1
    elif word.islower():
        lowerWords += 1
    elif word.isnumeric():
        numericWords += 1
        sumOfNumbers += int(word)

print(f"Here is the text of your choice:")
print(TEXTS[textNumber])
print("-" * 65)
print(f"There are {wordsCount} words in the selected text.")
print(f"There are {titledWords} titlecase words.")
print(f"There are {upperWords} uppercase words.")
print(f"There are {lowerWords} lowercase words.")
print(f"There are {numericWords} numeric strings.")
print("-" * 65)

words = []
words = TEXTS[textNumber].replace(",", "").replace(".", "").split()
counts = {}
for word in words:
    counts[len(word)] = counts.setdefault(len(word), 0) + 1

for key in sorted(counts):
    print(f"{key} {(counts[key]) * '*'} {counts[key]}")

print("-" * 65)
print(f"If we summed all the numbers in this text we would get: {float(sumOfNumbers)}")
print("-" * 65)

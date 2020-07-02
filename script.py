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

USERS = {"bob":"123","ann":"pass123","mike":"password123","liz":"pass123"}

titledWords = 0
upperWords = 0
lowerWords = 0
numericWords = 0
sumOfNumbers = 0
textCount = len(TEXTS)

print("-" * 60)
print("Welcome to TextApp. Please log in.")
print("-" * 60)
username = input("Username: ")
password = input("Password: ")
if (username not in USERS.keys()) or (password != USERS[username]):
    print("Username or password is not correct!")
    exit()

print("-" * 60)
print(f"We have {textCount} texts to be analyzed.")
textNumber = int(input(f"Enter a number btw. 1 and {textCount} to select: "))-1
print("-" * 60)

splittedTexts = TEXTS[textNumber].split()
wordsCount = len(splittedTexts)

for word in splittedTexts:
    if word.istitle():
        titledWords += 1

for word in splittedTexts:
    if word.isupper():
        upperWords += 1

for word in splittedTexts:
    if word.islower():
        lowerWords += 1

for word in splittedTexts:
    if word.isnumeric():
        numericWords += 1
        sumOfNumbers += int(word)

print(f"There are {wordsCount} words in the selected text.")
print(f"There are {titledWords} titlecase words.")
print(f"There are {upperWords} uppercase words.")
print(f"There are {lowerWords} lowercase words.")
print(f"There are {numericWords} numeric strings.")
print("-" * 60)

words = []
words = TEXTS[textNumber].replace(",","").replace(".","").split()
counts = {}
for word in words:
  if (counts.get(len(word))==None):
    counts.setdefault(len(word),1)
  else:
    counts[len(word)] += 1
for key in sorted(counts):
  print(f"{key} {(counts[key])*'*'} {counts[key]}")

print("-" * 60)
print(f"If we summed all the numbers in this text we would get: {float(sumOfNumbers)}")
print("-" * 60)
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

l_titledWords = 0
l_upperWords = 0
l_lowerWords = 0
l_numericWords = 0
l_sumOfNumbers = 0

print("-" * 60)
print("Welcome to TextApp. Please log in.")
print("-" * 60)
l_username = input("Username: ")
l_password = input("Password: ")
if l_username in USERS.keys():
    if not(l_password == USERS[l_username]):
        print("Username or password is not correct!")
        exit()
else:
    print("Username or password is not correct!")
    exit()

print("-" * 60)
print("We have 3 texts to be analyzed.")
l_textNumber = int(input("Enter a number btw. 1 and 3 to select: "))-1
print("-" * 60)

l_wordsCount = len(TEXTS[l_textNumber].split())
for word in TEXTS[l_textNumber].split():
    if word.istitle():
        l_titledWords += 1

for word in TEXTS[l_textNumber].split():
    if word.isupper():
        l_upperWords += 1

for word in TEXTS[l_textNumber].split():
    if word.islower():
        l_lowerWords += 1

for word in TEXTS[l_textNumber].split():
    if word.isnumeric():
        l_numericWords += 1
        l_sumOfNumbers += int(word)


print(f"There are {l_wordsCount} words in the selected text.")
print(f"There are {l_titledWords} titlecase words.")
print(f"There are {l_upperWords} uppercase words.")
print(f"There are {l_lowerWords} lowercase words.")
print(f"There are {l_numericWords} numeric strings.")
print("-" * 60)

l_words = []
l_words = TEXTS[l_textNumber].replace(",","").replace(".","").split()
l_counts = {}
for word in l_words:
  if (l_counts.get(len(word))==None):
    l_counts.setdefault(len(word),1)
  else:
    l_counts[len(word)] += 1
for key in sorted(l_counts):
  print(f"{key} {(l_counts[key])*'*'} {l_counts[key]}")

print("-" * 60)
print(f"If we summed all the numbers in this text we would get: {float(l_sumOfNumbers)}")
print("-" * 60)
"""
project_1.py: První projekt do Engeto Online Python Akademie

author: Lucia Solčanová
email: lucia.solcanova@gmail.com
discord: Lucka #0676
"""


from pprint import pprint

# Text "task template" a oddělovač

text_list = ['''
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

# separator = '----------------------------------------'
# lenght_of_separator = len(separator)
# print(lenght_of_separator)
separator = '-' * 40

# Registrovaní uživatelé

registrated_users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# Přihlášení uživatele

user_name = input('username: ').lower()
password = input('password: ').lower()
print(separator)

# Uvítání uživatele, pokud splňuje podmínky

if registrated_users.get(user_name) == password:
    print(f'Welcome to the app, {user_name.capitalize()}'.center(len(separator)))
    print('We have 3 texts to be analyzed.'.center(len(separator)))
else:
    print('Unregistrated user, terminating the program...')
    quit()

print(separator)

# Výběr textu uživatelem se zadanými podmínkami

user_number = input('Enter a number btw. 1 and 3 to select: ')
print(separator)

if user_number.isnumeric() and int(user_number) in range(1, 4):
    user_selection = text_list[int(user_number) -1]
    print(f'{user_selection}\n')
    print(separator)
else:
    print('Selection is not correct, terminating the program...')
    quit()

# Vyčistíme texty a odstraníme interpunkci

clear_list = []

for one_word in user_selection.split():
    clean_word = one_word.strip(',.')
    clear_list.append(clean_word)
# print(clear_list)

# Statistiky pro vybraný text:

#   počet slov

number_of_words = len(clear_list)
print(f'There are {number_of_words} words in the selected text.')

# Statistiky

title_case = 0
upper_case = 0
lower_case = 0
numeric = 0
sum = 0        #možná by šlo aplikovat funkci "sum"?

for index in clear_list:
    if (index.istitle()):
        title_case += 1
    elif (index.isupper()):
        upper_case += 1
    elif (index.islower()):
        lower_case += 1
    elif (index.isnumeric()):
        numeric += 1

for index in clear_list:
    if (index.isdigit()):
        sum += int(index)

print(f'There are {title_case} titlecase words.')
print(f'There are {upper_case} uppercase words.')
print(f'There are {lower_case} lowercase words.')
print(f'There are {numeric} numeric strings.')
print(f'The sum of all the numbers is {sum}.')

print(separator)

# Výsledný sloupcový graf pro uživatele

clear_text = []

for one_letter in user_selection.split():
    clean_letter = one_letter.strip(',.')
    clear_text.append(clean_letter.lower())
# pprint(clear_text)

ocurrence = {}

for one_letter in clear_text:
    if len(one_letter) not in ocurrence:
        ocurrence[len(one_letter)] = 1
    else:
        ocurrence[len(one_letter)] += 1
# pprint(ocurrence)

# Finální výpis sloupcového grafu, seřazení

sorted_ocurrence = dict(sorted(zip(ocurrence.keys(), ocurrence.values())))

print('LEN|\t\tOCURRENCES\t\t|NR.')
print(separator)

for i, ocurrences in enumerate(sorted_ocurrence.values(), 1):
    print(f'{i:>3}|{ocurrences * "*":<24}|{ocurrences:<10}')
print(separator)


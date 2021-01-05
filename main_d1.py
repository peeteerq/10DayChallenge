# 10 Day Coding Challenge - Day 1
# Title: Palindrom i anagram
"""Description: Program pobiera od usera napis, a nastepnie wyswietla go wspak.
                Program wyswietla komunikat czy podane slowo jest palindromem.
                Program ignoruje znaki niebedace literami i wielkosc liter.
                Program wywola strone o anagramach: https://poocoo.pl/scrabble-slowa-z-liter/hardcoder
"""

import re
import webbrowser

temp = []

user_in = input("Podaj slowo do odwrocenia: ")
user_in = user_in.lower()

txt_only = re.findall("[a-z]", user_in)

print("Podane slowo: " + "".join(txt_only))

for x in range(len(txt_only)):
    temp.append(txt_only[len(txt_only) - 1 - x])

odwr = "".join(temp)
print("Slowo odwrocone to: " + odwr)

for x in range(int(len(txt_only) / 2)):
    if txt_only[x] != odwr[x]:
        palindrom = False
        break
    else:
        palindrom = True
        continue
if palindrom:
    print("Podane slowo jest palindromem")
else:
    print("Podane slowo nie jest palindromem")

print("Otwieram strone poswiecona anagramom https://poocoo.pl/scrabble-slowa-z-liter/hardcoder")
webbrowser.open("https://poocoo.pl/scrabble-slowa-z-liter/hardcoder")
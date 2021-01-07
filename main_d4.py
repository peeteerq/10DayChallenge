# 10 Day Coding Challenge - Day 4
# Title: Fat Burner
"""Description: Program wylicza BMI na podstawie wprowadzonej masy ciala i wzrostu oraz informuje uzytkownika.
                Program losuje jedna z aktywnosci fizycznej i czas wykonania. Czas nie dluzszy niz podany przez uzytkownika.
                Uzaleznic czas aktywnosci od BMI. Utworzyc plan treningowy na 7dni, zapisany do txt.
                Extra: urozmaicony plan treningowy
"""
import random

avg_train_time = 30.0

BMI_range = {
    "Very severely underweight" : {
        "min" : 0.00,
        "max" : 14.99,
        "multiplier": 0.25,
        "eat": "much more",
        "train": "less"
    },
    "Severely underweight" : {
        "min" : 15.00,
        "max" : 15.99,
        "multiplier": 0.5,
        "eat": "more",
        "train": "less"
    },
    "Underweight" : {
        "min": 16.00,
        "max": 18.49,
        "multiplier": 0.7,
        "eat": "more",
        "train": "the same"
    },
    "Normal (healthy weight)" : {
        "min": 18.50,
        "max": 24.99,
        "multiplier" : 1.0,
        "eat" : "the same",
        "train" : "the same"
    },
    "Overweight" : {
        "min": 25.00,
        "max": 29.99,
        "multiplier": 1.25,
        "eat": "less",
        "train": "the same"
    },
    "Obese Class I (Moderately obese)" : {
        "min": 30.00,
        "max": 34.99,
        "multiplier": 1.5,
        "eat": "less",
        "train": "more"
    },
    "Obese Class II (Severely obese)" : {
        "min": 35.00,
        "max": 39.99,
        "multiplier": 2.0,
        "eat": "much less",
        "train": "more"
    },
    "Obese Class III (Very severely obese)" : {
        "min": 40.00,
        "max": 40.00,
        "multiplier": 5.0,
        "eat": "much less",
        "train": "much more"
    }
}

sports = ["running", "biking", "swimming", "whole-body training", "rope jumping", "yoga", "walking"]

while True:
    try:
        user_mass = float(input("Please fill in your mass in kg: "))
        user_height = float(input("Please fill in your height in cm: "))
        break
    except:
        print("Incorrect data provided. Only numbers allowed")

BMI = user_mass/((user_height / 100) ** 2)

for key, value in BMI_range.items():
    if BMI >= value["max"]:
        user_condition = key
        pass
    else:
        user_condition = key
        break

print("Your BMI value is: {:.2f}, which means: {}".format(BMI, user_condition))

while True:
    try:
        user_train_time = float(input("How much time in minutes could you spent on daily training: "))
        break
    except:
        print("Incorrect data provided. Only numbers allowed")

for key, value in BMI_range.items():
    if key == user_condition:
        print("Your condition is: {}, you should eat {} amount of food and train {} as now.".format(user_condition,
                                                                                    value["eat"], value["train"]))
        multiplier = value["multiplier"]

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if avg_train_time * multiplier >= float(user_train_time):
    print("Recommendation for you for today is to do {} for {} minutes\n".format(sports[random.randint(0,6)], user_train_time))
    print("Your training plan for next week is: ")
    for x in range(7):
        print("{} - {} minutes of {}".format(weekdays[x], user_train_time, sports[random.randint(0,6)]))

else:
    print("Recommendation for you for today is to do {} for {} minutes\n".format(sports[random.randint(0, 6)], avg_train_time * multiplier))
    print("Your training plan for next week is: ")
    for x in range(7):
        print("{} - {} minutes of {}".format(weekdays[x], avg_train_time * multiplier, sports[random.randint(0,6)]))



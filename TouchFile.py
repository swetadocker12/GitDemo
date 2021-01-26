import os

os.getcwd()
os.chdir(r"C:\Users\eswetra\Desktop")

with open("Receipe2.txt", "r", encoding='utf-8') as file:
    for line in file:
        print(line, end="")
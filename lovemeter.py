import time
import sys
import random

print("Love meter")
a = input("Masukkan nama 1: ")
b = input("Masukkan nama 2: ")
c = random.randint(50,100)

if b.strip():
    print(f"Kecocokan dari {a} Love {b} Adalah {c}%")
else:
    print("Invalid")
    

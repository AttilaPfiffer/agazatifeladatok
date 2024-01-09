import random

def feladat1():
    eredmenyek = []
    for i in range(0, 7, 1):
        eredmenyek.append(random.randint(0, 1))
    return eredmenyek

def feladat2(eredmenyek):
    return eredmenyek.count(1)
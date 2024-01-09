def feladat1():
    jatekos_neve: str = (input("Adja meg a nevét: "))
    szerepkor: str = (input("Adja meg a szerepkörét: "))
    print("\n")
    if "varázsló" in szerepkor:
        print(f"Üdvözlünk {jatekos_neve}, 2 életed van!")
    elif "harcos" in szerepkor:
        print(f"Üdvözlünk {jatekos_neve}, 10 életed van!")
    else:
        print(f"Üdzözlünk {jatekos_neve}, 8 életed van!")

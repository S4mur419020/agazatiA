def szinkod():
    print("\nElső feladat: ")
    szinmod:str=str(input("\tKérek egy színkeverési módszert: "))
    szinkod:str=str(input("\tKérem a kódot: "))
    
    if szinmod=="RGB":
        if 5<=len(szinkod)<=11:
            print("\tMegfelelő hossz.")
        else:
            print("\tTúl bonyolult kiszámolni.")
    elif szinmod=="HEX":
        if len(szinkod)==6:
            print("\tMegfelelő hossz.")
        else:
            print("\tTúl bonyolult kiszámolni.")
    elif szinmod=="HSL":
        if 7<=len(szinkod)<=13:
            print("\tMegfelelő hossz.")
        else:
            print("\tTúl bonyolult kiszámolni.")
    elif szinmod=="RGBA":
        print("\tTúl bonyolult kiszámolni.")
    elif szinmod=="HSLA":
        print("\tTúl bonyolult kiszámolni.")
    else:
        print(f"\tA {szinkod} kód nem ismert.")
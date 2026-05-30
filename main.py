INVENTAR = {
    "zelezna_tyc": False,
    "baterka1": False,
    "baterka2": False,
    "pila": False,
    "svitilna": False,
    "nabita svitilna": False,
    "prkno": False,
    "zidle": False,
    "klic": False,
    "mop": False,
    "sroubovak": False,
    "drat": False,
    "nuz": False,
}

POKOJ = "koupelna"
POKOJ_OTEVREN = False
PREKLIZKA = False
ZABIL = False


def ukaz_inventar():
    print("Inventář:")
    if not any(INVENTAR.values()):
        print("Nic není")
    else:
        for key in INVENTAR:
            if INVENTAR[key]:
                print(" - " + key)


# ============================================================
RUNNING = True

while RUNNING:
    if POKOJ == "koupelna":
        print("Jsi v koupelně")
        print("\nCo dělat?")
        print("1. Otevřít dveře")
        print("2. Podívat se pod umyvadlo")
        print("3. Podívat se pod vanu")
        print("4. Podívat se za zrcadlem")
        print("5. Vzít mop")
        print("6. Inventář")
        print("\n7. Ukončit hru")
        x = input(">>> ")

        if x == "1":
            if INVENTAR["zelezna_tyc"]:
                POKOJ_OTEVREN = True
                POKOJ = "koridor1"
            else:
                print("Nemůžeš otevřít dveře, potřebuješ nějakou tyč")
        elif x == "2":
            while True:
                if not INVENTAR["zelezna_tyc"] or ("baterka1" in INVENTAR and not INVENTAR["baterka1"]):
                    print(" \nPod umyvadlem se nachází:")
                    if not INVENTAR["zelezna_tyc"]:
                        print("1. Vzít železnou tyč")
                    if "baterka1" in INVENTAR and not INVENTAR["baterka1"]:
                        print("2. Vzít baterii")
                else:
                    print("\nTady nic není")
                print("3. Zpátky")
                y = input(">>> ")
                if y == "1":
                    if not INVENTAR["zelezna_tyc"]:
                        INVENTAR["zelezna_tyc"] = True
                        print("\nMáš železnou tyč")
                    else:
                        print("\nTato věc tady není")
                elif y == "2":
                    if "baterka1" in INVENTAR and not INVENTAR["baterka1"]:
                        INVENTAR["baterka1"] = True
                        print("\nMáš baterii")
                    if "baterka1" in INVENTAR and INVENTAR["baterka1"] and INVENTAR["baterka2"] and INVENTAR["svitilna"]:
                        INVENTAR["nabita svitilna"] = True
                        del INVENTAR["baterka1"]
                        del INVENTAR["baterka2"]
                        del INVENTAR["svitilna"]
                        print("\nMáš nabitou svítilnu")
                elif y == "3":
                    break
                else:
                    print("\nTato věc tady není")
        elif x == "3":
            while True:
                if not INVENTAR["nabita svitilna"]:
                    print("Tady je moc tma, potřebuješ rozsvítit")
                else:
                    if not INVENTAR["nuz"]:
                        print(" \nPod vanou je nůž")
                        print("1. Vzít nůž")
                    else:
                        print("\nNic tady není")
                print("2. Zpátky")
                y = input(">>> ")
                if y == "1":
                    if not INVENTAR["nuz"]:
                        INVENTAR["nuz"] = True
                        print("\nMáš nůž")
                    else:
                        print("\nTato věc tady není")
                elif y == "2":
                    break
                else:
                    print("\nTato věc tady není")
        elif x == "4":
            print("Rozbil jsi zrcadlo, zaslechl tě protivník a zabil tě")
            print("Konec")
            break
        elif x == "5":
            if not INVENTAR["mop"]:
                INVENTAR["mop"] = True
                print("\nMáš mop")
            else:
                print("\nUž jsi ho vzal")
        elif x == "6":
            ukaz_inventar()
        elif x == "7":
            print("Konec")
            break
        else:
            print("Nemůžeš to udělat")

    elif POKOJ == "koridor1":
        print("Jsi v chodbě")
        print("\nCo dělat?")
        print("1. Jít ke schodům")
        print("2. Otevřít pravé dveře od koupelny")
        print("3. Otevřít levé dveře od koupelny")
        print("4. Jít do koupelny")
        print("5. Inventář")
        print("\n6. Ukončit hru")
        x = input(">>> ")

        if x == "1":
            POKOJ = "koridor2"
        elif x == "2":
            while True:
                if not ZABIL:
                    if not INVENTAR["nuz"]:
                        print("Tam byl protivník, zabil tě")
                        print("Konec")
                        RUNNING = False
                        break
                    else:
                        print("\nMáš zbraň. On tě nevidí. Můžeš ho zabít")
                        print("\nCo dělat?")
                        print("1. Zabít ho")
                else:
                    print("\nTady leží mrtvé tělo")
                print("2. Zpátky")
                y = input(">>> ")
                if y == "1":
                    if not ZABIL:
                        ZABIL = True
                        print("\nZabil jsi protivníka")
                    else:
                        print("\nNemůžeš to udělat")
                elif y == "2":
                    break
                else:
                    print("\nNemůžeš to udělat")
        elif x == "3":
            POKOJ = "levy pokoj"
        elif x == "4":
            POKOJ = "koupelna"
        elif x == "5":
            ukaz_inventar()
        elif x == "6":
            print("Konec")
            break
        else:
            print("Nemůžeš to udělat")

    elif POKOJ == "levy pokoj":
        print("Jsi v levém pokoji")
        print("\nCo dělat?")
        print("1. Odejít z pokoje")
        print("2. Podívat se")
        print("3. Inventář")
        print("\n4. Ukončit hru")
        x = input(">>> ")

        if x == "1":
            POKOJ = "koridor1"
        elif x == "2":
            while True:
                if not INVENTAR["pila"]:
                    print(" \nNa podlaze se nachází pila")
                    print("1. Vzít pilu")
                else:
                    print("\nNic tady není")
                print("2. Zpátky")
                y = input(">>> ")
                if y == "1":
                    if not INVENTAR["pila"]:
                        INVENTAR["pila"] = True
                        print("\nMáš pilu")
                    else:
                        print("\nTato věc tady není")
                elif y == "2":
                    break
                else:
                    print("\nTato věc tady není")
        elif x == "3":
            ukaz_inventar()
        elif x == "4":
            print("Konec")
            break
        else:
            print("Nemůžeš to udělat")

    elif POKOJ == "koridor2":
        print("Jsi v chodbě")
        print("\nCo dělat?")
        print("1. Jít do koupelny")
        print("2. Ke schodům")
        print("3. Otevřít dřevěné dveře")
        print("4. Otevřít červené dveře")
        print("5. Jít do pokoje bez dveří")
        print("6. Podívat se pod topením")
        print("7. Inventář")
        print("\n8. Ukončit hru")
        x = input(">>> ")

        if x == "1":
            POKOJ = "koridor1"
        elif x == "2":
            POKOJ = "schody"
        elif x == "3":
            POKOJ = "dreveny pokoj"
        elif x == "4":
            POKOJ = "cerveny pokoj"
        elif x == "5":
            while True:
                print("\nStojíš před pokojem")
                if not INVENTAR["mop"]:
                    print("Tam je tma. Nic nevidíš")
                    print("\n1. Vstoupit do místnosti")
                    print("2. Jít zpátky")
                else:
                    print("Je osvětlený")
                    POKOJ = "temny pokoj"
                    break
                y = input(">>> ")
                if y == "1":
                    print("Tam byla propast")
                    print("Spadl jsi do ní a zlomil si krk")
                    print("Konec")
                    RUNNING = False
                    break
                elif y == "2":
                    break
                else:
                    print("\nNemůžeš to udělat")
        elif x == "6":
            while True:
                if not PREKLIZKA:
                    print("Potřebuješ odstranit překližku")
                    if INVENTAR["sroubovak"]:
                        PREKLIZKA = True
                        print("Odstranil jsi překližku")
                        if not INVENTAR["svitilna"]:
                            print(" \nPod topením se nachází svítilna")
                            print("1. Vzít svítilnu")
                        else:
                            print("\nNic tady není")
                    else:
                        print("\nNemůžeš ji sundat. Potřebuješ šroubovák")
                else:
                    if "svitilna" in INVENTAR and not INVENTAR["svitilna"]:
                        print(" \nPod topením se nachází svítilna")
                        print("1. Vzít svítilnu")
                    else:
                        print("\nNic tady není")
                print("2. Zpátky")
                y = input(">>> ")
                if y == "1":
                    if PREKLIZKA and "svitilna" in INVENTAR and not INVENTAR["svitilna"]:
                        INVENTAR["svitilna"] = True
                        print("\nMáš svítilnu")
                    else:
                        print("\nTato věc tady není")
                    if "svitilna" in INVENTAR and INVENTAR["svitilna"] and \
                        "baterka1" in INVENTAR and INVENTAR["baterka1"] and \
                        "baterka2" in INVENTAR and INVENTAR["baterka2"]:
                        INVENTAR["nabita svitilna"] = True
                        del INVENTAR["svitilna"]
                        del INVENTAR["baterka1"]
                        del INVENTAR["baterka2"]
                        print("\nMáš nabitou svítilnu")
                elif y == "2":
                    break
                else:
                    print("\nTato věc tady není")
        elif x == "7":
            ukaz_inventar()
        elif x == "8":
            print("Konec")
            break
        else:
            print("Nemůžeš to udělat")

    elif POKOJ == "cerveny pokoj":
        print("Jsi v červeném pokoji")
        print("\nCo dělat?")
        print("1. Odejít z pokoje")
        print("2. Podívat se na povrch komody")
        print("3. Vzít židli")
        print("4. Inventář")
        print("\n5. Ukončit hru")
        x = input(">>> ")

        if x == "1":
            POKOJ = "koridor2"
        elif x == "2":
            while True:
                if not INVENTAR["zidle"]:
                    print("Nemůžeš dosáhnout")
                else:
                    if not INVENTAR["klic"]:
                        print(" \nNa komodě se nachází klíč")
                        print("1. Vzít klíč")
                    else:
                        print("\nNic tady není")
                print("2. Zpátky")
                y = input(">>> ")
                if y == "1":
                    if not INVENTAR["zidle"]:
                        print("Nemůžeš to udělat")
                    else:
                        if not INVENTAR["klic"]:
                            INVENTAR["klic"] = True
                            print("\nMáš klíč")
                        else:
                            print("\nTato věc tady není")
                elif y == "2":
                    break
                else:
                    print("\nTato věc tady není")
        elif x == "3":
            if not INVENTAR["zidle"]:
                INVENTAR["zidle"] = True
                print("\nMáš židli")
            else:
                print("\nTato věc tady není")
        elif x == "4":
            ukaz_inventar()
        elif x == "5":
            print("Konec")
            break
        else:
            print("Nemůžeš to udělat")

    elif POKOJ == "dreveny pokoj":
        print("Jsi v dřevěném pokoji")
        print("\nCo dělat?")
        print("1. Odejít z pokoje")
        print("2. Zkusit rozřezat prkno")
        print("3. Podívat se do krabice")
        print("4. Inventář")
        print("\n5. Ukončit hru")
        x = input(">>> ")
        if x == "1":
            POKOJ = "koridor2"
        elif x == "2":
            if INVENTAR["pila"]:
                if not INVENTAR["prkno"]:
                    INVENTAR["prkno"] = True
                    print("\nMáš prkno")
                else:
                    print("\nUž máš prkno")
            else:
                print("Nemáš na to síly, potřebuješ nějaký nástroj")
        elif x == "3":
            while True:
                if not INVENTAR["drat"]:
                    print(" \nV krabici je drát")
                    print("1. Vzít drát")
                else:
                    print("\nNic tady není")
                print("2. Zpátky")
                y = input(">>> ")
                if y == "1":
                    if not INVENTAR["drat"]:
                        INVENTAR["drat"] = True
                        print("\nMáš drát")
                    else:
                        print("\nTato věc tady není")
                elif y == "2":
                    break
                else:
                    print("\nTato věc tady není")
        elif x == "4":
            ukaz_inventar()
        elif x == "5":
            print("Konec")
            break
        else:
            print("Nemůžeš to udělat")

    elif POKOJ == "temny pokoj":
        print("Jsi v místnosti, uprostřed je díra")
        print("\nCo dělat?")
        print("1. Jít zpátky")
        print("2. Podívat se do skříňky")
        print("3. Podívat se do propasti")
        print("4. Inventář")
        print("\n5. Ukončit hru")
        x = input(">>> ")

        if x == "1":
            POKOJ = "koridor2"
        elif x == "2":
            while True:
                if "baterka2" in INVENTAR and not INVENTAR["baterka2"]:
                    print(" \nVe skříni je baterie")
                    print("1. Vzít baterii")
                else:
                    print("\nNic tady není")
                print("2. Zpátky")
                y = input(">>> ")
                if y == "1":
                    if "baterka2" in INVENTAR and not INVENTAR["baterka2"]:
                        INVENTAR["baterka2"] = True
                        print("\nMáš baterii")
                    else:
                        print("\nTato věc tady není")
                    if "baterka1" in INVENTAR and INVENTAR["baterka1"] and \
                        "baterka2" in INVENTAR and INVENTAR["baterka2"] and \
                        "svitilna" in INVENTAR and INVENTAR["svitilna"]:
                        INVENTAR["nabita svitilna"] = True
                        del INVENTAR["baterka1"]
                        del INVENTAR["baterka2"]
                        del INVENTAR["svitilna"]
                        print("\nMáš nabitou svítilnu")
                elif y == "2":
                    break
                else:
                    print("\nTato věc tady není")
        elif x == "3":
            while True:
                if not INVENTAR["sroubovak"]:
                    print("\nDole leží šroubovák")
                    print("1. Vzít šroubovák")
                else:
                    print("\nNic tady není")
                print("2. Zpátky")
                y = input(">>> ")
                if y == "1":
                    if not INVENTAR["drat"]:
                        print("\nNemůžeš dosáhnout, potřebuješ něco")
                    else:
                        INVENTAR["sroubovak"] = True
                        print("\nMáš šroubovák")
                elif y == "2":
                    break
                else:
                    print("\nTato věc tady není")
        elif x == "4":
            ukaz_inventar()
        elif x == "5":
            print("Konec")
            break
        else:
            print("Nemůžeš to udělat")

    elif POKOJ == "schody":
        print("Jsi u schodů")
        print("\nCo dělat?")
        print("1. Jít zpátky")
        print("2. Jít k východu")
        print("3. Inventář")
        print("\n4. Ukončit hru")
        x = input(">>> ")

        if x == "1":
            POKOJ = "koridor2"
        elif x == "2":
            if INVENTAR["prkno"]:
                POKOJ = "vychod"
            else:
                print("Nemůžeš projít, na schodech chybí prkno")
        elif x == "3":
            ukaz_inventar()
        elif x == "4":
            print("Konec")
            break
        else:
            print("Nemůžeš to udělat")

    elif POKOJ == "vychod":
        print("Jsi u východu")
        print("\nCo dělat?")
        print("1. Jít zpátky")
        print("2. Utéct")
        print("3. Inventář")
        print("\n4. Ukončit hru")
        x = input(">>> ")

        if x == "1":
            POKOJ = "schody"
        elif x == "2":
            while True:
                if not INVENTAR["klic"]:
                    print("\nNemůžeš otevřít dveře. Potřebuješ klíč.")
                elif not ZABIL and not INVENTAR["nabita svitilna"]:
                    print("\nUtekl jsi, ale v lese je moc tma. Zabloudil jsi.")
                    print("Špatný konec")
                    RUNNING = False
                    break
                elif INVENTAR["nabita svitilna"] and not ZABIL:
                    print("\nUtekl jsi.")
                    print("Svítilna ti osvětluje cestu, ale kvůli amputované noze jsi moc pomalý.")
                    print("Našel tě protivník a odnesl tě zpátky")
                    print("Špatný konec")
                    RUNNING = False
                    break
                else:
                    print("\nUtekl jsi.")
                    print("Svítilna ti osvětluje cestu, ale kvůli amputované noze jsi moc pomalý.")
                    print("Nic jsi nenašel a vrátil ses zpátky.")
                    print("Ve sklepě jsi našel vodu a určité množství jídla.")
                    print("Žiješ jen s nadějí, že tě někdo najde.")
                    print("Dobrý konec (možná)")
                    RUNNING = False
                    break
        elif x == "3":
            ukaz_inventar()
        elif x == "4":
            print("Konec")
            break
        else:
            print("Nemůžeš to udělat")

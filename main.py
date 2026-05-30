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
    print("inventar:")
    if not any(INVENTAR.values()):
        print("nic neni")
    else:
        for key in INVENTAR:
            if INVENTAR[key]:
                print(" - " + key)


# ============================================================
RUNNING = True

while RUNNING:
    if POKOJ == "koupelna":
        print("jsi v koupelne")
        print("\nco delat?")
        print("1. otevrit dvere")
        print("2. podivat se pod umivadlo")
        print("3. podivat se pod vanu")
        print("4. podivat se za zrdcadlem")
        print("5. vzit mop")
        print("6. inventar")
        print("\n7. ukoncit hru")
        x = input(">>> ")

        if x == "1":
            if INVENTAR["zelezna_tyc"]:
                POKOJ_OTEVREN = True
                POKOJ = "koridor1"
            else:
                print("nemuzes otevrit dvere potrebujes nejakou tyc")
        elif x == "2":
            while True:
                if not INVENTAR["zelezna_tyc"] or ("baterka1" in INVENTAR and not INVENTAR["baterka1"]):
                    print(" \npod umyvadlem se nachazi:")
                    if not INVENTAR["zelezna_tyc"]:
                        print(f"1. vzit zelezna_tyc")
                    if "baterka1" in INVENTAR and not INVENTAR["baterka1"]:
                        print(f"2. vzit baterka1")
                else:
                    print("\ntady nic neni")
                print("3. zpatky")
                y = input(">>> ")
                if y == "1":
                    if not INVENTAR["zelezna_tyc"]:
                        INVENTAR["zelezna_tyc"] = True
                        print(f"\nmas zelezna_tyc")
                    else:
                        print("\ntato vec tady neni")
                elif y == "2":
                    if "baterka1" in INVENTAR and not INVENTAR["baterka1"]:
                        INVENTAR["baterka1"] = True
                        print(f"\nmas baterka1")
                    if "baterka1" in INVENTAR and INVENTAR["baterka1"]  and INVENTAR["baterka2"] and INVENTAR["svitilna"]:
                        INVENTAR["nabita svitilna"] = True
                        del INVENTAR["baterka1"] 
                        del INVENTAR["baterka2"]
                        del INVENTAR["svitilna"]
                        print("\nmas nabitou svitilnu")
                elif y == "3":
                    break
                else:
                    print("\ntato vec tady neni")
        elif x == "3":
             while True:
                if not INVENTAR["nabita svitilna"]:
                    print("tady je moc temno potrebujes rozsvitit")
                else:
                    if not INVENTAR["nuz"]:
                        print(" \npod vanou je nuz")
                        print("1. vzit nuz")
                    else:
                        print("\nnic tady neni")
                print("2. zpatky")
                y = input(">>> ")
                if y == "1":
                    if not INVENTAR["nuz"]:
                        INVENTAR["nuz"] = True
                        print("\nmas nuz")
                    else:
                        print("\ntato vec tady neni")
                elif y == "2":
                    break
                else:
                    print("\ntato vec tady neni")
        elif x == "4":
            print("rozbil si zrcadlo te zaslechl protivnik a zabil te")
            print("konec")
            break
        elif x == "5":
            if not INVENTAR["mop"]:
                INVENTAR["mop"] = True
                print("\nmas mop")
            else:
                print("\nuz jsi ji vzal")
        elif x == "6":
            ukaz_inventar()
        elif x == "7":
            print("konec")
            break
        else:
            print("nemuzes to udelat")

    elif POKOJ == "koridor1":
        print("jsi v koridore")
        print("\nco delat?")
        print("1. jit ke schodam")
        print("2. otevrit pravou dvere od koupelny")
        print("3. otevrit levou dveri od koupelny")
        print("4. jit v koupelnu")
        print("5. inventar")
        print("\n6. ukoncit hru")
        x = input(">>> ")
        
        if x == "1":
            POKOJ = "koridor2"
        elif x == "2":
            while True:
                if not ZABIL:
                    if not INVENTAR["nuz"]:
                        print("tam byl protivnik on te zabil")
                        print("konec")
                        RUNNING = False
                        break
                    else:
                        print("\nmas zbran. on te nevidi. muzes ho zabit")
                        print("\nco delat?")
                        print("1. zabit jeho")
                else:
                    print("\ntady lezi mrtve telo")
                print("2. zpatky")
                y = input(">>> ")
                if y == "1":
                    if not ZABIL:
                        ZABIL = True
                        print("\nzabil jsi protivnika")
                    else:
                        print("\nnemuzes to udelat")
                elif y == "2":
                    break
                else:
                    print("\nnemuzes to udelat")
        elif x == "3":
            POKOJ = "levy pokoj"
        elif x == "4":
            POKOJ = "koupelna"
        elif x == "5":
            ukaz_inventar()
        elif x == "6":
            print("konec")
            break
        else:
            print("nemuzes to udelat")

    elif POKOJ == "levy pokoj":
        print(" jsi v levym pokoje")
        print("\nco delat?")
        print("1. odejit z pokoje")
        print("2. podivat se")
        print("3. inventar")
        print("\n4. ukoncit hru")
        x = input(">>> ")

        if x == "1":
            POKOJ = "koridor1"
        elif x == "2":
            while True:
                if not INVENTAR["pila"]:
                    print(" \nna podlaze se nachazi pila")
                    print("1. vzit pilu")
                else:
                    print("\nnic tady neni")
                print("2. zpatky")
                y = input(">>> ")
                if y == "1":
                    if not INVENTAR["pila"]:
                        INVENTAR["pila"] = True
                        print("\nmas pilu")
                    else:
                        print("\ntato vec tady neni")
                elif y == "2":
                    break
                else:
                    print("\ntato vec tady neni")
        elif x == "3":
            ukaz_inventar()
        elif x == "4":
            print("konec")
            break
        else:
            print("nemuzes to udelat")

    elif POKOJ == "koridor2":
        print(" jsi v koridore")
        print("\nco delat?")
        print("1. jit ke koupelne")
        print("2. ke schodam")
        print("3. otevrit drevenou dveri")
        print("4. otevrit cervenou dveri")
        print("5. jit v pokoj bez dveri")
        print("6. podivat se pod topenim")
        print("7. inventar")
        print("\n8. ukoncit hru")
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
                print("\nstojis pred pokojem")
                if not INVENTAR["mop"]:
                    print("tam je tma. nic nevidis")
                    print("\n1. vstoupit do mistnosti")
                    print("2. jit zpatky")
                else:
                    print("on je rozsviceny")
                    POKOJ = "temny pokoj"
                    break
                y = input(">>> ")
                if y == "1":
                    print("tam byla propast")
                    print("jsi do ni spadl a zlomil krk")
                    print("konec")
                    RUNNING = False
                    break
                elif y == "2":
                    break
                else:
                    print("\nnemuzes to udelat")
        elif x == "6":
            while True:
                if not PREKLIZKA:
                    print("potrebujes odstranit preklizku")
                    if INVENTAR["sroubovak"]:
                        PREKLIZKA = True
                        print("jsi odstranil preklizku")
                        if not INVENTAR["svitilna"]:
                            print(" \npod topenim se nachazi svitilna")
                            print("1. vzit svitilnu")
                        else:
                            print("\nnic tady neni")
                    else:
                        print("\nnemuzes ji sundat. potrebujes sroubovak")
                else:
                    if "svitilna" in INVENTAR and not INVENTAR["svitilna"]:
                        print(" \npod topenim se nachazi svitilna")
                        print("1. vzit svitilnu")
                    else:
                        print("\nnic tady neni")
                print("2. zpatky")
                y = input(">>> ")
                if y == "1":
                    if PREKLIZKA and "svitilna" in INVENTAR and not INVENTAR["svitilna"]:
                        INVENTAR["svitilna"] = True
                        print("\nmas svitilnu")
                    else:
                        print("\ntato vec tady neni")
                    if "svitilna" in INVENTAR and INVENTAR["svitilna"] and \
                        "baterka1" in INVENTAR and INVENTAR["baterka1"] and \
                        "baterka2" in INVENTAR and INVENTAR["baterka2"]:
                        INVENTAR["nabita svitilna"] = True
                        del INVENTAR["svitilna"]
                        del INVENTAR["baterka1"]
                        del INVENTAR["baterka2"]
                        print("\nmas nabitou svitilnu")
                elif y == "2":
                    break
                else:
                    print("\ntato vec tady neni")
        elif x == "7":
            ukaz_inventar()
        elif x == "8":
            print("konec")
            break
        else:
            print("nemuzes to udelat")

    elif POKOJ == "cerveny pokoj":
        print("jsi v cervenem pokoje")
        print("\nco delat?")
        print("1. odejit z pokoje")
        print("2. podivat se na povrch komody")
        print("3. vzit zidle")
        print("4. inventar")
        print("\n5. ukoncit hru")
        x = input(">>> ")

        if x == "1":
            POKOJ = "koridor2"
        elif x == "2":
            while True:
                if not INVENTAR["zidle"]:
                    print("nemuzes dosahnout")
                else:
                    if not INVENTAR["klic"]:
                        print(" \nna komode se nachazi klic")
                        print("1. vzit klic")
                    else:
                        print("\nnic tady neni")
                print("2. zpatky")
                y = input(">>> ")
                if y == "1":
                    if not INVENTAR["zidle"]:
                        print("nemuzes to udelat")
                    else:
                        if not INVENTAR["klic"]:
                            INVENTAR["klic"] = True
                            print("\nmas klic")
                        else:
                            print("\ntato vec tady neni")
                elif y == "2":
                    break
                else:
                    print("\ntato vec tady neni")
        elif x == "3":
            if not INVENTAR["zidle"]:
                INVENTAR["zidle"] = True
                print("\nmas zidle")
            else:
                print("\ntato vec tady neni")
        elif x == "4":
            ukaz_inventar()
        elif x == "5":
            print("konec")
            break
        else:
            print("nemuzes to udelat")

    elif POKOJ == "dreveny pokoj":
        print("jsi v drevenym pokoje")
        print("\nco delat?")
        print("1. odejit z pokoje")
        print("2. zkusit zlomit prkno")
        print("3. podivat se do krabice")
        print("4. inventar")
        print("\n5. ukoncit hru")
        x = input(">>> ")
        if x == "1":
            POKOJ = "koridor2"
        elif x == "2":
            if INVENTAR["pila"]:
                if not INVENTAR["prkno"]:
                    INVENTAR["prkno"] = True
                    print("\nmas prkno")
                else:
                    print("\nuz mas prkno")
            else:
                print("nemas na to sily potrebujes nejaky stroj")
        elif x == "3":
            while True:
                if not INVENTAR["drat"]:
                    print(" \nv krabice je drat")
                    print("1. vzit drat")
                else:
                    print("\nnic tady neni")
                print("2. zpatky")
                y = input(">>> ")
                if y == "1":
                    if not INVENTAR["drat"]:
                        INVENTAR["drat"] = True
                        print("\nmas drat")
                    else:
                        print("\ntato vec tady neni")
                elif y == "2":
                    break
                else:
                    print("\ntato vec tady neni")
        elif x == "4":
            ukaz_inventar()
        elif x == "5":
            print("konec")
            break
        else:
            print("nemuzes to udelat")

    elif POKOJ == "temny pokoj":
        print("jsi v mistnisti uprostred je dira")
        print("\nco delat?")
        print("1. jit zpatky")
        print("2. podivat se do skrinky")
        print("3. podivat se do propasti")
        print("4. inventar")
        print("\n5. ukoncit hru")
        x = input(">>> ")
        
        if x == "1":
            POKOJ = "koridor2"
        elif x == "2":
            while True:
                if "baterka2" in INVENTAR and not INVENTAR["baterka2"]:
                    print(" \nve skrine je baterka")
                    print("1. vzit baterku")
                else:
                    print("\nnic tady neni")
                print("2. zpatky")
                y = input(">>> ")
                if y == "1":
                    if "baterka2" in INVENTAR and not INVENTAR["baterka2"]:
                        INVENTAR["baterka2"] = True
                        print("\nmas baterku")
                    else:
                        print("\ntato vec tady neni")
                    if "baterka1" in INVENTAR and INVENTAR["baterka1"] and \
                        "baterka2" in INVENTAR and INVENTAR["baterka2"] and \
                        "svitilna" in INVENTAR and INVENTAR["svitilna"]:
                        INVENTAR["nabita svitilna"] = True
                        del INVENTAR["baterka1"]
                        del INVENTAR["baterka2"]
                        del INVENTAR["svitilna"]
                        print("\nmas nabitou svitilnu")
                elif y == "2":
                    break
                else:
                    print("\ntato vec tady neni")
        elif x == "3":
            while True:
                if not INVENTAR["sroubovak"]:
                    print("\ndolu lezi sroubovak")
                    print("1. vzit sroubovak")
                else:
                    print("\nnic tady neni")
                print("2. zpatky")
                y = input(">>> ")
                if y == "1":
                    if not INVENTAR["drat"]:
                        print("\nnemuzes dosahnout potrebujes neco")
                    else:
                        INVENTAR["sroubovak"] = True
                        print("\nmas sroubovak")
                elif y == "2":
                    break
                else:
                    print("\ntato vec tady neni")
        elif x == "4":
            ukaz_inventar()
        elif x == "5":
            print("konec")
            break
        else:
            print("nemuzes to udelat")

    elif POKOJ == "schody":
        print("jsi u schodu")
        print("\nco delat?")
        print("1. jit zpatky")
        print("2. jit k vychodu")
        print("3. inventar")
        print("\n4. ukoncit hru")
        x = input(">>> ")

        if x == "1":
            POKOJ = "koridor2"
        elif x == "2":
            if INVENTAR["prkno"]:
                POKOJ = "vychod"
            else:
                print("nemuzes projit na schodach chyby prkno")
        elif x == "3":
            ukaz_inventar()
        elif x == "4":
            print("konec")
            break
        else:
            print("nemuzes to udelat")

    elif POKOJ == "vychod":
        print("jsi u vychodu")
        print("\nco delat?")
        print("1. jit zpatky")
        print("2. utict")
        print("3. inventar")
        print("\n4. ukoncit hru")
        x = input(">>> ")

        if x == "1":
            POKOJ = "schody"
        elif x == "2":
            while True:
                if not INVENTAR["klic"]:
                    print("\nnemuzes otevrit dvere. potrebujes klic.")
                elif not ZABIL and not INVENTAR["nabita svitilna"]:
                    print("\njsi utekl ale v lese je moc temno. jsi se zabloudil")
                    print("spatny konec")
                    RUNNING = False
                    break
                elif INVENTAR["nabita svitilna"] and not ZABIL:
                    print("\njsi utekl.")
                    print("svitilna ti osvicuje cestu, ale kvuli amputovane noze jsi moc pomaly.")
                    print("tebe nasel protivnik a odnesl te zpatky")
                    print("spatny konec")
                    RUNNING = False
                    break
                else:
                    print("\njsi utekl.")
                    print("svitilna ti osvicuje cestu, ale kvuli amputovane noze jsi moc pomaly.")
                    print("nic jsi nenasel a vratil se zpatky.")
                    print("ve sklepe jsi nasel vodu a urcite mnozstvi jidla.")
                    print("zijes jen s nadeji ze te nekdo najde.")
                    print("dobry konec (mozna)")
                    RUNNING = False
                    break 
        elif x == "3":
            ukaz_inventar()
        elif x == "4":
            print("konec")
            break
        else:
            print("nemuzes to udelat")

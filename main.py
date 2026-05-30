inventar = {
    "zelezna_tyc": False,
    "baterka1": False,
    "baterka2": False,
    "pila": False,
    "svitilna": False,
    "nabita svitilna": False,
    "prkno": False,
    "zidle": False,
    "klic": False,
    "zarovka": False,
    "lepici_paska": False,
    "mop": False,
    "sroubovak": False,
    "drat": False,
    "nuz": False,
    "pomocna tyc s zarovkou": False
}

pokoj = "koupelna"
pokoj_otevren = False
preklizka = False
zabil = False
vychod = False


def ukaz_inventar():
    print("inventar:")
    if not any(inventar.values()):
        print("nic neni")
    else:
        for key in inventar:
            if inventar[key]:
                print(" - " + key)


# ============================================================
running = True

while running:
    if pokoj == "koupelna":
        vec1 = "zelezna_tyc"
        vec2 = "baterka1"
        vec3 = "nabita svitilna"
        vec4 = "nuz"
        vec5 = "baterka2"
        vec6 = "svitilna"

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
            if inventar["zelezna_tyc"]:
                pokoj_otevren = True
                pokoj = "koridor1"
            else:
                print("nemuzes otevrit dvere potrebujes nejakou tyc")
        elif x == "2":
            while True:
                if not inventar[vec1] or (vec2 in inventar and not inventar[vec2]):
                    print(" \npod umzvadlem se nachazi:")
                    if not inventar[vec1]:
                        print(f"1. vzit {vec1}")
                    if not inventar[vec2]:
                        print(f"2. vzit {vec2}")
                else:
                    print("\ntady nic neni")
                print("3. zpatky")
                y = input(">>> ")
                if y == "1":
                    if not inventar[vec1]:
                        inventar[vec1] = True
                        print(f"\nmas {vec1}")
                    else:
                        print("\ntato vec tady neni")
                elif y == "2":
                    if vec2 in inventar and not inventar[vec2]:
                        inventar[vec2] = True
                        print(f"\nmas {vec2}")
                    if inventar[vec2] and inventar[vec6] and inventar[vec5]:
                        inventar[vec3] = True
                        del inventar[vec2] 
                        del inventar[vec6] 
                        del inventar[vec5] 
                        print("\nmas nabitou svitilnu")
                elif y == "3":
                    break
                else:
                    print("\ntato vec tady neni")
        elif x == "3":
             while True:
                if not inventar[vec3]:
                    print("tady je moc temno potrebujes rozsvitit")
                else:
                    if not inventar[vec4]:
                        print(" \npod vanou je nuz")
                        print("1. vzit nuz")
                    else:
                        print("\nnic tady neni")
                print("2. zpatky")
                y = input(">>> ")
                if y == "1":
                    if not inventar[vec4]:
                        inventar[vec4] = True
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
            if "mop" in inventar and not inventar["mop"]:
                inventar["mop"] = True
                print("\nmas mop")
            else:
                print("\nuz jsi ji vzal")
            if ("mop" in inventar and not inventar["mop"]) and inventar["lepici_paska"] and inventar["zarovka"]:
                inventar["pomocna tyc s zarovkou"] = True
                del inventar["mop"]
                del inventar["lepici_paska"]
                del inventar["zarovka"]
                print("\nmas pomocnou tyc aby dosadit zarovku")
        elif x == "6":
            ukaz_inventar()
        elif x == "7":
            print("konec")
            break
        else:
            print("nemuzes to udelat")

    elif pokoj == "koridor1":
        vec1 = "nuz"

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
            pokoj = "koridor2"
        elif x == "2":
            while True:
                if not zabil:
                    if not inventar[vec1]:
                        print("tam byl protivnik on te zabil")
                        print("konec")
                        running = False
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
                    if not zabil:
                        zabil = True
                        print("\nzabil jsi protivnika")
                    else:
                        print("\nnemuzes to udelat")
                elif y == "2":
                    break
                else:
                    print("\nnemuzes to udelat")
        elif x == "3":
            pokoj = "levy pokoj"
        elif x == "4":
            pokoj = "koupelna"
        elif x == "5":
            ukaz_inventar()
        elif x == "6":
            print("konec")
            break
        else:
            print("nemuzes to udelat")

    elif pokoj == "levy pokoj":
        vec1 = "pila"

        print(" jsi v levym pokoje")
        print("\nco delat?")
        print("1. odejit z pokoje")
        print("2. podivat se")
        print("3. inventar")
        print("\n4. ukoncit hru")
        x = input(">>> ")
        if x == "1":
            pokoj = "koridor1"
        elif x == "2":
            while True:
                if not inventar[vec1]:
                    print(" \nna podlaze se nachazi pila")
                    print("1. vzit pilu")
                else:
                    print("\nnic tady neni")
                print("2. zpatky")
                y = input(">>> ")
                if y == "1":
                    if not inventar[vec1]:
                        inventar[vec1] = True
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

    elif pokoj == "koridor2":
        vec1 = "svitilna"
        vec2 = "baterka1"
        vec3 = "baterka2"
        vec4 ="pomocna tyc s zarovkou"

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
            pokoj = "koridor1"
        elif x == "2":
            pokoj = "schody"
        elif x == "3":
            pokoj = "dreveny pokoj"
        elif x == "4":
            pokoj = "cerveny pokoj"
        elif x == "5":
            while True:
                print("\nstojis pred pokojem")
                if not inventar[vec4]:
                    print("tam je tma. nic nevidis")
                    print("\n1. vstoupit do mistnosti")
                    print("2. jit zpatky")
                else:
                    print("on je rozsviceny")
                    pokoj = "temny pokoj"
                    break
                y = input(">>> ")
                if y == "1":
                    print("tam byla propast")
                    print("jsi do ni spadl a zlomil krk")
                    print("konec")
                    running = False
                    break
                elif y == "2":
                    break
                else:
                    print("\nnemuzes to udelat")
        elif x == "6":
            while True:
                if not preklizka:
                    print("potrebujes odstranit preklizku")
                    if inventar["sroubovak"]:
                        preklizka = True
                        print("jsi odstranil preklizku")
                else:
                    if not inventar[vec1]:
                        print(" \npod topenim se nachazi svitilna")
                        print("1. vzit svitilnu")
                    else:
                        print("\nnic tady neni")
                print("2. zpatky")
                y = input(">>> ")
                if y == "1":
                    if vec1 in inventar and not inventar[vec1]:
                        inventar[vec1] = True
                        print("\nmas svitilnu")
                    else:
                        print("\ntato vec tady neni")
                    if inventar[vec1] and inventar[vec2] and inventar[vec3]:
                        inventar[vec4] = True
                        del inventar[vec1]
                        del inventar[vec2]
                        del inventar[vec3]
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

    elif pokoj == "cerveny pokoj":
        vec1 = "zarovka"
        vec2 = "zidle"
        vec3 = "klic"
        vec4 = "lepici_paska"
        vec5 = "mop"
        vec6 = "pomocna tyc s zarovkou"

        print("jsi v cervenem pokoje")
        print("\nco delat?")
        print("1. odejit z pokoje")
        print("2. otevrit suflik")
        print("3. podivat se na povrch komody")
        print("4. vzit zidle")
        print("5. inventar")
        print("\n6. ukoncit hru")
        x = input(">>> ")
        if x == "1":
            pokoj = "koridor2"
        elif x == "2":
            while True:
                if vec1 in inventar and not inventar[vec1]:
                    print(" \nv supliku je zarovka")
                    print("1. vzit zarovku")
                else:
                    print("\nnic tady neni")
                print("2. zpatky")
                y = input(">>> ")
                if y == "1":
                    if vec1 in inventar and not inventar[vec1]:
                        inventar[vec1] = True
                        print("\nmas zarovku")
                    else:
                        print("\ntato vec tady neni")
                    if inventar[vec1] and inventar[vec4] and inventar[vec5]:
                        inventar[vec6] = True
                        del inventar[vec1]
                        del inventar[vec4]
                        del inventar[vec5]
                        print("\nmas pomocnou tyc aby dosadit zarovku")
                elif y == "2":
                    break
                else:
                    print("\ntato vec tady neni")
        elif x == "3":
            while True:
                if not inventar[vec2]:
                    print("nemuzes dosahnout")
                else:
                    if not inventar[vec3]:
                        print(" \nna komode se nachazi klic")
                        print("1. vzit klic")
                    else:
                        print("\nnic tady neni")
                print("2. zpatky")
                y = input(">>> ")
                if y == "1":
                    if not inventar[vec3]:
                        inventar[vec3] = True
                        print("\nmas klic")
                    else:
                        print("\ntato vec tady neni")
                elif y == "2":
                    break
                else:
                    print("\ntato vec tady neni")
        elif x == "4":
            if not inventar[vec2]:
                inventar[vec2] = True
                print("\nmas zidle")
            else:
                print("\ntato vec tady neni")
        elif x == "5":
            ukaz_inventar()
        elif x == "6":
            print("konec")
            break
        else:
            print("nemuzes to udelat")

    elif pokoj == "dreveny pokoj":
        vec1 = "pila"
        vec2 = "prkno"
        vec3 = "drat"
        vec4 = "lepici_paska"
        vec5 = "mop"
        vec6 = "zarovka"
        vec7 = "pomocna tyc s zarovkou"

        print("jsi v drevenym pokoje")
        print("\nco delat?")
        print("1. odejit z pokoje")
        print("2. zkusit zlomit prkno")
        print("3. podivat se do krabice")
        print("4. inventar")
        print("\n5. ukoncit hru")
        x = input(">>> ")
        if x == "1":
            pokoj = "koridor2"
        elif x == "2":
            if inventar[vec1]:
                if not inventar[vec2]:
                    inventar[vec2] = True
                    print("\nmas prkno")
                else:
                    print("\nuz mas prkno")
            else:
                print("nemas na to sily potrebujes nejaky stroj")
        elif x == "3":
            while True:
                if not inventar[vec3] or (vec4 in inventar and not inventar[vec4]):
                    print(" \nv krabice se nachazi:")
                    if not inventar[vec3]:
                        print("1. vzit drat")
                    if vec4 in inventar and not inventar[vec4]:
                        print("2. vzit lepici pasku")
                else:
                    print("\ntady nic neni")
                print("3. zpatky")
                y = input(">>> ")
                if y == "1":
                    if not inventar[vec3]:
                        inventar[vec3] = True
                        print("\nmas drat")
                    else:
                        print("\ntato vec tady neni")
                elif y == "2":
                    if vec4 in inventar and not inventar[vec4]:
                        inventar[vec4] = True
                        print("\nmas lepici pasku")
                    if inventar[vec4] and inventar[vec5] and inventar[vec6]:
                        inventar[vec7] = True
                        del inventar[vec4]
                        del inventar[vec5]
                        del inventar[vec6]
                        print("\nmas pomocnou tyc aby dosadit zarovku")
                elif y == "3":
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

    elif pokoj == "temny pokoj":
        vec1 = "baterka2"
        vec2 = "sroubovak"
        vec3 = "drat"
        vec4 = "baterka2"
        vec5 = "svitilna"
        vec6 = "nabita svitilna"

        print("jsi v mistnisti uprostred je dira")
        print("\nco delat?")
        print("1. jit zpatky")
        print("2. podivat se do skrinky")
        print("3. podivat se do propasti")
        print("4. inventar")
        print("\n5. ukoncit hru")
        x = input(">>> ")
        
        if x == "1":
            pokoj = "koridor2"
        elif x == "2":
            while True:
                if not inventar[vec1]:
                    print(" \nve skrine je baterka")
                    print("1. vzit baterku")
                else:
                    print("\nnic tady neni")
                print("2. zpatky")
                y = input(">>> ")
                if y == "1":
                    if vec1 in inventar and not inventar[vec1]:
                        inventar[vec1] = True
                        print("\nmas baterku")
                    else:
                        print("\ntato vec tady neni")
                    if inventar[vec1] and inventar[vec4] and inventar[vec5]:
                        inventar[vec6] = True
                        del inventar[vec1]
                        del inventar[vec4]
                        del inventar[vec5]
                        print("\nmas nabitou svitilnu")
                elif y == "2":
                    break
                else:
                    print("\ntato vec tady neni")
        elif x == "3":
            while True:
                if not inventar[vec2]:
                    print("\ndolu lezi sroubovak")
                    print("1. vzit sroubovak")
                else:
                    print("\nnic tady neni")
                print("2. zpatky")
                y = input(">>> ")
                if y == "1":
                    if not inventar[vec3]:
                        print("\nnemuzes dosahnout potrebujes neco")
                    else:
                        inventar[vec2] = True
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

    elif pokoj == "schody":
        print("jsi u schodu")
        print("\nco delat?")
        print("1. jit zpatky")
        print("2. jit k vychodu")
        print("3. inventar")
        print("\n4. ukoncit hru")
        x = input(">>> ")
        if x == "1":
            pokoj = "koridor2"
        elif x == "2":
            if inventar["prkno"]:
                vychod = True
                pokoj = "vychod"
            else:
                print("nemuzes projit na schodach chyby prkno")
        elif x == "3":
            ukaz_inventar()
        elif x == "4":
            print("konec")
            break
        else:
            print("nemuzes to udelat")

    elif pokoj == "vychod":
        vec1 = "nuz"
        vec2 = "nabita svitilna"
        vec3 = "klic"

        print("jsi u vychodu")
        print("\nco delat?")
        print("1. jit zpatky")
        print("2. utict")
        print("3. inventar")
        print("\n4. ukoncit hru")
        x = input(">>> ")
        if x == "1":
            pokoj = "schody"
        elif x == "2":
            while True:
                if not inventar[vec3]:
                    print("\nnemuzes otevrit dvere. potrebujes klic.")
                elif not zabil and not inventar[vec1]:
                    print("\njsi utekl ale v lese je moc temno. jsi se zabloudil")
                    print("spatny konec")
                    running = False
                    break
                elif inventar[vec2] and not zabil:
                    print("\njsi utekl.")
                    print("svitilna ti osvicuje cestu, ale kvuli amputovane noze jsi moc pomaly.")
                    print("tebe nasel protivnik a odnesl te zpatky")
                    print("spatny konec")
                    running = False
                    break
                else:
                    print("\njsi utekl.")
                    print("svitilna ti osvicuje cestu, ale kvuli amputovane noze jsi moc pomaly.")
                    print("nic jsi nenasel a vratil se zpatky.")
                    print("ve sklepe jsi nasel vodu a urcite mnozstvi jidla.")
                    print("zijes jen s nadeji ze te nekdo najde.")
                    print("dobry konec (mozna)")
                    running = False
                    break 
        elif x == "3":
            ukaz_inventar()
        elif x == "4":
            print("konec")
            break
        else:
            print("nemuzes to udelat")
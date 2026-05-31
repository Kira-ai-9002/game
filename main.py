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

print("\nByl jsi unesen.")
print("Nic si nepamatuješ.")
print("Probudíš se ve vaně plné ledu.")
print("Chybí ti jedna noha.")
print("Musíš se dostat ven a nenarazit na únosce.")

while RUNNING:
    if POKOJ == "koupelna":
        print("\nJsi v koupelně.")
        print("Je tu umyvadlo se zrcadlem a toaleta.")
        print("Za zrcadlem a pod umyvadlem jsou skříňky.")
        print("U dveří leží mop.")
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
                POKOJ = "koridor1"
            else:
                print("\nNedokážeš na něj dosáhnout. Potřebuješ dlouhý předmět, který se zachytí za kliku.")
        elif x == "2":
            while True:
                if not INVENTAR["zelezna_tyc"] or ("baterka1" in INVENTAR and not INVENTAR["baterka1"]):
                    print(" \nPod umyvadlem se nachází:")
                    if not INVENTAR["zelezna_tyc"]:
                        print("1. Vzít Ohnutý kus železné tyče.")
                    if "baterka1" in INVENTAR and not INVENTAR["baterka1"]:
                        print("2. Vzít baterku")
                else:
                    print("\nTady nic není")
                print("3. Zpátky")
                y = input(">>> ")
                if y == "1":
                    if not INVENTAR["zelezna_tyc"]:
                        INVENTAR["zelezna_tyc"] = True
                        print("\nMáš ohnutý kus železné tyče.")
                    else:
                        print("\nNemůžeš to udělat")
                elif y == "2":
                    if "baterka1" in INVENTAR and not INVENTAR["baterka1"]:
                        INVENTAR["baterka1"] = True
                        print("\nMáš baterku")
                    else:
                        print("\nNemůžeš to udělat")
                    if "baterka1" in INVENTAR and INVENTAR["baterka1"] and INVENTAR["baterka2"] and INVENTAR["svitilna"]:
                        INVENTAR["nabita svitilna"] = True
                        del INVENTAR["baterka1"]
                        del INVENTAR["baterka2"]
                        del INVENTAR["svitilna"]
                        print("\nNabil jsi svítilnu dvěma baterkami.")
                elif y == "3":
                    break
                else:
                    print("\nNemůžeš to udělat") 
        elif x == "3":
            while True:
                if not INVENTAR["nabita svitilna"]:
                    print("\nNení tu nic vidět. Potřebuješ si posvítit.")
                else:
                    if not INVENTAR["nuz"]:
                        print(" \nPod vanou je nůž")
                        print("1. Vzít nůž")
                    else:
                        print("\nNic tady není")
                print("2. Zpátky")
                y = input(">>> ")
                if y == "1":
                    if INVENTAR["nabita svitilna"]:
                        if not INVENTAR["nuz"]:
                            INVENTAR["nuz"] = True
                            print("\nMáš nůž")
                        else:
                            print("\nNemůžeš to udělat")
                    else:
                        print("\nNemůžeš to udělat")
                elif y == "2":
                    break
                else:
                    print("\nNemůžeš to udělat")
        elif x == "4":
            print("\nOpřel ses o umyvadlo a podařilo se ti postavit.")
            print("Když jsi otevřel horní skříňku, dvířka se zrcadlem se utrhla a rozbila.")
            print("Únosce tě uslyšel a přišel za tebou.")
            print("\nKonec")
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
            print("\nKonec")
            break
        else:
            print("\nNemůžeš to udělat")

    elif POKOJ == "koridor1":
        print("\nJsi v dlouhé chodbě s mnoha dveřmi.")
        print("Na konci chodby jsou schody.")
        print("Za dveřmi napravo slyšíš hluk.")
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
                        print("\nPootevřel jsi dveře a uviděl únosce.")
                        print("Něco dělal u stolu.")
                        print("Chceš nenápadně odejít, ale on tě zaslechl.")
                        print("\nKonec")
                        RUNNING = False
                        break
                    else:
                        print("\nPootevřel jsi dveře a uviděl únosce.")
                        print("Máš nůž a on tě nevidí.")
                        print("\nCo dělat?")
                        print("1. Zabít ho")
                else:
                    print("\nLeží tu zohavené tělo únosce.")
                print("2. Odejít z pokoje")
                y = input(">>> ")
                if y == "1":
                    if not ZABIL:
                        ZABIL = True
                        print("\nOpatrně ses k němu doplazil a řízl ho do šlachy.")
                        print("Spadl a začal křičet.")
                        print("Neváhal jsi a podřízl mu hrdlo.")
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
            print("\nKonec")
            break
        else:
            print("\nNemůžeš to udělat")

    elif POKOJ == "levy pokoj":
        print("\nDoplazil ses do téměř prázdné místnosti, ale v rohu stojí regál.")
        print("\nCo dělat?")
        print("1. Odejít z pokoje")
        print("2. Prohlédnout regál")
        print("3. Inventář")
        print("\n4. Ukončit hru")
        x = input(">>> ")

        if x == "1":
            POKOJ = "koridor1"
        elif x == "2":
            while True:
                if not INVENTAR["pila"]:
                    print(" \nNa regálu leží pila.")
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
                        print("\nNemůžeš to udělat")
                elif y == "2":
                    break
                else:
                    print("\nNemůžeš to udělat")
        elif x == "3":
            ukaz_inventar()
        elif x == "4":
            print("\nKonec")
            break
        else:
            print("\nNemůžeš to udělat")

    elif POKOJ == "koridor2":
        print("\nJsi v chodbě.")
        print("Vedle jsou schody, ale chybí u něj jeden schod.")
        print("Jsou tu červené a dřevěné dveře.")
        print("Jedna místnost nemá dveře a je v ní tma.")
        print("Vedle tebe je topení a pod ním je hodně místa, ale je zahrazené dřevěnými deskami.")
        print("\nCo dělat?")
        print("1. Jít ke koupelně")
        print("2. Jít ke schodům")
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
                print("\nJsi před vstupem do místnosti.")
                if not INVENTAR["mop"]:
                    print("\nJe tam tma.")
                    print("Žárovka se nakřivila v objímce a přestala svítit.")
                    print("Musíš ji nějakou dlouhou tyčí zatlačit zpět.")
                    print("\n1. Vstoupit do místnosti")
                    print("2. Jít zpátky")
                else:
                    print("\nDíky mopu žárovka je zpět v objímce. Místnost je osvětlená.")
                    POKOJ = "temny pokoj"
                    break
                y = input(">>> ")
                if y == "1":
                    print("\nDoplazíš se do místnosti.")
                    print("V jediném okamžiku pod tebou zmizí podlaha.")
                    print("Spadnul jsi do propasti a zlomil si vaz.")
                    print("\nKonec")
                    RUNNING = False
                    break
                elif y == "2":
                    break
                else:
                    print("\nNemůžeš to udělat")
        elif x == "6":
            while True:
                if not PREKLIZKA:
                    print("\nDíváš se pod topením.")
                    print("Je tam otvor, ale je zakrytý překližkou připevněnou šroubami.")
                    if INVENTAR["sroubovak"]:
                        PREKLIZKA = True
                        print("Odstranil jsi překližku.")
                        if not INVENTAR["svitilna"]:
                            print(" \nPod topením se nachází svítilna")
                            print("1. Vzít svítilnu")
                        else:
                            print("\nNic tady není")
                    else:
                        print("\nPotřebuješ šroubovák.")
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
                        print("\nNemůžeš to udělat")
                    if "svitilna" in INVENTAR and INVENTAR["svitilna"] and \
                        "baterka1" in INVENTAR and INVENTAR["baterka1"] and \
                        "baterka2" in INVENTAR and INVENTAR["baterka2"]:
                        INVENTAR["nabita svitilna"] = True
                        del INVENTAR["svitilna"]
                        del INVENTAR["baterka1"]
                        del INVENTAR["baterka2"]
                        print("\nNabil jsi svítilnu dvěma baterkami.")
                elif y == "2":
                    break
                else:
                    print("\nNemůžeš to udělat")
        elif x == "7":
            ukaz_inventar()
        elif x == "8":
            print("\nKonec")
            break
        else:
            print("\nNemůžeš to udělat")

    elif POKOJ == "cerveny pokoj":
        print("\nJsi v červené místnosti.")
        print("U stěny stojí vysoká komoda a vedle tebe je malá stolička.")
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
                    print("\nKomoda je příliš vysoká.")
                    print("Nedokážeš na ni dosáhnout.")
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
                        print("\nNemůžeš to udělat")
                    else:
                        if not INVENTAR["klic"]:
                            INVENTAR["klic"] = True
                            print("\nMáš klíč")
                        else:
                            print("\nNemůžeš to udělat")
                elif y == "2":
                    break
                else:
                    print("\nNemůžeš to udělat")
        elif x == "3":
            if not INVENTAR["zidle"]:
                INVENTAR["zidle"] = True
                print("\nMáš židli")
            else:
                print("\nNemůžeš to udělat")
        elif x == "4":
            ukaz_inventar()
        elif x == "5":
            print("\nKonec")
            break
        else:
            print("\nNemůžeš to udělat")

    elif POKOJ == "dreveny pokoj":
        print("\nJsi v dřevěné místnosti.")
        print("Z podlahy trčí téměř vytržené prkno a v rohu stojí krabice.")
        print("\nCo dělat?")
        print("1. Odejít z pokoje")
        print("2. Zkusit zlomit prkno")
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
                    print("\nOdřízl jsi prkno.")
                    print("Máš prkno.")
                else:
                    print("\nUž máš prkno")
            else:
                print("\nNemáš dost na to síly.")
                print("Potřebuješ nějaký nástroj, kterým prkno odřízneš.")
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
                        print("\nNemůžeš to udělat")
                elif y == "2":
                    break
                else:
                    print("\nNemůžeš to udělat")
        elif x == "4":
            ukaz_inventar()
        elif x == "5":
            print("\nKonec")
            break
        else:
            print("\nNemůžeš to udělat")

    elif POKOJ == "temny pokoj":
        print("\nJsi v místnosti.")
        print("Uprostřed je velká díra, ale dá se obejít.")
        print("Na druhé straně propasti je skříň.")
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
                    print(" \nVe skříni je baterka")
                    print("1. Vzít baterku")
                else:
                    print("\nNic tady není")
                print("2. Zpátky")
                y = input(">>> ")
                if y == "1":
                    if "baterka2" in INVENTAR and not INVENTAR["baterka2"]:
                        INVENTAR["baterka2"] = True
                        print("\nMáš baterku")
                    else:
                        print("\nNemůžeš to udělat")
                    if "baterka1" in INVENTAR and INVENTAR["baterka1"] and \
                        "baterka2" in INVENTAR and INVENTAR["baterka2"] and \
                        "svitilna" in INVENTAR and INVENTAR["svitilna"]:
                        INVENTAR["nabita svitilna"] = True
                        del INVENTAR["baterka1"]
                        del INVENTAR["baterka2"]
                        del INVENTAR["svitilna"]
                        print("\nNabil jsi svítilnu dvěma baterkami.")
                elif y == "2":
                    break
                else:
                    print("\nNemůžeš to udělat")
        elif x == "3":
            while True:
                if not INVENTAR["sroubovak"]:
                    print("\nNa dně propasti leží šroubovák.")
                    print("1. Vzít šroubovák")
                else:
                    print("\nNic tady není")
                print("2. Zpátky")
                y = input(">>> ")
                if y == "1":
                    if not INVENTAR["drat"]:
                        print("\nNemůžeš na něj dosáhnout.")
                        print("Musíš ho něčím vytáhnout.")
                    else:
                        INVENTAR["sroubovak"] = True
                        print("\nZ drátu jsi vyrobil háček a vytáhl šroubovák.")
                        print("Máš šroubovák.")
                elif y == "2":
                    break
                else:
                    print("\nNemůžeš to udělat")
        elif x == "4":
            ukaz_inventar()
        elif x == "5":
            print("\nKonec")
            break
        else:
            print("\nNemůžeš to udělat")

    elif POKOJ == "schody":
        print("\nJsi před schodami.")
        print("Nahoře je východ.")
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
                print("\nNemůžeš projít.")
                print("Schodišti chybí jeden schod.")
        elif x == "3":
            ukaz_inventar()
        elif x == "4":
            print("\nKonec")
            break
        else:
            print("\nNemůžeš to udělat")

    elif POKOJ == "vychod":
        print("\nJsi před východem.")
        print("Pod dveřmi fouká vítr.")
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
                    print("\nDveře jsou zamčené. Potřebuješ klíč.")
                elif not ZABIL and not INVENTAR["nabita svitilna"]:
                    print("\nOtevřeš dveře a doplazíš se ven.")
                    print("Před tebou je temný les. Nic není vidět.")
                    print("Plazíš se náhodným směrem.")
                    print("Po dlouhé době jsi stále v hlubokém lese.")
                    print("Ztratil ses a nemůžeš najít cestu ven.")
                    print("\nŠpatný konec (Zmrzl jsi v lese. Není to zas tak špatná smrt.)")
                    RUNNING = False
                    break
                elif INVENTAR["nabita svitilna"] and not ZABIL:
                    print("\nUtekl jsi.")
                    print("Otevřeš dveře a doplazíš se ven. Před tebou je temný les.")
                    print("Svítilna ti osvětluje cestu, ale kvůli amputované noze jsi velmi pomalý.")
                    print("Po nějaké době tě, kvůli světlu svítilny mezi stromy, najde únosce a odnese tě zpět.")
                    print("\nŠpatný konec (našli tě)")
                    RUNNING = False
                    break
                else:
                    print("\nUtekl jsi.")
                    print("Otevřeš dveře a doplazíš se ven. Před tebou je temný les.")
                    print("Svítilna ti osvětluje cestu, ale kvůli amputované noze jsi velmi pomalý.")
                    print("Po dlouhé době jsi stále v hlubokém lese. Podle vlastních stop ses vrátil zpět.")
                    print("V místnosti s mrtvým tělem jsi našel jídlo a z kohoutku tekla voda.")
                    print("Každý den se snažíš najít cestu z lesa, ale nedaří se ti to.")
                    print("Žiješ jen s nadějí, že tě někdo najde a zachrání.")
                    print("\nDobrý konec (asi).")
                    RUNNING = False
                    break
        elif x == "3":
            ukaz_inventar()
        elif x == "4":
            print("\nKonec")
            break
        else:
            print("\nNemůžeš to udělat")

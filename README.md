# Game-1

Textová RPG hra v Pythonu (únikovka) .

## Příběh

Hráč byl unesen, únosce mu amputoval nohu. Musí se dostat ven ze sklepa, aniž by narazil na únosce.

## Struktura hry

- Globální inventář `INVENTAR` s předměty (svítilna, nůž, pila, klíč atd.)
- Proměnná `POKOJ` sleduje aktuální místnost
- Hlavní smyčka `while` s kontrolou místnosti přes `elif`

## Místnosti

| Název | Popis |
|---|---|
| `koupelna` | Koupelna (startovací) |
| `koridor1` / `koridor2` | Chodby |
| `levy pokoj` | Levý pokoj (pila) |
| `cerveny pokoj` | Červený pokoj (klíč) |
| `dreveny pokoj` | Dřevěný pokoj (prkno, drát) |
| `temny pokoj` | Temný pokoj (baterie, šroubovák) |
| `schody` | Schodiště |
| `vychod` | Východ |

## Konce

- **Špatný konec 1:** Zmrzl v lese (odešel bez svítilny)
- **Špatný konec 2:** Nalezen únoscem (odešel se svítilnou, ale nezabil únosce)
- **Dobrý konec:** Přežívá ve sklepě (zabil únosce a má nabitou svítilnu)

## Jak funguje kód

**Hlavní smyčka** - hra běží v `while RUNNING`. V každé iteraci se zkontroluje proměnná `POKOJ` a spustí odpovídající `elif` blok pro danou místnost. Hráč zadává číslo volby přes `input(">>> ")`.

**Systém místností** - každá místnost je jeden velký `elif` blok. Přechod mezi místnostmi probíhá změnou hodnoty `POKOJ` (např. `POKOJ = "koridor1"`). Hra končí buď příkazem `break` (ukončení smyčky) nebo nastavením `RUNNING = False`.

**Inventář** - slovník `INVENTAR`, kde klíč je název předmětu a hodnota `True/False` označuje, zda ho hráč drží. Některé předměty se po sebrání automaticky zkombinují - pokud hráč má `baterka1`, `baterka2` i `svitilna` zároveň, všechny tři se odstraní a nahradí klíčem `nabita svitilna`.

**Podmenu** - interakce s předměty (prohledání skříně, výběr akce) probíhají ve vnořené smyčce `while True`. Z ní se vychází přes `break`.

**Stavové proměnné** - `ZABIL` (bool) sleduje, zda byl únosce zabit; `PREKLIZKA` (bool) zda byla odstraněna překližka pod topením. Tyto stavy ovlivňují dostupné akce a výsledný konec hry.

**Konce hry** - jsou určeny kombinací `ZABIL` a `nabita svitilna` v momentě útěku: bez svítilny hráč zmrzne, se svítilnou ale živým únoscem je dopaden, s oběma přežije.

## Spuštění

```bash
python main.py
```

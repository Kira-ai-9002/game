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
- **Dobrý konec:** Přežívá ve slkepě (zabil únosce a má nabitou svítilnu)

## Spuštění

```bash
python main.py
```

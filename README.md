# Game-1

Textová hra v Pythonu v českém jazyce.

## Příběh

Hráč byl unesen, probudil se ve vaně plné ledu a chybí mu jedna noha. Musí se dostat ven z budovy, aniž by narazil na únosce.

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
| `temny pokoj` | Tmavý pokoj (baterie, šroubovák) |
| `schody` | Schodiště |
| `vychod` | Východ |

## Konce

- **Špatný konec 1:** Zmrzl v lese — odešel bez svítilny
- **Špatný konec 2:** Nalezen únoscem — odešel se svítilnou, ale nezabil únosce
- **Dobrý konec:** Zabil únosce + má nabitou svítilnu → přežívá v lese

## Spuštění

```bash
python main.py
```

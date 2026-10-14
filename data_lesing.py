"""
Felles funksjon for å lese inn værdata fra Sinnes (Sirdal).

Alle de andre filene i prosjektet bruker les_data(), så det er
bare her vi trenger å tenke på filformatet.

Ting vi oppdaget når vi så på CSV-fila:
 - skilletegnet er semikolon
 - desimaltall har komma (1,4 og ikke 1.4)
 - manglende målinger er skrevet som "-"
 - siste linje i fila er bare en lisenstekst, ikke data
 - radene ligger ikke helt i datorekkefølge, så vi sorterer etter dato
"""

import csv
from datetime import datetime

STANDARD_FIL = "data/sinnes_2014_2025_med_makstemperatur.csv"


def til_tall(tekst):
    """Gjør om en tekst som '2,8' til 2.8. Returnerer None hvis verdien mangler."""
    tekst = tekst.strip()
    if tekst == "" or tekst == "-":
        return None
    return float(tekst.replace(",", "."))


def les_data(filnavn=STANDARD_FIL):
    """
    Leser CSV-fila og returnerer en liste med én dict per dag, sortert på dato.

    Nøklene i hver dict er:
        dato, maks_temp, temp, nedbor, vind, snodybde
    Verdier som mangler blir None.
    Hvis fila ikke har kolonnen for maksimumstemperatur blir maks_temp None.
    """
    data = []

    # utf-8-sig fordi fila starter med en usynlig BOM-markør
    with open(filnavn, encoding="utf-8-sig") as fil:
        leser = csv.reader(fil, delimiter=";")
        overskrifter = next(leser)

        # finn kolonnene på navn, ikke på nummer, siden de to filene er ulike
        def kol(navn):
            for i, o in enumerate(overskrifter):
                if o.startswith(navn):
                    return i
            return None

        i_dato = kol("Tid")
        i_maks = kol("Maksimumstemperatur")
        i_temp = kol("Middeltemperatur")
        i_nedbor = kol("Nedbør")
        i_vind = kol("Høyeste middelvind")
        i_snø = kol("Snødybde")

        for rad in leser:
            # hopper over lisensteksten på slutten (og eventuelle tomme linjer).
            # Lisenslinja har like mange kolonner som resten, men datokolonnen er tom.
            if len(rad) < len(overskrifter) or rad[i_dato].strip() == "":
                continue

            dag = {
                "dato": datetime.strptime(rad[i_dato], "%d.%m.%Y"),
                "maks_temp": til_tall(rad[i_maks]) if i_maks is not None else None,
                "temp": til_tall(rad[i_temp]),
                "nedbor": til_tall(rad[i_nedbor]),
                "vind": til_tall(rad[i_vind]),
                "snodybde": til_tall(rad[i_snø]),
            }
            data.append(dag)

    data.sort(key=lambda d: d["dato"])
    return data


def velg_aar(data, aar):
    """Returnerer bare dagene som hører til et gitt år."""
    return [d for d in data if d["dato"].year == aar]


def spor_om_aar(data):
    """Spør brukeren om et årstall og sjekker at vi har data for det."""
    forste = data[0]["dato"].year
    siste = data[-1]["dato"].year
    while True:
        svar = input(f"Skriv inn årstall ({forste}-{siste}): ")
        try:
            aar = int(svar)
        except ValueError:
            print("Det der var ikke et heltall, prøv igjen.")
            continue
        if forste <= aar <= siste:
            return aar
        print(f"Vi har bare data fra {forste} til {siste}.")


if __name__ == "__main__":
    # liten test: kjør denne fila direkte for å se at innlesingen virker
    d = les_data()
    print("Antall dager:", len(d))
    print("Første dag:", d[0])
    print("Siste dag:", d[-1])

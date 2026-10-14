"""
Oppgave h) Antall sommerdager, høysommerdager og tropedager i et år.

    sommerdag       maks temperatur over 20 grader
    høysommerdag    maks temperatur over 25 grader
    tropedag        maks temperatur over 30 grader

En tropedag er altså også en høysommerdag og en sommerdag.
Dette krever kolonnen for maksimumstemperatur, så vi bruker fila
sinnes_2014_2025_med_makstemperatur.csv.
"""

from data_lesing import les_data, velg_aar, spor_om_aar


def tell_dager(data, aar):
    """Returnerer (sommerdager, høysommerdager, tropedager) for året."""
    sommer = 0
    hoysommer = 0
    trope = 0

    for d in velg_aar(data, aar):
        maks = d["maks_temp"]
        if maks is None:
            continue  # manglende måling
        if maks > 20:
            sommer += 1
        if maks > 25:
            hoysommer += 1
        if maks > 30:
            trope += 1

    return sommer, hoysommer, trope


if __name__ == "__main__":
    data = les_data()
    aar = spor_om_aar(data)
    sommer, hoysommer, trope = tell_dager(data, aar)
    print(f"I {aar} var det:")
    print(f"  {sommer} sommerdager (over 20 grader)")
    print(f"  {hoysommer} høysommerdager (over 25 grader)")
    print(f"  {trope} tropedager (over 30 grader)")

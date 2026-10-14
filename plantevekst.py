"""
Oppgave f) Forenklet plantevekst
Oppgave i) Plantevekst med frostskade (frivillig)
"""

from datetime import datetime

from data_lesing import les_data, velg_aar, spor_om_aar

MIN_TEMP = 5  # planten trenger minst 5 grader for å vokse


# ---------- del f ----------

def vekst_en_dag(temp):
    """Veksten en dag er temperaturen minus 5, men aldri under 0 (ingen frost her)."""
    if temp is None or temp < MIN_TEMP:
        return 0
    return temp - MIN_TEMP


def total_vekst(data, aar):
    """Summerer veksten for alle dagene i året."""
    sum_vekst = 0
    for d in velg_aar(data, aar):
        sum_vekst += vekst_en_dag(d["temp"])
    return sum_vekst


# ---------- del i ----------

def vekst_med_frost(temp):
    """
    Som vekst_en_dag, men nå skader minusgrader planten.
    Under 0 grader er veksten negativ og like stor som antall minusgrader.
    Mellom 0 og 5 grader skjer det ingenting.
    """
    if temp is None:
        return 0
    if temp < 0:
        return temp          # f.eks. -3 grader gir -3 i vekst
    if temp < MIN_TEMP:
        return 0
    return temp - MIN_TEMP


def vekst_fra_dato(data, aar, startdato):
    """
    Går gjennom året fra startdato og legger sammen veksten dag for dag.
    Returnerer (maks, sluttverdi):
      maks       = det høyeste vekstnivået planten når på et tidspunkt i året
      sluttverdi = totalen ved årets slutt (frost etter toppen drar den ned igjen)
    """
    kumulativ = 0
    maks = 0
    for d in velg_aar(data, aar):
        if d["dato"] < startdato:
            continue
        kumulativ += vekst_med_frost(d["temp"])
        if kumulativ > maks:
            maks = kumulativ
    return maks, kumulativ


def vekst_fra_1_april(data, aar):
    """Maksimal plantevekst hvis planten starter 1. april."""
    return vekst_fra_dato(data, aar, datetime(aar, 4, 1))


def beste_startdato(data, aar):
    """
    Prøver alle mulige startdatoer i året og finner den som gir høyest maksverdi.
    Returnerer (beste startdato, vekst den gir).
    Hvis flere datoer gir samme vekst tar vi den første.
    """
    beste_dato = None
    beste_vekst = -1

    for d in velg_aar(data, aar):
        maks, _ = vekst_fra_dato(data, aar, d["dato"])
        if maks > beste_vekst:
            beste_vekst = maks
            beste_dato = d["dato"]

    return beste_dato, beste_vekst


if __name__ == "__main__":
    data = les_data()
    aar = spor_om_aar(data)

    print(f"Total plantevekst i {aar} (f): {total_vekst(data, aar):.1f}")

    maks, slutt = vekst_fra_1_april(data, aar)
    print(f"Med frostskade, start 1. april (i): maks {maks:.1f}, ved årsslutt {slutt:.1f}")

    dato, vekst = beste_startdato(data, aar)
    print(f"Beste startdato {dato.strftime('%d.%m.%Y')} gir vekst {vekst:.1f}")

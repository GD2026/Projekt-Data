"""
Oppgave g) Lengste periode uten nedbør
"""

from datetime import timedelta

from data_lesing import les_data


def lengste_toerke(data):
    """
    Finner den lengste sammenhengende perioden der døgnnedbøren er 0.
    Returnerer (lengde i dager, startdato, sluttdato).

    Viktig: data må være sortert på dato (det gjør les_data), og dagene må
    komme rett etter hverandre. Hvis nedbøren mangler en dag avbryter vi
    perioden, siden vi ikke vet om det regnet.
    """
    beste_lengde = 0
    beste_start = None
    beste_slutt = None

    naa_lengde = 0
    naa_start = None
    forrige_dato = None

    for d in data:
        # hvis det er hull i datoene starter vi på nytt
        if forrige_dato is not None and d["dato"] - forrige_dato != timedelta(days=1):
            naa_lengde = 0

        if d["nedbor"] == 0:
            if naa_lengde == 0:
                naa_start = d["dato"]
            naa_lengde += 1

            if naa_lengde > beste_lengde:
                beste_lengde = naa_lengde
                beste_start = naa_start
                beste_slutt = d["dato"]
        else:
            # nedbør større enn 0, eller måling mangler (None)
            naa_lengde = 0

        forrige_dato = d["dato"]

    return beste_lengde, beste_start, beste_slutt


if __name__ == "__main__":
    data = les_data()
    lengde, start, slutt = lengste_toerke(data)
    print(f"Lengste periode uten nedbør: {lengde} dager")
    print(f"Fra {start.strftime('%d.%m.%Y')} til {slutt.strftime('%d.%m.%Y')}")

"""
Oppgave e) Hvor mange dager var det skiføre?

Skiføre = snødybde på minst 20 cm.
Sesongen går fra 1. november året før til og med 31. mai i det oppgitte året.
"""

from datetime import datetime

from data_lesing import les_data, spor_om_aar

MIN_SNODYBDE = 20  # cm


def antall_skidager(data, aar):
    """
    Teller dager med skiføre i sesongen som slutter i 'aar'.
    Returnerer (antall skidager, antall dager i sesongen vi har data for,
    antall dager der snødybden mangler).
    """
    start = datetime(aar - 1, 11, 1)
    slutt = datetime(aar, 5, 31)

    skidager = 0
    dager_i_sesong = 0
    mangler = 0

    for d in data:
        if start <= d["dato"] <= slutt:
            dager_i_sesong += 1
            if d["snodybde"] is None:
                # vi vet ikke hva snødybden var, så dagen telles ikke som skiføre
                mangler += 1
            elif d["snodybde"] >= MIN_SNODYBDE:
                skidager += 1

    return skidager, dager_i_sesong, mangler


if __name__ == "__main__":
    data = les_data()
    aar = spor_om_aar(data)
    skidager, dager, mangler = antall_skidager(data, aar)

    if aar == data[0]["dato"].year:
        print("OBS: datane starter 1. januar", aar, "så november og desember mangler.")

    print(f"Skisesongen {aar - 1}/{aar}: {skidager} dager med skiføre")
    print(f"({dager} dager i sesongen, snødybde mangler på {mangler} av dem)")

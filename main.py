"""
Hovedprogram for data-projekt (DAT120, øving 7 og 10).
Kjør med:  python main.py
"""

from data_lesing import les_data, spor_om_aar
from plotting import plott_aar
from skiforhold import antall_skidager
from plantevekst import total_vekst, vekst_fra_1_april, beste_startdato
from nedbor import lengste_toerke
from temperaturdager import tell_dager


def meny():
    print()
    print("Velg oppgave:")
    print(" d) plott et år")
    print(" e) skiføre")
    print(" f) plantevekst")
    print(" g) lengste periode uten nedbør")
    print(" h) sommerdager, høysommerdager og tropedager")
    print(" i) plantevekst med frostskade")
    print(" q) avslutt")
    return input("Valg: ").strip().lower()


def main():
    data = les_data()
    print(f"Leste {len(data)} dager fra {data[0]['dato'].date()} til {data[-1]['dato'].date()}")

    while True:
        valg = meny()

        if valg == "q":
            break

        elif valg == "d":
            plott_aar(data, spor_om_aar(data))

        elif valg == "e":
            aar = spor_om_aar(data)
            skidager, dager, mangler = antall_skidager(data, aar)
            print(f"Skisesongen {aar - 1}/{aar}: {skidager} dager med skiføre")
            print(f"({dager} dager i sesongen, snødybde mangler på {mangler})")

        elif valg == "f":
            aar = spor_om_aar(data)
            print(f"Total plantevekst i {aar}: {total_vekst(data, aar):.1f}")

        elif valg == "g":
            lengde, start, slutt = lengste_toerke(data)
            print(f"Lengste periode uten nedbør: {lengde} dager")
            print(f"Fra {start.strftime('%d.%m.%Y')} til {slutt.strftime('%d.%m.%Y')}")

        elif valg == "h":
            aar = spor_om_aar(data)
            sommer, hoysommer, trope = tell_dager(data, aar)
            print(f"{aar}: {sommer} sommerdager, {hoysommer} høysommerdager, {trope} tropedager")

        elif valg == "i":
            aar = spor_om_aar(data)
            maks, slutt = vekst_fra_1_april(data, aar)
            print(f"Start 1. april: maks vekst {maks:.1f} (ved årsslutt {slutt:.1f})")
            dato, vekst = beste_startdato(data, aar)
            print(f"Beste startdato er {dato.strftime('%d.%m.%Y')} med vekst {vekst:.1f}")

        else:
            print("Kjenner ikke igjen valget, prøv igjen.")


if __name__ == "__main__":
    main()

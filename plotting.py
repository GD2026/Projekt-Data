"""
Oppgave d) Plotting av snødybde, nedbør, middeltemperatur og vind for ett år.
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from data_lesing import les_data, velg_aar, spor_om_aar


def plott_aar(data, aar, lagre_som=None):
    """
    Lager fire plott under hverandre for året 'aar'.
    Hvis lagre_som er satt lagres figuren som bildefil, ellers vises den.
    """
    dager = velg_aar(data, aar)
    if len(dager) == 0:
        print(f"Ingen data for {aar}")
        return

    datoer = [d["dato"] for d in dager]

    # (nøkkel i dicten, tittel, enhet, farge)
    serier = [
        ("snodybde", "Snødybde", "cm", "tab:blue"),
        ("nedbor", "Nedbør", "mm", "tab:green"),
        ("temp", "Middeltemperatur", "°C", "tab:red"),
        ("vind", "Høyeste middelvind", "m/s", "tab:gray"),
    ]

    fig, akser = plt.subplots(4, 1, figsize=(10, 9), sharex=True)

    for akse, (nokkel, tittel, enhet, farge) in zip(akser, serier):
        # None gjør at matplotlib lager hull i linja der målingen mangler
        verdier = [d[nokkel] if d[nokkel] is not None else float("nan") for d in dager]
        akse.plot(datoer, verdier, color=farge, linewidth=1)
        akse.set_ylabel(f"{tittel} ({enhet})")
        akse.grid(True, alpha=0.3)

    # temperatur: tegn en strek ved 0 grader så det er lett å se frost
    akser[2].axhline(0, color="black", linewidth=0.8)

    # penere datoer på x-aksen (en tick per måned)
    akser[-1].xaxis.set_major_locator(mdates.MonthLocator())
    akser[-1].xaxis.set_major_formatter(mdates.DateFormatter("%b"))
    akser[-1].set_xlabel("Dato")

    fig.suptitle(f"Sinnes værstasjon, {aar}")
    fig.tight_layout()

    if lagre_som:
        fig.savefig(lagre_som, dpi=120)
        print("Lagret figur som", lagre_som)
        plt.close(fig)
    else:
        plt.show()


if __name__ == "__main__":
    data = les_data()
    aar = spor_om_aar(data)
    plott_aar(data, aar)

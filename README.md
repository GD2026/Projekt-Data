# data-projekt (DAT120, øving 7 og 10)

Python-program som leser og analyserer værdata fra Sinnes værstasjon i Sirdal. Dataene kommer fra Meteorologisk institutt (seklima.met.no) og har CC BY 4.0-lisens.

## Kjøre programmet

Du trenger Python 3 og matplotlib (`pip install matplotlib`). Kjør fra mappa med:

```
python main.py
```

Da får du en meny der du velger oppgave og skriver inn årstall. Hver modul kan også kjøres for seg, for eksempel `python skiforhold.py`.

## Filer

| Fil | Oppgave |
|---|---|
| `data_lesing.py` | leser CSV-fila, felles for alle |
| `plotting.py` | d) plott av snødybde, nedbør, temperatur og vind |
| `skiforhold.py` | e) antall dager med skiføre |
| `plantevekst.py` | f) plantevekst og i) plantevekst med frostskade |
| `nedbor.py` | g) lengste periode uten nedbør |
| `temperaturdager.py` | h) sommerdager, høysommerdager og tropedager |
| `main.py` | meny som kobler alt sammen |
| `data/` | CSV-filene |

Vi bruker `sinnes_2014_2025_med_makstemperatur.csv` som hovedfil, siden den også har maksimumstemperatur (trengs i oppgave h). Den andre fila ligger i mappa, og `les_data()` takler begge to.

## Oppgavefordeling (oppgave c)

`les_data()` måtte være ferdig først, siden alle de andre bruker den. Den skrev vi sammen, og etter det kunne resten gjøres hver for seg fordi funksjonene ikke avhenger av hverandre.

Vi er to på gruppa, Azad og Marius, og delte oppgavene likt.

| Hvem | Oppgave | Branch |
|---|---|---|
| Begge | `data_lesing.py`, GitHub-oppsett | `main` |
| Azad | d) plotting | `plotting` |
| Azad | e) skiføre | `skiforhold` |
| Azad | g) lengste periode uten nedbør | `nedbor` |
| Azad | `main.py` (meny) | `main` |
| Marius | f) og i) plantevekst | `plantevekst` |
| Marius | h) sommerdager, høysommerdager og tropedager | `temperaturdager` |
| Marius | README og testing av alle funksjonene | `main` |

Marius har oppgave f og i, som er den største enkeltoppgaven, så Azad tok én deloppgave mer til gjengjeld. Vi leste gjennom og testet hverandres kode før hver merge. Hver branch ble merget inn i `main` når oppgaven var ferdig.

## Valg vi har tatt

**Manglende målinger.** I CSV-fila er manglende verdier skrevet som `-`. Vi leser dem inn som `None` og håndterer dem slik:

- Skiføre: en dag uten snødybde teller ikke som skiføre. Programmet skriver ut hvor mange dager som manglet, så man ser hvor sikkert tallet er.
- Plantevekst: dager uten temperatur gir 0 i vekst.
- Tørkeperiode: manglende nedbørsmåling avbryter perioden, siden vi ikke vet om det regnet.
- Sommerdager osv.: dager uten maksimumstemperatur hoppes over.

**Sortering.** Radene i fila ligger ikke helt i datorekkefølge (noen blokker er forskjøvet). Det ødelegger oppgave g, som bygger på at dagene kommer etter hverandre, så `les_data()` sorterer alltid på dato.

**Lisenslinja.** Siste linje i fila er en lisenstekst med tomme felt. Den hoppes over.

**Skisesong 2014.** Dataene starter 1. januar 2014, så november og desember 2013 finnes ikke. Sesongen 2014 blir derfor ufullstendig, og alle dagene vi har fra januar til mai har manglende snødybde. Tallet for 2014 er altså ikke til å stole på.

**Oppgave i (frostskade).** Modellen vi bruker per dag:

- under 0 grader: vekst lik temperaturen (negativ)
- 0 til 5 grader: ingen vekst
- over 5 grader: temperatur minus 5

Planten legger sammen veksten dag for dag fra startdatoen. «Maksimal vekst» tolker vi som det høyeste nivået planten når et sted i løpet av året. Siden frost på høsten drar summen ned igjen, skriver programmet også ut verdien ved årsslutt. Beste startdato finner vi ved å prøve alle datoer i året og velge den som gir høyest maksverdi. Oppgaveteksten kan tolkes litt forskjellig her, så dette bør vi forklare for studentassistenten.

## Eksempelresultater

| År | Skidager | Total vekst (f) | Sommerdager | Høysommerdager | Tropedager |
|---|---|---|---|---|---|
| 2018 | 122 | 1161,4 | 57 | 9 | 0 |
| 2020 | 77 | 936,7 | 31 | 8 | 0 |
| 2022 | 79 | 940,7 | 24 | 1 | 1 |

Lengste periode uten nedbør i hele datasettet: 24 dager, fra 05.05.2018 til 28.05.2018.

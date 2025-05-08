# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjän on mahdollista pelata miinaharavaa, jossa tehtävänä on paljasta ruudukon ruutuja ja vältellä miinoja.

Inspiraatiota käyttöliittymästä otettu [Windows 98:n Miinaharavasta](https://minesweepergame.com/download/windows-98-minesweeper.php)

![Minesweeper 98](https://minesweepergame.com/download/windows-98-minesweeper.png)

## Peruversion tarjoama toiminnallisuus

- Käyttäjä voi pelata miinaharavaa.
- Tarjolla kolme eri vaikeustasoa:
  - **Helppo**: 9x9 ruudukko, 10 miinaa.
  - **Keskitaso**: 16x16 ruudukko, 40 miinaa.
  - **Vaikea**: 16x30 ruudukko, 99 miinaa.
- Pelit tallentuvat tietokantaan.
- Käyttäjä voi tarkastella omia statistiikoitaan, kuten:
  - Pelien määrä
  - Voittojen määrä
  - Häviöiden määrä
  - Keskimääräinen peliaika
  - Nopein voitto vaikeusasteittain
- Peliajan ja löydettyjen miinojen laskenta.
- Miinojen liputtaminen oikealla hiirenpainikkeella.
- Pelaaja voi klikata ruutuja paljastaakseen ne.
- Ruutuun ilmestyy luku, joka kertoo kuinka monta miinaa ruudun ympärillä on.
- Peli päättyy, jos pelaaja paljastaa miinan.
- Peli päättyy, jos pelaaja paljastaa kaikki ruudut, jotka eivät sisällä miinaa.
- Vasen + oikea -klikkaus
  - Jos pelaaja on jo paljastanut ruudun ja sen ympärillä on täsmälleen oikea määrä liputettuja miinoja, ruutua voi klikata samanaikaisesti vasemmalla ja oikealla hiiren painikkeella.
  - Tämä paljastaa automaattisesti kaikki muut ympäröivät ruudut, jotka eivät ole liputettuja.
  - Mikäli liputus oli virheellinen ja miina paljastuu, peli päättyy.

## Jatkokehitysideoita

Ideioita jatkokehitykselle ja lisätoiminnallisuuksille:

- Muokattavat vaikeustasot
  - Käyttäjä voi valita ruudukon koon ja miinojen määrän
- Mahdollisuus asettaa aikarajoitusta
- Tulostaulukko kaikista peleistä

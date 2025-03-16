# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjän on mahdollista pelata miinaharavaa, jossa tehtävänä on paljasta ruudukon ruutuja ja vältellä miinoja.

## Peruversion tarjoama toiminnallisuus

- Käyttäjä voi pelata miinaharavaa
- Tarjolla kolme eri vaikeustasoa
  - Helppo: 9x9 ruudukko, 10 miinaa
  - Keskitaso: 16x16 ruudukko, 40 miinaa
  - Vaikea: 16x30 ruudukko, 99 miinaa
- Tulokset tallennetaan leaderboardiin
- Käyttäjä voi tarkastella omia tuloksiaan leaderboardista
- Peliajan ja löydettyjen miinojen laksenta
- Miinojen liputtaminen oikealla hiirenpainikkeella
- Pelaaja voi klikata ruutuja paljastaakseen ne
- Ruutuun ilmestyy luku, joka kertoo kuinka monta miinaa ruudun ympärillä on
- Peli päättyy, jos pelaaja paljastaa miinan
- Peli päättyy, jos pelaaja paljastaa kaikki ruudut, jotka eivät sisällä miinaa

## Jatkokehitysideoita

- Muokattavat vaikeustasot
  - Käyttäjä voi valita ruudukon koon ja miinojen määrän
- Mahdollisuus asettaa aikarajoitusta
- Left + Right -klikkaus
  - Jos pelaaja on jo paljastunut ruudun ja sen ympäriltä löytyy oikea määrä liputettuja miinoja, pelaaja voi klikata ruutua samanaikaisesti vasemmalla ja oikealla hiirenpainikkeella
  - Tämä avaa kaikki muut ympäröivät ruudut atuomaattisesti, jos ne eivät sisällä miinaa.
  - Jos liputus oli virheellinen, miina voi paljastua ja peli päättyy.

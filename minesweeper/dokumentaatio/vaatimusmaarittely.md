# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjän on mahdollista pelata miinaharavaa, jossa tehtävänä on paljasta ruudukon ruutuja ja vältellä miinoja.

## Peruversion tarjoama toiminnallisuus

- [x] Käyttäjä voi pelata miinaharavaa.
- [x] Tarjolla kolme eri vaikeustasoa:
  - [x] **Helppo**: 9x9 ruudukko, 10 miinaa.
  - [x] **Keskitaso**: 16x16 ruudukko, 40 miinaa.
  - [x] **Vaikea**: 16x30 ruudukko, 99 miinaa.
- [ ] Tulokset tallennetaan leaderboardiin.
- [ ] Käyttäjä voi tarkastella omia tuloksiaan leaderboardista.
- [x] Peliajan ja löydettyjen miinojen laskenta.
- [x] Miinojen liputtaminen oikealla hiirenpainikkeella.
- [x] Pelaaja voi klikata ruutuja paljastaakseen ne.
- [x] Ruutuun ilmestyy luku, joka kertoo kuinka monta miinaa ruudun ympärillä on.
- [x] Peli päättyy, jos pelaaja paljastaa miinan.
- [x] Peli päättyy, jos pelaaja paljastaa kaikki ruudut, jotka eivät sisällä miinaa.

## Jatkokehitysideoita

- [ ] Muokattavat vaikeustasot
  - Käyttäjä voi valita ruudukon koon ja miinojen määrän
- [ ] Mahdollisuus asettaa aikarajoitusta
- [x] Left + Right -klikkaus
  - Jos pelaaja on jo paljastanut ruudun ja sen ympäriltä löytyy oikea määrä liputettuja miinoja, pelaaja voi klikata ruutua samanaikaisesti vasemmalla ja oikealla hiirenpainikkeella
  - Tämä avaa kaikki muut ympäröivät ruudut automaattisesti, jos ne eivät sisällä miinaa.
  - Jos liputus oli virheellinen, miina voi paljastua ja peli päättyy.

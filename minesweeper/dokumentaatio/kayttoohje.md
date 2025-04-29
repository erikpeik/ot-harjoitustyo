# Käyttöohje

## Asennus

Siirrytään alikansioon:

```bash
ot-harjoitustyo/minesweeper
```

Asennetaan riippuvuudet komennolla:

```bash
poetry install
```

Jonka jälkeen suorita alustustoimeenpiteet kommolla:

```bash
poetry run invoke build
```

Nyt ohjelma on valmis ajettavaksi seuraavalla komennolla:

```bash
poetry run invoke start
```

## Valikkonäkymä

Sovellus kännistyy valikkonäkymästä, jossa käyttäjä voi valita pelin vaikeustason. Valittavissa on kolme vaihtoehtoa:

- Helppo (9x9, 10 miinaa)
- Keskivaikea (16x16, 40 miinaa)
- Vaikea (30x16, 99 miinaa)

![Aloitusnäkymä](./kuvat/aloitusnakyma.png)

## Pelinäkymä

Pelinäkymässä pelaaja voi pelata peliä. Pelissä on käytössä seuraavat toiminnot:

- Klikkaamalla ruutua, paljastaa sen. Jos ruudussa on miina, peli päättyy.
- Hymiö-nappi, jonka klikkaamalla voi aloittaa pelin alusta.

Vasemalla yläreunassa näkyy jäljellä olevien miinojen määrä ja oikealla puolella aika, joka on kulunut pelissä.

![Pelinäkymä](./kuvat/pelinakyma.png)

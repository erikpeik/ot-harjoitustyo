# Ohjelmistotekniikka, harjoitustyö

Tämän sovelluksen avulla voit pelata **miinaharavaa**. Sovellus tallentaa tuloksesi leaderboardiin, josta voit tarkastella parhaita tuloksia.

## Dokumentaatio

- [Käyttöohje](./minesweeper/dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./minesweeper/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./minesweeper/dokumentaatio/tuntikirjanpito.md)

## Asennus

1. Siirry alikansioon `/minesweeper`.
2. Lataa riippuvuudet komennolla `poetry install`.
3. Käynnistä sovellus komennolla `poetry run invoke start`.

## Komentorivitoiminnot

Komennot suoritetaan alikansiossa `/minesweeper`.

### Pelin käynnistäminen

```bash
poetry run invoke start
```

### Pylint-tarkistus

```bash
poetry run invoke lint
```

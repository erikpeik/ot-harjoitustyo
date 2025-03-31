# Ohjelmistotekniikka, harjoitustyö

Tämän sovelluksen avulla voit pelata **miinaharavaa**. Sovellus on toteutettu Pythonilla ja sen käyttöliittymä on tehty Pygame-kirjastolla.

## Dokumentaatio

- [Käyttöohje](./minesweeper/dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./minesweeper/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./minesweeper/dokumentaatio/tuntikirjanpito.md)
- [Changelog](./minesweeper/dokumentaatio/changelog.md)

## Asennus

1. Siirry alikansioon `/minesweeper`
2. Lataa riippuvuudet komennolla `poetry install`
3. Käynnistä sovellus komennolla `poetry run invoke start`

## Komentorivitoiminnot

Komennot suoritetaan alikansiossa `/minesweeper`

### Pelin käynnistäminen

```bash
poetry run invoke start
```
### Testaus

```bash
poetry run invoke test
```
### Testikattavuuden tarkistus

```bash
poetry run invoke coverage-report
```
Raportti generoituu *htmlcov*-kansioon.


### Pylint-tarkistus

```bash
poetry run invoke lint
```

## Credits

Projektissa käytetyt kuvat ovat tehneet [Black Squirrel](https://www.spriters-resource.com/submitter/Black+Squirrel/), TCRF, Inky ja DaSpriter121. Sheets on ladattu [The Spriters Resource](https://www.spriters-resource.com/pc_computer/minesweeper/sheet/19849/) -sivustolta.

# Arkkitehtuurikuvaus

## Rakenne

Koodin pakkausrakenne on seuraava:

![Pakkauskaavio](./kuvat/pakkauskaavio.svg)

Pakaus *ui* sisältää käyttöliittymän, *logic* joka sisältää pelilogiikan.
services-pakkaus sisältää pelin tallennukseen liittyvän logiikan ja *repositories* tietojen pysyväistallennukseen vastaavan koodin.
*entities*-pakkaus sisältää tyypit, joita käytetään pelin sisällä.

## Käyttöliittymä

Käyttöliittymä sisältää kolme näkymää:

- Valikkonäkymä, jossa valitaan vaikeustaso
- Pelinäkymä, jossa pelataan peliä
- Tilastot-näkymä, jossa näytetään pelin tilastot

Jokainen näistä toteutettu omana, erillisenä luokkana ja käyttöliittymä on totetettu Pygame-kirjastolla. Käyttöliittymä on yritetty eristää pelilogiikasta.

## Sovelluslogiikka

Yksinkertaistettu luokkakaavio pelilogiikasta on esitetty alla. Pelilogiikka on toteutettu luokassa `Minesweeper`, joka käyttää `Board`-luokkaa pelilaudan hallintaan ja `Piece`-luokkaa yksittäisten ruutujen hallintaan.

```mermaid
classDiagram
    class Minesweeper {
        +reset_game()
    }
    class Board {
        +tuple size
        +int mine_count


        +empty_board()
        +place_bombs()
        +is_clicked_position()
        +calculate_adjacent_bombs()
        +reveal_empty_tiles()
        +chord_piece()
        +reset_board()
        +mines_left()
        +check_win()
        +get_time()
    }

    class Piece {
        +bool is_bomb
        +bool clicked
        +bool flagged
        +tuple location

        +reveal()
        +flag_piece()
    }

    Minesweeper "1" --> "1" Board
    Board "1" --> "*" Piece
```

## Tietojen pysyväistallennus

Pakkauksen *repositories* sisältää luokan `ResultRepository` joka vastaa pelin tilastojen tallentamisesta ja lataamisesta. Se käyttää SQLite-tietokantaa tietojen pysyväistallennukseen.

## Päätoiminnallisuudet

Kuvataan seuraavaksi muutama päätoiminnallisuus sekvenssikaaviona.

### Käyttäjä klikkaa ruutua pelilaudalla

```mermaid
sequenceDiagram
    actor User


    User->>UI: Clicks on tile
    UI->>GameView: handle_click(pos, action)
    GameView->>Tile: handle_click(pos, top_left, piece, action)
    Tile->>Piece: reveal()
    Piece-->UI:  clicked = True
    UI->>GameView: draw()

```

### Käyttäjä paljastaa viimeisen tyhjän ruudun, jolloin peli päättyy voittoon

```mermaid
sequenceDiagram
    actor User
    participant UI
    participant GameView
    participant Board
    participant Tile
    participant Piece
    User->>UI: Clicks on tile
    UI->>GameView: handle_click(pos, action)
    GameView->>Tile: handle_click(pos, top_left, piece, action)
    Tile->>Piece: reveal()
    Piece-->UI:  clicked = True

    GameView->>Board: check_win()
    Board->>ResultRepository: save_result()
    Board->>GameView: True
    UI->>GameView: draw()

```

## Github Actions

Projektissa käytetään *GitHub Actions* -automaatiota koodin laadun varmistamiseen. [`format.yml`](https://github.com/erikpeik/ot-harjoitustyo/blob/main/.github/workflows/format.yml) suorittaa automaattisesti *autopep8*-tarkistuksen. [`pylint.yml`](https://github.com/erikpeik/ot-harjoitustyo/blob/main/.github/workflows/pylint.yml) ajaa Pylint-analyysin koodin laadun ja virheiden tunnistamiseksi.

Työnkulut on määritelty `.github/workflows`-kansiossa. Työnkulut suoritetaan automaattisesti jokaisen commitin yhteydessä ja ne voidaan tarkistaa GitHubin käyttöliittymässä [Actions-välilehdeltä](https://github.com/erikpeik/ot-harjoitustyo/actions)

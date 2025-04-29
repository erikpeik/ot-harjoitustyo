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

## Luokkakaavio

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


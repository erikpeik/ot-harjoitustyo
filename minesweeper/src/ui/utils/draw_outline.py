import pygame as pg


def draw_outline(
        top_left,
        bottom_right,
        screen,
        reverse=False,
        width=5,
        *,
        dark_gray_color=(128, 128, 128),
        white_color=(255, 255, 255)):
    top_left = (top_left[0] + 2, top_left[1] + 2)
    bottom_right = (bottom_right[0] - 2, bottom_right[1] - 2)
    bottom_left = (top_left[0], bottom_right[1])
    top_right = (bottom_right[0], top_left[1])

    pg.draw.line(
        screen,
        white_color if not reverse else dark_gray_color,
        top_left,
        top_right,
        width,
    )
    pg.draw.line(
        screen,
        dark_gray_color if not reverse else white_color,
        top_right,
        bottom_right,
        width,
    )
    pg.draw.line(
        screen,
        dark_gray_color if not reverse else white_color,
        bottom_right,
        bottom_left,
        width,
    )
    pg.draw.line(
        screen,
        white_color if not reverse else dark_gray_color,
        bottom_left,
        top_left,
        width,
    )

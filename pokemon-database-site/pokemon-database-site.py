"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...

def search():
    return rx.hstack(
        rx.link(
            rx.icon(tag="search", color="white", size=30),
            href="https://cow.com"
        ),
        rx.input(
            placeholder="Search",
            color="white",
            font_size="3.5vh",
            width="100%",
            background_color="rgba(255, 255, 255, 0)",
            border="none",
            border_width="0px",
            height="30",
        ),
        
        bg="rgba(0, 0, 0, 0.29)",
        border_radius="1087vh",
        padding="0.5vh",
        width="80vw",
        position="absolute",
        left="10vw",
        top="2vh",
    ),


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        search(),
        rx.hstack(
            rx.text(
                "Pokemon Database",
                font_weight="bold",
                font_size="10.5vh",
                text_wrap="nowrap",
            
            ),
            rx.image(
                src="https://cloud-531arvufv-hack-club-bot.vercel.app/0image.png",
                width = "6vw",
                height="13vh"
            ),
            position="relative",
            left="10vw",
            top="10vh",
            width="47vw",
            height="14vh"
        ),
        height="100vh",
        padding_left = "10vw",
        padding_right = "10vw",
        bg = "#141218",
        spacing="0"
    )


app = rx.App()
app.add_page(index)
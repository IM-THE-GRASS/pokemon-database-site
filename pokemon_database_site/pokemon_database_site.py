"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import os
import reflex as rx
import json
from rxconfig import config
import pokebase

class State(rx.State):
    
    def get_pokemon_data():
        f = open(os.path.join("pokemon_database_site", "pokemon.json"))
        data = json.loads(f.read())
        return data
    pokemon:list[dict[str, str]] = get_pokemon_data()
    
def pokemon_card(info, index):
    return rx.box(
        rx.vstack(
            rx.image(
                src=info["img"],
                height="31.5vh",
                width="100%",
                object_fit = "cover",
                image_rendering="pixelated"
            ),
            rx.vstack(
                rx.text(
                    info["name"],
                    font_size="30px",
                    line_height="30px",
                    letter_spacing="-1px",
                    font_weight="bold"
                ),
                rx.text(
                    info["desc"],
                    font_size="14px",
                    letter_spacing="0.25px",
                    line_height="20px",
                    text_color="E7E0EC"
                )
            )
        ),
        height="65vh",
        bg = "#0F0D13",
        padding="0.8vw",
        border_radius = "12px",
        border_width="1px",
        border_color="rgba(255, 255, 255, 0.2)"
    )
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
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
            width="47vw",
            height="14vh"
        ),
        rx.grid(
            rx.foreach(
                State.pokemon,
                pokemon_card  
            ),
            columns="4",
            spacing="4",
            width="100%",
            
            
        ),
        padding_left = "10vw",
        padding_right = "10vw",
        padding_top = "10vh",
        bg = "#141218",
        spacing="3"
    )

style = {
    
    "html": {
        "background-color": "#141218"
    },
    "body":{
        "background-color":"#141218",
    },
    "img": { 
        "image-rendering": "optimizeSpeed"            ,
        "image-rendering": "-moz-crisp-edges"          ,
        "image-rendering": "-o-crisp-edges"            ,
        "image-rendering": "-webkit-optimize-contrast ",
        "image-rendering": "pixelated "                ,
        "image-rendering": "optimize-contrast"        ,
        "-ms-interpolation-mode": "nearest-neighbor" 

    }
}
app = rx.App(style=style)
app.add_page(index)
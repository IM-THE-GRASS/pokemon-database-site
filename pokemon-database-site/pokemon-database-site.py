"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    pass

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

def pokemon_card():
    return rx.box(
        rx.vstack(
            rx.image(
                src="https://cloud-94weoqu9j-hack-club-bot.vercel.app/11.png",
                height="31.5vh",
                width="100%",
                object_fit = "cover",
                image_rendering="pixelated"
            ),
            rx.vstack(
                rx.text(
                    "Bulbasour",
                    font_size="36px",
                    line_height="24px",
                    letter_spacing="-1px",
                    font_weight="bold"
                ),
                rx.hstack(
                    rx.image(
                        src="https://cloud-94weoqu9j-hack-club-bot.vercel.app/012.png"
                    ),
                    rx.image(
                        src="https://cloud-94weoqu9j-hack-club-bot.vercel.app/012.png"
                    ),
                    max_height="2.1vh"
                ),
                rx.text(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor",
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
            width="47vw",
            height="14vh"
        ),
        rx.grid(
            rx.foreach(
                rx.Var.range(12),
                lambda i:pokemon_card()  
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
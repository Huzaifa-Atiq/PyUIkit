from pyhtmlkit import Body, Div
from pyhtmlkit.components import Input, Button, Text

def show_input():
    single_val = Input.get_input("singleInput")
    multi_val = Input.get_input("multiInput")
    Text.set_text("displayText", f"Single: {single_val}\nMulti: {multi_val}")

app = Body(title="Input Test", width=600, height=500, bg_color="#f5f5f5")

# Top-level Div
Div(
    x=50,
    y=50,
    width=500,
    height=400,
    bg_color="#e0e0e0",
    padding=10,
    children=[
        Text(text="Enter something below:", font_size=16, id="displayText"),
        # Single-line Input
        Input(
            id="singleInput",
            x=50,
            y=50,
            width=300,
            height=40,
            placeholder="Type here...",
            multiline=False,
            bg_color="#ffffff",
            text_color="#ff0000",
        ),
        # Multi-line Input
        Input(
            id="multiInput",
            x=50,
            y=120,
            width=400,
            height=100,
            placeholder="Multi-line text...",
            multiline=True,
            bg_color="red",
            text_color="#008000",
        ),
        # Button to fetch values
        Button(
            text="Show Input",
            x=50,
            y=240,
            width=150,
            height=40,
            color="#007acc",
            text_color="#ffffff",
            on_click=show_input
        )
    ],
    id="mainDiv"
)

app.run()

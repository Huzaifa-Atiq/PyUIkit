from pyuikit import Body, Div
from pyuikit.components import Button, Switch, Toast

app = Body(title="Complex Component Test", width=700, height=600)

# ----------------- Toast Functions -----------------
def toast_top_right():
    Toast(text="Top Right Toast!", bg_color="#4caf50", duration=3).show()

def toast_bottom_left():
    Toast(text="Bottom Left Toast!", bg_color="#f44336", duration=3, position="bottom-left").show()

def toast_custom_xy():
    Toast(text="Custom XY Toast", bg_color="#2196f3", x=250, y=250, duration=4, show_close=True, width=250).show()

# ----------------- Nested Divs -----------------
Div(
    width=650,
    height=550,
    bg_color="#222222",
    children=[
        # Horizontal top row
        Div(
            width=600,
            height=100,
            bg_color="#333333",
            horizontal=True,
            nested=True,
            children=[
                Button(text="Show Top Right Toast", on_click=toast_top_right, color="#4caf50"),
                Button(text="Show Bottom Left Toast", on_click=toast_bottom_left, color="#f44336"),
                Button(text="Show Custom XY Toast", on_click=toast_custom_xy, color="#2196f3"),
            ]
        ),

        # Vertical middle column with switches (auto-stacking)
        Div(
            width=600,
            height=150,
            bg_color="#444444",
            nested=True,
            children=[
                Switch(text="Enable Feature A", default=True, bg_color="#555555", progress_color="#00ff00"),
                Switch(text="Enable Feature B", default=False, bg_color="#555555", progress_color="#ff0000"),
                Switch(text="Enable Feature C", default=True, bg_color="#555555", progress_color="#0000ff"),
            ]
        ),

        # Mixed row with horizontal auto-stacking buttons
        Div(
            width=600,
            height=120,
            bg_color="#333333",
            horizontal=True,
            nested=True,
            children=[
                Button(text="Button 1", color="#ff9800"),
                Button(text="Button 2", color="#9c27b0"),
                Button(text="Button 3", color="#03a9f4"),
            ]
        ),

        # Nested vertical inside horizontal div
        Div(
            width=600,
            height=150,
            bg_color="#555555",
            horizontal=True,
            nested=True,
            children=[
                Div(
                    width=200,
                    height=150,
                    bg_color="#777777",
                    nested=True,
                    children=[
                        Button(text="Nested Btn 1", color="#ffb74d"),
                        Switch(text="Nested Switch 1")
                    ]
                ),
                Div(
                    width=200,
                    height=150,
                    bg_color="#888888",
                    nested=True,
                    children=[
                        Button(text="Nested Btn 2", color="#ba68c8"),
                        Switch(text="Nested Switch 2")
                    ]
                ),
                Div(
                    width=200,
                    height=150,
                    bg_color="#999999",
                    nested=True,
                    children=[
                        Button(text="Nested Btn 3", color="#4fc3f7"),
                        Switch(text="Nested Switch 3")
                    ]
                ),
            ]
        )
    ]
)

app.run()

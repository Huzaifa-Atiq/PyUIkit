from pyuikit import Body, Div
from pyuikit.components import Button
from pyuikit.components.toast import Toast

app = Body(title="Toast Demo", width=600, height=400)


# ---------------------------
# 1. Simple top-right toast
# ---------------------------
def toast_top_right():
    Toast(
        text="Top Right Toast!",
        fg_color="#444",
        text_color="white",
        duration=3,
        position="top-right",
        show_close=True
    ).render(app.root)


# ---------------------------
# 2. Bottom-left warning toast
# ---------------------------
def toast_bottom_left():
    Toast(
        text="Bottom Left Warning",
        fg_color="#cc8800",
        text_color="black",
        duration=5,
        position="bottom-left",
        show_close=False,       # no close button
        width=260,
        height=55,
        font_name="Arial",
        font_size=15,
    ).render(app.root)


# ---------------------------
# 3. Custom position toast with manual x,y
# ---------------------------
def toast_custom_xy():
    Toast(
        text="Custom Positioned Toast",
        fg_color="#0066aa",
        text_color="white",
        duration=4,
        x=150,
        y=120,                 # custom exact position
        show_close=True,
        width=240,
        height=50,
    ).render(app.root)


# ----------------------------
# Layout UI
# ----------------------------
Div(
    width=600,
    height=400,
    children=[
        Button(text="Show Top-Right Toast", on_click=toast_top_right),
        Button(text="Show Bottom-Left Toast", on_click=toast_bottom_left),
        Button(text="Show Custom XY Toast", on_click=toast_custom_xy),
    ]
)

app.run()

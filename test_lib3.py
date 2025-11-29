from pyuikit import Body, Div
from pyuikit.components import Text, Button

# ---------- App Setup ----------
app = Body(title="Calculator", width=330, height=400, bg_color="#1a1a1a")

# ---------- Global State ----------
current_expression = ""

# ---------- Functions ----------
def press(value):
    global current_expression
    current_expression += str(value)
    Text.set_text("display", current_expression)

def clear():
    global current_expression
    current_expression = ""
    Text.set_text("display", current_expression)

def calculate():
    global current_expression
    try:
        result = str(eval(current_expression))
        current_expression = result
    except Exception:
        current_expression = "Error"
    Text.set_text("display", current_expression)

# ---------- Layout ----------
Div(
    x=20,
    y=20,
    width=290,
    height=350,
    bg_color="#222222",
    children=[
        # Display
        Text(text="", x=10, y=10, font_size=24, color="#00ff88", id="display"),

        # Buttons
        Button(text="7", x=10, y=60, width=60, height=50, color="#00ff88", text_color="#000000", on_click=lambda: press(7)),
        Button(text="8", x=80, y=60, width=60, height=50, color="#00ff88", text_color="#000000", on_click=lambda: press(8)),
        Button(text="9", x=150, y=60, width=60, height=50, color="#00ff88", text_color="#000000", on_click=lambda: press(9)),
        Button(text="/", x=220, y=60, width=60, height=50, color="#ff5555", text_color="#ffffff", on_click=lambda: press("/")),

        Button(text="4", x=10, y=120, width=60, height=50, color="#00ff88", text_color="#000000", on_click=lambda: press(4)),
        Button(text="5", x=80, y=120, width=60, height=50, color="#00ff88", text_color="#000000", on_click=lambda: press(5)),
        Button(text="6", x=150, y=120, width=60, height=50, color="#00ff88", text_color="#000000", on_click=lambda: press(6)),
        Button(text="*", x=220, y=120, width=60, height=50, color="#ff5555", text_color="#ffffff", on_click=lambda: press("*")),

        Button(text="1", x=10, y=180, width=60, height=50, color="#00ff88", text_color="#000000", on_click=lambda: press(1)),
        Button(text="2", x=80, y=180, width=60, height=50, color="#00ff88", text_color="#000000", on_click=lambda: press(2)),
        Button(text="3", x=150, y=180, width=60, height=50, color="#00ff88", text_color="#000000", on_click=lambda: press(3)),
        Button(text="-", x=220, y=180, width=60, height=50, color="#ff5555", text_color="#ffffff", on_click=lambda: press("-")),

        Button(text="0", x=10, y=240, width=60, height=50, color="#00ff88", text_color="#000000", on_click=lambda: press(0)),
        Button(text="C", x=80, y=240, width=60, height=50, color="#ff5555", text_color="#ffffff", on_click=clear),
        Button(text="=", x=150, y=240, width=60, height=50, color="#10b981", text_color="#ffffff", on_click=calculate),
        Button(text="+", x=220, y=240, width=60, height=50, color="#ff5555", text_color="#ffffff", on_click=lambda: press("+")),
    ]
)

# ---------- Run App ----------
app.run()

from pyuikit import Body, Div
from pyuikit.components import Text, Input, Button, Dropdown

# ---------- Callback Function ----------
def convert_unit():
    try:
        value = float(Input.get_input("inputValue"))
        from_unit = Dropdown.get_value("fromUnit")
        to_unit = Dropdown.get_value("toUnit")
        
        # Conversion factors relative to meters
        factors = {
            "Meters": 1,
            "Kilometers": 1000,
            "Miles": 1609.34,
            "Feet": 0.3048
        }
        
        result = value * factors[from_unit] / factors[to_unit]
        Text.set_text("resultText", f"{value} {from_unit} = {result:.4f} {to_unit}")
    except ValueError:
        Text.set_text("resultText", "❌ Enter a valid number!")

# ---------- Create App ----------
app = Body(title="Unit Converter", width=500, height=300, bg_color="#1f2937")

# ---------- Main Div ----------
Div(
    x=50,
    y=50,
    width=400,
    height=200,
    bg_color="#111827",
    padding=15,
    children=[
        Text(text="Unit Converter", x=20, y=0, font_size=20, color="#f9fafb"),
        
        Input(id="inputValue", x=20, y=40, width=180, placeholder="Enter value", bg_color="#1f2937", text_color="#ffffff"),
        
        Dropdown(options=["Meters", "Kilometers", "Miles", "Feet"], id="fromUnit", x=220, y=40),
        Dropdown(options=["Meters", "Kilometers", "Miles", "Feet"], id="toUnit", x=220, y=80),
        
        Button(text="Convert", x=20, y=80, width=180, height=35, color="#3b82f6", text_color="#ffffff", on_click=convert_unit),
        
        Text(text="", x=20, y=130, font_size=16, color="#f9fafb", id="resultText")
    ]
)

app.run()

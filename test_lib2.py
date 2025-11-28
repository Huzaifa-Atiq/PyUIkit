from pyuikit import Body, Div
from pyuikit.components import RadioButton, Text, Button

# Create the main window
app = Body(title="RadioButton Test", width=600, height=400)

# Callback function to show selected option
def show_selected():
    selected = RadioButton.get_value(id="radio1")
    Text.set_text(id="resultText", new_text=f"Selected: {selected}")

# Callback functions for radio buttons
def radio1_changed(new_val):
    print(f"Radio1 changed to: {new_val}")

# Top-level Div
Div(
    x=50,
    y=50,
    width=500,
    height=300,
    bg_color="#f0f0f0",
    id="mainDiv",
    children=[
        Text(text="Choose your favorite fruit:", x=20, y=20, font_size=16),
        RadioButton(
            options=["Apple", "Banana", "Cherry"],
            x=20,
            y=60,
            id="radio1",
            default="Banana",
            on_change=radio1_changed,
            text_color='black'
        ),
        Button(text="Show Selected", x=20, y=145, on_click=show_selected),
        Text(text="Waiting for selection...", x=20, y=200, id="resultText", font_size=14, color="#007acc")
    ]
    
)

app.run()

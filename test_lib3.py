
from pyuikit import Body, Div
from pyuikit.components import Dropdown, Text, Button



# Callback for dropdown change
def on_dropdown_change(value):
    Text.set_text("dropdownStatus", f"Selected: {value}")

# Create main window
app = Body(title="Dropdown Test", width=600, height=400)

# Parent Div
Div(
    x=50, y=50, width=500, height=300, bg_color="#f0f0f0",
    children=[
        # Dropdown without x/y to trigger warning
        Dropdown(
            options=["Red", "Green", "Blue"],
            id="colorDropdown",
            default="Green",
            on_change=on_dropdown_change
        ),

        # Button to dynamically change selected value
        Button(
            text="Set Blue",
            x=50, y=100,
            on_click=lambda: Dropdown.set_value("colorDropdown", "Blue")
        ),

        # Button to change options dynamically
        Button(
            text="Add Options",
            x=150, y=100,
            on_click=lambda: Dropdown.set_options("colorDropdown", ["Cyan", "Magenta", "Yellow"])
        ),

        # Text to show selected value
        Text(text="Selected:", x=50, y=150, id="dropdownStatus")
    ],
    id="testDiv"
)

app.run()

from pyuikit import Body, Div, Switch
from pyuikit.components import Button

# Create the main app window
app = Body(width=500, height=400)

# Callback function for the button
def toggle_switch():
    # Get current state
    current_state = Switch.get_state("customSwitch")
    # Toggle the state
    Switch.set_state("customSwitch", not current_state)

Div(
    x=50, y=50,
    width=400, height=300,
    bg_color='grey',
    children=[
        # The Switch
        Switch(
            x=20,
            y=20,
            id="customSwitch",
            text="Custom Switch",
            default=True,
            fg_color="#333333",
            progress_color="#4caf50",
            button_color="#ffffff",
            button_hover_color="#888888",
            text_color="#ffffff",
            font_name="Courier New",
            font_size=16,
            on_change=lambda state: print("Current state:", state)
        ),
        # The Button to toggle the Switch
        Button(
            x=20,
            y=80,
            text="Toggle Switch",
            width=150,
            height=40,
            color="#10b981",
            text_color="#ffffff",
            on_click=toggle_switch
        )
    ]
)

app.run()

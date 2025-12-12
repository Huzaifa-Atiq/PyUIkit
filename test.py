from pyuikit import *

# Create main app window
app = Body(width=500, height=800)

# Create a div container
Div(
    children=[
        Switch(               # Y position
            id="switch1",        # ID for dynamic access
            width=80,            # Width of the switch
            height=40,           # Height of the switch
            text="Enable Feature", # Label text
            default=True,        # Initial state (ON)
            on_change=lambda: print("Switch toggled! Current state:", Switch.get_state("switch1")),
            fg_color="#2b2b2b",       # Background of the switch
            progress_color="#3b82f6", # Color of the "on" slider
            button_color="#ff0000",    # Color of the toggle knob
            button_hover_color="#ff0000"
        )
    ]
)

# Run the app
app.run()

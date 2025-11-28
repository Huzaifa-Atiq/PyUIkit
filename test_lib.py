from pyuikit import Body, Div
from pyuikit.components import Text, Checkbox, Button

# Create main window
app = Body(title="Checkbox Test", width=600, height=400, bg_color="#1a1a1a")

# Callback to read checkbox state
def check_status():
    status1 = Checkbox.is_checked("cb1")
    status2 = Checkbox.is_checked("cb2")
    Text.set_text("statusText", f"Checkbox 1: {status1}, Checkbox 2: {status2}")

# Callback to toggle checkbox 1
def toggle_cb1():
    current = Checkbox.is_checked("cb1")
    Checkbox.set_checked("cb1", not current)
    Text.set_text("statusText", f"Toggled Checkbox 1 to {not current}")

# Absolute layout Div
Div(
    x=50,
    y=50,
    width=500,
    height=300,
    bg_color="#0d0d0d",
    children=[
        Text(text="Test Checkboxes:", x=20, y=20, font_size=20, color="#00ff88"),

        Checkbox(text="Option 1", x=20, y=60, id="cb1", default=False, text_color="#00ff88", color="#1a1a1a"),
        Checkbox(text="Option 2", x=20, y=100, id="cb2", default=True, text_color="#00ff88", color="#1a1a1a"),

        Button(text="Check Status", x=20, y=150, width=180, height=35, color="#00ff88", text_color="#000000", on_click=check_status),
        Button(text="Toggle Checkbox 1", x=220, y=150, width=180, height=35, color="#00ff88", text_color="#000000", on_click=toggle_cb1),

        Text(text="Waiting...", x=20, y=200, font_size=16, color="#00ff88", id="statusText")
    ]
)

# Run the app
app.run()

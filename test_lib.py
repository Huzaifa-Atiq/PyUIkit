# file: packed_layout.py
from pyhtmlkit import Body, Div
from pyhtmlkit.components import Text, Button, Input

def on_button_click():
    text_value = Input.get_input("inputField")
    Text.set_text("statusText", f"You entered: {text_value}")

# Create main window
app = Body(title="Packed Layout Example", width=500, height=400, bg_color="#f5f5f5")

# Main Div with padding
Div(
    padding=20,
    bg_color="#eaeaea",
    height=200,
    width=200,
    children=[
        Text(text="Enter something:", id="labelText", font_size=16, padx=5, pady=5),
        Input(id="inputField", placeholder="Type here...", padx=5, pady=5,bg_color='grey',text_color='white'),
        Button(text="Submit", on_click=on_button_click, padx=5, pady=5),
        Text(text="", id="statusText", font_size=14, color="#333", padx=5, pady=5)
    ],
    id="mainDiv"
)

app.run()

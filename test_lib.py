from pyhtmlkit import Body, Div
from pyhtmlkit.components import FileDialog, Button, Text

# Callback to get the save path
def save_file():
    path = FileDialog.get_file("mySaveFile")
    print("Save path:", path)
    Text.set_text("statusText", f"Save path: {path}")

# App layout
app = Body(title="FileDialog Save Demo", width=500, height=300, bg_color="#1f2937")

Div(
    width=450,
    height=250,
    bg_color="#111827",
    padding=20,
    children=[
        Text(text="Save File Demo", font_size=18, color="#f9fafb", font="Arial Bold"),
        
        FileDialog(
            id="mySaveFile",
            width=350,
            height=50,
            placeholder="Choose where to save...",
            dialog_type="save",          # <-- Use save dialog
            padx=0,
            pady=20,
            frame_bg="#2b2b2b",
            entry_bg="#1f2937",
            entry_text_color="#f9fafb",
            button_color="#3b82f6",
            button_text_color="#ffffff"
        ),
        
        Button(
            text="Get Save Path",
            width=150,
            height=40,
            color="#10b981",
            text_color="#f9fafb",
            corner_radius=10,
            on_click=save_file,
            padx=0,
            pady=10
        ),
        
        Text(text="", id="statusText", font_size=14, color="#f87171")
    ]
)

app.run()

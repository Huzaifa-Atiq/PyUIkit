from pyuikit import Body, Div
from pyuikit.components import Text, ProgressBar, Button
import time
import threading
import random

# Create main window
app = Body(
    title="ProgressBar Advanced Test",
    width=600,
    height=450,
    bg_color="#1a1a1a"
)

# -----------------------------
# MAIN PROGRESS SIMULATION
# -----------------------------
def simulate_progress():
    for value in range(0, 101):
        ProgressBar.set_value(id="pb1", new_value=value)
        Text.set_text(id="statusText", new_text=f"Loading... {value}%")
        time.sleep(0.01)
    Text.set_text(id="statusText", new_text="✅ Finished!")

def start_progress():
    threading.Thread(target=simulate_progress).start()


# -----------------------------
# EXTRA TEST ACTIONS
# -----------------------------
def reset_progress():
    ProgressBar.set_value(id="pb1", new_value=0)
    Text.set_text(id="statusText", new_text="Progress reset to 0%")

def set_half():
    ProgressBar.set_value(id="pb1", new_value=50)
    Text.set_text(id="statusText", new_text="Set to 50%")

def add_ten():
    current = ProgressBar.get_value(id="pb1")
    new_val = min(current + 10, 100)
    ProgressBar.set_value(id="pb1", new_value=new_val)
    Text.set_text(id="statusText", new_text=f"Added +10 → {new_val}%")

def random_progress():
    val = random.randint(0, 100)
    ProgressBar.set_value(id="pb1", new_value=val)
    Text.set_text(id="statusText", new_text=f"Random value: {val}%")

def change_color():
    colors = ["#00ff88", "#ff0077", "#ffaa00", "#4488ff"]
    new_color = random.choice(colors)
    ProgressBar.set_colors(id="pb1", fg_color=new_color)
    Text.set_text(id="statusText", new_text=f"Changed color to {new_color}")

def ultra_smooth_progress():
    def run():
        for v in range(0, 101):
            ProgressBar.set_value(id="pb1", new_value=v)
            time.sleep(0.005)
    threading.Thread(target=run).start()


# -----------------------------
# MAIN UI
# -----------------------------
Div(
    x=50,
    y=50,
    width=525,
    height=350,
    bg_color="#0d0d0d",
    children=[
        Text(text="Advanced ProgressBar Test:", x=20, y=20, font_size=22, color="#00ff88"),

        ProgressBar(id="pb1", x=20, y=70, width=450, height=25, value=0, fg_color="#00ff88", bg_color="black"),

        Button(text="Start Simulation", x=20, y=120, width=200, height=35,
               color="#00ff88", text_color="#000000", on_click=start_progress),

        Button(text="Reset", x=240, y=120, width=100, height=35,
               color="#00ff88", text_color="#000000", on_click=reset_progress),

        Button(text="Set 50%", x=360, y=120, width=100, height=35,
               color="#00ff88", text_color="#000000", on_click=set_half),

        Button(text="Add +10%", x=20, y=170, width=150, height=35,
               color="#00ff88", text_color="#000000", on_click=add_ten),

        Button(text="Random Value", x=190, y=170, width=150, height=35,
               color="#00ff88", text_color="#000000", on_click=random_progress),

        Button(text="Change Color", x=360, y=170, width=150, height=35,
               color="#00ff88", text_color="#000000", on_click=change_color),

        Button(text="Ultra Smooth", x=20, y=220, width=200, height=35,
               color="#00ff88", text_color="#000000", on_click=ultra_smooth_progress),

        Text(text="Waiting...", x=20, y=280, font_size=16, color="#00ff88", id="statusText")
    ]
)

app.run()

## ProgressBar Component

`ProgressBar` in **PyUIkit** is a **visual indicator** to show progress for tasks like loading, uploading, or processing.  
It supports **dynamic updates**, custom colors, and works seamlessly with other UI components.

> ⚠️ **Note:** Before using this component, it is recommended to read the [Quickstart Guide](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Quickstart.md) if you haven't already to understand how to create windows, top-level Divs, and basic setup.

---

### 🔹 Features

- Display progress in **0–100%** range.
- Fully **customizable colors** for foreground (progress) and background.
- Can be updated **dynamically** using static methods.
- Optional `id` allows **dynamic access** after creation.
- Simple **absolute positioning** with `x` and `y`.

---

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `id`      | `str` | `None` | Unique identifier for dynamic access |
| `x`       | `int` | `None` | X-coordinate for placement |
| `y`       | `int` | `None` | Y-coordinate for placement |
| `width`   | `int` | `200`  | Width of the progress bar in pixels |
| `height`  | `int` | `20`   | Height of the progress bar in pixels |
| `value`   | `int` | `0`    | Initial value (0–100) |
| `fg_color`| `str` | `#3b82f6` | Foreground color (progress color) |
| `bg_color`| `str` | `#e5e7eb` | Background color |

---


### Basic Usage

```python
from pyuikit import Body, Div
from pyuikit.components import ProgressBar

app = Body(title="ProgressBar Demo", width=400, height=200)

Div(
    x=20,
    y=20,
    width=360,
    height=150,
    children=[
        ProgressBar(id="pb1", x=20, y=20, width=320, height=25, value=30)
    ]
)

app.run()
```

### Advanced Usage – Dynamic Update

```python
from pyuikit import Body, Div
from pyuikit.components import ProgressBar, Button, Text
import threading
import time

app = Body(title="ProgressBar Demo", width=500, height=300)

def simulate_progress():
    for val in range(0, 101, 5):
        ProgressBar.set_value(id="pb1", new_value=val)
        Text.set_text(id="statusText", new_text=f"Loading... {val}%")
        time.sleep(0.05)
    Text.set_text(id="statusText", new_text="✅ Finished!")

def start_progress():
    thread = threading.Thread(target=simulate_progress)
    thread.start()

Div(
    x=20,
    y=20,
    width=460,
    height=200,
    children=[
        ProgressBar(id="pb1", x=20, y=20, width=400, height=30, fg_color="#10b981", bg_color="#111827"),
        Button(text="Start Progress", x=20, y=70, width=150, height=35, color="#10b981", text_color="#000000", on_click=start_progress),
        Text(text="Waiting...", x=20, y=120, id="statusText", font_size=14, color="#10b981")
    ]
)

app.run()
```

### Static Methods

#### `ProgressBar.get_value(id)`  
Get the current progress value (0–100) of a ProgressBar by its `id`.

#### `ProgressBar.set_value(id, new_value)`  
Set the progress dynamically. `new_value` should be in 0–100 range.

#### `ProgressBar.set_colors(id, fg_color=None, bg_color=None)`  
Update foreground and/or background colors dynamically. Use `fg_color` for the progress color and `bg_color` for the bar background.

---

### Tips & Best Practices

- Always assign an id to a ProgressBar if you plan to update it dynamically.

- Use ProgressBar.set_value(id, new_value) instead of directly manipulating the widget.

- You can combine with Text or Labels to show the percentage or status.
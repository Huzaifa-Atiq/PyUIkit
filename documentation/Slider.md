# Slider Component 

The `Slider` component provides a **horizontal slider** for selecting numeric values in a specified range.  
It’s perfect for **volume controls, brightness settings, or any numeric input** where a user can drag a handle to select a value.

You can **set min/max values, default value, colors**, and provide an **on_change callback** for dynamic updates.

> ⚠️ **Note:** Before using this component, it is recommended to read the [Quickstart Guide](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Quickstart.md) if you haven't already to understand how to create windows, top-level Divs, and basic setup.

---

## Features

- Select a numeric value in a specified range (`min_value` → `max_value`).  
- Fully **customizable colors** for background, progress, and slider button.  
- Supports **dynamic get/set value** via `id`.  
- Optional **on_change callback** to react when value changes.  
- Simple **absolute positioning** with `x` and `y`.  
- Works seamlessly with other PyUIkit components.  

---

## Parameters

| Parameter         | Type       | Default      | Description |
|------------------|-----------|-------------|-------------|
| `x`              | int       | None        | X-coordinate for absolute positioning |
| `y`              | int       | None        | Y-coordinate for absolute positioning |
| `id`             | str       | None        | Unique identifier for dynamic access |
| `width`          | int       | 200         | Width of the slider in pixels |
| `height`         | int       | 20          | Height of the slider in pixels |
| `min_value`      | int/float | 0           | Minimum numeric value |
| `max_value`      | int/float | 100         | Maximum numeric value |
| `default`        | int/float | `min_value` | Default value of the slider |
| `on_change`      | function  | None        | Callback function triggered when the slider value changes |
| `fg_color`       | str       | `#2b2b2b`   | Background color of the slider track |
| `progress_color` | str       | `#3b82f6`   | Foreground color representing the filled portion |
| `button_color`   | str       | `#ffffff`   | Color of the slider handle/button |

---

## Static Methods

### `Slider.get_value(id)`  
Returns the current value of the slider.

### `Slider.set_value(id, value)`  
Sets the slider to a new value programmatically.

---

## Basic Usage

```python
from pyuikit import Body, Div
from pyuikit.components import Slider, Text

def show_value(val):
    Text.set_text("sliderStatus", f"Value: {val:.0f}")

app = Body(title="Slider Demo", width=400, height=200)

Div(
    x=20,
    y=20,
    width=360,
    height=150,
    children=[
        Slider(
            id="volumeSlider",
            x=20,
            y=20,
            min_value=0,
            max_value=100,
            default=50,
            on_change=show_value,
            fg_color="#222222",
            progress_color="#10b981",
            button_color="#f9fafb"
        ),
        Text(
            text="Value: 50",
            id="sliderStatus",
            x=20,
            y=60,
            color="#10b981",
            font_size=14
        )
    ]
)

app.run()
```

## Advanced Usage — Dynamic Updates
```python
from pyuikit import Body, Div
from pyuikit.components import Slider, Text, Button

def show_value(val):
    Text.set_text("status", f"Slider: {val:.0f}")

def set_to_75():
    Slider.set_value("mySlider", 75)
    Text.set_text("status", "Slider set to 75")

def read_value():
    val = Slider.get_value("mySlider")
    Text.set_text("status", f"Current Value: {val:.0f}")

app = Body(title="Slider Advanced", width=400, height=250)

Div(
    x=20,
    y=20,
    width=360,
    height=200,
    bg_color='black',
    children=[
        Slider(
            id="mySlider",
            x=20,
            y=20,
            min_value=0,
            max_value=100,
            default=30,
            on_change=show_value,
            fg_color="#222222",
            progress_color="#3b82f6",
            button_color="#ffffff"
        ),
        Button(
            text="Set to 75",
            x=20,
            y=60,
            width=120,
            height=30,
            color="#10b981",
            text_color="#000000",
            on_click=set_to_75
        ),
        Button(
            text="Read Value",
            x=160,
            y=60,
            width=120,
            height=30,
            color="#3b82f6",
            text_color="#ffffff",
            on_click=read_value
        ),
        Text(
            text="Slider: 30",
            id="status",
            x=20,
            y=110,
            color="#f9fafb",
            font_size=14
        )
    ]
)

app.run()
```

# Dropdown Component

`Dropdown` is a **select menu component** in PyUIkit that lets users choose an option from a list.  
It supports **custom colors, dynamic value updates, option updates, and on-change callbacks**.

> ⚠️ **Note:** Before using this component, it is recommended to read the [Quickstart Guide](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Quickstart.md) if you haven't already to understand how to create windows, top-level Divs, and basic setup.

---

## Features
- Choose from a list of options.
- Fully customizable colors (text, background, hover).
- Supports dynamic **get/set value** and **changing options** via `id`.
- Optional **on_change callback** when the selection changes.
- Auto-placement warning if no `x, y` are provided.

---

### Parameters

| Parameter        | Type        | Default       | Description |
|-----------------|-------------|---------------|-------------|
| `options`       | `list`      | **Required**  | List of strings to display in the dropdown |
| `x`             | `int`       | `None`        | X-coordinate for absolute positioning |
| `y`             | `int`       | `None`        | Y-coordinate for absolute positioning |
| `width`         | `int`       | `140`         | Dropdown width |
| `height`        | `int`       | `32`          | Dropdown height |
| `id`            | `str`       | `None`        | Unique identifier for dynamic access |
| `default`       | `str`       | `options[0]`  | Default selected option |
| `on_change`     | `function`  | `None`        | Callback fired when option changes |
| `text_color`    | `str`       | `"#ffffff"`   | Text color of selected option |
| `bg_color`      | `str`       | `"#2b2b2b"`   | Background color of the dropdown |
| `hover_color`   | `str`       | `"#3b3b3b"`   | Hover color for the button & dropdown list |

---

## Static Methods

### `Dropdown.get_value(id)`
Returns the current selected value of the dropdown.

### `Dropdown.set_value(id, value)`
Sets the selected option dynamically.

### `Dropdown.set_options(id, new_options)`
Replaces the dropdown's option list with new values.

---

## Basic Usage 

```python
from pyuikit import Body, Div
from pyuikit.components import Dropdown

app = Body(title="Dropdown Demo", width=400, height=200)

Div(
    width=300,
    height=150,
    children=[
        Dropdown(
            options=["Option A", "Option B", "Option C"],
            id="myDrop",
            x=20,
            y=20
        )
    ]
)

app.run()
```
---

## Advanced Usage (Simple & Clean)

This example shows how to:

- Detect when the user changes the dropdown  
- Update a text element based on the selection  
- Get the value using a button  

---

```python
from pyuikit import Body, Div
from pyuikit.components import Dropdown, Text, Button

# Callback runs whenever the dropdown value changes
def on_change(selected):
    Text.set_text("resultText", f"Selected: {selected}")

app = Body(title="Simple Advanced Dropdown", width=400, height=250)

Div(
    width=350,
    height=200,
    children=[

        Dropdown(
            options=["Red", "Green", "Blue"],
            id="colorDrop",
            x=20,
            y=20,
            on_change=on_change
        ),

        Button(
            text="Get Selected",
            x=20,
            y=70,
            on_click=lambda: Text.set_text(
                "resultText",
                f"Current: {Dropdown.get_value('colorDrop')}"
            )
        ),

        Text(
            id="resultText",
            text="Waiting...",
            x=20,
            y=120,
            font_size=14,
            color="#ffffff"
        )
    ]
)

app.run()
```

## Complete Usage

```python
from pyuikit import Body, Div
from pyuikit.components import Dropdown, Text, Button

# Callback function for selection change
def option_changed(choice):
    Text.set_text("status", f"Selected: {choice}")

app = Body(title="Dropdown Demo", width=400, height=300, bg_color="#1f2937")

Div(
    width=350,
    height=200,
    bg_color="#111827",
    padding=20,
    children=[
        Dropdown(
            options=["Python", "JavaScript", "C++", "Rust"],
            id="langSelect",
            x=10,
            y=10,
            width=200,
            height=32,
            default="Python",
            on_change=option_changed,
            text_color="#f9fafb",
            bg_color="#222222",
            hover_color="#333333"
        ),
        Button(
            text="Get Value",
            width=120,
            height=35,
            x=10,
            y=60,
            color="#3b82f6",
            text_color="#ffffff",
            on_click=lambda: Text.set_text("status", Dropdown.get_value("langSelect"))
        ),
        Button(
            text="Set Rust",
            width=120,
            height=35,
            x=150,
            y=60,
            color="#10b981",
            text_color="#ffffff",
            on_click=lambda: Dropdown.set_value("langSelect", "Rust")
        ),
        Button(
            text="Set New Options",
            width=150,
            height=35,
            x=10,
            y=110,
            color="#f59e0b",
            text_color="#000000",
            on_click=lambda: Dropdown.set_options("langSelect", ["Apple", "Banana", "Cherry"])
        ),
        Text(id="status", text="", x=10, y=160, color="#f9fafb")
    ]
)

app.run()
```
# RadioButton Component — PyUIkit

A `RadioButton` in PyUIkit lets the user pick **ONE option from a list**.  
It’s perfect for settings, preferences, and forms where only one choice is allowed.

Unlike checkboxes, **you cannot select more than one**.

> ⚠️ **Note:** Before using this component, it is recommended to read the [Quickstart Guide](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Quickstart.md) if you haven't already to understand how to create windows, top-level Divs, and basic setup.


---

## How It Works

- You provide a list of `options=["Apple", "Banana", "Cherry"]`
- Only **one** option can be selected at a time  
- You can set a **default** value  
- You can provide an **on_change callback** to detect changes  
- Each option is automatically stacked vertically  

---

## Parameters

| Parameter      | Type      | Default | Description |
|----------------|----------|---------|-------------|
| `options`      | list     | —       | List of choices to display |
| `x`, `y`       | int      | None    | Position of the **first** radio button |
| `id`           | str      | None    | Unique ID to access this component |
| `default`      | str      | First option | Default selected value |
| `on_change`    | function | None    | Called with the new value when selection changes |
| `text_color`   | str      | `#ffffff` | Label color |
| `font`         | str      | `'Arial'` | Font family |
| `font_size`    | int      | `14`    | Label font size |

---

## Static Methods

| Method | Description |
|--------|------------|
| `RadioButton.get_value(id)` | Returns the currently selected option |
| `RadioButton.set_value(id, value)` | Programmatically changes the selection |

---

# Basic Usage

A very simple example showing how to create a RadioButton group.

```python
from pyuikit import Body, Div
from pyuikit.components import RadioButton

app = Body(title="Radio Example", width=400, height=250)

Div(
    x=20,
    y=20,
    width=300,
    height=200,
    children=[
        RadioButton(
            options=["Red", "Green", "Blue"],
            id="colorRadio",
            x=10,
            y=10
        )
    ]
)

app.run()
```

# Intermediate Example — Handle Selection Changes

```python
from pyuikit import Body, Div
from pyuikit.components import RadioButton, Text

def handle_change(selected):
    Text.set_text("resultText", f"Selected: {selected}")

app = Body(title="Radio Change Example", width=400, height=250)

Div(
    x=30,
    y=30,
    width=300,
    height=200,
    children=[
        RadioButton(
            options=["Dog", "Cat", "Bird"],
            id="animalRadio",
            x=10,
            y=10,
            on_change=handle_change
        ),
        Text(
            id="resultText",
            text="Waiting...",
            x=10,
            y=120,
            color="#00b4ff"
        )
    ]
)

app.run()
```

# Advanced Example — Reading Value With a Button

```python
from pyuikit import Body, Div
from pyuikit.components import RadioButton, Text, Button

def change_callback(val):
    Text.set_text("status", f"Changed to: {val}")

def show_current():
    current = RadioButton.get_value("themeRadio")
    Text.set_text("status", f"Current value: {current}")

app = Body(title="Advanced Radio Example", width=400, height=300)

Div(
    x=30,
    y=30,
    width=350,
    height=240,
    children=[
        RadioButton(
            options=["Light", "Dark", "System"],
            id="themeRadio",
            x=10,
            y=10,
            default="Dark",
            on_change=change_callback
        ),

        Button(
            text="Get Selected Value",
            x=10,
            y=130,
            on_click=show_current
        ),

        Text(
            text="Waiting...",
            id="status",
            x=10,
            y=180,
            color="#ffd700",
            font_size=14
        )
    ]
)

app.run()


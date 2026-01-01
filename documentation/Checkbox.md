# Checkbox Component — PyUIkit

A `Checkbox` in PyUIkit lets the user pick **one or more options** independently.
It’s perfect for toggles, settings, and forms where multiple selections are allowed.

Unlike radio buttons, **you can select multiple checkboxes at the same time**.

> ⚠️ **Note:** Before using this component, it is recommended to read the [Quickstart Guide](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Quickstart.md) if you haven't already to understand how to create windows, top-level Divs, and basic setup.

---

## How It Works

* Each checkbox is **independent** and can be toggled on/off.
* You can set a **default state** (checked or unchecked).
* You can **read or change the state dynamically** with static methods.
* Each checkbox is placed individually using `x` and `y` coordinates.

---

## Parameters

| Parameter    | Type | Default   | Description                            |
| ------------ | ---- | --------- | -------------------------------------- |
| `text`       | str  | ""        | Label for the checkbox                 |
| `x`, `y`     | int  | None      | Position of the checkbox               |
| `id`         | str  | None      | Unique ID to access this component     |
| `text_color` | str  | `#ffffff` | Color of the label text                |
| `color`      | str  | `#00ff88` | Checkbox toggle color                  |
| `font_size`  | int  | 14        | Label font size                        |
| `default`    | bool | False     | Initial checked state (True = checked) |

---

## Static Methods

| Method                                 | Description                                                                      |
| -------------------------------------- | -------------------------------------------------------------------------------- |
| `Checkbox.is_checked(id)`              | Returns `True` if the checkbox is checked, otherwise `False`                     |
| `Checkbox.set_checked(id, value=True)` | Programmatically sets the checkbox state (`True` = checked, `False` = unchecked) |

---

# Basic Usage

A very simple example showing how to create a single checkbox.

```python
from pyuikit import Body, Div
from pyuikit.components import Checkbox

app = Body(title="Checkbox Example", width=400, height=250)

Div(
    x=20,
    y=20,
    width=300,
    height=200,
    children=[
        Checkbox(
            text="Accept Terms",
            id="termsCheckbox",
            x=10,
            y=10
        )
    ]
)

app.run()
```

---

# Intermediate Example — Multiple Checkboxes

```python
from pyuikit import Body, Div, Text
from pyuikit.components import Checkbox

app = Body(title="Multiple Checkbox Example", width=400, height=300)

Div(
    x=20,
    y=20,
    width=350,
    height=250,
    children=[
        Checkbox(
            text="Option A",
            id="optionA",
            x=10,
            y=10,
            default=True,
            text_color='#000000'
        ),
        Checkbox(
            text="Option B",
            id="optionB",
            x=10,
            y=50,
            text_color='#000000'
        ),
        Checkbox(
            text="Option C",
            id="optionC",
            x=10,
            y=90,
            text_color='#000000'
        ),
        Text(
            text="Check your choices",
            id="statusText",
            x=10,
            y=150,
            color="#ffd700",
            font_size=14,
            text_color='#000000'
        )
    ]
)

app.run()
```

---

# Advanced Example — Dynamic Updates

```python
from pyuikit import Body, Div, Button, Text
from pyuikit.components import Checkbox

def show_selected():
    checked = []
    for cid in ["optionA", "optionB", "optionC"]:
        if Checkbox.is_checked(cid):
            checked.append(cid)
    Text.set_text("statusText", f"Checked: {', '.join(checked) if checked else 'None'}")

def check_all():
    for cid in ["optionA", "optionB", "optionC"]:
        Checkbox.set_checked(cid, True)

app = Body(title="Checkbox Update Example", width=400, height=300)

Div(
    x=20,
    y=20,
    width=350,
    height=250,
    children=[
        Checkbox(text="Option A", id="optionA", x=10, y=10,text_color='#000000'),
        Checkbox(text="Option B", id="optionB", x=10, y=50,text_color='#000000'),
        Checkbox(text="Option C", id="optionC", x=10, y=90,text_color='#000000'),

        Button(text="Show Checked", x=10, y=140, on_click=show_selected),
        Button(text="Check All", x=150, y=140, on_click=check_all),

        Text(text="Waiting...", id="statusText", x=10, y=180, color="#ffd700", font_size=14)
    ]
)

app.run()
```


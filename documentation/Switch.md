## Switch Component

`Switch` is an interactive **toggle component** in PyUIkit, allowing users to switch between **on/off states**.
It supports **custom colors, fonts, sizes, hover effects**, absolute positioning, and automatic state handling.
You can also dynamically read or set its state using its `id`.

> ⚠️ **Note:** Before using this component, it is recommended to read the [Quickstart Guide](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Quickstart.md) if you haven't already to understand how to create windows, top-level Divs, and basic setup.

---

### Features

* Toggle between **on/off states**.
* Fully customizable **size, colors, font, and hover effects**.
* Absolute positioning using `x` and `y`.
* Optional `id` for **dynamic updates** and state queries.
* `on_change` callback automatically receives the **current state** (`0` = off, `1` = on).

---

### Parameters

| Parameter            | Type       | Default   | Description                                                         |
| -------------------- | ---------- | --------- | ------------------------------------------------------------------- |
| `x`                  | `int`      | `None`    | X position for absolute placement inside a Div                      |
| `y`                  | `int`      | `None`    | Y position for absolute placement inside a Div                      |
| `id`                 | `str`      | `None`    | Unique identifier for dynamic updates                               |
| `width`              | `int`      | `60`      | Width of the switch component                                       |
| `height`             | `int`      | `30`      | Height of the switch component                                      |
| `text`               | `str`      | `""`      | Label displayed next to the switch                                  |
| `default`            | `bool`     | `False`   | Initial switch state (`True` = ON, `False` = OFF)                   |
| `on_change`          | `function` | `None`    | Callback function when toggled; receives current state (`0` or `1`) |
| `bg_color`           | `str`      | `#2b2b2b` | Background color of the switch                                      |
| `progress_color`     | `str`      | `#3b82f6` | Color when the switch is ON                                         |
| `button_color`       | `str`      | `#ffffff` | Color of the switch button/knob                                     |
| `button_hover_color` | `str`      | `None`    | Hover color for the switch button                                   |
| `text_color`         | `str`      | `None`    | Color of the label text                                             |
| `font_name`          | `str`      | `"Arial"` | Font family for the label text                                      |
| `font_size`          | `int`      | `14`      | Font size for the label text                                        |

---

### Dynamic Methods

| Method                        | Description                                                        |
| ----------------------------- | ------------------------------------------------------------------ |
| `Switch.get_state(id)`        | Returns the current state of the switch (`0` = OFF, `1` = ON)      |
| `Switch.set_state(id, value)` | Programmatically set the switch state (`True` = ON, `False` = OFF) |

---

### Example 1 — Basic Switch

```python
from pyuikit import Body, Div, Switch

app = Body(width=400, height=300)

Div(
    x=50, y=50,
    bg_color='grey',
    width=300, height=200,
    children=[
        Switch(
            text="Enable Feature",
            default=True
        )
    ]
)

app.run()
```

---

### Example 2 — Switch with Separate Callback Function

```python
from pyuikit import Body, Div, Switch

app = Body(width=400, height=300)

def handle_switch(state):
    if state:
        print("Switch is ON")
    else:
        print("Switch is OFF")

Div(
    x=50, y=50,bg_color='grey',
    width=300, height=200,
    children=[
        Switch(
            id="featureSwitch",
            text="Feature A",
            default=False,
            on_change=handle_switch
        )
    ]
)

app.run()
```

---

### Example 3 — Custom Colors, Font, and Hover Effects

```python
from pyuikit import Body, Div, Switch

app = Body(width=500, height=400)

Div(
    x=50, y=50,
    width=400, height=300,
    bg_color='grey',
    children=[
        Switch(
            x=20,
            y=20,
            id="customSwitch",
            text="Custom Switch",
            default=True,
            bg_color="#333333",
            progress_color="#4caf50",
            button_color="#ffffff",
            button_hover_color="#888888",
            text_color="#ffffff",
            font_name="Courier New",
            font_size=16,
            on_change=lambda state: print("Current state:", state)
        )
    ]
)

app.run()
```

---

### Notes

* Switch **must be placed inside a Div**. It cannot exist directly on the window.
* Always assign an `id` if you plan to dynamically read or set the switch state.
* The `on_change` callback **always receives the current state** (`0` or `1`).
* `button_hover_color` and `text_color` are optional but recommended for better styling.

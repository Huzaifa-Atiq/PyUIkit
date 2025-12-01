## Input Component

`Input` is a component used to get user text input inside a **Div**.  
It supports **single-line and multi-line modes**, custom colors, placeholder text, padding, and absolute positioning.

An `Input` component **must always be placed inside a Div**.

> ⚠️ **Note:** Before using this component, it is recommended to read the [Quickstart Guide](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Quickstart.md) if you haven't already to understand how to create windows, top-level Divs, and basic setup.


---

### Features

- Single-line **or** multi-line input (`multiline=True`)  
- Custom background and text color  
- Custom placeholder text  
- Supports **absolute positioning** using `x` AND `y`  
- Auto-positions when `x` and `y` are not provided  
- Padding support (`padx`, `pady`)  
- Fully dynamic API using the component’s `id`:
  - Get input text
  - Set/replace input text
  - Change input text color (including placeholder color automatically)

---

### Parameters

| Parameter      | Type    | Default     | Description |
|----------------|---------|-------------|-------------|
| `id`           | `str`   | `None`      | Unique ID used for dynamic control |
| `x`            | `int`   | `None`      | Absolute X-position (must be used with `y`) |
| `y`            | `int`   | `None`      | Absolute Y-position (must be used with `x`) |
| `width`        | `int`   | `200`       | Width of input box |
| `height`       | `int`   | `30`        | Height of input |
| `placeholder`  | `str`   | `""`        | Placeholder text |
| `multiline`    | `bool`  | `False`     | Enables multi-line typing (like a textarea) |
| `padx`         | `int`   | `0`         | Horizontal padding (only for auto layout) |
| `pady`         | `int`   | `0`         | Vertical padding |
| `bg_color`     | `str`   | `#ffffff`   | Background color |
| `text_color`   | `str`   | `#000000`   | Text + placeholder color |

---

## Example 1 — Basic Input (Auto Placement)

```python
from pyuikit.components import Input
from pyuikit import Div

Div(
    x=20, y=20,
    width=300, height=200,
    children=[
        Input(placeholder="Enter your name...")
    ]
)
```

## Example 2 — Input With Absolute Position

```python
from pyuikit.components import Input
from pyuikit import Div

Div(
    x=20, y=20,
    width=350, height=250,
    children=[
        Input(
            id="emailBox",
            placeholder="Email",
            x=40, y=30,
            width=250,
            bg_color="#eeeeee",
            text_color="#222222"
        )
    ]
)
```

## Example 3 — Multi-line Input 

multiline inputs do not support placeholders

```python
from pyuikit.components import Input
from pyuikit import Div

Div(
    x=10, y=10,
    width=400, height=300,
    children=[
        Input(
            id="bioBox",
            multiline=True,
            height=120,
        )
    ]
)
```

## Example 4 — Getting & Setting Input Text Dynamically

```python
from pyuikit.components import Input
from pyuikit import Div

Div(
    x=20, y=20,
    width=300, height=200,
    children=[
        Input(
            id="msgBox",
            placeholder="Type a message",
            width=240
        )
    ]
)

# Later in code:

# Get the text
text = Input.get_input(id="msgBox")

# Set new text
Input.set_input(id="msgBox", value="Hello World!")

# Change input color (also updates placeholder automatically)
Input.set_input_color(id="msgBox", color="#ff0000")

```


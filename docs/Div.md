## Div Component

`Div` is a **top-level container component** in PyHtmlKit that behaves like a web `<div>`.  
It is used to group and structure your UI by holding child components such as `Text` or `Button`.

A `Div` is **always a top-level container** —  
❌ You **cannot place a Div inside another Div**.  
✔ All other components (Text, Button, Input, etc.) must be placed **inside a Div**.

⚠ **Important:**  
If you want to position a Div manually, **you must provide both `x` and `y`**.  
Providing only one of them will cause the Div **not to be positioned**.

---

### 🔹 Features

- Works like a web `<div>` for grouping UI elements  
- Supports **absolute positioning**, but requires giving **both `x` and `y`**  
- If no `x`/`y` are given, PyHtmlKit will place the Div automatically  
- Customizable background color, width, height, and padding  
- Holds child components that automatically render inside it  
- Optional `id` for identifying the Div or accessing internal components later  
- Prevents nested Divs to keep layout clean and simple  

---

### 🔹 Parameters

| Parameter  | Type        | Default      | Description |
|------------|------------|-------------|-------------|
| `children` | `list`     | `[]`        | Components inside this Div (Text, Button, etc.) |
| `parent`   | Component  | `None`      | Parent container (auto-attaches to window) |
| `bg_color` | `str`      | `#FFFFFF`   | Background color |
| `padding`  | `int`      | `0`         | Space around child components |
| `id`       | `str`      | `None`      | Optional unique identifier |
| `width`    | `int`      | `100`       | Width in pixels |
| `height`   | `int`      | `100`       | Height in pixels |
| `x`        | `int`      | `None`      | Left position on screen |
| `y`        | `int`      | `None`      | Top position on screen |

---

### 🔹 Example 1 — Basic Div With Text

```python
from pyhtmlkit import Div
from pyhtmlkit.components import Text

Div(
    x=50,
    y=50,
    width=400,
    height=300,
    bg_color="#eaeaea",
    padding=10,
    children=[
        Text(text="Hello inside a Div!", color="#333", font_size=18, id="innerText")
    ],
    id="mainDiv"
)
```

---

### 🔹 Example 2 — Multiple Components Inside a Div

```python
from pyhtmlkit import Div
from pyhtmlkit.components import Text, Button

def say_hi():
    Text.set_text(id="status", new_text="Button clicked!")

Div(
    x=20,
    y=20,
    width=300,
    height=200,
    bg_color="#fafafa",
    padding=10,
    children=[
        Text(text="Click the button:", font_size=16),
        Button(text="Say Hi", on_click=say_hi),
        Text(text="", id="status", font_size=14, color="#444")
    ],
    id="interactiveDiv"
)
```

---

### 🔹 Example 3 — Full Window With Div Layout

```python
from pyhtmlkit import Body, Div
from pyhtmlkit.components import Text

app = Body(title="Div Example", width=500, height=400)

Div(
    x=100,
    y=100,
    width=300,
    height=200,
    bg_color="#dcdcdc",
    padding=20,
    children=[
        Text(text="Welcome to PyHtmlKit!", font_size=20, color="#222")
    ]
)

app.run()
```

---

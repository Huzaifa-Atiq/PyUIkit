## Div Component

A `Div` in PyHtmlKit is like a **box or container** that can hold other UI components such as `Text`, `Button`, or `Input`.  
Think of it like a section on a webpage where you can put things together to organize your interface neatly.

### 🔹 Nested Divs
Sometimes you may want a **Div inside another Div** — for example, a small card inside a bigger container.  
This is called a **nested Div**. To create one, just use the parameter `nested=True` when making the inner Div.  

- The inner Div will appear **inside the outer Div**.  
- You can put any components inside the nested Div just like a normal Div.  
- You can also have multiple levels of Divs inside each other if needed.  

⚠ Tip: Use **padding** to control spacing inside Divs **only if `x` and `y` are not provided**.  
If you use `x` and `y`, the Div will use absolute positioning instead and padding will not affect

---

### 🔹 Features

- Groups UI components together  
- Can hold other Divs as **nested Divs**  
- Customizable background color, width, height, and padding  
- Optional `id` for referencing the Div in your code  

---

### 🔹 Parameters

| Parameter  | Type        | Default      | Description |
|------------|------------|-------------|-------------|
| `children` | `list`     | `[]`        | Components inside this Div (Text, Button, Input, or Div with nested=True) |
| `parent`   | `Component`  | `None`      | Parent container (auto-attaches to window if top-level) |
| `bg_color` | `str`      | `#FFFFFF`   | Background color |
| `padding`  | `int`      | `0`         | Space around child components |
| `id`       | `str`      | `None`      | Optional unique identifier |
| `width`    | `int`      | `100`       | Width in pixels |
| `height`   | `int`      | `100`       | Height in pixels |
| `x`        | `int`      | `None`      | Left position on screen |
| `y`        | `int`      | `None`      | Top position on screen |
| `nested`   | `bool`     | `False`     | Whether this Div is nested inside another Div |

---

### 🔹 Example — Basic Div

```python
from pyhtmlkit import Body, Div
from pyhtmlkit.components import Text, Button

# Example 1 — Basic Div With Text
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

# Example 2 — Multiple Components Inside a Div
```python
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

# Example 3 — Nested Divs
```python
app = Body(title="Nested Div Example", width=500, height=400)

Div(
    x=50,
    y=50,
    width=400,
    height=300,
    bg_color="#dcdcdc",
    padding=20,
    children=[
        Text(text="Parent Div", font_size=18, color="#222"),
        Div(
            width=200,
            height=100,
            bg_color="#bbbbbb",
            padding=10,
            nested=True,
            children=[
                Text(text="Nested Div Content", font_size=16, color="#111"),
                Button(text="Click Me")
            ],
            id="nestedDiv"
        )
    ],
    id="parentDiv"
)
```

# Example 4 — Full Window Layout With Divs
```python
Div(
    width=150,
    height=500,
    bg_color="#111827",
    padding=10,
    children=[
        Text(text="Sidebar", color="#f9fafb", font_size=16),
        Button(text="Option 1"),
        Button(text="Option 2")
    ],
    id="sidebar"
)

Div(
    width=430,
    height=500,
    bg_color="#1f2937",
    padding=15,
    nested=True,
    children=[
        Text(text="Main Content", color="#f9fafb", font_size=18),
        Button(text="Action")
    ],
    id="contentDiv"
)

app.run()
```
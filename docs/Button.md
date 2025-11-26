## Button Component

`Button` is an interactive component in PyHtmlKit used to trigger actions when clicked.  
It behaves similarly to an HTML `<button>` and supports **absolute positioning**, custom colors, dynamic updates, and click events.

---

### 🔹 Features
- Customizable text, size, colors, and corner radius  
- Supports **absolute positioning** with `x` and `y`  
- Works as a child of a `Div` (cannot be placed directly on the window)  
- Supports unique `id` for dynamic updates  
- Clickable with `on_click` callback functions  
- Lightweight, built on top of **CustomTkinter CTkButton**

---

### 🔹 Parameters

| Parameter        | Type       | Default       | Description |
|------------------|------------|---------------|-------------|
| `text`           | `str`      | `"Button"`    | Button label |
| `x`              | `int`      | `None`        | X position for absolute placement |
| `y`              | `int`      | `None`        | Y position for absolute placement |
| `id`             | `str`      | `None`        | Unique identifier for updates |
| `width`          | `int`      | `120`         | Button width |
| `height`         | `int`      | `40`          | Button height |
| `corner_radius`  | `int`      | `8`           | Rounded corner radius |
| `color`          | `str`      | `#3b82f6`     | Background color |
| `hover_color`    | `str`      | `#2563eb`     | Background color when hovered |
| `text_color`     | `str`      | `#ffffff`     | Text color |
| `on_click`       | `function` | `None`        | Function to run on click |

---

### 🔹 Dynamic Update Methods

| Method | Description |
|--------|-------------|
| `Button.set_text(id, text)` | Change the button label |
| `Button.set_color(id, color)` | Change button background color |
| `Button.set_text_color(id, color)` | Change button text color |
| `Button.set_size(id, width, height)` | Resize the button |

---

---

## 🧪 Examples

### ✅ Example 1 — Simple Button inside a Div
```python
from pyhtmlkit import Div
from pyhtmlkit.components import Button

Div(
    x=50,
    y=50,
    width=300,
    height=200,
    bg_color="#f0f0f0",
    children=[
        Button(
            text="Click Me",
            x=20,
            y=20
        )
    ]
)
```

### ✅ Example 2 — Button with Click Event
```python
from pyhtmlkit import Div
from pyhtmlkit.components import Button

def say_hello():
    print("Hello from PyHtmlKit!")

Div(
    x=50,
    y=50,
    width=300,
    height=200,
    bg_color="#f0f0f0",
    children=[
        Button(
            text="Say Hello",
            x=20,
            y=20,
            on_click=say_hello
        )
    ]
)
```

### ✅ Example 3 — Dynamic Updates Using id
```python
from pyhtmlkit import Div
from pyhtmlkit.components import Button

def change_button():
    Button.set_text("myButton", "Updated!")
    Button.set_color("myButton", "#10b981")
    Button.set_size("myButton", width=180, height=50)

Div(
    x=40,
    y=40,
    width=300,
    height=200,
    bg_color="#eaeaea",
    children=[
        Button(
            text="Update Me",
            id="myButton",
            x=20,
            y=20,
            on_click=change_button
        )
    ]
)
```

## 🔍 Notes

- Button must be placed inside a Div

- If x and y are not provided, the button stacks vertically inside the Div

- Each button can be updated at runtime using its


## 📦 Div Component

`Div` is a **container component** in PyHtmlKit that can hold other components like `Text` or `Button`.  
It acts like a **web `<div>`** and supports **absolute positioning** or **pack layout**.  

---

### 🔹 Features
- Container for other components
- Absolute positioning using `x` and `y` coordinates
- Pack layout fallback if `x` and `y` are omitted
- Prevents nested `Div`s to maintain simple layout
- Customizable **width, height, background color, and padding**
- Supports `id` for dynamic updates of child components

---

### 🔹 Parameters

| Parameter  | Type        | Default      | Description |
|------------|------------|-------------|-------------|
| `children` | `list`     | `[]`        | List of child components inside the Div (Text, Button, etc.) |
| `parent`   | Component  | `None`      | Optional parent component (auto-attaches to window if None) |
| `bg_color` | `str`      | `#FFFFFF`   | Background color of the Div |
| `padding`  | `int`      | `0`         | Padding around child components if using pack layout |
| `id`       | `str`      | `None`      | Optional unique identifier for dynamic updates |
| `width`    | `int`      | `100`       | Width of the Div in pixels |
| `height`   | `int`      | `100`       | Height of the Div in pixels |
| `x`        | `int`      | `None`      | X coordinate for absolute placement |
| `y`        | `int`      | `None`      | Y coordinate for absolute placement |

---

### 🔹 Example

```python
from pyhtmlkit import Div
from pyhtmlkit.components import Text

# Create a top-level Div
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

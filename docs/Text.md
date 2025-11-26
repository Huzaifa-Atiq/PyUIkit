## Text Component

`Text` is a simple component used to display text inside a **Div**.  
It supports **custom fonts, colors, sizes, and optional positioning**.

A `Text` component **must always be placed inside a Div**.  
It cannot exist on its own.

---

### 🔹 Features

- Display static or dynamically-updatable text  
- Supports **absolute positioning** using `x` **and** `y`  
  ❗ **Giving only `x` or only `y` will not work — both must be provided**  
- If no `x` and `y` are given, the Text auto-positions itself  
- Customizable font family, size, and color  
- Can be dynamically updated *using its `id`*  
- Clean API for changing text, color, and font size after rendering  

---

### 🔹 Parameters

| Parameter   | Type    | Default     | Description |
|-------------|---------|-------------|-------------|
| `text`      | `str`   | *required*  | The text to display |
| `x`         | `int`   | `None`      | Absolute X-position (must be used with `y`) |
| `y`         | `int`   | `None`      | Absolute Y-position (must be used with `x`) |
| `font`      | `str`   | `"Arial"`   | Font family |
| `font_size` | `int`   | `14`        | Text size |
| `color`     | `str`   | `#000000`   | Text color |
| `id`        | `str`   | `None`      | Used for dynamic updates |

---

### 🔹 Example 1 — Basic Text (Auto Placement)

```python
from pyhtmlkit.components import Text
from pyhtmlkit import Div

Div(
    x=20, y=20,
    width=300, height=200,
    children=[
        Text(text="Hello World!")
    ]
)
```

### 🔹 Example 2 — Text With Absolute Position (x AND y required)

```python
from pyhtmlkit.components import Text
from pyhtmlkit import Div

Div(
    x=20, y=20,
    width=300, height=200,
    children=[
        Text(text="Positioned Text", x=50, y=40, color="#444", font_size=18)
    ]
)

```

### 🔹 Example 3 — Using id for Dynamic Updates
```python
from pyhtmlkit.components import Text
from pyhtmlkit import Div

Div(
    x=20, y=20,
    width=300, height=200,
    children=[
        Text(text="Waiting for update...", id="statusText", font_size=16)
    ]
)

# Later in your code:
Text.set_text(id="statusText", new_text="Updated successfully!")
Text.set_color(id="statusText", color="#0080ff")
Text.set_font_size(id="statusText", font_size=20)
```

### 🔹 API for Dynamic Updates

- All updates use the id of the Text.

✔ Change the text
```python
Text.set_text(id="myText", new_text="Hello!")
```

✔ Change the color
```python
Text.set_color(id="myText", color="#ff0000")
```

✔ Change the font size
```python
Text.set_font_size(id="myText", font_size=22)
```


## 🔹 Notes
- Text must be inside a Div

- For absolute positioning, both x and y must be given

- If no x/y are provided, text auto-positions inside the Div

- Always assign an id if you plan to update the text dynamically
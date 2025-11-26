# PyHtmlKit

PyHtmlKit is a Python library for building desktop applications with a **simple, HTML-like syntax**.  
It aims to bring **simplicity and web-like component structure** to Python GUI development, allowing developers to create windows, divs, and components without dealing with complex layout management.  
The interface is built on **CustomTkinter**, making it lightweight, modern, and easy to use.

---

## ⚡ Features

### Simple Layouts
- Create windows with a single line of code
- Use **Divs** as containers for components
- Absolute positioning with `x` and `y` or pack layout for flexibility
- Automatic handling of component IDs for dynamic updates

### Components
- **Text**: Display text with color, font size, and dynamic updates
- **Button**: Clickable buttons with customizable size, color, text, corner radius, and click functions
- Easily extendable for future components (Images, Inputs, etc.)

### Dynamic Updates
- Update text, colors, and fonts at runtime using component IDs
- Simple, consistent API for changing UI elements without rebuilding

---

## 🚀 Quickstart

### 1. Install
```bash
pip install pyhtmlkit
```

### 2. Create your first window
```python
from pyhtmlkit import Body

app = Body(title="My First App", width=600, height=400, bg_color="#f5f5f5")
app.run()
```

### 3. Add a Div container
```python
from pyhtmlkit import Div

Div(
    x=50,
    y=50,
    width=400,
    height=300,
    bg_color="#eaeaea",
    padding=10,
    id="mainDiv"
)

```

### 4. Add Text inside a Div
```python
from pyhtmlkit.components import Text

Div(
    x=50,
    y=50,
    width=400,
    height=300,
    bg_color="#eaeaea",
    padding=10,
    children=[
        Text(text="Hello PyHtmlKit!", color="#333", font_size=20, id="mainText")
    ],
    id="mainDiv"
)
```

### 5. Update Text dynamically
```python
from pyhtmlkit.components import Text

# Change text after some action
Text.set_text("mainText", "Updated Text!")
Text.set_color("mainText", "#ff0000")
Text.set_font_size("mainText", 30)

```

## 📚 Components Documentation

For detailed usage of individual components, check the docs:

- [Div Component](https://github.com/Huzaifa-Atiq/pyhtmlkit/blob/main/docs/Div.md)
- [Button Component](https://github.com/Huzaifa-Atiq/pyhtmlkit/blob/main/docs/Button.md)
- [Text Component](https://github.com/Huzaifa-Atiq/pyhtmlkit/blob/main/docs/Text.md)
- [Input Component](https://github.com/Huzaifa-Atiq/pyhtmlkit/blob/main/docs/Input.md)
- [FileDialog Component](https://github.com/Huzaifa-Atiq/pyhtmlkit/blob/main/docs/FileDialog.md)
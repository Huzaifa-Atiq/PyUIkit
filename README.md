<div style="display: flex; align-items: center;">
  <img src="https://raw.githubusercontent.com/Huzaifa-Atiq/PyUIkit/refs/heads/main/logo.svg" width="500" />
</div>
<br>



**PyUIkit** is a modern, web-like, component-based **Python GUI framework** built on top of [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter). It aims to bring **simplicity and web-like component structure** to Python GUI development, allowing developers to create windows, divs, and components without dealing with complex layout management. It allows you to create **beautiful and interactive desktop applications** with minimal code, using **Div-based layouts** and reusable UI components.

---

## Features
- Create **nested layouts** with `Div` containers.
- Use **Text, Input, Button** components and more.
- Interactive components with **event handling**.
- Component IDs for **dynamic updates**.
- Easy to use for both **beginners and experienced developers**.
- Supports **modern styling** and **dark/light themes** (future updates).

---

## Installation
```bash
pip install pyuikit
```

## Getting started

1. Create a simple window

```python
from pyuikit import Body

app = Body(width=400, height=300, bg_color='white')
app.run()
```

This creates a blank window with the specified size and background color.

![window](https://raw.githubusercontent.com/Huzaifa-Atiq/PyUIkit/main/documentation/images/gettingstarted1.png)

2. Add components inside a Div

```python
from pyuikit import Body, Div
from pyuikit.components import Text, Button, Input

def greet():
    name = Input.get_input(id='name_input')
    Text.set_text(id='greeting', new_text=f'Hello, {name}!')

app = Body(width=400, height=300, bg_color='white')

Div(
    width=360,
    height=250,
    children=[
        Text(text='Enter your name:'),
        Input(placeholder='Name',id='name_input'),
        Button(text='Greet',on_click=greet),
        Text(text='', id='greeting')
    ]
)

app.run()
```

Note: Every app must have at least one top-level Div to hold components.

![window](https://raw.githubusercontent.com/Huzaifa-Atiq/PyUIkit/main/documentation/images/gettingstarted2.png)

## Documentation:

Full documentation and examples: 

- [Quickstart guide](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Quickstart.md)
- [Div component](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Div.md)
- [Body component](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Body.md)

Other components:

- [Button component](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Button.md)
- [Text component](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Text.md)
- [Input component](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Input.md)
- [Filedialog component](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Filedialog.md)
- [Slider component](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Slider.md)
- [Radiobutton component](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Radiobutton.md)
- [Progressbar component](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Progressbar.md)
- [Dropdown component](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Dropdown.md)
- [Switch component](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Switch.md)
- [Checkbox component](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Checkbox.md)
- [Toast component](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Toast.md)

Example Applications:

- [Password strength checker](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/examples/passwordchecker.md)
- [Color mixer](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/examples/colormixer.md)

<br><br>
**Note:** PyUIkit is now in a stable release, but issues may still occur. We welcome and appreciate contributions! Feel free to submit PRs or report any problems via the [GitHub Issues](https://github.com/Huzaifa-Atiq/PyUIkit/issues) tab.


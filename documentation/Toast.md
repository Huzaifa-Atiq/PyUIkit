# Toast Component

The `Toast` component provides **temporary notifications** that slide in and out of the screen.
It’s perfect for **alerts, status messages, confirmations, or any short feedback** to the user.

You can **customize colors, position, size, duration, and optional close buttons**, and the toast automatically slides in and slides out with smooth animations.

> ⚠️ **Note:** Before using this component, it is recommended to read the [Quickstart Guide](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Quickstart.md) if you haven't already to understand how to create windows, top-level Divs, and basic setup.

---

## Features

* Fully **customizable text, colors, and size**.
* Optional **close button** for manual dismissal.
* **Slide-in and slide-out animations** by default.
* Supports **absolute positioning** via `x`/`y` or preset positions (`top-left`, `top-right`, `bottom-left`, `bottom-right`).
* **Automatic parent detection** — no need to pass the root manually.
* Can be **shown programmatically** using `.show()`.
* Works seamlessly with other PyUIkit components.

---

## Parameters

| Parameter    | Type      | Default       | Description                                                              |
| ------------ | --------- | ------------- | ------------------------------------------------------------------------ |
| `text`       | str       | `""`          | Text to display inside the toast                                         |
| `duration`   | int/float | `3`           | Time in seconds before the toast auto-dismisses                          |
| `x`          | int       | None          | X-coordinate for custom absolute positioning                             |
| `y`          | int       | None          | Y-coordinate for custom absolute positioning                             |
| `position`   | str       | `"top-right"` | Preset position (`top-left`, `top-right`, `bottom-left`, `bottom-right`) |
| `width`      | int       | `220`         | Width of the toast in pixels                                             |
| `height`     | int       | `50`          | Height of the toast in pixels                                            |
| `bg_color`   | str       | `#333333`     | Background color of the toast                                            |
| `text_color` | str       | `#ffffff`     | Color of the text                                                        |
| `font_name`  | str       | `"Arial"`     | Font family of the text                                                  |
| `font_size`  | int       | `14`          | Font size of the text                                                    |
| `show_close` | bool      | `True`        | Whether to show a close button for manual dismissal                      |
| `id`         | str       | None          | Unique identifier to access the toast programmatically                   |

---

## Basic Usage

```python
from pyuikit import Body, Div
from pyuikit.components import Button, Toast

app = Body(title="Toast Demo", width=600, height=400)

def show_toast():
    Toast(
        text="This is a toast!",
        bg_color="#444",
        text_color="white",
        position="top-right",
        show_close=True,
        duration=4,
    ).show()

Div(
    width=400,
    height=400,
    children=[Button(text="Show Toast", on_click=show_toast)]
)

app.run()
```

---

## Advanced Usage — Multiple Toasts

```python
from pyuikit import Body, Div
from pyuikit.components import Button, Toast

app = Body(title="Multiple Toasts", width=600, height=400)

def toast_success():
    Toast(
        text="✅ Success!",
        bg_color="#10b981",
        text_color="white",
        position="top-right",
        duration=3
    ).show()

def toast_warning():
    Toast(
        text="⚠️ Warning!",
        bg_color="#facc15",
        text_color="#000000",
        position="bottom-left",
        duration=4
    ).show()

def toast_custom_xy():
    Toast(
        text="Custom Position!",
        bg_color="#0066aa",
        text_color="white",
        duration=4,
        x=150,
        y=120,
        width=240,
        height=50,
        show_close=True
    ).show()

Div(
    width=500,
    height=400,
    children=[
        Button(text="Success Toast", on_click=toast_success),
        Button(text="Warning Toast", on_click=toast_warning),
        Button(text="Custom Position Toast", on_click=toast_custom_xy),
    ]
)

app.run()
```

---

## Notes

* **Slide animations** automatically move the toast in from the right and out to the right.
* **Custom `x`/`y` coordinates** override preset positions.
* Close button is optional but recommended for user-controlled dismissal.
* Works with all PyUIkit components and respects parent window sizing.
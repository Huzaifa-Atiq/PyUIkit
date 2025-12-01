# Body Component

The `Body` component is the **main application window** in PyUIkit.  
It acts as the **root container** for all other components like `Div`, `Text`, `Button`, and `Input`.  
Think of it like the canvas or the main frame where your UI lives.

> ⚠️ **Note:** Before using Body, it is recommended to read the [Quickstart Guide](https://github.com/Huzaifa-Atiq/PyUIkit/blob/main/documentation/Quickstart.md) if you haven't already to understand how to create windows, top-level Divs, and basic setup.

---

### 🔹 Features

- Creates a **customizable window** for your app  
- Sets **window title, size, background color, and icon**  
- Keeps track of **all components by ID**  
- Required as the **starting point** for every PyUIkit app  

---

### 🔹 Parameters

| Parameter      | Type       | Default        | Description |
|----------------|------------|----------------|-------------|
| `title`        | `str`      | `"PyUIkit App"` | The window title |
| `width`        | `int`      | `600`           | Window width in pixels |
| `height`       | `int`      | `400`           | Window height in pixels |
| `resizable`    | `tuple`    | `(True, True)`  | Allow resizing `(width_resizable, height_resizable)` |
| `bg_color`     | `str`      | `#FFFFFF`       | Background color of the main window |
| `icon`         | `str`      | `'logo.ico'`    | Path to window icon (optional) |

---

### 🔹 Methods

#### `run()`
Starts the main event loop and **renders the window**.

```python
app = Body(width=500, height=400, bg_color="#f0f0f0", title="My App")
app.run()
```

> This opens a blank window. All components like `Div` or `Text` must be added inside this `Body`.

### Example — Simple Window

```python
from pyuikit import Body

# Create the main application window
app = Body(
    title="My First PyUIkit App",
    width=400,
    height=300,
    bg_color="#ffffff"
)

app.run()
```

> This will display a **400x300 white window** with the title "My First PyUIkit App".

### Example — Full Body Initialization

This example demonstrates **all parameters** of `Body` and how they affect your app window:

```python
from pyuikit import Body

# Create the main app window with full customization
app = Body(
    title="Custom App Window",      # Window title
    width=600,                      # Window width in pixels
    height=450,                     # Window height in pixels
    resizable=(False, True),        # Width not resizable, height resizable
    bg_color="#1e1e2f",             # Background color of the window
    icon="logo.ico"                 # Custom icon (ensure 'logo.ico' exists)
)

# Run the app to display the window
app.run()
```

Explanation of parameters used:

- title="Custom App Window" → Sets the window title shown in the OS title bar.

- width=600 & height=450 → Sets the initial window size.

- resizable=(False, True) → Prevents resizing in width but allows height adjustment.

- bg_color="#1e1e2f" → Sets a dark background color.

- icon="logo.ico" → Adds a custom window icon.

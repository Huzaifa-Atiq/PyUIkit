## FileDialog Component

`FileDialog` is a **file picker component** in PyUIkit that allows users to **select or save files**.  
You can style it, set a placeholder, and retrieve the selected file path easily.

---

### 🔹 Features

- Open or save files with a native file dialog.
- Fully customizable **frame, entry, and button colors**.
- Supports **placeholder text** in the entry field.
- Can retrieve the selected file dynamically using an **`id`**.

---

### 🔹 Parameters

| Parameter           | Type        | Default           | Description |
|--------------------|------------|-----------------|-------------|
| `id`               | `str`      | `None`          | Unique identifier for dynamic access |
| `width`            | `int`      | `200`           | Width of the FileDialog component |
| `height`           | `int`      | `30`            | Height of the FileDialog component |
| `placeholder`      | `str`      | `"Select a file"` | Placeholder text inside the entry |
| `dialog_type`      | `str`      | `"open"`        | `"open"` to select a file, `"save"` to save a file |
| `filetypes`        | tuple      | `(("All Files", "*.*"),)` | Tuple specifying file types |
| `frame_bg`         | `str`      | `"#ffffff"`     | Background color of the frame |
| `entry_bg`         | `str`      | `"#ffffff"`     | Background color of the entry |
| `entry_text_color` | `str`      | `"#000000"`     | Text color inside the entry |
| `button_color`     | `str`      | `"#3b82f6"`     | Browse button background color |
| `button_text_color`| `str`      | `"#ffffff"`     | Browse button text color |
| `padx`             | `int`      | `0`             | Horizontal padding around the component |
| `pady`             | `int`      | `0`             | Vertical padding around the component |

---

#### `get_file(id)` (Static)
Retrieve the currently selected file path by the FileDialog's `id`.

### 🔹 Example Usage
```python
from pyuikit import Body, Div
from pyuikit.components import FileDialog, Button, Text

# Callback function
def show_file_path():
    path = FileDialog.get_file("myFile")
    print("Selected file:", path)
    Text.set_text("statusText", f"Selected: {path}")

app = Body(title="FileDialog Demo", width=400, height=300, bg_color="#1f2937")

Div(
    width=350,
    height=100,
    bg_color="#111827",
    padding=20,
    children=[
        FileDialog(
            id="myFile",
            width=250,
            height=35,
            placeholder="Choose a file...",
            dialog_type="open",
            frame_bg="#222222",
            entry_bg="#000000",
            entry_text_color="#ffffff",
            button_color="#3b82f6",
            button_text_color="#f9fafb",
            padx=0,
            pady=10
        ),
        Button(
            text="Get File Path",
            width=120,
            height=35,
            color="#10b981",
            text_color="#ffffff",
            on_click=show_file_path
        ),
        Text(text="", id="statusText", font_size=14, color="#f9fafb")
    ]
)

app.run()
```

⚠ Tip: Always assign an id to your FileDialog so you can get the selected file path dynamically using FileDialog.get_file("id").
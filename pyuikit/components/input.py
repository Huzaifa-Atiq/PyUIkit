from customtkinter import CTkEntry, CTkTextbox
from ..app import App
import warnings

class Input:
    def __init__(self, id=None, x=None, y=None, width=200, height=30, placeholder="", multiline=False,
                 bg_color="#ffffff", text_color="#000000",font_size=14):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.placeholder = placeholder
        self.multiline = multiline
        self.bg_color = bg_color
        self.text_color = text_color
        self.font_size = font_size
        self.widget = None

    def render(self, parent):
        if parent is None:
            raise ValueError("Input must be a child of a Div.")

        # Create the widget
        if self.multiline:
            self.widget = CTkTextbox(
                parent,
                width=self.width,
                height=self.height,
                fg_color=self.bg_color,
                text_color=self.text_color,
            )
        else:
            self.widget = CTkEntry(
                parent,
                width=self.width,
                height=self.height,
                font=('Arial', self.font_size),
                placeholder_text=self.placeholder,
                fg_color=self.bg_color,
                text_color=self.text_color,
                placeholder_text_color=self.text_color,
            )

        # Absolute positioning only
        if self.x is not None and self.y is not None:
            self.widget.place(x=self.x, y=self.y)
        else:
            self.widget.place(x=0, y=0)
            warnings.warn(
                f"[PyUIkit] Warning: Input '{self.id or self.placeholder}' missing x or y coordinates. "
                f"Auto-placing at (0, 0).",
                stacklevel=2
            )

        # Register ID for dynamic access
        if self.id:
            App.instance.ids[self.id] = self.widget

    # Dynamic Update Methods 

    @staticmethod
    def get_input_text(id):
        widget = App.instance.ids.get(id)
        if widget is None:
            raise ValueError(f"No Input found with id '{id}'.")

        if isinstance(widget, CTkEntry):
            return widget.get()
        else:  # CTkTextbox
            return widget.get("1.0", "end-1c")

     
    @staticmethod
    def set_input_text(id, value):
        widget = App.instance.ids.get(id)
        if widget is None:
            raise ValueError(f"No Input found with id '{id}'.")

        if isinstance(widget, CTkEntry):
            widget.delete(0, "end")
            widget.insert(0, value)
        else:  # CTkTextbox
            widget.delete("1.0", "end")
            widget.insert("1.0", value)

    @staticmethod
    def set_input_color(id, color):
        """Update both text and placeholder color dynamically."""
        widget = App.instance.ids.get(id)
        if widget is None:
            raise ValueError(f"No Input found with id '{id}'.")

        if isinstance(widget, CTkEntry):
            widget.configure(text_color=color, placeholder_text_color=color)
        else:
            widget.configure(text_color=color)

    @staticmethod
    def set_input_bg_color(id, color):
        """Update background color dynamically for both single-line and multiline inputs."""
        widget = App.instance.ids.get(id)
        if widget is None:
            raise ValueError(f"No Input found with id '{id}'.")

        # Update background color
        widget.configure(fg_color=color)

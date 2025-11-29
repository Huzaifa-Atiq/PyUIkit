from customtkinter import CTkProgressBar
from ..app import App
import warnings

class ProgressBar:
    def __init__(
        self,
        id=None,
        x=None,
        y=None,
        width=200,
        height=20,
        value=0,
        fg_color="#3b82f6",
        bg_color="#e5e7eb"
    ):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.value = max(0, min(value, 100)) / 100  # ensure 0–1 for CTk
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.widget = None

    def render(self, parent):
        if parent is None:
            raise ValueError("ProgressBar must be a child of a Div.")

        # ---- Create widget ---- #
        self.widget = CTkProgressBar(
            master=parent,
            width=self.width,
            height=self.height,
            progress_color=self.fg_color,
            fg_color=self.bg_color
        )

        self.widget.set(self.value)  # initial %

        # Absolute positioning
        if self.x is not None and self.y is not None:
            self.widget.place(x=self.x, y=self.y)
        else:
            self.widget.place(x=0, y=0)
            warnings.warn(
                f"[PyUIkit] Warning: ProgressBar '{self.id or 'unnamed'}' missing x or y coordinates. "
                f"Auto-placing at (0, 0).",
                stacklevel=2
            )

        # Register ID 
        if self.id:
            App.instance.ids[self.id] = self.widget

    # Dynamic Update Methods 

    
    @staticmethod
    def get_value(id):
        widget = App.instance.ids.get(id)
        if widget is None:
            raise ValueError(f"No ProgressBar found with id '{id}'.")
        # CTkProgressBar.get() returns a float 0.0–1.0
        return widget.get() * 100  # convert to 0–100 range

    @staticmethod
    def set_value(id, new_value):
        widget = App.instance.ids.get(id)
        if widget is None:
            raise ValueError(f"No ProgressBar found with id '{id}'.")

        clamped = max(0, min(new_value, 100)) / 100
        widget.set(clamped)

    @staticmethod
    def set_colors(id, fg_color=None, bg_color=None):
        widget = App.instance.ids.get(id)
        if widget is None:
            raise ValueError(f"No ProgressBar found with id '{id}'.")

        if fg_color:
            widget.configure(progress_color=fg_color)
        if bg_color:
            widget.configure(fg_color=bg_color)

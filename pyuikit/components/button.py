from customtkinter import CTkButton
from ..app import App
import warnings

class Button:
    def __init__(
        self,
        text="Button",
        x=None,
        y=None,
        id=None,
        width=120,
        height=40,
        corner_radius=8,
        color="#3b82f6",
        text_color="#ffffff",
        hover_color='#3b82f6',  
        on_click=None,
    ):
        self.text = text
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.corner_radius = corner_radius
        self.color = color
        self.text_color = text_color
        self.hover_color = hover_color 
        self.on_click = on_click
        self.button = None

    def render(self, parent):
        if parent is None:
            raise ValueError("Button must be a child of a Div.")

        self.button = CTkButton(
            master=parent,
            text=self.text,
            width=self.width,
            height=self.height,
            corner_radius=self.corner_radius,
            fg_color=self.color,
            hover_color=self.hover_color,  
            text_color=self.text_color,
            command=self.on_click
        )

        # Render positioning
        if self.x is not None and self.y is not None:
            self.button.place(x=self.x, y=self.y)
        else:
            self.button.place(x=0, y=0)
            warnings.warn(
                f"[PyUIkit] Warning: Button '{self.text}' missing x or y coordinates. "
                f"Auto-placing at (0, 0).",
                stacklevel=2
            )

        # Register ID for updates
        if self.id:
            App.instance.ids[self.id] = self.button

    # Dynamic Update Methods 
    @staticmethod
    def set_text(id, text):
        widget = App.instance.ids.get(id)
        if widget:
            widget.configure(text=text)
        else:
            raise ValueError(f"No Button found with id '{id}'.")

    @staticmethod
    def set_color(id, color):
        widget = App.instance.ids.get(id)
        if widget:
            widget.configure(fg_color=color)
        else:
            raise ValueError(f"No Button found with id '{id}'.")

    @staticmethod
    def set_text_color(id, color):
        widget = App.instance.ids.get(id)
        if widget:
            widget.configure(text_color=color)
        else:
            raise ValueError(f"No Button found with id '{id}'.")

    @staticmethod
    def set_size(id, width=None, height=None):
        widget = App.instance.ids.get(id)
        if widget:
            widget.configure(
                width=width if width is not None else widget.cget("width"),
                height=height if height is not None else widget.cget("height")
            )
        else:
            raise ValueError(f"No Button found with id '{id}'.")

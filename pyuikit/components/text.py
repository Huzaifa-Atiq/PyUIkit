from customtkinter import CTkLabel
from ..app import App
import warnings

class Text:
    def __init__(self, text, x=None, y=None, id=None, color="#000000", font_size=14):
        self.text = text
        self.id = id
        self.color = color
        self.font_size = font_size
        self.x = x
        self.y = y
        self.label = None

    def render(self, parent):
        if parent is None:
            raise ValueError("Text must be a child of a Div.")

        self.label = CTkLabel(
            master=parent,
            text=self.text,
            text_color=self.color,
            font=('Arial', self.font_size)
        )

        # Absolute positioning only
        if self.x is not None and self.y is not None:
            self.label.place(x=self.x, y=self.y)
        else:
            self.label.place(x=0, y=0)
            warnings.warn(
                f"[PyUIkit] Warning: Text '{self.text}' missing x or y coordinates. Auto-placing at (0, 0).",
                stacklevel=2
            )

        # Register in App instance by ID
        if self.id:
            App.instance.ids[self.id] = self.label

    # Dynamic Update Methods 
    @staticmethod
    def set_text(id, new_text):
        widget = App.instance.ids.get(id)
        if widget:
            widget.configure(text=new_text)
        else:
            raise ValueError(f"No Text found with id '{id}'.")

    @staticmethod
    def set_color(id, color):
        widget = App.instance.ids.get(id)
        if widget:
            widget.configure(text_color=color)
        else:
            raise ValueError(f"No Text found with id '{id}'.")

    @staticmethod
    def set_font_size(id, font_size):
        widget = App.instance.ids.get(id)
        if widget:
            current_font = widget.cget("font")  # returns a tuple like ("Arial", 14)
            font_family = current_font[0]
            widget.configure(font=(font_family, font_size))
        else:
            raise ValueError(f"No Text found with id '{id}'.")

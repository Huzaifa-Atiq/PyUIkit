from customtkinter import CTkCheckBox
from tkinter import BooleanVar
from ..app import App
import warnings

class Checkbox:
    def __init__(
        self,
        text="",
        x=None,
        y=None,
        id=None,
        text_color="#ffffff",
        color="#00ff88",
        font_size=14,
        default=False
    ):
        self.text = text
        self.id = id
        self.text_color = text_color
        self.color = color
        self.font_size = font_size
        self.x = x
        self.y = y
        self.default = default
        self._variable = BooleanVar(value=self.default)
        self.checkbox = None

    def render(self, parent):
        if parent is None:
            raise ValueError("Checkbox must be a child of a Div.")

        self.checkbox = CTkCheckBox(
            master=parent,
            text=self.text,
            text_color=self.text_color,
            fg_color=self.color,
            font=('Arial', self.font_size),
            variable=self._variable
        )

        if self.x is not None and self.y is not None:
            self.checkbox.place(x=self.x, y=self.y)
        else:
            self.checkbox.place(x=0, y=0)
            warnings.warn(
                f"[PyUIkit] Warning: Checkbox '{self.text}' missing x or y coordinates. "
                f"Auto-placing at (0, 0).",
                stacklevel=2
            )

        if self.id:
            App.instance.ids[self.id] = self

    # Dynamic Update Methods 
    @staticmethod
    def is_checked(id):
        widget = App.instance.ids.get(id)
        if widget:
            return widget._variable.get()
        else:
            raise ValueError(f"No Checkbox found with id '{id}'.")

    @staticmethod
    def set_checked(id, value=True):
        widget = App.instance.ids.get(id)
        if widget:
            widget._variable.set(value)
        else:
            raise ValueError(f"No Checkbox found with id '{id}'.")

from customtkinter import CTkRadioButton, StringVar
from ..app import App
import warnings

class RadioButton:
    def __init__(
        self,
        options,
        x=None,
        y=None,
        id=None,
        default=None,
        on_change=None,
        text_color="#ffffff",
        font_size=14
    ):
        self.options = options
        self.x = x
        self.y = y
        self.id = id
        self.default = default or (options[0] if options else "")
        self.on_change = on_change
        self.text_color = text_color
        self.font_size = font_size

        self.var = StringVar(value=self.default)
        self.radio_buttons = []

    def render(self, parent):
        if parent is None:
            raise ValueError("RadioButton must be a child of a Div.")

        if self.x is None or self.y is None:
            warnings.warn(
                f"[PyUIkit] Warning: RadioButton '{self.id or self.options}' missing x or y coordinates. "
                "Please provide x and y to properly position the RadioButton",
                stacklevel=2
            )
            self.x = 0
            self.y = 0
            return

        for idx, option in enumerate(self.options):
            rb = CTkRadioButton(
                master=parent,
                text=option,
                variable=self.var,
                value=option,
                text_color=self.text_color,
                font=('Arial', self.font_size),
                command=lambda val=option: self.on_change(val) if self.on_change else None
            )
            rb.place(x=self.x, y=self.y + idx * (self.font_size + 10))
            self.radio_buttons.append(rb)

        if self.id:
            App.instance.ids[self.id] = self

    # Dynamic Update Methods 
    @staticmethod
    def get_value(id):
        widget = App.instance.ids.get(id)
        if widget:
            return widget.var.get()
        else:
            raise ValueError(f"No RadioButton found with id '{id}'.")

    @staticmethod
    def set_value(id, value):
        widget = App.instance.ids.get(id)
        if widget:
            widget.var.set(value)
        else:
            raise ValueError(f"No RadioButton found with id '{id}'.")

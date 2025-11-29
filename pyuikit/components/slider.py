from customtkinter import CTkSlider
from ..app import App
import warnings

class Slider:
    def __init__(
        self,
        x=None,
        y=None,
        id=None,
        width=200,
        height=20,
        min_value=0,
        max_value=100,
        default=None,
        on_change=None,
        fg_color="#2b2b2b",
        progress_color="#3b82f6",
        button_color="#ffffff"
    ):
        self.x = x
        self.y = y
        self.id = id
        self.width = width
        self.height = height
        self.min_value = min_value
        self.max_value = max_value
        self.default = default if default is not None else min_value
        self.on_change = on_change
        self.fg_color = fg_color
        self.progress_color = progress_color
        self.button_color = button_color

        self.slider = None

    def render(self, parent):
        if parent is None:
            raise ValueError("Slider must be a child of a Div.")

        self.slider = CTkSlider(
            master=parent,
            width=self.width,
            height=self.height,
            from_=self.min_value,
            to=self.max_value,
            number_of_steps=self.max_value - self.min_value,
            fg_color=self.fg_color,
            progress_color=self.progress_color,
            button_color=self.button_color,
            command=self.on_change
        )
        self.slider.set(self.default)

        if self.x is not None and self.y is not None:
            self.slider.place(x=self.x, y=self.y)
        else:
            self.slider.place(x=0, y=0)
            warnings.warn(
                f"[PyUIkit] Warning: Slider missing x or y coordinates. Auto-placing at (0, 0).",
                stacklevel=2
            )

        if self.id:
            App.instance.ids[self.id] = self.slider

    # Dynamic Update Methods 
    @staticmethod
    def get_value(id):
        widget = App.instance.ids.get(id)
        if widget:
            return widget.get()
        else:
            raise ValueError(f"No Slider found with id '{id}'.")

    @staticmethod
    def set_value(id, value):
        widget = App.instance.ids.get(id)
        if widget:
            widget.set(value)
        else:
            raise ValueError(f"No Slider found with id '{id}'.")

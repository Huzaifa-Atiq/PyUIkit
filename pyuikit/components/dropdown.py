from customtkinter import CTkComboBox, StringVar
from ..app import App
import warnings

class Dropdown:
    def __init__(
        self,
        options,
        x=None,
        y=None,
        width=140,
        height=32,
        id=None,
        default=None,
        on_change=None,
        text_color="#ffffff",
        bg_color="#2b2b2b",
        hover_color="#3b3b3b"
    ):
        self.options = options
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.id = id
        self.default = default or (options[0] if options else "")
        self.on_change = on_change
        self.text_color = text_color
        self.bg_color = bg_color
        self.hover_color = hover_color

        self.combo = None
        self.var = StringVar(value=self.default)

    def render(self, parent):
        if parent is None:
            raise ValueError("Dropdown must be a child of a Div.")

        self.combo = CTkComboBox(
            master=parent,
            values=self.options,
            variable=self.var,
            width=self.width,
            height=self.height,
            text_color=self.text_color,
            fg_color=self.bg_color,
            button_color=self.bg_color,
            button_hover_color=self.hover_color,
            dropdown_fg_color=self.bg_color,
            dropdown_hover_color=self.hover_color,
            command=self.on_change
        )

        # Absolute positioning
        if self.x is not None and self.y is not None:
            self.combo.place(x=self.x, y=self.y)
        else:
            self.combo.place(x=0, y=0)
            warnings.warn(
                f"[PyUIkit] Warning: Dropdown missing x or y coordinates. Auto-placing at (0, 0).",
                stacklevel=2
            )

        # Register in App instance
        if self.id:
            App.instance.ids[self.id] = self.combo

    # Dynamic Update Methods 
    @staticmethod
    def get_value(id):
        widget = App.instance.ids.get(id)
        if widget:
            return widget.get()
        raise ValueError(f"No Dropdown found with id '{id}'.")

    @staticmethod
    def set_value(id, value):
        widget = App.instance.ids.get(id)
        if widget:
            widget.set(value)
        else:
            raise ValueError(f"No Dropdown found with id '{id}'.")

    @staticmethod
    def set_options(id, new_options):
        widget = App.instance.ids.get(id)
        if widget:
            widget.configure(values=new_options)
        else:
            raise ValueError(f"No Dropdown found with id '{id}'.")

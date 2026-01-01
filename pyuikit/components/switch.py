from customtkinter import CTkSwitch
from ..app import App
import warnings


class Switch:
    def __init__(
        self,
        x=None,
        y=None,
        id=None,
        width=60,
        height=30,
        text="",
        default=False,
        on_change=None,
        bg_color="#2b2b2b",
        progress_color="#3b82f6",
        button_color="#ffffff",
        button_hover_color=None,
        text_color=None,
        font_size=14
    ):
        self.x = x
        self.y = y
        self.id = id
        self.width = width
        self.height = height
        self.text = text
        self.default = default
        self.on_change = on_change
        self.bg_color = bg_color
        self.progress_color = progress_color
        self.button_color = button_color
        self.button_hover_color = button_hover_color
        self.text_color = text_color
        self.font_size = font_size

        self.switch = None

    def render(self, parent):
        if parent is None:
            raise ValueError("Switch must be a child of a Div.")

        # Prepare font tuple dynamically
        font_tuple = ('Arial', self.font_size)

        # Wrap callback so it passes the current state automatically
        callback = (lambda: self.on_change(Switch.get_state(self.id))) if self.on_change else None

        self.switch = CTkSwitch(
            master=parent,
            width=self.width,
            height=self.height,
            text=self.text,
            command=callback,
            bg_color=self.bg_color,
            progress_color=self.progress_color,
            button_color=self.button_color,
            button_hover_color=self.button_hover_color,
            text_color=self.text_color,
            font=font_tuple
        )

        # Set default state
        if self.default:
            self.switch.select()
        else:
            self.switch.deselect()

        # Auto placement like Slider
        if self.x is not None and self.y is not None:
            self.switch.place(x=self.x, y=self.y)
        else:
            self.switch.place(x=0, y=0)
            warnings.warn(
                f"[PyUIkit] Warning: Switch missing x or y coordinates. Auto-placing at (0, 0).",
                stacklevel=2
            )

        # Save ID reference
        if self.id:
            App.instance.ids[self.id] = self.switch

    # -------- Dynamic Methods ----------
    @staticmethod
    def get_state(id):
        widget = App.instance.ids.get(id)
        if widget:
            return widget.get()  # returns 1 or 0
        else:
            raise ValueError(f"No Switch found with id '{id}'.")

    @staticmethod
    def set_state(id, value: bool):
        widget = App.instance.ids.get(id)
        if widget:
            if value:
                widget.select()
            else:
                widget.deselect()
        else:
            raise ValueError(f"No Switch found with id '{id}'.")

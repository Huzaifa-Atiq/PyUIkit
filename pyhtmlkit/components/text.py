from customtkinter import CTkLabel
from ..app import App

class Text:
    def __init__(self, text, x=None, y=None,font='Arial', id=None, color="#000000", font_size=14):
        self.text = text
        self.id = id
        self.color = color
        self.font_size = font_size
        self.x = x
        self.y = y
        self.font = font
        self.label = None

    def render(self, parent):
        if parent is None:
            raise ValueError("Text must be a child of a Div.")

        self.label = CTkLabel(
            master=parent,
            text=self.text,
            text_color=self.color,
            font=(self.font, self.font_size)
        )

        # Use place if x/y provided, else pack
        if self.x is not None and self.y is not None:
            self.label.place(x=self.x, y=self.y)
        else:
            self.label.pack()

        # Register in App instance by ID for dynamic updates
        if self.id:
            App.instance.ids[self.id] = self.label

    # Dynamic update methods via ID
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


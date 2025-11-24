from customtkinter import CTkFrame
from .app import App

class Div:
    def __init__(
        self,
        children=None,         # list of child components
        parent=None,
        bg_color="#FFFFFF",
        padding=0,
        id=None,
        width=100,
        height=100,
        x=None,
        y=None
    ):
        self.children = children or []  # default empty list
        self.parent = parent
        self.bg_color = bg_color
        self.padding = padding
        self.id = id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        # Prevent nested Divs
        for child in self.children:
            if isinstance(child, Div):
                raise ValueError("Cannot include a Div inside another Div. Use other components instead.")

        self.frame = None

        # Auto-render if top-level Div
        if self.parent is None and App.instance is not None:
            self.render(parent=App.instance.main_frame)

    def render(self, parent=None):
        if parent is not None:
            self.parent = parent

        if self.parent is None:
            self.parent = App.instance.main_frame

        # Create the frame
        self.frame = CTkFrame(
            self.parent,
            fg_color=self.bg_color,
            width=self.width,
            height=self.height
        )

        # Prevent the frame from resizing due to children
        self.frame.pack_propagate(False)

        # Use place if x/y provided, else pack
        if self.x is not None and self.y is not None:
            self.frame.place(x=self.x, y=self.y)
        else:
            self.frame.pack(padx=self.padding, pady=self.padding)

        if self.id:
            App.instance.ids[self.id] = self.frame

        # Render all children inside this Div
        for child in self.children:
            if hasattr(child, "render"):
                child.render(parent=self.frame)
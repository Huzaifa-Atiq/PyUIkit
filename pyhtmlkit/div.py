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
        y=None,
        nested=False           # new parameter to indicate nested Div
    ):
        self.children = children or []
        self.parent = parent
        self.bg_color = bg_color
        self.padding = padding
        self.id = id
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.nested = nested
        self.frame = None

        # Auto-render only if not nested and top-level
        if not self.nested and App.instance is not None and self.parent is None:
            self.render(parent=App.instance.main_frame)

    def render(self, parent=None):
        # Update parent if provided
        if parent is not None:
            self.parent = parent

        # Default to App main frame if still None
        if self.parent is None:
            self.parent = App.instance.main_frame

        # Create the frame
        self.frame = CTkFrame(
            self.parent,
            fg_color=self.bg_color,
            width=self.width,
            height=self.height
        )

        # Prevent resizing due to children
        self.frame.pack_propagate(False)

        # Use place if x/y provided, else pack
        if self.x is not None and self.y is not None:
            self.frame.place(x=self.x, y=self.y)
        else:
            self.frame.pack(padx=self.padding, pady=self.padding)

        # Register ID if provided
        if self.id:
            App.instance.ids[self.id] = self.frame

        # Render all children inside this Div
        for child in self.children:
            if hasattr(child, "render"):
                child.render(parent=self.frame)

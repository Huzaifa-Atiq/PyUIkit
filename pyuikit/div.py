from customtkinter import CTkFrame
from .app import App

class Div:
    def __init__(
        self,
        children=None,         # list of child components
        parent=None,
        bg_color="#FFFFFF",
        padding=10,            # increased padding
        id=None,
        width=100,
        height=100,
        x=None,
        y=None,
        corner_radius=0,
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
        self.corner_radius = corner_radius
        self.nested = nested
        self.frame = None

        # Keep track of last child position for stacking
        self._last_x = self.padding
        self._last_y = self.padding

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
            height=self.height,
            corner_radius=self.corner_radius
        )

        # Prevent resizing due to children
        self.frame.pack_propagate(False)

        # Place the Div itself
        if self.x is not None and self.y is not None:
            self.frame.place(x=self.x, y=self.y)
        else:
            self.frame.place(x=0, y=0)  # top-left default if no x/y

        # Register ID if provided
        if self.id:
            App.instance.ids[self.id] = self.frame

        # Render all children inside this Div
        for child in self.children:
            if hasattr(child, "render"):
                # Auto-stack logic
                if getattr(child, "x", None) is None:
                    child.x = self._last_x
                if getattr(child, "y", None) is None:
                    child.y = self._last_y

                # Render child
                child.render(parent=self.frame)

                # Update last_x and last_y for next child
                child_height = getattr(child, "height", None)
                if child_height is None and hasattr(child, "frame"):
                    child.frame.update_idletasks()
                    child_height = child.frame.winfo_height()
                elif child_height is None:
                    child_height = 30  # fallback height

                # Increase vertical spacing using padding
                self._last_x = child.x
                self._last_y = child.y + child_height + self.padding * 1.5  # double padding for nicer gap

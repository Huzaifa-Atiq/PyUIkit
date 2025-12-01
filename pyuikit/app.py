from customtkinter import CTk, CTkFrame
from importlib.resources import files
import os

class App:
    instance = None  # Class variable for singleton
    def __init__(
        self,
        title="PyUIkit App",
        width=600,
        height=400,
        resizable=(True, True),
        bg_color="#FFFFFF",  # default to white
        icon=None,
    ):
        App.instance = self  # <<< set the singleton immediately
        self.root = CTk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(resizable[0], resizable[1])
        

        # Root frame fills the whole window
        self.main_frame = CTkFrame(self.root, fg_color=bg_color)
        self.main_frame.pack(fill="both", expand=True)

        # Optional styling
        try:
            if icon:  # user provided their own icon
                self.root.iconbitmap(icon)
            else:  # use library default
                icon_path = files("pyuikit").joinpath("logo.ico")
                self.root.iconbitmap(str(icon_path))
        except Exception as e:
            print(f"Could not set icon: {e}")


        # Store widgets by ID
        self.ids = {}
    def run(self):
        self.root.mainloop()

Body = App
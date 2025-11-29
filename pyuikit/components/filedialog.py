from customtkinter import CTkEntry, CTkButton, CTkFrame
from tkinter import filedialog, Tk
from ..app import App
import warnings

class FileDialog:
    def __init__(
        self,
        id=None,
        x=None,
        y=None,
        width=200,
        height=30,
        placeholder="Select a file",
        dialog_type="open",
        filetypes=(("All Files", "*.*"),),
        frame_bg="#ffffff",
        entry_bg="#ffffff",
        entry_text_color="#000000",
        button_color="#3b82f6",
        button_text_color="#ffffff"
    ):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.placeholder = placeholder
        self.dialog_type = dialog_type
        self.filetypes = filetypes
        self.frame_bg = frame_bg
        self.entry_bg = entry_bg
        self.entry_text_color = entry_text_color
        self.button_color = button_color
        self.button_text_color = button_text_color
        self.path = ""
        self.entry = None
        self.button = None
        self.frame = None

    def render(self, parent):
        if parent is None:
            raise ValueError("FileDialog must be a child of a Div.")

        self.frame = CTkFrame(
            parent,
            width=self.width,
            height=self.height,
            fg_color=self.frame_bg
        )
        self.frame.pack_propagate(False)

        if self.x is not None and self.y is not None:
            self.frame.place(x=self.x, y=self.y)
        else:
            self.frame.place(x=0, y=0)
            warnings.warn(
                f"[PyUIkit] Warning: FileDialog missing x or y coordinates. Auto-placing at (0, 0).",
                stacklevel=2
            )

        self.entry = CTkEntry(
            self.frame,
            width=self.width - 60,
            placeholder_text=self.placeholder,
            fg_color=self.entry_bg,
            text_color=self.entry_text_color
        )
        self.entry.pack(side="left", fill="x", expand=True)

        self.button = CTkButton(
            self.frame,
            text="Browse",
            width=60,
            fg_color=self.button_color,
            text_color=self.button_text_color,
            command=self.open_dialog
        )
        self.button.pack(side="right")

        if self.id:
            App.instance.ids[self.id] = self

    def open_dialog(self):
        root = Tk()
        root.withdraw()  # hide main window
        if self.dialog_type == "open":
            self.path = filedialog.askopenfilename(filetypes=self.filetypes)
        elif self.dialog_type == "save":
            self.path = filedialog.asksaveasfilename(filetypes=self.filetypes)
        root.destroy()
        self.entry.delete(0, "end")
        self.entry.insert(0, self.path)

    # Dynamic Update Methods 
    @staticmethod
    def get_file(id):
        widget = App.instance.ids.get(id)
        if widget is None:
            raise ValueError(f"No FileDialog found with id '{id}'.")
        return widget.path

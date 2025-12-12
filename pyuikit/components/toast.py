from customtkinter import CTkFrame, CTkLabel, CTkButton
from ..app import App
import threading


class Toast:
    def __init__(
        self,
        text="",
        duration=3,
        x=None,
        y=None,
        position="top-right",
        width=220,
        height=50,
        bg_color="#333333",
        text_color="#ffffff",
        font_name="Arial",
        font_size=14,
        show_close=True,
        id=None
    ):
        self.text = text
        self.duration = duration
        self.x = x
        self.y = y
        self.position = position
        self.width = width
        self.height = height
        self.fg_color = bg_color
        self.text_color = text_color
        self.font_name = font_name
        self.font_size = font_size
        self.show_close = show_close
        self.id = id

        self.frame = None
        self.label = None

        # Animation state
        self.start_x = None
        self.final_x = None
        self.final_y = None

    # SLIDE IN ANIMATION
    def slide_in(self):
        if not self.frame:
            return

        current_x = self.frame.winfo_x()

        if current_x > self.final_x:
            self.frame.place(x=current_x - 14, y=self.final_y)
            self.frame.after(10, self.slide_in)
        else:
            self.frame.place(x=self.final_x, y=self.final_y)

    # SLIDE OUT ANIMATION
    def slide_out(self):
        if not self.frame:
            return

        current_x = self.frame.winfo_x()

        if current_x < self.final_x + 300:
            self.frame.place(x=current_x + 14, y=self.final_y)
            self.frame.after(10, self.slide_out)
        else:
            self.destroy()

    # RENDER TOAST
    def render(self, parent=None):
        if parent is None:
            parent = App.instance.root

        # ---------------- Create Frame ----------------
        self.frame = CTkFrame(
            master=parent,
            width=self.width,
            height=self.height,
            fg_color=self.fg_color,
            corner_radius=0,
        )
        self.frame.pack_propagate(False)

        # Text label
        self.label = CTkLabel(
            master=self.frame,
            text=self.text,
            text_color=self.text_color,
            font=(self.font_name, self.font_size)
        )
        self.label.pack(side="left", padx=15, pady=10)

        # Close button
        if self.show_close:
            close_btn = CTkButton(
                master=self.frame,
                text="✕",
                width=28,
                height=28,
                fg_color="#555555",
                hover_color="#444444",
                command=self.destroy
            )
            close_btn.pack(side="right", padx=10)

        parent.update_idletasks()
        w = parent.winfo_width()
        h = parent.winfo_height()

        # ---------------- Positioning ----------------
        if self.x is not None and self.y is not None:
            self.final_x = self.x
            self.final_y = self.y
        else:
            if self.position == "top-right":
                self.final_x = w - self.width - 20
                self.final_y = 20
            elif self.position == "top-left":
                self.final_x = 20
                self.final_y = 20
            elif self.position == "bottom-right":
                self.final_x = w - self.width - 20
                self.final_y = h - self.height - 20
            elif self.position == "bottom-left":
                self.final_x = 20
                self.final_y = h - self.height - 20

        # Start off-screen (right side)
        self.start_x = self.final_x + 300
        self.frame.place(x=self.start_x, y=self.final_y)

        # Animate slide-in after a short delay
        parent.after(10, self.slide_in)

        if self.id:
            App.instance.ids[self.id] = self.frame

        # Auto hide
        threading.Timer(self.duration, self.slide_out).start()


    # SHOW
    def show(self):
        self.render()


    # DESTROY
    def destroy(self):
        if self.frame:
            self.frame.destroy()
            self.frame = None

from pyuikit import Body, Div
from pyuikit.components import Button, Toast

app = Body(title="Multiple Toasts", width=600, height=400)

def toast_success():
    Toast(
        text="✅ Success!",
        bg_color="#10b981",
        text_color="white",
        position="top-right",
        duration=3
    ).show()

def toast_warning():
    Toast(
        text="⚠️ Warning!",
        bg_color="#facc15",
        text_color="#000000",
        position="bottom-left",
        duration=4
    ).show()

def toast_custom_xy():
    Toast(
        text="Custom Position!",
        bg_color="#0066aa",
        text_color="white",
        duration=4,
        x=150,
        y=120,
        width=240,
        height=50,
        show_close=True
    ).show()

Div(
    width=500,
    height=400,
    children=[
        Button(text="Success Toast", on_click=toast_success),
        Button(text="Warning Toast", on_click=toast_warning),
        Button(text="Custom Position Toast", on_click=toast_custom_xy),
    ]
)

app.run()
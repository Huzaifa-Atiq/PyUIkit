from pyuikit import *

def test_input_methods():
    # Get initial text
    name = Input.get_input_text("single_input")
    print("Initial single-line input:", name)

    # Set text dynamically
    Input.set_input_text("single_input", "Alice")
    name = Input.get_input_text("single_input")
    print("After set_input_text:", name)

    # Change text color
    Input.set_input_color("single_input", "red")

    # Change background color
    Input.set_input_bg_color("single_input", "lightblue")

    # Test multiline input
    multi_text = Input.get_input_text("multi_input")
    print("Initial multiline input:", multi_text)

    Input.set_input_text("multi_input", "This is\nmulti-line text")
    multi_text = Input.get_input_text("multi_input")
    print("After set_input_text:", multi_text)

    Input.set_input_color("multi_input", "green")
    Input.set_input_bg_color("multi_input", "lightyellow")

def greet():
    # Use the single-line input for greeting
    name = Input.get_input_text("single_input")
    Text.set_text(id="greeting", new_text=f"Hello, {name}!")
    # Also change input bg to show dynamic update
    Input.set_input_bg_color("single_input", "pink")

# Create the app
app = Body(width=500, height=400, bg_color="white")

# Add UI components
Div(
    width=480,
    height=400,
    children=[
        Text(text="Single-line input test:"),
        Input(placeholder="Name", id="single_input", height=40, width=200, font_size=16),
        Text(text="Multiline input test:"),
        Input(placeholder="Type something...", id="multi_input", height=100, width=300, font_size=14, multiline=True),
        Button(text="Greet", on_click=greet),
        Button(text="Run Input Tests", on_click=test_input_methods),
        Text(text="", id="greeting")
    ]
)

# Run the app
app.run()

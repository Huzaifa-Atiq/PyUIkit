# --- 1️⃣ Test top-level import ---
def test_top_level_import():
    import pyuikit


# --- 2️⃣ Test components import ---
def test_components_importable():
    from pyuikit import Body, Div
    from pyuikit.components import Text, Button, Input

    # Simple assertions to make sure they exist
    assert Body is not None
    assert Div is not None
    assert Text is not None
    assert Button is not None
    assert Input is not None


# --- 3️⃣ Test container creation ---
def test_body_creation():
    from pyuikit import Body

    app = Body(width=400, height=300, bg_color='white')
    assert app.width == 400
    assert app.height == 300
    assert app.bg_color == 'white'


def test_div_creation():
    from pyuikit import Div
    from pyuikit.components import Text, Input, Button

    btn = Button(text='Click me')
    div = Div(
        width=360,
        height=250,
        children=[
            Text(text='Enter your name:'),
            Input(placeholder='Name', id='name_input'),
            btn,
        ]
    )

    assert div.width == 360
    assert div.height == 250
    assert len(div.children) == 3
    assert div.children[2] is btn


# --- 4️⃣ Test Input/Text/Button logic (simulate greet function) ---
def test_greet_logic():
    from pyuikit.components import Text, Input, Button

    # Mock the input
    Input._mock_inputs = {"name_input": "Alice"}  # simulate user input
    greeting_text = Text(text='', id='greeting')

    def greet():
        name = Input.get_input(id='name_input')
        Text.set_text(id='greeting', new_text=f'Hello, {name}!')

    greet()  # call the function

    # Check if greeting text updated correctly
    assert Text.get_text(id='greeting') == "Hello, Alice!"


# --- 5️⃣ Optional: Test button on_click triggers greet ---
def test_button_on_click_triggers_greet():
    from pyuikit.components import Text, Input, Button

    Input._mock_inputs = {"name_input": "Bob"}
    Text.set_text(id='greeting', new_text='')

    def greet():
        name = Input.get_input(id='name_input')
        Text.set_text(id='greeting', new_text=f'Hello, {name}!')

    btn = Button(text='Greet', on_click=greet)
    btn._trigger_click()  # simulate click

    assert Text.get_text(id='greeting') == "Hello, Bob!"

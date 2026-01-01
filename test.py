from pyuikit import *

def greet():
    name = Input.get_input(id='name_input')
    Text.set_text(id='greeting', new_text=f'Hello, {name}!')

app = Body(width=400, height=300, bg_color='white')

Div(
    width=360,
    height=250,
    children=[
        Text(text='Enter your name:'),
        Input(placeholder='Name',id='name_input',height=40,width=40,font_size=20),
        Button(text='Greet',on_click=greet),
        Text(text='', id='greeting')
    ]
)

app.run()
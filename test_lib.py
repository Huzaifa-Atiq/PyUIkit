from pyuikit import Body, Div
from pyuikit.components import Text, Input, Button

def calc():
    height = float(Input.get_input(id='height'))
    weight = float(Input.get_input(id='weight'))
    bmi = weight / (height ** 2)
    Text.set_text(id='output', new_text=f'Your BMI is {bmi:.2f}')

app = Body(width=400, height=500, bg_color='white')

Div(
    x=20,
    y=20,
    width=360,
    height=450,
    bg_color='#f0f0f0',
    padding=10,
    children=[
        Text(text='BMI Calculator', font_size=30, x=10, y=10),
        Input(placeholder='Enter height (m)', id='height', x=10, y=60),
        Input(placeholder='Enter weight (kg)', id='weight', x=10, y=100),
        Button(text='Calculate', color='green', x=10, y=140, on_click=calc),
        Text(text='', font_size=25, id='output', x=10, y=200)
    ],
    id='mainDiv'
)

app.run()

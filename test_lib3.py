# test3_mixed_nested.py
from pyuikit import Body, Div
from pyuikit.components import Text, Input, Button

def calc():
    height = float(Input.get_input(id='height'))
    weight = float(Input.get_input(id='weight'))
    bmi = weight / (height * height)
    Text.set_text(id='output', new_text=f'Your BMI is {bmi:.2f}')

app = Body(width=500, height=600, bg_color='white')

Div(
    width=480,
    height=580,
    padding=20,
    children=[
        Text(text='Your BMI calculator', font_size=30, x=10, y=10),
        Div(
            width=450,
            height=300,
            bg_color='#f0f0f0',
            padding=15,
            nested=True,
            children=[
                Input(placeholder='Enter your height(meters)', id='height'),  # auto-stack
                Input(placeholder='Enter your weight(kg)', id='weight'),       # auto-stack
                Button(text='Submit', color='green', x=10, y=90, on_click=calc),
                Text(text='', font_size=25, id='output')                      # auto-stack
            ]
        )
    ]
)

app.run()

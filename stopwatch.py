from pyuikit import Body,Div
from pyuikit.components import Text,Input,Button

def calc():
    height = float(Input.get_input(id='height'))
    weight = float(Input.get_input(id='weight'))
    
    bmi = weight / (height ** 2)  # square the height here
    Text.set_text(id='output',new_text=f'Your bmi is {bmi}')


app = Body(width=400,height=500,bg_color='white')

Div(
    height=500,
    width=400,
    children=[
        Text(text='Your BMI calculator',font_size=30),

        Input(placeholder='Enter your height(meters)',id='height'),
        Input(placeholder='Enter your weight(kg)',id='weight'),

        Button(text='Submit',color='green',on_click=calc),

        Text(text='22',font_size=25,id='output')
    ]
)




app.run()
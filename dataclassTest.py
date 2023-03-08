from dataclasses import dataclass, asdict
from dataclass_csv import DataclassReader
import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc, Input, Output

#Obviously, DataFrame.read_csv is the better option

@dataclass
class Student():
    key: int
    name: str
    age: int
    grade: str = None
    score: int = None
    gpa: float = None

app = Dash()

app.layout = html.Div([
                    html.H4("Scores"),
                    html.P("Box graph of scores"),
                    dcc.RadioItems(
                                    id = 'info-options',
                                    options = ['Scores', 'GPA'],
                                    value = 'Scores'
                                ),
                    dcc.Dropdown(
                                    id = 'color-options',
                                    options = ['Inferno', 'Tealgrn', 'Oranges', 'Rainbow'],
                                    value = 'Inferno'
                                ),
                    html.Div(id = 'output')
                ])

@app.callback(
                Output("output", "children"),
                [Input("color-options", "value"), Input('info-options', "value")]
            )
def render_graph(color_option, info_option):

    students = []
    with open("Students.csv") as users_csv:
        reader = DataclassReader(users_csv, Student)
        for row in reader:
            students.append(row)

    keys = []
    names = []
    age = []
    scores = []
    gpa = []

    student_dict = {}

    for row in students:
        keys.append(row.key)
        names.append(row.name)
        age.append(row.age)
        scores.append(row.score)
        gpa.append(row.gpa)
    
    student_dict["keys"] = keys
    student_dict["names"] = names
    student_dict["age"] = age
    student_dict["scores"] = scores
    student_dict["gpa"] = gpa
    
    df = pd.DataFrame(student_dict)
    if info_option == "Scores":
        fig = px.bar(df, x = "names", y = "scores", color = 'scores', color_continuous_scale = color_option, title = f"Graph with color {color_option}")
    elif info_option == "GPA":
        fig = px.bar(df, x = "names", y = "gpa", color = 'gpa', color_continuous_scale = color_option, title = f"Graph with color {color_option}")
    return dcc.Graph(figure = fig)
    

app.run_server(debug = True)



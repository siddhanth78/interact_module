from dataclasses import dataclass, asdict
from dataclass_csv import DataclassReader
import plotly.express as px
import pandas as pd

@dataclass
class Student():
    key: int
    name: str
    age: int
    grade: str = None
    score: int = None

students = []
with open("Students.csv") as users_csv:
    reader = DataclassReader(users_csv, Student)
    for row in reader:
        students.append(row)

keys = []
names = []
age = []
scores = []

student_dict = {}

for row in students:
    keys.append(row.key)
    names.append(row.name)
    age.append(row.age)
    scores.append(row.score)
    
student_dict["keys"] = keys
student_dict["names"] = names
student_dict["age"] = age
student_dict["scores"] = scores
    
df = pd.DataFrame(student_dict)

fig = px.bar(df, x = "names", y = "scores", template = "plotly_dark", color = "scores")
fig.show()



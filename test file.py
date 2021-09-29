import pandas as pd
import numpy as np
import plotly.express as px

xvals = np.arange(-10,10,0.01)

df = pd.DataFrame({
                    "x":xvals,
                    "sin x":np.sin(xvals)
                })
                
fig = px.line(df, x = "x", y = "sin x", template = "plotly_dark", title = "Sin x graph")

fig.update_xaxes(title = "X")
fig.update_yaxes(title = "Y")

fig.update_layout(legend = dict(title = None, orientation = "h", yanchor = "bottom", y = 1, xanchor = "center", x=0.5),
                    title = dict(yanchor = "top", y = 0.95, xanchor = "center", x=0.5))

fig.show()
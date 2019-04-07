import json
import pandas as pd

from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Category20
from bokeh.plotting import figure
from bokeh.layouts import column

JSON_FILE = 'e-contacts.json'

with open(JSON_FILE) as f:
    data = json.loads(f.read())

output_file("e-contacts.html")

figures = []
for country_code, hist in data.items():
    data = pd.Series(hist).reset_index(name='value').rename(columns={'index': 'type'})
    data['color'] = Category20[len(hist)]

    source = ColumnDataSource(dict(x=data['type'], top=data['value'], color=data['color']))

    p = figure(
        x_range=data['type'],
        plot_height=400,
        plot_width=1200,
        tooltips="@x: @top",
        title=country_code
    )
    p.vbar(x='x', top='top', bottom=0, width=0.8, fill_color='color', source=source)

    figures.append(p)

show(column(*figures))

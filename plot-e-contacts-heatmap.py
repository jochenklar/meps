import json
import pandas as pd

from bokeh.io import show, output_file
from bokeh.models import LinearColorMapper, BasicTicker, PrintfTickFormatter, ColorBar
from bokeh.palettes import Inferno
from bokeh.plotting import figure

JSON_FILE = 'e-contacts.json'

with open(JSON_FILE) as f:
    data = json.loads(f.read())

output_file("e-contacts.html")

keys = list(data['*'].keys())[1:]
countries = list(data.keys())[1:]

matrix = []
for key, hist in data.items():
    total = list(hist.values())[0]
    values = list(hist.values())[1:]
    matrix.append([key] + [100 * value / total for value in values])

df = pd.DataFrame(matrix, columns=['Country'] + keys)
df = df.set_index('Country')
df.columns.name = 'Type'

df_stack = pd.DataFrame(df.stack(), columns=['value']).reset_index()

colors = Inferno[10]
mapper = LinearColorMapper(palette=colors, low=df_stack.value.min(), high=df_stack.value.max())

p = figure(
    title='E Contacts',
    x_range=keys, y_range=countries,
    plot_width=1200, plot_height=600,
    tooltips=[('Field', '@Type @Country'), ('value', '@value%')]
)

p.rect(x='Type', y='Country', width=1, height=1,
       source=df_stack,
       fill_color={'field': 'value', 'transform': mapper},
       line_color=None)

color_bar = ColorBar(color_mapper=mapper, major_label_text_font_size="5pt",
                     ticker=BasicTicker(desired_num_ticks=len(colors)),
                     formatter=PrintfTickFormatter(format="%d%%"),
                     label_standoff=6, border_line_color=None, location=(0, 0))

p.add_layout(color_bar, 'right')

show(p)

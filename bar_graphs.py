from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.palettes import Spectral3
from bokeh.transform import factor_cmap
import random

fruits = ["Apples", "Pears", "Kiwis", "Plums", "Bananas", "Strawberries"]
years = ["2020", "2021", "2022"]

data_2020 = random.sample(range(1, 10), len(fruits))
data_2021 = random.sample(range(1, 10), len(fruits))
data_2022 = random.sample(range(1, 10), len(fruits))

data = {"fruits": fruits, "2020": data_2020, "2021": data_2021, "2022": data_2022}

fruit_year = [(fruit, year) for fruit in fruits for year in years]
counts = sum(zip(data["2020"], data["2021"], data["2022"]), ())

df = dict(fruit_year = fruit_year, counts = counts)
source = ColumnDataSource(data=df)

p = figure(x_range = FactorRange(*fruit_year), height = 250, title = "Fruit Counts by Year", toolbar_location = None, tools = "")

p.vbar(x = "fruit_year", top = "counts", width = 0.9, source = source, fill_color = factor_cmap("fruit_year", palette = Spectral3, factors = years, start = 1, end = 2))

p.y_range.start = 0

# range padding
p.x_range.factor_padding = 0.1

# tilt
p.xaxis.major_label_orientation = 1

# gets rid of grid line color
p.xgrid.grid_line_color = None

show(p)
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, FactorRange, Range1d, HoverTool
from bokeh.palettes import Spectral3
from bokeh.transform import factor_cmap
import random

# data
x = [5]
y = [2]

# j = x/y

# tools
tools = "box_zoom, undo, crosshair, lasso_select"

# create figure
p = figure(title = "Test Scatter Plot", x_axis_label = "x", y_axis_label = "y", tools = tools)

# add hover tool to figure
p.add_tools(
    HoverTool(
        tooltips = [("test", "@x"),
                    ("test", "test")]
    )
)

# scatter plot data
p.scatter(x, y, alpha = 0.5)

p.x_range = Range1d(2, 14)
p.y_range = Range1d(0, 5)
show(p)
from bokeh.plotting import figure, output_file, show

x = [1,2,3,4,5]
y = [4,6,7,8,2]

output_file("index.html")

# add plot
p = figure (
    title = "Simple example",
    x_axis_label = "X Axis",
    y_axis_label = "Y Axis"
)

# render glyph
p.line(x, y, line_width=2)

# show results
show(p)
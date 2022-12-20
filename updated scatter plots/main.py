from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool, Range1d

# data input
source = ColumnDataSource(data = dict(
    m_e_stdrows_mc = [1,2,3,4,5],
    m_e_stdrows_row = [9,8,7,6,5]
))

# instantiate figure properties
tools = "box_zoom, undo, crosshair, lasso_select"
p = figure(tools=tools,title='Row-by-Row Overscan: ITL', x_axis_label='Read Noise [ADU]',y_axis_label='StdDev of Row Means [ADU]') 

# add hovertool
p.add_tools(
    HoverTool(
        tooltips = [('x', "@m_e_stdrows_mc"),
                    ('y', '@m_e_stdrows_row')]
    )
)

# draw scatter plot
p.scatter("m_e_stdrows_mc", "m_e_stdrows_row", alpha=0.5, source = source)

# range values
p.x_range = Range1d(0, 15)
p.y_range = Range1d(0, 15)

# display plot
show(p)
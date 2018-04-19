from bokeh.plotting import figure, output_file, show
from motion_detect import dataframe_motion
from bokeh.models import HoverTool, ColumnDataSource

dataframe_motion["Entry_string"] = dataframe_motion["Entry"].dt.strftime("%Y-%m-%d %H:%M:%S")
dataframe_motion["Exit_string"] = dataframe_motion["Exit"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds_time = ColumnDataSource(dataframe_motion)

plot = figure(height = 150, width = 400, x_axis_type = "datetime", responsive = True)

plot.title.text = "Motion Detection plot"
plot.xaxis.axis_label = "Time of Detection"
plot.yaxis.minor_tick_line_color = None
plot.ygrid[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips = [("Entered at","@Entry_string"), ("Exited at", "@Exit_string")])
plot.add_tools(hover)

plot.quad(top = 1, bottom = 0, left = "Entry", right = "Exit", color = "green", alpha = 0.8, source = cds_time)

output_file("Plot.html")
show(plot)

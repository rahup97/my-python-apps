from pandas_datareader import data
from datetime import datetime as dt
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN

start_date = dt(2016, 3, 1)
end_date = dt(2016, 3, 20)

dframe = data.DataReader(name = "GOOG", data_source = "google",start = start_date, end = end_date)

plot = figure(x_axis_type = 'datetime', width = 1000, height = 400, responsive = True)
plot.title.text = "Stock CandleStick"
plot.grid.grid_line_alpha = 0.35

#making the plot with different colors - red for when close price < open price and green for the other possibility
def price_status(closep, openp):
    if closep > openp:
        value = "Increase"
    elif closep < openp:
        value = "Decrease"
    else:
        value = "Equal"
    return value

dframe["Status"] = [price_status(c, o) for c, o in zip(dframe.Close, dframe.Open)]
dframe["Height"] = abs(dframe.Open - dframe.Close)
dframe["Middle"] = (dframe.Open + dframe.Close)/2
dframe.to_csv("dataframe.csv")


hour12 = 12*60*60*1000

plot.segment(x0=dframe.index[dframe.Status == "Increase"], y0=dframe.Low[dframe.Status == "Increase"], x1=dframe.index[dframe.Status == "Increase"],
          y1=dframe.High[dframe.Status == "Increase"], color="black", line_width=3)
plot.segment(x0=dframe.index[dframe.Status == "Decrease"], y0=dframe.Low[dframe.Status == "Decrease"], x1=dframe.index[dframe.Status == "Decrease"],
          y1=dframe.High[dframe.Status == "Decrease"], color="black", line_width=3)

plot.rect(dframe.index[dframe.Status == "Increase"], dframe.Middle[dframe.Status == "Increase"], hour12, height = dframe.Height[dframe.Status == "Increase"], color = "darkcyan", line_color = "black")
plot.rect(dframe.index[dframe.Status == "Decrease"], dframe.Middle[dframe.Status == "Decrease"], hour12, height = dframe.Height[dframe.Status == "Decrease"], color = "red", line_color = "black")

components(plot)
cdn_js = CDN.js_files
cdn_css = CDN.css_files
#output_file("Plot1.html")
#show(plot)

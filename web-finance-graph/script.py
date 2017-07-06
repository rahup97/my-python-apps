from pandas_datareader import data
from datetime import datetime as dt
from bokeh.plotting import figure, show, output_file

start_date = dt(2016, 3, 1)
end_date = dt(2016, 3, 10)

dframe = data.DataReader(name = "GOOG", data_source = "google",start = start_date, end = end_date)

dframe.to_csv("dataframe.csv")

plot = figure(x_axis_type = 'datetime', width = 1000, height = 400)
plot.title.text = "Stock CandleStick"

#making the plot with different colors - red for when close price < open price and green for the other possibility
hour12 = 12*60*60*1000

plot.rect(dframe.index[dframe.Close > dframe.Open], (dframe.Close + dframe.Open)/2, hour12, height = abs(dframe.Close - dframe.Open), color = "green")
plot.rect(dframe.index[dframe.Close < dframe.Open], (dframe.Close + dframe.Open)/2, hour12, height = abs(dframe.Open - dframe.Close), color = "red")
#plot.segment(x0 = dframe.index, y0 = dframe.Low, x1 = dframe.index,
         # y1 = dframe.High, color = "black", line_width = 2)

output_file("Plot1.html")
show(plot)

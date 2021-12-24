import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df = pd.read_csv(r"mediumData.csv")
data = df["reading_time"].tolist()
mean = statistics.mean(data)
total_stdev = statistics.stdev(data)

def  random_sample(counter):
    dataSet = []
    for i in range(0,counter):
        index = random.randint(0,len(data)-1)
        value = data[index]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

mean_list = []
for i in range(0,1000):
    set = random_sample(30)
    mean_list.append(set)
sample_mean = statistics.mean(mean_list)
sample_stdev = statistics.stdev(mean_list)

first_stdev_start,first_stdev_end = sample_mean-sample_stdev, sample_mean+sample_stdev
second_stdev_start,second_stdev_end = sample_mean-(2*sample_stdev), sample_mean+(2*sample_stdev)
third_stdev_start,third_stdev_end = sample_mean-(3*sample_stdev), sample_mean+(3*sample_stdev)

graph = ff.create_distplot([mean_list],["Sample Means"],show_hist = False)
graph.add_trace(go.Scatter(x=[sample_mean,sample_mean],y=[0,0.77],mode="lines",name="mean"))
graph.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.77],mode="lines",name="First Standard Deviation Start"))
graph.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.77],mode="lines",name="First Standard Deviation End"))
graph.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.77],mode="lines",name="Second Standard Deviation Start"))
graph.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.77],mode="lines",name="Second Standard Deviation End"))
graph.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.77],mode="lines",name="Third Standard Deviation Start"))
graph.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.77],mode="lines",name="Third Standard Deviation End"))
graph.show()

z_score = sample_mean-mean/total_stdev
print(z_score)

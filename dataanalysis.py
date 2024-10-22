# import the necessary libraries
import pandas as pd
import numpy as np
import plotly.express as px


# read and build the dataframe for iris
df = pd.read_csv("iris.csv")


# plot the scatter for sepal_length and petal_length with species as hue

fig_scatter = px.scatter(data_frame=df, x="sepal_width",
                         y="petal_width", color="species")

# plot the bar plot
fig_hist = px.histogram(data_frame=df, x="sepal_width", color="species")

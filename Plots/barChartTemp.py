import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Filtering US Cases
#filtered_df = df[df['Date'] == '']

# Removing empty spaces from State column to avoid errors
filtered_df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of number of cases group by State Column
new_df = filtered_df.groupby(['date'])['actual_mean_temp'].sum().reset_index()

# Sorting values and select first 20 states
new_df = new_df.sort_values(by='date').head(365)

# Preparing data
data = [go.Bar(x=new_df['date'], y=new_df['actual_mean_temp'])]

# Preparing layout
layout = go.Layout(title='Different Weather Temperature between 2014 & 2015 ', xaxis_title="Date",
                   yaxis_title="Average Temperatures")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barchartTemp.html')

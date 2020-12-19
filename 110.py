import statistics
import random
import pandas as pd
import plotly.figure_factory as pf

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

pf.create_distplot([data], ["reading_time"], show_hist=False).show()
print("Population Mean: " + str(statistics.mean(data)))

set_of_means = []
for i in range(100):
    temp_arr = []
    for i in range(30):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        temp_arr.append(value)
    set_of_means.append(statistics.mean(temp_arr))
    
pf.create_distplot([set_of_means], ["reading_time"], show_hist=False).show()
print("Sampling Mean: " + str(statistics.mean(set_of_means)))

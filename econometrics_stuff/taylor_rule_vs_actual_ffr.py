from fredapi import Fred # import the fred api
import matplotlib.pyplot as plt # import the matplotlib library
import pandas as pd # import pandas 
import numpy as np # import numpy

# connect the fred api
# you will need your own key for this
fred = Fred(api_key="Your API Key Here")

# get the unemployment rate (you can find these series names on the FRED website)
ur = fred.get_series('UNRATE', observation_start="01/01/2010", 
                     observation_end="06/01/2024")

# get the natural rate of unemployment
nairu = fred.get_series('NROU', observation_start="01/01/2010", 
                        observation_end="06/01/2024")

# get the fed funds rate
ffr = fred.get_series('FEDFUNDS', observation_start="01/01/2010", 
                      observation_end="06/01/2024")

# get the cpi
quart_inf = fred.get_series('CPIAUCSL', observation_start="01/01/2010", 
                                 observation_end="06/01/2024", frequency = "q", 
                                 aggregation_method = "eop", units = 'pch')

# make the values a dataframe
ur = pd.DataFrame({"time": ur.index, "rate": ur.values})
nairu = pd.DataFrame({"time": nairu.index, "rate": nairu.values})
ffr = pd.DataFrame({"time": ffr.index, "rate": ffr.values})
quart_inf = pd.DataFrame({"time": quart_inf.index, "rate": quart_inf.values})

# prin thte length of each series
print("length of ur series: ", len(ur))
print("length of nairu series: ", len(nairu))
print("length of ffr series: ", len(ffr))
print("length of quart_inf series: ", len(quart_inf))

# this makes sure that they are all the same length
nairu = nairu.loc[nairu.index.repeat(3)].reset_index(drop=True)
quart_inf = quart_inf.loc[quart_inf.index.repeat(3)].reset_index(drop=True)

"""
this is so you can adjust depending on the quarters
nairu = nairu.iloc[:-2] 
quart_inf = quart_inf.iloc[:-2]

"""

# define the taylor formula
def taylor_rule(ffr: float, quart_inf: float, ur: float, nairu: float):
    annualized_inf = 4 * quart_inf
    implied_ffr = 0.8 * ffr + 0.2 * (1.5 * annualized_inf - 0.5 * (ur - nairu))
    return implied_ffr

# compute the ffr from the taylor rule for all periods
implied_ffr = []

for i in range(len(ffr)):
    implied_ffr.append(taylor_rule(ffr['rate'].iloc[i], quart_inf['rate'].iloc[i], 
                                   ur['rate'].iloc[i], nairu['rate'].iloc[i]))
print(implied_ffr[0:5])

# plot the results
plt.plot(ffr.time, ffr.rate, label = 'Actual FFR')
plt.plot(ffr.time, implied_ffr, label = 'Taylor Rule Implied FFR')
plt.title("Actual FFR vs Implied FFR from Taylor Rule")
plt.ylabel("Percent")
plt.xlabel("Month")
plt.legend()
plt.show()
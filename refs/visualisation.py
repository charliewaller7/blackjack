
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
import pandas as pd


import plotly.offline as pyo
import plotly.graph_objs as go

import cufflinks as cf
# For Notebooks
pyo.init_notebook_mode(connected=True)
# For offline use
cf.go_offline()

def plot(df, col_list='all', notebook=False):
    
    if col_list == 'all':
        col_list = list(df.columns)
    
    fig = go.Figure()

    data = []
    for col in col_list:
        fig.add_trace(go.Scatter(x=list(df.index), y=df[col].tolist(),
                      mode='lines+markers',
                      name=col))

        # Create traces
        trace = go.Scatter(
            x=list(df.index),
            y=df[col].tolist(),
            mode='lines',
            name=col
        )

        data.append(trace)
    
    if notebook:
        pyo.iplot(data)
    else:
        pyo.plot(data)


def metric_cum_balance_by_player(table):
    val_dict = dict()
    for player in table.players:
        vals = [h.hand_value for h in player.history]
        # Take subtotal when splitting
        vals = [sum(item) for item in vals]
        
        # Create cumulative values
        cum_vals = [] 
        prev_val = 0
        for v in vals:
            cum_vals.append(v+prev_val)
            prev_val = v+prev_val
        val_dict[player.name] = cum_vals
        
    return pd.DataFrame(val_dict)

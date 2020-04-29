# Heatmap representation of Death toll in top 5 countries affected from COVID-19, from 24th,April,2020 to 28th,April,2020 #

import plotly.express as px
data=[[367, 378, 288, 331, 301], [768, 813, 413, 360, 586], [420, 415, 260, 333, 382], [389, 369, 242, 437, 367], [1957, 2065, 1156, 1384, 2470]]
fig = px.imshow(data,
                labels=dict(x="Date", y="Country", color="Deaths"),
                x=['24-Apr-20', '25-Apr-20', '26-Apr-20', '27-Apr-20', '28-Apr-20'],
                y=['Spain', 'United Kingdom', 'Italy', 'France', 'United States']
               )
fig.update_xaxes(side="bottom")
fig.show()
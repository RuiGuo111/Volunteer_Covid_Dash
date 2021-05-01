# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 01:19:25 2021

@author: GUORUI
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import dash_table


stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# pandas dataframe to html table
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

app = dash.Dash(__name__, external_stylesheets=stylesheet)

df = pd.read_pickle('covid_studies.pkl')


app.layout = html.Div([
    html.H1('Where Recruit Volunteers for COVID Clinical Trials?', style={'textAlign': 'center'}),
    html.H3('User Guide of this Dashborad:',style = {'textAlign':'left'}),
    html.P('This dashboard summarizes and re-categorizes the information of on-going \
           clinical trials related to COVID-19 treatment in United States.It provides an \
               easy-to-access pathway for the volunteers to search COVID-19 clinical trial \
                   recruiting information filtered by location, gender and clinical phase and \
                       finally help them to make the best decision. All the data source from:'),
    html.A('Click here for the website',href = " https://clinicaltrials.gov/",
           target = "_blank"),
    html.P('The pie chart displays the percentage and number of clinical trails related \
           to Covid diseases by city in certain criterias. Detailed information \
               about the recruiting status, study topic, reference ID, location and authority \
                   is shown in the following table.'),
    html.Br(),
    html.Div([
             html.Label(["Choose the State:"]),
             dcc.Dropdown(
                 id='states_dropdown', 
                 options=[{'value': x, 'label': x} 
                   for x in df.State.sort_values().unique()],
                 value='Massachusetts',
                 multi = False,
                 clearable=False,
                 style = {"width":"50%"}
                         ),
             html.Br(),
             html.Label(["Choose the Status:"]),
             dcc.Dropdown(
                 id='status_dropdown', 
                 options=[{'value': y, 'label': y} 
                   for y in df.Status.sort_values().unique()],
                 value='Potential Recruiting',
                 multi = False,
                 clearable=False,
                 style = {"width":"50%"}
                         ),
            html.Br(),
            html.Label(["Choose the Gender:"]),
            dcc.RadioItems(
                           id = 'gender_radioItems',
                           options=[
                                    {'label': 'All', 'value': 'All'},
                                    {'label': 'Female Only', 'value': 'Famale Only'},
                                    {'label': 'Male Only', 'value': 'Male Only'}
                                   ],
                           value='All',
                           labelStyle={'display': 'inline-block'}
                          ),
            html.Br(),
            html.Label(["Choose the Phase:"]),
            dcc.RadioItems(
                          id = 'phase_radioItems',
                          options=[
                                  {'label': y, 'value': y}
                                  for y in df.Phases.sort_values().unique()],
                                   value='No Defined Phase'
                                   ),
            dcc.Graph(id = 'pie_chart',style = {'textAlign':'right'})
                      ],
            style={'columnCount': 2}),
    html.H2('Searched Results:',style={'textAlign': 'left'}),
    html.Div(id = 'datatable'),
    html.Br(),
    html.Br(),
    html.P('April 2021 RuiGuo'),
    html.Br(),
         ])
       

@app.callback(
    Output(component_id = 'pie_chart',component_property = 'figure'),
    [Input(component_id = 'states_dropdown',component_property = 'value'),
     Input(component_id = 'status_dropdown',component_property = 'value'),
     Input(component_id = 'gender_radioItems',component_property = 'value'),
     Input(component_id = 'phase_radioItems',component_property = 'value')]   
    )
def update_piechart(state,status,gender,phase):
    df1 = df
    df2 = df1.loc[(df1.State == state) & (df1['Status'] == status) &
                           (df1['Gender'] == gender) & (df1['Phases'] == phase)]
    fig = px.pie(df2,
                 values = df2.City.value_counts(),
                 names = df2.City.unique(),height = 660)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(title= str(len(df2)) + " clinical trials are found",                     
                      font=dict(
                          family="Arial",
                          size=25,
                          color="RebeccaPurple"))

    return fig
    

@app.callback(
    Output(component_id = 'datatable',component_property = 'children'),
    [Input(component_id = 'states_dropdown',component_property = 'value'),
     Input(component_id = 'status_dropdown',component_property = 'value'),
     Input(component_id = 'gender_radioItems',component_property = 'value'),
     Input(component_id = 'phase_radioItems',component_property = 'value')] 
    )
def update_table(state,status,gender,phase):
    df3 = df
    df4 = df3.loc[(df3.State == state) & (df3['Status'] == status) &
                           (df3['Gender'] == gender) & (df3['Phases'] == phase)]
    x = df4
    tab = dash_table.DataTable(
          data=x.to_dict('records'),
          columns=[{'id': c, 'name': c} for c in x.columns],
          style_cell_conditional=[
        {
            'if': {'column_id': c},
            'textAlign': 'left'
        } for c in ['Title', 'URL']
    ],
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(248, 248, 248)'
        }
    ],
    style_header={
        'backgroundColor': 'rgb(230, 230, 230)',
        'fontWeight': 'bold'
    },
    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
        'lineHeight': '25px'
     },
    page_size=20,  # we have less data in this example, so setting to 20
    style_table={'height': '500px', 'overflowY': 'auto'}
     )
    
    return tab

server = app.server

if __name__ == '__main__':
     app.run_server(debug=False)



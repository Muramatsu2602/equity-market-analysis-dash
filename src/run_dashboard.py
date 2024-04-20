import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

from fetch_data import fetch_stock_data
from analysis import calculate_moving_average, calculate_exponential_moving_average, calculate_RSI, calculate_bollinger_bands

# Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='stock-input', type='text', value='AAPL'),
    dcc.DatePickerRange(
        id='date-picker',
        start_date='2023-01-01',
        end_date='2023-01-31'
    ),
    dcc.Graph(id='stock-graph'),
    dcc.Graph(id='ema-graph'),
    dcc.Graph(id='rsi-graph'),
    dcc.Graph(id='bollinger-graph')
])

@app.callback(
    [Output('stock-graph', 'figure'),
     Output('ema-graph', 'figure'),
     Output('rsi-graph', 'figure'),
     Output('bollinger-graph', 'figure')],
    [Input('stock-input', 'value'),
     Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date')])
def update_graphs(stock_symbol, start_date, end_date):
    df = fetch_stock_data(stock_symbol, start_date, end_date)
    df = calculate_moving_average(df)
    df = calculate_exponential_moving_average(df)
    df = calculate_RSI(df)
    df = calculate_bollinger_bands(df)

    # Candlestick Chart
    candlestick_fig = go.Figure(data=[
        go.Candlestick(
            x=df.index,
            open=df['Open'], high=df['High'],
            low=df['Low'], close=df['Close'],
            name='Candlestick'
        )
    ])

    # EMA Chart
    ema_fig = go.Figure(data=[
        go.Scatter(
            x=df.index, y=df['EMA'],
            mode='lines', name='Exponential Moving Average'
        )
    ])

    # RSI Chart
    rsi_fig = go.Figure(data=[
        go.Scatter(
            x=df.index, y=df['RSI'],
            mode='lines', name='Relative Strength Index'
        )
    ])

    # Bollinger Bands Chart
    bollinger_fig = go.Figure(data=[
        go.Scatter(
            x=df.index, y=df['Bollinger_Upper'],
            mode='lines', name='Bollinger Upper'
        ),
        go.Scatter(
            x=df.index, y=df['Bollinger_Lower'],
            mode='lines', name='Bollinger Lower',
            fill='tonexty'
        )
    ])

    return candlestick_fig, ema_fig, rs

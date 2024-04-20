import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

from fetch_data import fetch_stock_data
from analysis import calculate_moving_average, calculate_exponential_moving_average, calculate_RSI, calculate_bollinger_bands

# Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Equity Market Analysis for Institutional Equity Division - Strats"),
    html.H2("Created by: Pedro Muramatsu"),
    html.Br(),
    html.Div([
        html.H3("Stock Symbol Input"),
        dcc.Input(id='stock-input', type='text', value='AAPL', style={'width': '300px'}),
        html.H3("Select Date Range"),
        dcc.DatePickerRange(
            id='date-picker',
            start_date='2023-01-01',
            end_date='2023-01-31'
        ),
    ]),
    html.Div([
        html.H3("Stock Candlestick Chart"),
        html.P("This chart represents the stock's price movements over time with candlestick markers indicating the open, high, low, and close prices each day."),
        dcc.Graph(id='stock-graph'),
    ]),
    html.Div([
        html.H3("Exponential Moving Average (EMA)"),
        html.P("The EMA graph shows the stock's closing price along with its exponential moving average, which gives more weight to recent prices and reacts faster to price changes."),
        dcc.Graph(id='ema-graph'),
    ]),
    html.Div([
        html.H3("Relative Strength Index (RSI)"),
        html.P("The RSI graph indicates whether the stock is potentially overbought (over 70) or oversold (under 30), helping predict the potential reversal points."),
        dcc.Graph(id='rsi-graph'),
    ]),
    html.Div([
        html.H3("Bollinger Bands"),
        html.P("This graph plots two standard deviations away from a simple moving average. It's useful for identifying whether prices are high or low on a relative basis."),
        dcc.Graph(id='bollinger-graph'),
    ])
], style={'fontFamily': 'Arial', 'padding': '20px'})

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

    return candlestick_fig, ema_fig, rsi_fig, bollinger_fig

if __name__ == '__main__':
    app.run_server(debug=True)

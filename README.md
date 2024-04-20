
# Equity Market Analysis Dashboard

## Project Overview

This **Equity Market Analysis Dashboard** is a Python-based tool designed to fetch, process, and visualize real-time equity data. The dashboard provides actionable insights through advanced analysis of market trends, supporting traders and analysts in making informed decisions. Developed for roles within the Institutional Equity Division STRATS team at Morgan Stanley, this project highlights capabilities in data manipulation, visualization, and application development.

## Features

- **Real-Time Data Fetching:** Utilizes [Alpha Vantage](https://www.alphavantage.co/) or [Yahoo Finance API](https://finance.yahoo.com/) to pull live stock data.
- **Interactive Dashboards:** Built with [Dash by Plotly](https://plotly.com/dash/), the dashboards offer interactive controls to select stocks, date ranges, and types of analysis.
- **Data Analysis Tools:** Includes calculations for financial indicators like moving averages, RSI, and MACD.
- **Comparative Analysis:** Allows users to compare multiple stocks simultaneously to identify correlations and variances.
- **Forecasting:** Implements basic forecasting models to predict future stock prices based on historical data.

## Installation

### Prerequisites

- **Python 3.8+**
- **Pip**

### Setup

```bash
# Clone this repository
git clone https://github.com/yourusername/equity-market-analysis-dashboard.git
cd equity-market-analysis-dashboard

# Install required Python libraries
pip install -r requirements.txt

# Activate the virtual environment
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## Usage

```bash
# Run the dashboard
python src/run_dashboard.py
```

Navigate to `http://127.0.0.1:8050/` in your web browser to view the dashboard.

## Documentation and Resources

- **API Documentation:**
  - [Alpha Vantage Documentation](https://www.alphavantage.co/documentation/)
  - [Yahoo Finance API Guide](https://www.yahoofinanceapi.com/)
- **Library Documentation:**
  - [Dash User Guide](https://dash.plotly.com/introduction)
  - [Plotly Python Graphing Library](https://plotly.com/python/)
  - [Pandas Documentation](https://pandas.pydata.org/docs/)

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests to the main branch. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

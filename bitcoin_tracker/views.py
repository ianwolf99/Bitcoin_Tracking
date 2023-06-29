import os
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from django.shortcuts import render
import matplotlib
matplotlib.use('Agg')

def bitcoin_chart_view(request):
    try:
        # Fetch Bitcoin data using yfinance
        bitcoin_data = yf.download("BTC-USD", start="2020-01-01", end="2023-06-12")

        # Create a line chart
        line_chart_file = os.path.join('bitcoin_tracker', 'static', 'bitcoin_tracker', 'line_chart.png')
        plt.figure(figsize=(10, 6))
        plt.plot(bitcoin_data.index, bitcoin_data['Close'])
        plt.title('Bitcoin Closing Prices')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.savefig(line_chart_file)
        plt.close()

        # Create a bar chart
        bar_chart_file = os.path.join('bitcoin_tracker', 'static', 'bitcoin_tracker', 'bar_chart.png')
        plt.figure(figsize=(10, 6))
        plt.bar(bitcoin_data.index, bitcoin_data['Close'])
        plt.title('Bitcoin Closing Prices')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.savefig(bar_chart_file)
        plt.close()

        # Create an area chart
        area_chart_file = os.path.join('bitcoin_tracker', 'static', 'bitcoin_tracker', 'area_chart.png')
        plt.figure(figsize=(10, 6))
        plt.fill_between(bitcoin_data.index, bitcoin_data['Close'], alpha=0.5)
        plt.title('Bitcoin Closing Prices')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.savefig(area_chart_file)
        plt.close()

        # Create a scatter plot
        scatter_plot_file = os.path.join('bitcoin_tracker', 'static', 'bitcoin_tracker', 'scatter_plot.png')
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=bitcoin_data.index, y=bitcoin_data['Close'])
        plt.title('Bitcoin Closing Prices')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.savefig(scatter_plot_file)
        plt.close()

        # Create a candlestick chart using Plotly
        candlestick_chart_file = os.path.join('bitcoin_tracker', 'static', 'bitcoin_tracker', 'candlestick_chart.html')
        fig = go.Figure(data=[go.Candlestick(x=bitcoin_data.index,
                                             open=bitcoin_data['Open'],
                                             high=bitcoin_data['High'],
                                             low=bitcoin_data['Low'],
                                             close=bitcoin_data['Close'])])
        fig.update_layout(title='Bitcoin Candlestick Chart',
                          xaxis_title='Date',
                          yaxis_title='Price (USD)')
        fig.write_html(candlestick_chart_file)

        # Render the template with the file paths
        return render(request, 'bitcoin_tracker/bitcoin_chart.html', {
            'line_chart_file': line_chart_file,
            'bar_chart_file': bar_chart_file,
            'area_chart_file': area_chart_file,
            'scatter_plot_file': scatter_plot_file,
            'candlestick_chart_file': candlestick_chart_file,
        })
    except Exception as e:
        # Print the error result
        print(f"An error occurred: {str(e)}")
        return render(request, 'bitcoin_tracker/error.html', {'error_message': str(e)})

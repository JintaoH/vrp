import numpy as np
import pandas as pd
import yfinance as yf

# Function to calculate the historical volatility for the past 30 days
def calculate_historical_volatility(returns):
    return np.std(returns) * np.sqrt(252 / 12)  # Adjusted for 30 days

# Example usage
if __name__ == "__main__":
    # Define the ticker symbols
    spx_ticker = "^GSPC"  # S&P 500 index ticker
    vix_ticker = "^VIX"   # VIX index ticker
    
    # Define the start and end dates for the data retrieval (past 30 days)
    end_date = pd.Timestamp.today()
    start_date = end_date - pd.DateOffset(30)  # Retrieve data for the past 30 days
    
    # Fetch historical data for the S&P 500 index
    spx_data = yf.download(spx_ticker, start=start_date, end=end_date)
    
    # Fetch historical data for the VIX index
    vix_data = yf.download(vix_ticker, start=start_date, end=end_date)
    
    # Calculate daily returns for S&P 500
    spx_returns = spx_data['Adj Close'].pct_change()
    
    # Calculate historical volatility for the past 30 days
    historical_volatility = calculate_historical_volatility(spx_returns)
    
    # Get the current day's VIX value (implied volatility)
    current_vix = vix_data['Adj Close'].iloc[-1] / 100  # Convert VIX to a percentage
    
    # Calculate the VRP
    vrp = current_vix - historical_volatility
    
    # Print the VRP
    print("Variance Risk Premium (VRP):", vrp)

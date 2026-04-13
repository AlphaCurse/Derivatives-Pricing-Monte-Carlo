import yfinance as yf
import pandas as pd

class MarketData:
    @staticmethod
    def get_params():
        """Fetches live S&P 500 price, risk-free rate, and volatility."""
        # 1. Spot Price (S0)
        sp500 = yf.Ticker("^GSPC")
        s0 = sp500.fast_info['last_price']
        
        # 2. Risk-Free Rate (r) - Using 10Y Treasury Yield
        tnx = yf.Ticker("^TNX")
        r = tnx.fast_info['last_price'] / 100  # Converted percentage to decimal
        
        # 3. Volatility (sigma) - Using VIX as Implied Vol proxy
        vix = yf.Ticker("^VIX")
        sigma = vix.fast_info['last_price'] / 100
        
        return {
            "S0": round(s0, 2),
            "r": round(r, 4),
            "sigma": round(sigma, 4)
        }

data = MarketData.get_params()
print(f"Live Data Pulled: {data}")

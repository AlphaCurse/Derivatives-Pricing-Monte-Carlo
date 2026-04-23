import numpy as np

class VanillaPricer:
    def __init__(self, r, T):
        self.r = r
        self.T = T

    def call_payoff(self, K, paths):
        terminal_prices = paths[-1]
        payoffs = np.maximum(terminal_prices - K, 0)
        return np.exp(-self.r * self.T) * np.mean(payoffs)

    def put_payoff(self, K, paths):
        terminal_prices = paths[-1]
        payoffs = np.maximum(K - terminal_prices, 0)
        return np.exp(-self.r * self.T) * np.mean(payoffs)

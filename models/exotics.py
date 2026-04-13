import numpy as np

class ExoticPricer:
    def __init__(self, r, T):
        self.r = r
        self.T = T

    def price_asian_call(self, K, paths):
        """Payoff based on the average price over the life of the option."""
        # Average across the time steps (axis 0) for each simulation
        avg_prices = np.mean(paths, axis=0)
        payoffs = np.maximum(avg_prices - K, 0)
        return np.exp(-self.r * self.T) * np.mean(payoffs)

    def price_barrier_up_and_out_call(self, K, barrier, paths):
        """Payoff is zero if the price EVER hits the barrier."""
        # Find simulations where the maximum price exceeded the barrier
        max_prices = np.max(paths, axis=0)
        out_of_money = max_prices >= barrier
        
        # Calculate standard terminal payoffs
        terminal_payoffs = np.maximum(paths[-1] - K, 0)
        
        # Zero out the ones that hit the barrier
        terminal_payoffs[out_of_money] = 0
        
        return np.exp(-self.r * self.T) * np.mean(terminal_payoffs)

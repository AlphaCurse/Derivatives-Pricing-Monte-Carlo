import numpy as np

class MonteCarloEngine:
    def __init__(self, S0, r, sigma, T, steps, sims):
        self.S0 = S0
        self.r = r
        self.sigma = sigma
        self.T = T
        self.steps = steps
        self.sims = sims
        self.dt = T / steps

    def generate_paths(self, seed=None):
        """Generates asset price paths using vectorized GBM."""
        if seed: np.random.seed(seed)
        
        # Log-returns: (r - 0.5 * sigma^2) * dt + sigma * sqrt(dt) * Z
        z = np.random.standard_normal((self.steps, self.sims))
        drift = (self.r - 0.5 * self.sigma**2) * self.dt
        diffusion = self.sigma * np.sqrt(self.dt) * z
        
        # Accumulate returns over time
        daily_returns = np.exp(drift + diffusion)
        paths = np.zeros((self.steps + 1, self.sims))
        paths[0] = self.S0
        
        for t in range(1, self.steps + 1):
            paths[t] = paths[t-1] * daily_returns[t-1]
        return paths

    def price_european_call(self, K, paths):
        """Prices a vanilla call by averaging discounted terminal payoffs."""
        payoffs = np.maximum(paths[-1] - K, 0)
        price = np.exp(-self.r * self.T) * np.mean(payoffs)
        return price

# Usage Example
engine = MonteCarloEngine(S0=6816.89, r=0.0434, sigma=0.1923, T=1.0, steps=252, sims=100000)
simulated_paths = engine.generate_paths(seed=42)
call_price = engine.price_european_call(K=6800, paths=simulated_paths)

print(f"S&P 500 Monte Carlo Call Price (K=6800): ${call_price:.2f}")

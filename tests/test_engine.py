import numpy as np
from scipy.stats import norm
from models.engine import MonteCarloEngine
from models.vanillas import VanillaPricer

def black_scholes_call(S, K, T, r, sigma):
    """Analytical solution to verify Monte Carlo accuracy."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def test_pricing_accuracy():
    S0, K, T, r, sigma = 100, 100, 1.0, 0.05, 0.2
    
    engine = MonteCarloEngine(S0, r, sigma, T, steps=252, sims=100000)
    paths = engine.generate_paths(seed=42)
    pricer = VanillaPricer(r, T)
    
    mc_price = pricer.call_payoff(K, paths)
    bs_price = black_scholes_call(S0, K, T, r, sigma)
    
    diff = abs(mc_price - bs_price)
    
    print(f"Monte Carlo Price: {mc_price:.4f}")
    print(f"Black-Scholes Price: {bs_price:.4f}")
    print(f"Difference: {diff:.4f}")
    
    assert diff < 0.1, "Monte Carlo price is too far from Black-Scholes!"

if __name__ == "__main__":
    test_pricing_accuracy()

from data.data_fetcher import MarketData
from models.engine import MonteCarloEngine
from models.vanillas import VanillaPricer
from models.exotics import ExoticPricer
from greeks.calculator import GreeksCalculator

# 1. Fetch Real-World Data
data = MarketData.get_params()
print(f"S&P 500 Spot: {data['S0']} | Vol: {data['sigma']} | Rate: {data['r']}")

# 2. Setup Engine
engine = MonteCarloEngine(S0=data['S0'], r=data['r'], sigma=data['sigma'], T=1.0, steps=252, sims=100000)
paths = engine.generate_paths(seed=42)

# 3. Price Options
vanilla = VanillaPricer(r=data['r'], T=1.0)
exotic = ExoticPricer(r=data['r'], T=1.0)

call_p = vanilla.call_payoff(K=data['S0'], paths=paths)
asian_p = exotic.price_asian_call(K=data['S0'], paths=paths)

print(f"Vanilla Call Price: ${call_p:.2f}")
print(f"Asian Call Price: ${asian_p:.2f}")

# 4. Calculate Greeks
calc = GreeksCalculator(engine)
delta = calc.calculate_delta(K=data['S0'])
print(f"Option Delta: {delta:.4f}")

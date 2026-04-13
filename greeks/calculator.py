class GreeksCalculator:
    def __init__(self, engine):
        self.engine = engine
        self.epsilon_s = 0.01 * engine.S0  # 1% bump for Spot
        self.epsilon_v = 0.01              # 1% bump for Vol

    def calculate_delta(self, K):
        # Price at S + epsilon
        self.engine.S0 += self.epsilon_s
        p_plus = self.engine.price_european_call(K, self.engine.generate_paths(seed=42))
        
        # Price at S - epsilon
        self.engine.S0 -= 2 * self.epsilon_s
        p_minus = self.engine.price_european_call(K, self.engine.generate_paths(seed=42))
        
        # Reset S0
        self.engine.S0 += self.epsilon_s
        
        return (p_plus - p_minus) / (2 * self.epsilon_s)

    def calculate_vega(self, K):
        # Original price
        p_orig = self.engine.price_european_call(K, self.engine.generate_paths(seed=42))
        
        # Price at sigma + epsilon
        self.engine.sigma += self.epsilon_v
        p_plus = self.engine.price_european_call(K, self.engine.generate_paths(seed=42))
        
        # Reset sigma
        self.engine.sigma -= self.epsilon_v
        
        return (p_plus - p_orig) / self.epsilon_v

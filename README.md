# Derivatives Pricing: Monte Carlo Engine

A quantitative finance project implementing a high-performance **Monte Carlo Simulation Engine** to price vanilla and exotic derivatives using real-world market data.

## 📌 Project Overview
This engine solves the problem of pricing financial contracts where no closed-form analytical solution exists (e.g., path-dependent exotics). By simulating thousands of potential future price paths for the S&P 500, the system calculates fair values and market sensitivities (Greeks).

### Key Features
*   **Live Market Integration**: Fetches real-time S&P 500 spot prices, VIX (Volatility proxy), and Treasury yields via `yfinance`.
*   Utilizes `NumPy` for high-speed Geometric Brownian Motion (GBM) simulations.
*   Specialized payoffs for **Asian** (average price) and **Barrier** (knock-out) options.
*   High-precision Delta calculation using the Finite Difference Method.
*   Automated unit tests comparing Monte Carlo results against the **Black-Scholes** analytical model.

---

## 📈 Mathematical Framework

### Asset Price Dynamics
The engine assumes **Geometric Brownian Motion (GBM)** under the risk-neutral measure. The discretized evolution of the stock price is modeled as:

$$S_{t+\Delta t} = S_t \exp\left( (r - \frac{1}{2}\sigma^2)\Delta t + \sigma \sqrt{\Delta t} Z \right)$$

Where:
- $S_t$: Asset price at time $t$
- $r$: Risk-free interest rate
- $\sigma$: Volatility of the underlying asset
- $Z$: Random draw from a standard normal distribution $N(0,1)$

### Sensitivity Analysis (The Greeks)
I calculate **Delta ($\Delta$)** using a central difference approximation to measure the option's sensitivity to the underlying price:

$$\Delta = \frac{V(S_0 + \epsilon) - V(S_0 - \epsilon)}{2\epsilon}$$

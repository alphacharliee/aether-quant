import numpy as np
import pandas as pd

def run_monte_carlo(df, num_simulations=1000, num_days=30):
    df = df.copy()
    df["log_return"] = np.log(df["Close"] / df["Close"].shift(1))
    mu = df["log_return"].mean()
    sigma = df["log_return"].std()

    last_price = df["Close"].iloc[-1].item()
    simulations = []

    for _ in range(num_simulations):
        prices = [last_price]
        for _ in range(num_days):
            shock = np.random.normal(loc=mu, scale=sigma)
            price = prices[-1] * np.exp(shock)
            prices.append(price)
        simulations.append(prices)

    simulations = np.array(simulations)
    # Sharpe Ratio: (mean return - risk-free rate) / std dev
    log_returns = np.log(simulations[:, 1:] / simulations[:, :-1])
    avg_return = np.mean(log_returns)
    std_return = np.std(log_returns)
    sharpe_ratio = avg_return / std_return * np.sqrt(252)  # annualized

    # VaR 95%: 5th percentile of end returns
    ending_prices = simulations[:, -1]
    returns_from_today = (ending_prices - float(last_price)) / float(last_price)
    var_95 = np.percentile(returns_from_today, 5)

    # Explanations
    sharpe_exp = (
        f"Sharpe Ratio: {sharpe_ratio:.2f} → "
        + ("🟢 Good risk-adjusted return" if sharpe_ratio > 1 else "🟡 Moderate" if sharpe_ratio > 0.5 else "🔻 Weak reward/risk")
    )
    var_exp = f"VaR (95%): {var_95:.2%} → Estimated worst-case return with 95% confidence"

    return {
        "simulations": simulations,
        "sharpe_ratio": sharpe_ratio,
        "var_95": var_95,
        "sharpe_explanation": sharpe_exp,
        "var_explanation": var_exp
    }



# by alphacharlie X — 2025

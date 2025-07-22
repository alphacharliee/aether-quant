# Aether — Quant Toolkit v1

Aether is a lightweight Python-based quant toolkit that allows traders and analysts to run fast technical assessments and probabilistic simulations on any asset supported by Yahoo Finance.

### 🔧 Features
- RSI, Bollinger Bands, MACD, Z-score interpretation
- Monte Carlo simulations with customizable horizon
- Probabilistic outcomes (percentiles, median forecast)
- Risk metrics: Sharpe Ratio & Value at Risk (VaR)
- Clean, terminal-based interface

### 🖥 Requirements
- Python 3.9+
- pandas, numpy, matplotlib, yfinance, ta

Install dependencies with:
```bash
pip install -r requirements.txt


🚀 Usage

python aether.py


📈 Example
Enter ticker: ETH-USD
30-day forecast:
- 10% chance below: $2,900
- Median: $3,800
- 10% chance above: $5,100
Sharpe Ratio: 0.42 → Moderate
VaR (95%): -31.2%

This tool is for educational and research purposes only. No investment advice is provided.

⸻

🧠 Notes

Development is ongoing. Future updates will include strategy backtesting, anomaly detection, and Discord integration.
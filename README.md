# 📊 Aether — Quant Toolkit v1

> A lightweight, local quant analysis tool for crypto and stocks — no API keys, just pure signal.

---

### 🧠 Overview

**Aether** is a Python-based command-line toolkit that lets you analyze a ticker and get instant insights like:

- ✅ Real-time price & RSI
- 📈 Bollinger Bands + Z-score deviation
- 📊 MACD trends
- 🎯 Monte Carlo price forecast (30-day default)
- 📉 Risk metrics: Sharpe Ratio & Value at Risk (VaR)
- 🤖 Smart recommender with simple interpretations
- ⌛ Time horizon is adjustable by user input

No external dashboards. No noise. Just clean quant logic.

---

### ⚙️ Installation

1. Clone the repo:

```bash
git clone https://github.com/alphacharliee/aether-quant.git
cd aether-quant
```

2. Create and activate your virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # on macOS/Linux
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run Aether:

```bash
python aether.py
```

---

### 🧪 Example Run

```bash
📊 Bienvenido a Aether — Quant Toolkit v1
🔎 Ingresá el ticker: BTC-USD
💰 Precio de entrada: 62000

📈 Precio actual: 64,102.22
📊 RSI: 72.1 → 🔺 Overbought
• Bollinger: Normal range
• Z-score: 1.4 → 🟢 Normal deviation
• MACD: Bullish momentum

📉 Monte Carlo 30-day Forecast:
🔻 10% chance below: $58,300
⚖️ Median: $66,200
🚀 10% chance above: $74,500

📉 Risk Metrics:
• Sharpe Ratio: 0.54 → Balanced reward/risk
• VaR (95%): -17.8%
```

---

###  Tech Stack

- Python 3.11
- `yfinance`
- `pandas`, `numpy`
- `matplotlib` (optional for future visuals)
- `ta` for indicators
- Pure CLI design, easy to fork and build upon

---

###  Roadmap Ideas

- Add charting / visualizations
- JSON export / Discord bot wrapper
- Sentiment overlay module
- Strategy backtesting support

---

### ⚠ Disclaimer

This tool is for **educational and entertainment** purposes only. It does **not** constitute financial advice. DYOR. 🔍

---

###  Signature

`by alphacharlie × 2025`


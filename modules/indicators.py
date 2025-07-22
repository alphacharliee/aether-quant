from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator, EMAIndicator, MACD
from ta.volatility import BollingerBands
import pandas as pd
import numpy as np

def calcular_indicadores(df):
    df = df.copy()
    close = df["Close"]
    if hasattr(close, "values") and close.values.ndim > 1:
        close = close.squeeze()
    close = close.astype(float)

    # RSI
    df["RSI"] = RSIIndicator(close=close, window=14).rsi()

    # SMA & EMA
    df["SMA_20"] = SMAIndicator(close=close, window=20).sma_indicator()
    df["EMA_50"] = EMAIndicator(close=close, window=50).ema_indicator()

    # Bollinger Bands
    bb = BollingerBands(close=close, window=20, window_dev=2)
    df["bb_upper"] = bb.bollinger_hband()
    df["bb_lower"] = bb.bollinger_lband()
    df["bb_middle"] = bb.bollinger_mavg()

    # Z-score
    rolling_mean = df["Close"].rolling(window=20).mean()
    rolling_std = df["Close"].rolling(window=20).std()
    df["z_score"] = (df["Close"] - rolling_mean) / rolling_std

    # MACD
    macd = MACD(close=close)
    df["macd"] = macd.macd()
    df["macd_signal"] = macd.macd_signal()

    # Última fila con explicaciones
    latest = df.iloc[-1]
    expl = {}

    # Bollinger
    if latest["Close"].item() > latest["bb_upper"].item():
        expl["Bollinger"] = "Price is above upper band → ⚠️ Potential overbought/reversal"
    elif latest["Close"].item() < latest["bb_lower"].item():
        expl["Bollinger"] = "Price is below lower band → ⚠️ Potential oversold/bounce"
    else:
        expl["Bollinger"] = "Price is within Bollinger Bands → 🟢 Normal range"

    # Z-score
    z = latest["z_score"]
    z = latest["z_score"].item()
    expl["Z-score"] = f"Z-score: {z:.2f} → {'⚠️ High deviation' if abs(z) > 2 else '🟢 Normal deviation'}"

    # MACD
    if latest["macd"].item() > latest["macd_signal"].item():
        expl["MACD"] = "MACD crossed above signal → 🟢 Bullish momentum"
    elif latest["macd"].item() < latest["macd_signal"].item():
        expl["MACD"] = "MACD crossed below signal → 🔻 Bearish momentum"
    else:
        expl["MACD"] = "MACD near signal line → 🟡 Unclear momentum"

    return {"data": df, "explanation": expl}
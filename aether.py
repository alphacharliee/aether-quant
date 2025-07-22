import yfinance as yf
from modules.indicators import calcular_indicadores
from modules.montecarlo import run_monte_carlo
from modules.recommender import generar_recomendacion

def main():
    print("📊 Bienvenido a Aether — Quant Toolkit v1")

    # Entrada del usuario
    ticker = input("🔎 Ingresá el ticker (ej: BTC-USD, ETH-USD, AAPL): ").upper()
    entrada = input("💰 Precio de entrada (opcional, enter si no aplica): ")

    try:
        precio_entrada = float(entrada)
    except ValueError:
        precio_entrada = None

    # Descargar datos (6 meses de histórico)
    print(f"\n⬇️ Descargando datos de {ticker}...")
    data = yf.download(ticker, period="6mo", interval="1d", auto_adjust=True)

    if data.empty:
        print("❌ No se encontraron datos para el ticker.")
        return

    # Calcular indicadores técnicos
    result = calcular_indicadores(data)
    data = result["data"]
    expl = result["explanation"]

    # Mostrar resumen
    precio_actual = data["Close"].iloc[-1].item()
    rsi_actual = data["RSI"].iloc[-1].item()

    print(f"\n📈 Precio actual: {precio_actual:.2f}")
    print(f"📊 RSI actual: {rsi_actual:.2f} → {'🔺 Sobrecomprado' if rsi_actual > 70 else '🔻 Sobrevendido' if rsi_actual < 30 else '🟡 Neutral'}")

    print("\n🔬 Technical Summary:")
    for key, val in expl.items():
        print(f"• {key}: {val}")

    if precio_entrada:
        cambio = ((precio_actual - precio_entrada) / precio_entrada) * 100
        print(f"📌 Cambio desde tu entrada: {cambio:.2f}%")

    print("\n Análisis básico completado.\n")

    # Monte Carlo simulation
    print(" Running Monte Carlo simulation...")
    result = run_monte_carlo(data)
    simulations = result["simulations"]

    # Calcular percentiles
    import numpy as np
    final_prices = simulations[:, -1]
    pessimistic = np.percentile(final_prices, 10)
    expected = np.percentile(final_prices, 50)
    optimistic = np.percentile(final_prices, 90)

    print(f"\n📊 30-day Price Forecast (based on {simulations.shape[0]} simulations):")
    print(f"🔻 10% chance price ends below: ${pessimistic:.2f}")
    print(f"⚖️  50% chance price ends below (median): ${expected:.2f}")
    print(f"🚀 10% chance price ends above: ${optimistic:.2f}")

    print("\n📉 Risk Metrics:")
    print(f"• {result['sharpe_explanation']}")
    print(f"• {result['var_explanation']}")

    if precio_entrada:
        print("\n💡 Trade Evaluation:")
        rec = generar_recomendacion(precio_entrada, simulations)
        print(f"🎯 Suggested Take Profit: ${rec['take_profit']:.2f} (+{rec['upside_pct']}%)")
        print(f"🛑 Suggested Stop Loss: ${rec['stop_loss']:.2f} ({rec['downside_pct']}%)")
        print(f"📈 Estimated Success Probability: {rec['score']}%")
        print(f"📊 Confidence: {rec['confidence'].capitalize()}")

if __name__ == "__main__":
    main()
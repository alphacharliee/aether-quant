import numpy as np

def generar_recomendacion(precio_entrada, simulations):
    final_prices = simulations[:, -1]
    current_median = np.percentile(final_prices, 50)
    optimistic = np.percentile(final_prices, 90)
    pessimistic = np.percentile(final_prices, 10)

    if precio_entrada is None:
        return {
            "take_profit": optimistic,
            "stop_loss": pessimistic,
            "score": None,
            "confidence": "unknown"
        }

    prob_exito = np.mean(final_prices > precio_entrada) * 100
    upside = ((optimistic - precio_entrada) / precio_entrada) * 100
    downside = ((pessimistic - precio_entrada) / precio_entrada) * 100

    if prob_exito > 80:
        confianza = "alta"
    elif prob_exito > 60:
        confianza = "media"
    else:
        confianza = "baja"

    return {
        "take_profit": optimistic,
        "stop_loss": pessimistic,
        "score": round(prob_exito, 2),
        "confidence": confianza,
        "upside_pct": round(upside, 2),
        "downside_pct": round(downside, 2)
    }
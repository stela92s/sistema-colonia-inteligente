"""
Previsão de geração eólica usando regressão linear simples.

Modelo: y = a*x + b
x = velocidade do vento (m/s)
y = geração estimada (kWh)
"""

def calcular_regressao_linear(valores_x, valores_y):
    """Calcula inclinação (a) e intercepto (b) pelo método dos mínimos quadrados."""
    if len(valores_x) != len(valores_y):
        raise ValueError("As listas precisam ter o mesmo tamanho.")
    if len(valores_x) < 2:
        raise ValueError("São necessários pelo menos dois pares de dados.")

    quantidade = len(valores_x)
    media_x = sum(valores_x) / quantidade
    media_y = sum(valores_y) / quantidade

    numerador = sum(
        (x - media_x) * (y - media_y)
        for x, y in zip(valores_x, valores_y)
    )
    denominador = sum((x - media_x) ** 2 for x in valores_x)

    if denominador == 0:
        raise ValueError("Os valores de vento não podem ser todos iguais.")

    a = numerador / denominador
    b = media_y - a * media_x
    return a, b


def prever_geracao_eolica(vento_ms, historico):
    """Retorna a geração estimada, em kWh, para uma velocidade de vento."""
    a, b = calcular_regressao_linear(
        historico["vento_ms"],
        historico["geracao_kwh"]
    )
    previsao = a * vento_ms + b
    return max(0, previsao)


if __name__ == "__main__":
    from dados import HISTORICO_VENTO_GERACAO

    estimativa = prever_geracao_eolica(11, HISTORICO_VENTO_GERACAO)
    print(f"Previsão para vento de 11 m/s: {estimativa:.1f} kWh")

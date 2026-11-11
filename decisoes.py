"""
Regras de decisão e análise energética da colônia.
As prioridades são: preservar o suporte à vida e, depois, economizar energia.
"""

LIMITE_ENERGIA_BAIXA = 50
LIMITE_CONSUMO_ALTO = 60


def avaliar_situacao(dados):
    """Analisa energia disponível e consumo e devolve decisões em texto."""
    energia = dados["energia_disponivel_kwh"]
    consumo = dados["consumo_kwh"]
    decisoes = []

    # Prioridade máxima: sistemas essenciais não devem ser desligados.
    decisoes.append(
        "PRIORIDADE: manter oxigênio, água e controle de temperatura ligados."
    )

    if energia < LIMITE_ENERGIA_BAIXA and consumo > LIMITE_CONSUMO_ALTO:
        decisoes.append(
            "ALERTA CRÍTICO: energia baixa e consumo alto. Ativar modo economia."
        )
        decisoes.append(
            "AÇÃO: reduzir primeiro entretenimento e iluminação decorativa."
        )
    elif energia < LIMITE_ENERGIA_BAIXA:
        decisoes.append(
            "ALERTA: reserva de energia abaixo de 50 kWh. Reduzir consumo não essencial."
        )
    elif consumo > LIMITE_CONSUMO_ALTO:
        decisoes.append(
            "ALERTA: consumo elevado. Verificar equipamentos e reduzir cargas não essenciais."
        )
    else:
        decisoes.append("SITUAÇÃO: níveis de energia e consumo dentro dos limites definidos.")

    return decisoes


def analisar_balanco_energetico(geracao_kwh, consumo_kwh, reserva_kwh=0):
    """Compara geração e consumo e considera a reserva armazenada."""
    saldo = geracao_kwh - consumo_kwh

    if saldo < 0:
        deficit = abs(saldo)
        if reserva_kwh >= deficit:
            mensagem = (
                f"ALERTA: consumo supera a geração em {deficit:.1f} kWh. "
                "A reserva pode cobrir o déficit atual."
            )
        else:
            mensagem = (
                f"ALERTA: consumo supera a geração em {deficit:.1f} kWh "
                "e a reserva informada não cobre todo o déficit."
            )
    elif saldo > 0:
        mensagem = (
            f"SUGESTÃO: há excedente de {saldo:.1f} kWh. "
            "Armazenar o excedente na bateria, se houver capacidade."
        )
    else:
        mensagem = "EQUILÍBRIO: geração e consumo estão iguais."

    return {"saldo_kwh": saldo, "mensagem": mensagem}

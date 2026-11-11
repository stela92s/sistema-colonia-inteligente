"""
Sistema Integrado de Gerenciamento Inteligente da Colônia.
Execute com: python main.py
"""

from dados import (
    DADOS_ATUAIS,
    HISTORICO_VENTO_GERACAO,
    SISTEMAS_COLONIA,
)
from decisoes import avaliar_situacao, analisar_balanco_energetico
from previsao import prever_geracao_eolica


def exibir_estrutura(sistemas):
    """Percorre e apresenta a estrutura hierárquica de subsistemas."""
    print("\n1) ESTRUTURA DOS SISTEMAS DA COLÔNIA")
    for sistema, subsistemas in sistemas.items():
        print(f"- {sistema.replace('_', ' ').title()}")
        for nome, informacoes in subsistemas.items():
            print(f"    • {nome.replace('_', ' ').title()}: {informacoes}")


def executar_sistema(dados, historico, sistemas):
    """Executa as análises e apresenta resultados integrados."""
    exibir_estrutura(sistemas)

    print("\n2) DADOS MONITORADOS")
    for chave, valor in dados.items():
        print(f"- {chave}: {valor}")

    print("\n3) REGRAS DE DECISÃO")
    for decisao in avaliar_situacao(dados):
        print(f"- {decisao}")

    print("\n4) BALANÇO DE ENERGIA")
    bateria = sistemas["energetico"]["bateria"]["reserva_kwh"]
    balanco = analisar_balanco_energetico(
        dados["geracao_kwh"],
        dados["consumo_kwh"],
        bateria,
    )
    print(f"- Saldo (geração - consumo): {balanco['saldo_kwh']:.1f} kWh")
    print(f"- {balanco['mensagem']}")

    print("\n5) PREVISÃO DE GERAÇÃO EÓLICA")
    previsao = prever_geracao_eolica(dados["vento_ms"], historico)
    print(
        f"- Com vento de {dados['vento_ms']} m/s, "
        f"a geração estimada é {previsao:.1f} kWh."
    )

    print("\n6) RESUMO")
    print("O sistema monitora os dados, protege os serviços essenciais,")
    print("identifica desequilíbrios e estima a geração eólica futura.")


if __name__ == "__main__":
    executar_sistema(DADOS_ATUAIS, HISTORICO_VENTO_GERACAO, SISTEMAS_COLONIA)

"""
Dados de exemplo da colônia.
Os valores são fictícios e podem ser alterados pela equipe.
"""

# Estrutura hierárquica: sistema principal -> subsistemas.
SISTEMAS_COLONIA = {
    "energetico": {
        "solar": {"ativo": True, "geracao_kwh": 25},
        "eolico": {"ativo": True, "geracao_kwh": 15},
        "bateria": {"ativo": True, "reserva_kwh": 30},
    },
    "suporte_vida": {
        "oxigenio": {"ativo": True, "prioridade": 1},
        "agua": {"ativo": True, "prioridade": 1},
        "controle_temperatura": {"ativo": True, "prioridade": 1},
    },
    "nao_essenciais": {
        "iluminacao_decorativa": {"ativo": True, "prioridade": 3},
        "entretenimento": {"ativo": True, "prioridade": 3},
    },
}

# Leituras atuais. Energia disponível representa a energia armazenada na bateria.
DADOS_ATUAIS = {
    "energia_disponivel_kwh": 40,
    "geracao_kwh": 40,
    "consumo_kwh": 70,
    "vento_ms": 11,
    "clima": "nublado",
}

# Histórico simples para prever geração eólica a partir da velocidade do vento.
HISTORICO_VENTO_GERACAO = {
    "vento_ms": [8, 10, 12],
    "geracao_kwh": [20, 25, 30],
}

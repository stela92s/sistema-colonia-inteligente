# Sistema Inteligente de Gerenciamento de Energia da Colônia

## 1. Objetivo

Este projeto simula um sistema integrado que monitora a energia de uma colônia, organiza seus subsistemas, aplica regras automáticas de decisão, compara geração e consumo e estima a geração eólica por regressão linear simples.

O projeto utiliza apenas Python padrão, sem bibliotecas externas.

## 2. Como executar

É necessário ter Python 3 instalado.

1. Baixe ou clone este repositório.
2. Abra o terminal na pasta do projeto.
3. Execute:

```bash
python main.py
```

Em alguns computadores, o comando pode ser `python3 main.py`.

## 3. Organização dos arquivos

- `main.py`: coordena a execução e apresenta os resultados.
- `dados.py`: contém os dados atuais, o histórico e a estrutura hierárquica.
- `decisoes.py`: contém as regras de decisão e o balanço energético.
- `previsao.py`: calcula a regressão linear e estima a geração eólica.

## 4. Estruturas de dados

O dicionário `SISTEMAS_COLONIA` representa uma hierarquia: sistema energético, suporte à vida e sistemas não essenciais. Dentro do sistema energético existem os subsistemas solar, eólico e bateria.

O dicionário `DADOS_ATUAIS` armazena as leituras atuais em pares chave-valor. O histórico de vento e geração é armazenado em duas listas relacionadas pela posição dos elementos.

## 5. Regras de decisão

1. Oxigênio, água e controle de temperatura são prioridades e devem permanecer ligados.
2. Se a energia disponível for menor que 50 kWh e o consumo superar 60 kWh, o sistema ativa o alerta crítico e recomenda o modo economia.
3. Se apenas a reserva estiver baixa, recomenda reduzir cargas não essenciais.
4. Se o consumo estiver elevado, recomenda verificar equipamentos e reduzir cargas não essenciais.
5. Se o consumo superar a geração, o sistema informa o déficit e verifica se a reserva consegue cobri-lo.
6. Se a geração superar o consumo, recomenda armazenar o excedente, se houver capacidade.

Os limites são parâmetros didáticos de exemplo e podem ser ajustados pela equipe.

## 6. Modelo de previsão

É utilizada regressão linear simples:

**y = a · x + b**

- `x`: velocidade do vento em m/s.
- `y`: geração eólica estimada em kWh.
- `a`: inclinação da reta.
- `b`: intercepto.

Dados históricos de exemplo:

- Vento: `[8, 10, 12]`
- Geração: `[20, 25, 30]`

A reta calculada é `y = 2,5x`. Para vento de 11 m/s, a estimativa é:

`y = 2,5 × 11 = 27,5 kWh`

A previsão é uma estimativa baseada nos dados fornecidos, não uma garantia de geração real.

## 7. Exemplo de entrada e saída

Entrada usada no arquivo `dados.py`:

- Energia disponível: 40 kWh
- Geração: 40 kWh
- Consumo: 70 kWh
- Vento: 11 m/s
- Reserva da bateria: 30 kWh

Saídas esperadas, entre outras:

```text
PRIORIDADE: manter oxigênio, água e controle de temperatura ligados.
ALERTA CRÍTICO: energia baixa e consumo alto. Ativar modo economia.
AÇÃO: reduzir primeiro entretenimento e iluminação decorativa.
ALERTA: consumo supera a geração em 30.0 kWh. A reserva pode cobrir o déficit atual.
Com vento de 11 m/s, a geração estimada é 27.5 kWh.
```

## 8. Como adaptar

A equipe pode alterar os valores em `dados.py`, atualizar as listas históricas e ajustar os limites em `decisoes.py`. Para testar outros cenários, modifique os valores e execute novamente `python main.py`.

## 9. Publicação no GitHub

Crie um repositório público no GitHub, por exemplo `sistema-colonia-inteligente`, envie todos os arquivos desta pasta e copie o endereço do repositório para inserir no relatório. O endereço ainda precisa ser preenchido pela equipe após a publicação.

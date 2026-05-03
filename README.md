# SkyMetrics

O SkyMetrics é uma ferramenta profissional de interface de linha de comando (CLI) simples para consultar o clima atual de uma cidade usando a API do OpenWeatherMap. Ele busca automaticamente a temperatura, converte de Kelvin para Celsius e Fahrenheit, e exibe a umidade e a condição climática em uma interface visual bonita e colorida.

## Funcionalidades
- Consultas meteorológicas rápidas via linha de comando.
- Conversão automática de Kelvin para Celsius e Fahrenheit.
- Tratamento de erros para cidades não encontradas, problemas de rede e chaves de API inválidas.
- Lógica de conversão totalmente coberta por testes unitários.
- Interface de terminal visualmente atraente (utilizando a biblioteca Rich).

## Estrutura do Projeto
```
skymetrics/
├── docs/             # Documentação e backlog
├── src/              # Código fonte principal
├── tests/            # Testes unitários com pytest
├── main.py           # Ponto de entrada do CLI
└── requirements.txt  # Dependências do projeto
```

## Pré-requisitos
- Python 3.8+
- Uma chave de API do [OpenWeatherMap](https://openweathermap.org/)

## Instalação

1. Clone este repositório (ou copie os arquivos).
2. Navegue até o diretório do projeto:
   ```bash
   cd skymetrics
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Configuração

Configure a sua chave de API do OpenWeatherMap como uma variável de ambiente:

**Windows (PowerShell):**
```powershell
$env:OPENWEATHER_API_KEY="sua_chave_api_aqui"
```

**Linux/macOS:**
```bash
export OPENWEATHER_API_KEY="sua_chave_api_aqui"
```

## Como Usar

Execute o script `main.py` e passe o nome da cidade como argumento. Use aspas se o nome da cidade tiver espaços.

```bash
python main.py "São Paulo"
```

**Exemplo de Saída:**
```text
╭───────────────── SkyMetrics: São Paulo, BR ──────────────────╮
│                                                              │
│  Condition    ☀️ Clear sky                                    │
│  Temperature  28.5 °C / 83.3 °F                              │
│  Humidity     45%                                            │
│                                                              │
╰──────────────────────────────────────────────────────────────╯
```

## Testes

Para rodar os testes unitários, basta executar o comando `pytest`:

```bash
pytest
```

## Backlog

Consulte o arquivo `docs/backlog.md` para ver ideias de futuras melhorias.

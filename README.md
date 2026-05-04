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
│   ├── conversions.py  # Lógica de conversão de unidades
│   └── weather_api.py  # Lógica de comunicação com a API
├── tests/            # Testes unitários com pytest
├── main.py           # Ponto de entrada do CLI
├── LICENSE           # Licença MIT
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

## Configuração e Segurança de Credenciais

> ⚠️ **Importante:** Nunca exponha sua chave de API diretamente no código-fonte ou a faça commit no repositório. Utilize **variáveis de ambiente** para proteger seus secrets.

Configure a sua chave de API do OpenWeatherMap como uma variável de ambiente **antes** de executar o projeto:

**Windows (PowerShell):**
```powershell
$env:OPENWEATHER_API_KEY="sua_chave_api_aqui"
```

**Linux/macOS:**
```bash
export OPENWEATHER_API_KEY="sua_chave_api_aqui"
```

Como alternativa para desenvolvimento local, crie um arquivo `.env` na raiz do projeto (ele já está no `.gitignore` e não será rastreado):
```
OPENWEATHER_API_KEY=sua_chave_api_aqui
```

O arquivo `src/weather_api.py` lê a chave exclusivamente via `os.environ.get("OPENWEATHER_API_KEY")`, garantindo que nenhuma credencial fique embutida no código.

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

## Dependências

As dependências do projeto estão listadas em `requirements.txt`:

| Pacote     | Versão mínima | Finalidade                                    |
|------------|---------------|-----------------------------------------------|
| `requests` | 2.31.0        | Requisições HTTP à API do OpenWeatherMap       |
| `rich`     | 13.0.0        | Renderização da interface visual no terminal   |
| `pytest`   | 7.4.0         | Execução da suíte de testes unitários          |

## Apoio de IA Generativa

O desenvolvimento do SkyMetrics contou com o suporte de Inteligência Artificial Generativa (Google Gemini) em três frentes principais:

### 🏗️ Estruturação da Arquitetura
A IA auxiliou na definição da **arquitetura modular** do projeto, propondo a separação clara entre as responsabilidades:
- `src/weather_api.py` — encapsula toda a lógica de comunicação com a API externa (requisições HTTP, tratamento de erros de rede e autenticação).
- `src/conversions.py` — centraliza a lógica matemática de conversão de unidades (Kelvin → Celsius → Fahrenheit), mantendo-a isolada, pura e facilmente testável.

Essa separação garante baixo acoplamento, facilidade de manutenção e aderência ao Princípio da Responsabilidade Única (SRP).

### 🧪 Desenvolvimento de Testes
A IA colaborou na **criação da suíte de testes unitários** (`tests/test_conversions.py`), cobrindo cenários como:
- Conversão de temperatura zero absoluto (0 K).
- Validação de valores decimais com precisão de ponto flutuante.
- Verificação de temperaturas negativas em Celsius.

Os testes foram escritos com `pytest` e seguem o padrão **Arrange-Act-Assert (AAA)**, garantindo legibilidade e rastreabilidade dos casos de uso validados.

### 📝 Documentação e Backlog
A IA auxiliou na **redação técnica** deste README e na **organização do backlog** (`docs/backlog.md`), estruturando as histórias de usuário por prioridade e descrevendo critérios de aceite claros para cada funcionalidade futura planejada.

## Backlog

Consulte o arquivo `docs/backlog.md` para ver ideias de futuras melhorias.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

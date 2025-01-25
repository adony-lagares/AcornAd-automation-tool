# Acorn Advisory Automation Tool Project 🛠️

# 🎯 Propósito do Projeto

Este projeto foi desenvolvido como parte de um teste técnico de case para demonstrar habilidades em automação de processos, manipulação de dados e desenvolvimento de interfaces gráficas. O objetivo principal foi criar uma solução funcional e eficiente para automatizar buscas no YouTube, com base em uma entrada estruturada em planilhas Excel, e gerar um arquivo de saída consolidado e formatado.

# 📺 Automação de Busca no YouTube

Uma aplicação que automatiza a busca de vídeos no YouTube com base em palavras-chave fornecidas em um arquivo Excel. A aplicação utiliza Selenium para buscar no YouTube e extrair informações como título do vídeo, link e link do canal, apresentando os resultados em uma planilha Excel formatada.

---

## ✨ Funcionalidades

- Busca automática de vídeos no YouTube com base em palavras-chave.
- Extração de:
  - **Título do vídeo**.
  - **Link do vídeo**.
  - **Link do canal**.
- Geração de uma planilha Excel (`search_output.xlsx`) com os resultados.
- Formatação automática da planilha de saída:
  - Largura das colunas ajustada automaticamente.
  - Cabeçalhos em negrito e centralizados.
- Interface gráfica (GUI) amigável para usuários, criada com Tkinter.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Selenium** - Automação do navegador para buscas no YouTube.
- **Tkinter** - Interface gráfica do usuário.
- **OpenPyXL** - Manipulação e formatação de planilhas Excel.
- **Pandas** - Manipulação de dados.

---

## 📋 Pré-requisitos

Certifique-se de ter os seguintes itens configurados no seu sistema:

1. **Python 3.10 ou superior** - [Download](https://www.python.org/downloads/)
2. **Google Chrome** - [Download](https://www.google.com/intl/pt-BR/chrome/)
3. **ChromeDriver**:
   - Baixe a versão compatível com o seu navegador no site oficial: [ChromeDriver](https://chromedriver.chromium.org/downloads)
   - Coloque o arquivo `chromedriver.exe` na mesma pasta do executável gerado.

---

## ⚙️ Instalação

1. Clone o repositório ou baixe os arquivos:
   ```bash
   git clone https://github.com/adony-lagares/AcornAd-automation-tool.git
   cd seu-repositorio
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Certifique-se de que o arquivo **chromedriver.exe** está na mesma pasta do seu projeto.

---

## 🚀 Como Usar

### **1. Prepare o Arquivo de Entrada**
Crie um arquivo Excel (`.xlsx`) com uma coluna chamada `Keyword`, contendo as palavras-chave que deseja buscar no YouTube.

#### Exemplo de arquivo de entrada:
| Keyword            |
|--------------------|
| Importância da segurança no desenvolvimento de software |
| Twenty One Pilots Oldies Station |
| NVIDIA lançamento RTX 5090 |
| O futuro com IA |

---

### **2. Inicie a Aplicação**
1. Abra o terminal e navegue até o diretório do projeto.
2. Execute o comando:
   ```bash
   python automation_script.py
   ```

---

### **3. Utilize a Interface Gráfica**
- **Passo 1:** Clique no botão **Procurar** para selecionar o arquivo de entrada (Excel).
- **Passo 2:** Clique em **Iniciar Busca** para processar os dados.
- **Passo 3:** Clique em **Abrir Resultado** para visualizar a planilha gerada.

---

## 🧪 Testes Automatizados

O projeto conta com testes automatizados desenvolvidos para validar as principais funcionalidades. Eles utilizam a biblioteca **unittest** e estão localizados no diretório `tests/`.

### **Objetivo dos Testes**
- Garantir a confiabilidade do código.
- Verificar o correto funcionamento de funções como busca no YouTube, formatação de planilhas e processamento de arquivos de entrada.

### **Testes Implementados**
1. **Teste da Função `buscar_no_youtube`**:
   - Valida se as informações de título, link e link do canal são extraídas corretamente.
2. **Teste da Função `formatar_planilha_saida`**:
   - Garante que a planilha de saída seja formatada corretamente (largura de colunas ajustada e cabeçalhos estilizados).
3. **Teste da Função `processar_arquivo_entrada`**:
   - Verifica se o processamento de um arquivo de entrada gera o arquivo de saída esperado.

### **Como Executar os Testes**
1. Certifique-se de que as dependências estão instaladas.
2. Execute todos os testes com:
   ```bash
   python -m unittest discover -s tests -p "test_*.py"
   ```
3. Para rodar um teste específico:
   ```bash
   python -m unittest tests.test_automation_script
   ```

   ---

## 📂 Estrutura de Pastas do Projeto

```plaintext
AcornAd-automation-tool/
├── dist/
│   ├── automation_script.exe       # Executável gerado pelo PyInstaller
│   ├── chromedriver.exe            # ChromeDriver necessário para o Selenium
│   ├── input_keywords.xlsx         # Exemplo de arquivo de entrada
│   ├── search_output.xlsx          # Exemplo de arquivo de saída do resultado da busca
├── tests/
│   ├── fixtures/                   # Pasta para arquivos de entrada e saída usados nos testes
│   ├── test_automation_script.py   # Arquivo de teste do projeto
├── automation_script.py            # Arquivo com código fonte
├── automation_script.spec          # Arquivo de configuração gerado pelo PyInstaller
├── chromedriver.exe                # ChromeDriver necessário para o Selenium
├── input_keywords.xlsx             # Exemplo de arquivo de entrada (backup fora do dist/)
├── README.md                       # Documentação do projeto
├── requirements.txt                # Lista de dependências do projeto
├── search_output.xlsx              # Exemplo de arquivo de saída do resultado da busca
```

---
## 📄 Exemplo de Saída

A planilha de saída (`search_output.xlsx`) terá o seguinte formato:

| Palavra-chave                                         | Título do Vídeo                              | Link do Vídeo         | Canal          | Link do Canal           |
|-------------------------------------------------------|----------------------------------------------|-----------------------|----------------|-------------------------|
| Importância da segurança no desenvolvimento de software | DevSecOps ...                              | https://...           | Código Fonte TV | https://...          |
| Twenty One Pilots Oldies Station                      | Twenty One Pilots - Oldies Station ...       | https://...           | Twenty One Pilots | https://...          |
| NVIDIA lançamento RTX 5090                            | NVIDIA GeForce RTX 5090 é anunciada ...      | https://...           | Adrenaline     | https://...             |
| O futuro com IA                                       | NÓS devemos nos PREOCUPAR com o FUTURO ...   | https://...           | Cortes do Inteligência | https://...     |

---

## 🐞 Possíveis Problemas

### 1. **Erro: "chromedriver.exe" não encontrado**
Certifique-se de que o arquivo `chromedriver.exe` está no mesmo diretório que o executável gerado.

### 2. **Erro: "Arquivo de Entrada Inválido"**
Verifique se a planilha contém uma coluna chamada `Keyword` com palavras-chave válidas.

### 3. **Problemas com a Conexão à Internet**
A aplicação depende de uma conexão estável para acessar o YouTube. Certifique-se de que sua máquina está conectada à internet.

---

## 👨‍💻 Autor

Desenvolvido por **Ádony Lagares**.  
Entre em contato:
- GitHub: [adony-lagares](https://github.com/adony-lagares)
- Email: adonyhibari48@gmail.com

---

## 🖇️ Recursos Adicionais

- [Documentação do Selenium](https://selenium.dev/documentation/)
- [Python Oficial](https://www.python.org/)
- [PyInstaller](https://pyinstaller.org/)

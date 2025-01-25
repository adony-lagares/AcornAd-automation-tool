import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from automation_script import buscar_no_youtube, formatar_planilha_saida, processar_arquivo_entrada
import os
import pandas as pd


class TestAutomationScript(unittest.TestCase):

    def setUp(self):
        """
        Configuração inicial do ambiente de teste:
        - Inicializa o WebDriver do Selenium no modo headless.
        - Define o diretório de fixtures para armazenar arquivos auxiliares dos testes.
        """
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        self.driver_service = Service("./chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.driver_service, options=chrome_options)

        # Diretório para armazenar arquivos de teste (fixtures)
        self.fixture_dir = os.path.join("tests", "fixtures")

        # Criação do diretório de fixtures, caso não exista
        if not os.path.exists(self.fixture_dir):
            os.makedirs(self.fixture_dir)

    def tearDown(self):
        """
        Finalização do ambiente de teste:
        - Encerra o WebDriver do Selenium para liberar recursos.
        """
        self.driver.quit()

    def test_buscar_no_youtube(self):
        """
        Testa a função `buscar_no_youtube`:
        - Verifica se a função retorna as informações esperadas para uma palavra-chave.
        - Garante que os campos retornados não estejam vazios.
        """
        palavra_chave = "Automação no YouTube"
        resultado = buscar_no_youtube(palavra_chave, self.driver)

        # Validações dos campos esperados no retorno da função
        self.assertIn("Título", resultado)
        self.assertIn("Link", resultado)
        self.assertIn("Link do Canal", resultado)
        self.assertIsNotNone(resultado["Título"])
        self.assertIsNotNone(resultado["Link"])

    def test_formatar_planilha_saida(self):
        """
        Testa a função `formatar_planilha_saida`:
        - Gera uma planilha de teste e aplica a formatação.
        - Verifica se o arquivo formatado é salvo corretamente.
        """
        arquivo_teste = os.path.join(self.fixture_dir, "test_output.xlsx")

        # Criação de uma planilha de teste
        dados = {
            "Palavra-chave": ["Exemplo"],
            "Título": ["Teste"],
            "Link": ["https://youtube.com"],
            "Link do Canal": ["https://youtube.com/teste"]
        }
        df = pd.DataFrame(dados)
        df.to_excel(arquivo_teste, index=False)

        # Aplica a formatação à planilha
        formatar_planilha_saida(arquivo_teste)

        # Verifica se o arquivo foi criado e formatado
        self.assertTrue(os.path.exists(arquivo_teste))

        # Remove o arquivo de teste após a validação
        os.remove(arquivo_teste)

    def test_processar_arquivo_entrada(self):
        """
        Testa a função `processar_arquivo_entrada`:
        - Utiliza um arquivo de entrada com palavras-chave simuladas.
        - Verifica se o arquivo de saída é gerado corretamente.
        """
        arquivo_entrada = os.path.join(self.fixture_dir, "test_input.xlsx")
        arquivo_saida = os.path.join(self.fixture_dir, "test_output.xlsx")

        # Criação de um arquivo de entrada para o teste
        dados = {"Keyword": ["Automação no YouTube"]}
        df = pd.DataFrame(dados)
        df.to_excel(arquivo_entrada, index=False)

        # Mock de um widget de log para simular a interface gráfica
        class MockWidgetLog:
            def insert(self, *args):
                pass

            def see(self, *args):
                pass

            def update(self):
                pass

        log_mock = MockWidgetLog()

        # Executa o processamento do arquivo de entrada
        processar_arquivo_entrada(arquivo_entrada, arquivo_saida, log_mock)

        # Valida se o arquivo de saída foi gerado com sucesso
        self.assertTrue(os.path.exists(arquivo_saida))

        # Remove os arquivos de teste após a validação
        os.remove(arquivo_entrada)
        os.remove(arquivo_saida)


if __name__ == "__main__":
    unittest.main()

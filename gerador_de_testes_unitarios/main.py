import google.generativeai as genai
import flet as ft
import FPDF as pdf
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve(strict=True).parent / ".env"
load_dotenv(dotenv_path=env_path)

# coloque sua chave de API do Gemini no arquivo .env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = os.getenv("GEMINI_API_URL")  # URL base da API do Gemini

def main(page: ft.Page):
    page.title = "Gerador de Testes Unitários"

    arquivo=ft.TextField(label="arquivo a ser analisado",max_length=50)
    text=ft.Text(value="escolha a tipo de teste a ser gerado")
    tipo_arquivo = ft.RadioGroup(content=ft.Column([
        ft.Radio(value="database", label="banco de dados"),
        ft.Radio(value="function", label="funcao"),
        ft.Radio(value="values", label="valor")]))
    
    formato_do_log =ft.Text(value="escolha qual o formato q vc deseja salvar o log")

    tipo_arquivo_log = ft.RadioGroup(content=ft.Column([
        ft.Radio(value='txt',label='arquivo.txt'),
        ft.Radio(value='pdf',label='arquivo.pdf')]))

    def gerar_log (e):
        genai.configure(api_key=os.environ['GEMINI_API_KEY'])
        model = genai.GenerativeModel(model_name='gemini-2.5-flash')
        prompt=f"""analise este arquivo {arquivo.value} visando as seguintes possibilidades:
        sintaxe ,valor esperado,funcionalidade ,usabilidade e como se comporta de forma reutilavel
        e a partir deste contexto gere um teste unitario para este arquivo que considere sua arquitetura
        e funcionalidade afim de testa este codigo em uma situacao de uso normal e tambem em um cenario de 
        estresse como erro nas informacoes de entrada e adapte seus testes baseados em {tipo_arquivo.value}
        """
        response = model.generate_content(prompt)
    
   
        log = tipo_arquivo_log.value
        if log == 'txt':
            with open('log.txt', 'w') as texto:
                texto.write(response)

        elif log == 'pdf':
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, response)
            pdf.output("log.pdf")

        return response
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.adaptive =True
    gerar = ft.ElevatedButton(text='gerar log',on_click='gerar_log')
    page.add(arquivo,text,tipo_arquivo,formato_do_log,tipo_arquivo_log,gerar)


ft.app(target=main,view=ft.AppView.FLET_APP)


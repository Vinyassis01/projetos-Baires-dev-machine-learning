import os
import base64
import tempfile
from fastapi import FastAPI, UploadFile, Form, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from dotenv import load_dotenv
import requests  # Para chamadas HTTP à API do Gemini

env_path = Path(__file__).resolve(strict=True).parent / ".env"
load_dotenv(dotenv_path=env_path)

# Configuração do FastAPI
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)
# Configuração da API do Gemini
# coloque sua chave de API do Gemini no arquivo .env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = os.getenv("GEMINI_API_URL")  # URL base da API do Gemini

def criar_prompt_modelo_ameacas(tipo_aplicacao, 
                                autenticacao, 
                                acesso_internet, 
                                dados_sensiveis, 
                                descricao_aplicacao):
    prompt = f"""Aja como um especialista em cibersegurança com mais de 20 anos de experiência 
    utilizando a metodologia de modelagem de ameaças STRIDE para produzir modelos de ameaças 
    abrangentes para uma ampla gama de aplicações. Sua tarefa é analisar o resumo do código, 
    o conteúdo do README e a descrição da aplicação fornecidos para produzir uma lista de 
    ameaças específicas para essa aplicação.

    Presta atenção na descrição da aplicação e nos detalhes técnicos fornecidos.

    Para cada uma das categorias do STRIDE (Falsificação de Identidade - Spoofing, 
    Violação de Integridade - Tampering, 
    Repúdio - Repudiation, 
    Divulgação de Informações - Information Disclosure, 
    Negação de Serviço - Denial of Service, e 
    Elevação de Privilégio - Elevation of Privilege), liste múltiplas (3 ou 4) ameaças reais, 
    se aplicável. Cada cenário de ameaça deve apresentar uma situação plausível em que a ameaça 
    poderia ocorrer no contexto da aplicação.

    A lista de ameaças deve ser apresentada em formato de tabela, 
    com as seguintes colunas:Ao fornecer o modelo de ameaças, utilize uma resposta formatada em JSON 
    com as chaves "threat_model" e "improvement_suggestions". Em "threat_model", inclua um array de 
    objetos com as chaves "Threat Type" (Tipo de Ameaça), "Scenario" (Cenário), e 
    "Potential Impact" (Impacto Potencial).    

    Ao fornecer o modelo de ameaças, utilize uma resposta formatada em JSON com as chaves 
    "threat_model" e "improvement_suggestions". 
    Em "threat_model", inclua um array de objetos com as chaves "Threat Type" (Tipo de Ameaça), 
    "Scenario" (Cenário), e "Potential Impact" (Impacto Potencial).

    Em "improvement_suggestions", inclua um array de strings que sugerem quais informações adicionais 
    poderiam ser fornecidas para tornar o modelo de ameaças mais completo e preciso na próxima iteração. 
    Foque em identificar lacunas na descrição da aplicação que, se preenchidas, permitiriam uma 
    análise mais detalhada e precisa, como por exemplo:
    - Detalhes arquiteturais ausentes que ajudariam a identificar ameaças mais específicas
    - Fluxos de autenticação pouco claros que precisam de mais detalhes
    - Descrição incompleta dos fluxos de dados
    - Informações técnicas da stack não informadas
    - Fronteiras ou zonas de confiança do sistema não especificadas
    - Descrição incompleta do tratamento de dados sensíveis
    - Detalhes sobre
    Não forneça recomendações de segurança genéricas — foque apenas no que ajudaria a criar um
    modelo de ameaças mais eficiente.

    TIPO DE APLICAÇÃO: {tipo_aplicacao}
    MÉTODOS DE AUTENTICAÇÃO: {autenticacao}
    EXPOSTA NA INTERNET: {acesso_internet}
    DADOS SENSÍVEIS: {dados_sensiveis}
    RESUMO DE CÓDIGO, CONTEÚDO DO README E DESCRIÇÃO DA APLICAÇÃO: {descricao_aplicacao}

    Exemplo de formato esperado em JSON:

    {{
      "threat_model": [
        {{
          "Threat Type": "Spoofing",
          "Scenario": "Cenário de exemplo 1",
          "Potential Impact": "Impacto potencial de exemplo 1"
        }},
        {{
          "Threat Type": "Spoofing",
          "Scenario": "Cenário de exemplo 2",
          "Potential Impact": "Impacto potencial de exemplo 2"
        }}
        // ... mais ameaças
      ],
      "improvement_suggestions": [
        "Por favor, forneça mais detalhes sobre o fluxo de autenticação entre os componentes para permitir uma análise melhor de possíveis falhas de autenticação.",
        "Considere adicionar informações sobre como os dados sensíveis são armazenados e transmitidos para permitir uma análise mais precisa de exposição de dados.",
        // ... mais sugestões para melhorar o modelo de ameaças
      ]
    }}"""

    return prompt

@app.post("/analisar_ameacas")
async def analisar_ameacas(
    imagem: UploadFile = File(...),
    tipo_aplicacao: str = Form(...),
    autenticacao: str = Form(...),
    acesso_internet: str = Form(...),
    dados_sensiveis: str = Form(...),
    descricao_aplicacao: str = Form(...)
):
    try:
        # Criar o prompt para o modelo de ameaças
        prompt = criar_prompt_modelo_ameacas(tipo_aplicacao, 
                                              autenticacao, 
                                              acesso_internet, 
                                              dados_sensiveis, 
                                              descricao_aplicacao)
        # Salvar a imagem temporariamente
        content = await imagem.read()
        with tempfile.NamedTemporaryFile(delete=False, suffix=Path(imagem.filename).suffix) as temp_file:
            temp_file.write(content)
            temp_file_path = temp_file.name

        # Convert imagem para base64
        with open(temp_file_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('ascii')

        # Adicionar a imagem codificada ao payload
        payload = {
            "prompt": prompt,
            "image": f"data:image/png;base64,{encoded_string}"

        }

        # Definir os headers para a requisição
        headers = {
            "Authorization": f"Bearer {GEMINI_API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post(GEMINI_API_URL, json=payload, headers=headers)

        os.remove(temp_file_path)  # Remover o arquivo temporário após o uso

        # Verificar a resposta da API
        if response.status_code == 200:
            return JSONResponse(content=response.json(), status_code=200)
        else:
            return JSONResponse(content={"error": response.text}, status_code=response.status_code)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    

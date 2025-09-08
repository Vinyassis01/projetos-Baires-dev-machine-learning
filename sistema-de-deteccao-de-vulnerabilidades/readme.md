<!--START_SECTION:header-->
<div align="center">
  <p align="center">
    <img 
      alt="DIO Education" 
      src="./.github/assets/logo.webp" 
      width="100px" 
    />
    <h1>Formação: Agents de IA</h1>
  </p>
</div>
<!--END_SECTION:header-->

<p align="center">
  <img src="https://img.shields.io/static/v1?label=DIO&message=Education&color=E94D5F&labelColor=202024" alt="DIO Project" />
  <a href="LICENSE"><img  src="https://img.shields.io/static/v1?label=License&message=MIT&color=E94D5F&labelColor=202024" alt="License"></a>
</p>

<!--  -->
<table align="center">
<thead>
  <tr>
    <td>
        <p align="center">Expert</p>
        <a href="https://github.com/hsouzaeduardo">
        <img src="https://avatars.githubusercontent.com/u/1692867?s=400&u=b408cc35aea6b0b2cd69ba3745dbd134edd7ac8a&v=4" alt="@hsouzaeduardo"><br>
        <sub>@hsouzaeduardo</sub>
      </a>
    </td>
    <td colspan="3">
    <p>Especialista em Soluções distribuídas e Cloud, pós-graduado em Engenharia de Software, MBA em Arquitetura de Soluções e Dados &IA. Atuando há 25 anos com softwares para web, Mobile, Cloud, IoT, IIoT, e softwares embarcados. Atualmente atuando como Gerente de Arquitetura e inteligência Artificial . Instrutor Oficial Microsoft há mais de 10 anos, Microsoft MVP e apaixonado por tecnologia, inovação e defensor de que um bom feedback constrói gigantes e que todos merecem oportunidades e criador da fórmula:

R = (T + D + TD)²

Resultado = (Tempo + dedicação + Trabalho Duro)</p>
      <a 
      href="https://www.linkedin.com/in/felipe-me/" 
      align="center">
           <img 
            align="center" 
            alt="Material de Apoio" 
            src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"
            >
        </a>
    </td>
  </tr>
</thead>
</table>
<!--  -->

<div align="center">
  <h2>💻 Módulos</h2>
</div>

<div align="center">
<table>
  <thead>
    <tr align="left">
      <th>#</th>
      <th>Módulo</th>
      <th>Materiais</th>
    </tr>
  </thead>
  <tbody align="left">
    <tr>
      <td>01</td>
      <td>📁 Backend</td>
      <td align="center">
        <a href="https://learn.microsoft.com/pt-br/azure/security/develop/threat-modeling-tool-threats">
           <img 
              align="center" 
              alt="Material de Apoio" 
              src="https://img.shields.io/badge/Ver%20Material-E94D5F?style=for-the-badge"
            >
        </a>
      </td>
    </tr>
    <tr>
      <td>02</td>
      <td>📁 Frontend</td>
      <td align="center">
        <a href="https://js.cytoscape.org/">
           <img 
            align="center" 
            alt="Material de Apoio" 
            src="https://img.shields.io/badge/Ver%20Material-E94D5F?style=for-the-badge"
            >
        </a>
      </td>
    </tr>
  </tbody>
  <tfoot></tfoot>
</table>
</div>

<!--START_SECTION:footer-->
<br/>
<br/>
<p align="center">
  ⌨️ Feito com 💜 by DIO
</p>

<br />
<br />

<p align="center">
  <a href="https://www.dio.me/" target="_blank">
    <img align="center" src="./.github/assets/footer.png" alt="banner"/>
  </a>
</p>

<!--END_SECTION:footer-->
# STRIDE Threat Model Analyzer

Este projeto é uma solução completa para análise de ameaças baseada na metodologia STRIDE, composta por um backend em FastAPI (Python) e um front-end em HTML/CSS/JS com visualização de ameaças usando Cytoscape.js.

## Funcionalidades
- Upload de imagem de arquitetura e preenchimento de informações do sistema.
- Geração automática de modelo de ameaças STRIDE usando Azure OpenAI.
- Visualização do modelo de ameaças em grafo interativo (Cytoscape.js).
- Sugestões de melhoria para o modelo de ameaças.
- Botão para imprimir/exportar o grafo gerado.

---

## Como executar o projeto

### 1. Pré-requisitos
- Python 3.10+
- Node.js (opcional, apenas se quiser servir o front-end com algum servidor local)
- Conta e deployment configurado no Azure OpenAI (veja variáveis de ambiente)

### 2. Clonando o repositório

```bash
# Clone o projeto
 git clone https://github.com/digitalinnovationone/stride-demo.git
 cd stride-demo
```

### 3. Configurando o backend (FastAPI)

1. Acesse a pasta do backend:
   ```bash
   cd module-1/01-introducao-backend
   ```
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Crie um arquivo `.env` com as seguintes variáveis (preencha com seus dados do Azure OpenAI):
   ```env
   AZURE_OPENAI_API_KEY=xxxxxx
   AZURE_OPENAI_ENDPOINT=https://<seu-endpoint>.openai.azure.com/
   AZURE_OPENAI_API_VERSION=2023-05-15
   AZURE_OPENAI_DEPLOYMENT_NAME=<nome-do-deployment>
   ```
5. Execute o backend:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8001
   ```
   O backend estará disponível em http://localhost:8001

### 4. Configurando o front-end

1. Acesse a pasta do front-end:
   ```bash
   cd ../02-front-end
   ```
2. Basta abrir o arquivo `index.html` no navegador (duplo clique ou `open index.html`).
   - Se quiser servir via servidor local (opcional):
     ```bash
     npx serve .
     # ou
     python -m http.server 8080
     ```
3. O front-end espera que o backend esteja rodando em http://localhost:8001

---

## Cuidados e dicas
- **Azure OpenAI:** Certifique-se de que seu deployment está ativo e as variáveis do `.env` estão corretas.
- **CORS:** O backend já está configurado para aceitar requisições de qualquer origem, mas se for usar em produção, ajuste as origens permitidas.
- **Limite de tokens:** O modelo do Azure OpenAI pode ter limites de tokens. Ajuste `max_tokens` se necessário.
- **Impressão do grafo:** O botão "Imprimir Grafo" exporta a visualização atual do grafo como imagem para impressão ou PDF.
- **Formato do JSON:** O front-end espera o JSON no formato retornado pelo backend. Se mudar o backend, ajuste o front-end conforme necessário.
- **Portas:** Certifique-se de que as portas 8001 (backend) e 8080 (front-end, se usar servidor) estejam livres.

---

## Estrutura do projeto
```
stride-demo/
│
├── module-1/
│   ├── 01-introducao-backend/
│   │   ├── main.py
│   │   ├── requirements.txt
│   │   └── .env (crie este arquivo)
│   └── 02-front-end/
│       └── index.html
└── README.md
```

---

## Dúvidas?
Só chamar que podemos ajudar ! 
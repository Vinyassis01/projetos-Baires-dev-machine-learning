## Sistema de Detecção de Vulnerabilidades

<p align='center'>
Um programa que utiliza inteligência artificial para analisar desenhos<br>
de arquitetura e gerar modelos de ameaças baseados na metodologia STRIDE.<br>
O sistema possui um backend desenvolvido com FastAPI e um front-end<br>
interativo que exibe os resultados em forma de grafo.<br>
</p>

## Como funciona

<p align='center'>
O sistema é dividido em duas partes:<br>
<li> **Backend**: Processa os dados enviados pelo usuário, incluindo imagens<br>
e informações sobre a aplicação, e utiliza a API Gemini para gerar<br>
modelos de ameaças e sugestões de melhorias.
<li> **Front-end**: Permite ao usuário enviar os dados para análise e exibe<br>
os resultados em forma de grafo interativo utilizando Cytoscape.<br>
</p>

## Como usar

<p>Instale as bibliotecas necessárias:</p>

### Backend
```bash
pip install -r requirements.txt
```

### Front-end
Certifique-se de que o arquivo `index.html` está configurado corretamente e pode ser acessado por um navegador.

<p>Execute o backend:</p>

1. Configure sua chave de API no arquivo `.env`:
```plaintext
GEMINI_API_KEY="sua chave da api aqui"
GEMINI_API_URL="https://seu_link_aqui"
```

2. Inicie o servidor FastAPI:
```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

<p>Utilize o front-end:</p>

1. Abra o arquivo `index.html` em um navegador.
2. Preencha os campos do formulário:
   - **Desenho de Arquitetura**: Faça upload de uma imagem.
   - **Tipo de Aplicação**: Descreva o tipo de aplicação.
   - **Métodos de Autenticação**: Informe os métodos utilizados.
   - **Exposta na Internet**: Escolha "Sim" ou "Não".
   - **Dados Sensíveis**: Liste os dados sensíveis utilizados.
   - **Descrição da Aplicação**: Forneça uma descrição detalhada.
3. Clique no botão "Analisar" para enviar os dados ao backend.
4. Visualize os resultados no grafo interativo.

## Precauções

<p>
- Certifique-se de que a chave de API está configurada corretamente no arquivo `.env`.<br>
- Utilize imagens no formato suportado (`.png`, `.jpg`, etc.) para evitar erros.<br>
- Para evitar problemas de permissão, execute o backend em um ambiente com acesso<br>
de escrita ao diretório temporário.<br>
- Certifique-se de que o navegador suporta JavaScript para exibir o grafo.<br>
- Configure o ambiente para permitir conexões entre o front-end e o backend.<br>
</p>
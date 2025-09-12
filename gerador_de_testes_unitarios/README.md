## Gerador de Testes Unitários

<p align='center'>
Um programa simples que utiliza inteligência artificial para analisar arquivos<br>
e gerar testes unitários com base em sua arquitetura e funcionalidade.<br>
O programa também permite salvar os logs gerados em diferentes formatos<br>
como `.txt` ou `.pdf`.
</p>

## Como funciona

<p align='center'>
O programa utiliza as bibliotecas `flet` para criar uma interface gráfica<br>
e `google.generativeai` para interagir com a API de inteligência artificial.<br>
A partir de um arquivo fornecido pelo usuário, o programa analisa o conteúdo<br>
e gera um teste unitário adaptado ao tipo de arquivo selecionado.<br>
Os logs gerados podem ser salvos em formatos `.txt` ou `.pdf`.<br>
</p>

## Como usar

<p>Instale as bibliotecas necessárias:</p>

```bash
pip install flet
pip install google-generativeai
pip install fpdf
pip install python-dotenv
```

<p>Configure sua chave de API:</p>

1. Abra o arquivo `.env` na pasta do projeto.
2. Insira sua chave de API no campo `GEMINI_API_KEY` e a URL base no campo `GEMINI_API_URL`.

Exemplo:
```plaintext
GEMINI_API_KEY="sua chave da api aqui"
GEMINI_API_URL="https://seu_link_aqui"
```

<p>Execute o programa:</p>

```bash
python main.py
```

<p>Na interface:</p>
1. Insira o caminho do arquivo a ser analisado.
2. Escolha o tipo de teste a ser gerado (`banco de dados`, `função` ou `valor`).
3. Escolha o formato do log (`arquivo.txt` ou `arquivo.pdf`).
4. Clique no botão "Gerar Log".

<p>O arquivo gerado será salvo na pasta local.</p>

## Precauções

<p>
- Certifique-se de que sua chave de API está configurada corretamente no arquivo `.env`.<br>
- Para evitar problemas com permissões, execute o programa em um ambiente onde você tenha<br>
  acesso de escrita à pasta local.<br>
- Instale todas as dependências antes de executar o programa.<br>
- Para evitar problemas com display no `flet`, certifique-se de que o ambiente gráfico<br>
  está configurado corretamente no sistema operacional.
</p>

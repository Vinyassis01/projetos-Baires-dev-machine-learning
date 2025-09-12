## Redução de Dimensionalidade de Imagens

<p align='center'>
Um programa simples que utiliza a biblioteca `Pillow` para converter imagens<br>
em escala de cinza e aplicar uma redução de dimensionalidade, escurecendo<br>
as áreas da imagem com base em um limiar definido.<br>
O programa também utiliza `matplotlib` para exibir as imagens processadas.<br>
</p>

## Como funciona

<p align='center'>
O programa possui duas funções principais:<br>
<li> `img_to_gray`: Converte uma imagem colorida para escala de cinza.
<li> `img_to_dark`: Escurece a imagem em escala de cinza com base em um limiar.<br>
A partir de uma imagem fornecida pelo usuário, o programa gera duas novas imagens:<br>
uma em escala de cinza e outra escurecida.<br>
</p>

## Como usar

<p>Instale as bibliotecas necessárias:</p>

```bash
pip install pillow
pip install matplotlib
```
Aqui está um exemplo de arquivo README.md para o projeto de redução de dimensionalidade de imagens:

<p>Execute o script:</p>

1. Certifique-se de que a imagem original está no mesmo diretório do script ou forneça o caminho correto.
2. No arquivo `imag_to_grey_dark.py`, modifique os caminhos das imagens conforme necessário:

```python
# Substitua "/imagem.png" pelo caminho da sua imagem original
imagem_cinza = img_to_gray("/imagem.png")

# Substitua "/imagem_cinza.jpg" pelo caminho da imagem gerada em escala de cinza
imagem_escura = img_to_dark("/imagem_cinza.jpg")
```

3. Execute o script:

```bash
python imag_to_grey_dark.py
```

<p>Visualize os resultados:</p>
- A imagem em escala de cinza será salva como `imagem_cinza.jpg`.
- A imagem escurecida será salva como `imagem_escura.jpg`.

## Precauções

<p>
- Certifique-se de que os caminhos das imagens estão corretos.<br>
- Utilize imagens no formato suportado pela biblioteca `Pillow` (como `.jpg`, `.png`).<br>
- Para evitar problemas de permissão, execute o script em um diretório onde você tenha<br>
  acesso de escrita.<br>
- Ajuste o valor do limiar na função `img_to_dark` conforme necessário para obter<br>
  os resultados desejados.<br>
</p>

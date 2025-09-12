## Sistema de Recomendação por Similaridade

<p align='center'>
Um programa que utiliza aprendizado de máquina para classificar imagens<br>
e recomendar itens semelhantes com base em características extraídas.<br>
O sistema utiliza o dataset Fashion-MNIST e bibliotecas como `scikit-learn`,<br>
`matplotlib` e `opencv` para realizar as classificações e exibir os resultados.<br>
</p>

## Como funciona

<p align='center'>
O sistema possui as seguintes etapas:<br>
<li> Carregamento do dataset Fashion-MNIST.
<li> Treinamento de um modelo de classificação utilizando `SGDClassifier`.
<li> Classificação de novas imagens e recomendação de itens semelhantes.
<li> Exibição das imagens recomendadas utilizando `matplotlib`.<br>
A partir de uma imagem fornecida pelo usuário, o sistema identifica<br>
o rótulo e recomenda até 10 itens semelhantes.<br>
</p>

## Como usar

<p>Instale as bibliotecas necessárias:</p>

```bash
pip install scikit-learn
pip install matplotlib
pip install opencv-python
```

<p>Execute o script:</p>

1. Certifique-se de que as imagens estão no mesmo diretório do script ou forneça o caminho correto.
2. No arquivo `classification_recomendation.py`, modifique o caminho da imagem conforme necessário:

```python
# Substitua "/caminho/para/imagem.jpg" pelo caminho da sua imagem
image_path = "/caminho/para/imagem.jpg"
```

3. Execute o script:

```bash
python classification_recomendation.py
```

<p>Visualize os resultados:</p>
- O rótulo da imagem será exibido no console.
- Até 10 imagens semelhantes serão exibidas em uma janela gráfica.

## Precauções

<p>
- Certifique-se de que as imagens fornecidas estão no formato correto (`.jpg`, `.png`, etc.).<br>
- Instale todas as dependências antes de executar o script.<br>
- Para evitar problemas de memória, utilize imagens com resolução adequada.<br>
- Certifique-se de que o ambiente gráfico está configurado corretamente para exibir os resultados.<br>
</p>
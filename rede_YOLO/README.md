## Rede YOLO

<p align='center'>
Um programa que utiliza a framework Darknet para treinar e executar<br>
modelos de detecção de objetos utilizando YOLOv3.<br>
O projeto inclui um notebook configurado para ser executado no Google Colab<br>
com suporte a GPU, permitindo treinar modelos de forma eficiente.<br>
</p>

## Como funciona

<p align='center'>
O notebook `Tutorial_DarknetToColab(1).ipynb` guia o usuário por todas as etapas<br>
necessárias para configurar o ambiente, treinar o modelo YOLOv3 e realizar<br>
detecções em novas imagens.<br>
As etapas incluem:<br>
<li> Configuração do ambiente no Google Colab com suporte a GPU.
<li> Clonagem e compilação do repositório Darknet.
<li> Treinamento do modelo YOLOv3 com um conjunto de dados personalizado.
<li> Detecção de objetos em imagens utilizando o modelo treinado.
</p>

## Como usar

<p>Instale as bibliotecas necessárias:</p>

```bash
pip install matplotlib
pip install opencv-python
pip install google-colab
```

<p>Execute o notebook:</p>

1. Abra o arquivo `Tutorial_DarknetToColab(1).ipynb` no Google Colab.
2. Configure o ambiente para usar GPU:
   - Vá em **Menu > Runtime > Change runtime type** e selecione **GPU**.
3. Siga as instruções no notebook para:
   - Montar o Google Drive.
   - Clonar e compilar o repositório Darknet.
   - Configurar os arquivos de treinamento (como `obj.data`, `train.txt` e `yolov3.cfg`).
   - Treinar o modelo YOLOv3.
   - Realizar detecções em novas imagens.

<p>Exemplo de detecção:</p>

```python
# Substitua 'caminho/para/sua/imagem.jpg' pelo caminho real para a sua imagem
image_path = '/content/gdrive/My Drive/darknet/img/test_image.jpg'
weights_path = '/content/gdrive/My Drive/darknet/weights/yolov_last.weights'

# Execute o Darknet para detecção
!./darknet detector test "/content/gdrive/My Drive/darknet/obj.data" "/content/gdrive/My Drive/darknet/yolov3.cfg" {weights_path} {image_path} -thresh 0.25 -dont_show

# Exiba a imagem com as detecções
imShow('predictions.jpg')
```

## Precauções

<p>
- Certifique-se de que os arquivos de configuração (`obj.data`, `train.txt`, `yolov3.cfg`) estão corretamente configurados.<br>
- Verifique se os caminhos para os arquivos no Google Drive estão corretos.<br>
- Para evitar problemas de memória, ajuste os parâmetros `batch` e `subdivisions` no arquivo `yolov3.cfg`.<br>
- Certifique-se de que o ambiente está configurado para usar GPU no Google Colab.<br>
- Utilize imagens de alta qualidade para melhores resultados na detecção.<br>
</p>

## Reconhecimento Facial

<p align='center'>
Um programa simples que utiliza a biblioteca `MTCNN` para detectar rostos<br>
em imagens e destacar as áreas identificadas com retângulos.<br>
O programa também utiliza `matplotlib` para exibir as imagens processadas.<br>
</p>

## Como funciona

<p align='center'>
O programa utiliza a biblioteca `MTCNN` para detectar rostos em imagens.<br>
A partir de uma imagem fornecida pelo usuário, o detector identifica<br>
as coordenadas dos rostos e desenha retângulos ao redor deles.<br>
O resultado é exibido utilizando a biblioteca `matplotlib`.<br>
</p>

## Como usar

<p>Instale as bibliotecas necessárias:</p>

```bash
pip install mtcnn
pip install matplotlib
```

Aqui está um exemplo de arquivo README.md para o projeto de reconhecimento facial:

## Reconhecimento Facial

<p align='center'>
Um programa simples que utiliza a biblioteca `MTCNN` para detectar rostos<br>
em imagens e destacar as áreas identificadas com retângulos.<br>
O programa também utiliza `matplotlib` para exibir as imagens processadas.<br>
</p>

## Como funciona

<p align='center'>
O programa utiliza a biblioteca `MTCNN` para detectar rostos em imagens.<br>
A partir de uma imagem fornecida pelo usuário, o detector identifica<br>
as coordenadas dos rostos e desenha retângulos ao redor deles.<br>
O resultado é exibido utilizando a biblioteca `matplotlib`.<br>
</p>

## Como usar

<p>Instale as bibliotecas necessárias:</p>

```bash
pip install mtcnn
pip install matplotlib
```

<p>Execute o arquivo Jupyter Notebook:</p>

1. Abra o arquivo `reconhecimento_facial.ipynb` em um editor de notebooks, como Jupyter ou VS Code.
2. Certifique-se de que a imagem `pexels-pixabay-415829.jpg` está na mesma pasta do notebook.
3. Execute as células do notebook para carregar a imagem, detectar os rostos e exibir o resultado.

Exemplo de código no notebook:
```python
from mtcnn import MTCNN
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

# Carregar a imagem
img = plt.imread('pexels-pixabay-415829.jpg')

# Detectar rostos
detector = MTCNN()
faces = detector.detect_faces(img)

# Desenhar retângulos ao redor dos rostos
def imagens(img, faces):
    ax = plt.gca()
    for face in faces:
        x, y, width, height = face['box']
        rect = Rectangle((x, y), width, height, color='blue', fill=False, lw=4)
        ax.add_patch(rect)
    plt.imshow(img)

imagens(img, faces)
plt.show()
```

## Precauções

<p>
- Certifique-se de que a imagem fornecida está no formato correto (`.jpg`, `.png`, etc.).<br>
- Instale todas as dependências antes de executar o notebook.<br>
- Para evitar problemas com visualizações, certifique-se de que o ambiente gráfico<br>
  está configurado corretamente no sistema operacional.<br>
- Utilize imagens com boa resolução para melhores resultados na detecção.<br>
</p>
from PIL import Image
from matplotlib import pyplot as plt
def img_to_gray (path_img):
    imagem = Image.open(path_img)
    imagem_cinza = imagem.convert("L")  # Convert to grayscale
    imagem_cinza.save("imagem_cinza.jpg")
    return imagem_cinza

def img_to_dark (path_img_gray):
    imagem = Image.open(path_img_gray)
#    imagem_escura = imagem.point(lambda p: p * 1.0)  # Darken the image
    limiar = 128  # Ajustlambda x: 255 if x > limiar else 0, '1'e conforme necessário
    x = lambda x: 255 if x > limiar else 0
    imagem_escura = imagem_cinza.point(x)
    imagem_escura.save("imagem_escura.jpg")
    return imagem_escura
#colocar uma caminho para uma imagem qualquer
imagem_cinza = img_to_gray("/imagem.png")
# colocar o caminho da imagem cinza
# que foi criada no passo anterior
imagem_escura = img_to_dark("/imagem_cinza.jpg")

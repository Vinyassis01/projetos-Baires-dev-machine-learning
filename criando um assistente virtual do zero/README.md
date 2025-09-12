## assistente virtual 

<p align='center'>
um programa simples q converte um texto para um audio<br>
 e a partir deste audio ,o salva na pasta local como um arquivo<br>
 que pode ser reproduzido no sistema normalmente e a partir<br>
 deste arquivo o converte novamente para um texto que sera <br>
 usado como comando para um a automacao no sistema<br>
 acoes que podem ser :<br>
 <li> Abrir o Youtube
 <li> Abrir o Whatsapp web
 <li> Abrir o Firefox
 <li> Abrir o Google
<p>

## como funciona 
<p align='center'>
atraves das bibliotecas speech recogntion que reconhece e <br>
formata arquivos de audio ,OS que nos permite manipular<br> acoes do sistema operacional essa que usamos para salvar o audio<br>
e a principal o pyautogui que e o centro das nossas automacoes<br>
que nos permite automatizar acoes de mouse e teclado<br>
e o gTTs que nos permite mais opcoes de configuracoes
</p>

## Como usar 
<p> instalar as bibliotecas necessarias</p>

```bash
    pip install gTTs
    pip install pyautogui
    pip install SpeechRecognition
```
<p>
acesse o arquivo com um editor de codigo de sua preferencia<br> e modifique a variavel
teste 

```bash
text="comando para uma automacao"
```

<p>para salvar o audio defina a variavel correta</p>

```bash
# os.system("start output.mp4") # Para Windows
# os.system("afplay output.mp4") # Para macOS
os.system("mpg321 output.mp4") # Para linux
# Para Linux instale mpg321 primeiro: sudo apt-get install mpg321)
```
<p>para evitar problemas com display no pyautogui rode este comando no terminal :

```bash
xhost +
```
## Métricas de Avaliação de Desempenho

<p align='center'>
Um programa simples que utiliza a biblioteca `sklearn` para calcular<br>
métricas de avaliação de desempenho, como matriz de confusão,<br>
acurácia, precisão, sensibilidade, especificidade e F-score.<br>
O programa também gera visualizações utilizando `matplotlib`.<br>
</p>

## Como funciona

<p align='center'>
O programa utiliza a biblioteca `sklearn` para calcular a matriz de confusão<br>
com base em valores de predições e rótulos fornecidos pelo usuário.<br>
A partir da matriz de confusão, são calculadas métricas como acurácia,<br>
precisão, sensibilidade, especificidade e F-score.<br>
Além disso, o programa gera gráficos para visualização dos resultados.<br>
</p>

## Como usar

<p>Instale as bibliotecas necessárias:</p>

```bash
pip install scikit-learn
pip install matplotlib
```

<p>Execute o arquivo Jupyter Notebook:</p>

1. Abra o arquivo `matriz_de_confusao.ipynb` em um editor de notebooks, como Jupyter ou VS Code.
2. Insira os valores de predições e rótulos nas variáveis `predictions` e `labels`.

Exemplo:
```python
predictions = [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0]
labels = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1]
```

3. Execute as células do notebook para calcular as métricas e gerar os gráficos.

<p>Visualize os resultados:</p>
- A matriz de confusão será exibida no console.
- As métricas calculadas (acurácia, precisão, sensibilidade, especificidade e F-score) serão exibidas no console.
- Os gráficos gerados serão exibidos na interface do notebook.

## Precauções
<p>
- Certifique-se de que os valores de predições e rótulos têm o mesmo tamanho.<br>
- Instale todas as dependências antes de executar o notebook.<br>
- Para evitar problemas com visualizações, certifique-se de que o ambiente gráfico<br>
  está configurado corretamente no sistema operacional.<br>
- Utilize versões compatíveis das bibliotecas `matplotlib` e `sklearn`.<br>
</p>


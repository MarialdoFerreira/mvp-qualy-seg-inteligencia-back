# MVP - Qualidade, Segura e Sistemas inteligentes - Frontend

Aluno: **Marialdo Ramalho Ferreira**

O projeto do Sistema Intelegente para Análise de Crédito toma com base o dataset extraido do site:

**https://www.kaggle.com/code/eduardovbernardino/analise-de-dados-credito-ebac**

**Dataset tratado na fase de Manipulação de dados foi disponibilizado na pasta do GitHub, no link abaixo:**

Link: "https://raw.githubusercontent.com/MarialdoFerreira/mvp-qualy-seg-inteligencia-back/refs/heads/main/MachineLearning/data/credito-preprocessado.csv"

A escolha deste assunto, deve a afinidade com a área de trabalho que atuo.  
Este projeto foi desenvolvido visando colocar em prática os conhecimentos adquiridos nesta disciplina.

Tem por objetivo fazer a predição do cliente se tornar **Inadimplemte** ao contrair finaciamento de crédito na instituição finaceira.
Esta predição tem por base as observações de dados semelhantes aos do cliente, utilizando para análise os algoritmos de matemáticos e estatisticos.

---

## Como executar

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas, é bem simples o processo.

Após clonar o repositório, é necessário ir ao diretório raiz do projeto, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte.

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
ou
flask --app app run --debug
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

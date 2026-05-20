# Linguagem Lox

Este é o código fonte para o interpretador de Lox que será desenvolvido ao 
longo do curso. O código é testado usando a biblioteca Pytest e os testes
estão localizados na pasta `tests`.

Se você seguir uma estrura parecida com a do repostório do livro ou do código
produzido em sala de aula, os testes provavelmente serão capazes de encontrar o
seu código automaticamente. Caso contrário, ou caso queira utilizar outras
linguagens que não sejam o Python, consulte o professor.

Para instalar o ambiente de desenvolvimento, recomendo usar a ferramenta
[uv](https://docs.astral.sh/uv/). Siga as instruções de instalação por lá e use
o interpretador com o comando

    $ uv run pylox
    
## Rodando testes

Os testes automáticos podem ser executados com o comando

    $ uv run pytest

Se quiser maior controle, estude as opções que o pytest disponibiliza passando a
flag `--help`. O comando abaixo, por exemplo, mostra somente a primeira falha e
limita os testes ao módulo 08_control_flow.

    $ uv run pytest --maxfail=1 -k control_flow

Algumas opções úteis:

* `-k EXPRESSION` - Executa somente os testes cujo nome case com a expressão.
* `--maxfail=N` - Para após N falhas.
* `-v` - Modo verboso, mostra mais detalhes.
* `-q` - Modo silencioso, mostra menos detalhes.
* `--tb=no` ou `--tb=short` - Controla o estilo do traceback.
* `--lf` - Executa somente os testes que falharam na última execução.

## Pontuação

A pontuação total da atividade é proporcional ao número de testes que passam. 

No primeiro ponto de controle, executarei os testes dos capítulos 08 e 09. Estes
testes valem 30% da nota total e a data de entrega é no mesmo dia que a segunda
prova.

No segundo ponto de controle, executarei TODOS os testes para contabilizar os 60%
restantes da nota. A data de entrega é no mesmo dia que a terceira prova. 

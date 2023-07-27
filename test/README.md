# Unit tests using Unity framework for C

> Framework para testes unitários de programas do pacote Madagascar utilizando o 'Unity framework for C'

## Quick start

Para começar a utilizar este framework com um teste simples, basta rodar o 'Makefile' deste diretório utilizando
o comando a seguir:

```
make
```

O 'Makefile' irá compilar e rodar o teste 'test_example.c' disponível no diretório. Se precisar de ajuda e informações
sobre os comandos disponíveis utilize o comando 'make help'.

## Criando um teste

Para criar um teste para um programa do Madagascar basta listar o diretório do programa na sua instalação local
do Madagascar em '$RSFSRC/user' na variável 'SRC_DIR' do arquivo 'Makefile' deste diretório. E também listar as
dependências dos testes na variável 'DEP_LIST' do arquivo 'Makefile' deste diretório.

O 'Makefile' está configurado para gerar uma biblioteca estática com as dependências e compilar os testes utilizando
esta bilbioteca. Os testes são identificados pelo prefixo 'test_' e extensão '.c'. Os arquivos da pasta com esta extensão
e prefixo serão compilados como e, os executáveis gerados serão executados. Veja o exemplo a seguir:

```
# Put your source directory name here (your directory name inside $RFSRC/user)
SRC_DIR := velModelInterpolator
# Tests list will be extracted from current folder (Search files with test_*.c pattern)
TESTS := $(patsubst %.c,%.x,$(wildcard test_*.c))
# List your tests dependencies here (No '.c' extension)
DEP_LIST := velocity
```

Neste exemplo, o diretório 'velModelInterpolator', listado em 'SRC_DIR' será o diretório de onde serão buscadas as dependências.
No exemplo, apenas a dependência 'velocity' foi listada em 'DEP_LIST'. Ou seja, será gerada uma biblioteca estática
a partir da compilação do arquivo 'velocity.c' presente na pasta '$RSFSRC/user/velModelInterpolator'.

Os testes serão compilados utilizando a biblioteca estática gerada e as dependências do Unity na pasta 'Unity' deste
diretório.


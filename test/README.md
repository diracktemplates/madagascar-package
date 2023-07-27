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
dependências e o arquivo principal na variável 'DEP_LIST' do arquivo 'Makefile' deste diretório.

```
# Put your source directory name here (your directory name inside $RFSRC/user)
SRC_DIR :=
# Tests list will be extracted from current folder (Search files with test_*.c pattern)
TESTS := $(patsubst %.c,%.x,$(wildcard test_*.c))
# List your tests dependencies here (No '.c' extension)
DEP_LIST :=
```
```

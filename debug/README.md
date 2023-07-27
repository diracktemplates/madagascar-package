# Program versions for debug with GNU Debugger (GDB)

> Framework para debug de programas do pacote Madagascar utilizando o GNU Debugger (GDB)

## Quick start

Para começar a utilizar este framework, basta rodar o 'Makefile' deste diretório utilizando o comando a seguir:

```
make
```

O 'Makefile' irá compilar a versão para GDB de 'example.c' disponível no diretório. Se precisar de ajuda e informações sobre os comandos disponíveis utilize o comando 'make help'.

Você poderá rodar 'example.c' no modo de debug com:

```sh
make example.debug
```

Ou, se quiser, gerar a versão para o debug com GDB com o comando:

```sh
make example.gdbx
```

## Rodar um programa principal do Madagascar em modo debug com GDB

Para rodar um programa do Madagascar em modo debug basta listar o diretório do programa na sua instalação local do Madagascar
em '$RSFSRC/user' na variável 'SRC_DIR' do arquivo 'Makefile' deste diretório.
E também listar as dependências do programa na variável 'DEP_LIST' do arquivo 'Makefile' deste diretório.

O 'Makefile' está configurado para gerar uma biblioteca estática com as dependências e compilar o programa principal utilizando
esta bilbioteca. Veja o exemplo a seguir:

```
# Put your source directory name here (your directory name inside $RFSRC/user)
SRC_DIR := velModelInterpolator
# List the main programs here (No 'M' or 'sf' preffix nor extension)
PROGRAMS_LIST := velinterp
# List your programs dependencies here (No '.c' extension)
DEP_LIST := velocity
```
Neste exemplo, o diretório 'velModelInterpolator', listado em 'SRC_DIR' será o diretório de onde serão buscadas as dependências
e o programa principal listado em 'PROGRAMS_LIST'. No exemplo, apenas a dependência 'velocity' foi listada em 'DEP_LIST'.
Ou seja, será gerada uma biblioteca estática a partir da compilação do arquivo 'velocity.c' presente na pasta
'$RSFSRC/user/velModelInterpolator'. O programa principal será gerado na versão do GDB.

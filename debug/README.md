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

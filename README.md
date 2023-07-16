# Madagascar Package

> Template para o desenvolvimento de um pacote do Madagascar

## Arquivos templates para desenvolvimento de programas do Madagascar

Você pode utilizar os templates deste repositório para a criação de novos programas do Madagascar:

- __M2dtemplate.c:__ Exemplo de leitura e escrita de arquivo 2D do Madagascar. Lê um modelo de velocidades
e retorna o slowness. Teste o template com o comando a seguir:
```
sfmath output="1.5" n1=301 d1=0.01 o1=0 n2=1001 d2=0.01 o2=-2.| sf2dtemplate | sfgrey scalebar=y | sfpen
```

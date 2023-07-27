# Madagascar Package

> Template para o desenvolvimento de um pacote do Madagascar

## Arquivos templates para desenvolvimento de programas do Madagascar

Você pode utilizar os templates deste repositório para a criação de novos programas do Madagascar (Para saber como
fazer a instalação destes templates veja a próxima seção):

- __M2dtemplate.c:__ Exemplo de leitura e escrita de arquivo 2D do Madagascar. Lê um modelo de velocidades
e retorna o slowness. Teste o template com o comando a seguir:
```
sfmath output="1.5" n1=301 d1=0.01 o1=0 n2=1001 d2=0.01 o2=-2.| sf2dtemplate | sfgrey scalebar=y | sfpen
```

- __Mpytemplate.py:__ Exemplo de programa python do Madagascar. Conversor de arquivo txt para arquivo asc lido pelo
programa sfdd do Madagascar. O arquivo gerado pode ser convertido depois para RSF utilizando o sfdd. Para testar o programa
sfpytemplate, basta utilizar os seguintes comandos (os parâmetros recebidos pelo programa são o nome do arquivo de saída a
ser gerado e a coluna a ser lida do arquivo txt lido):
```
echo -e "1 2 3\n4 5 6" > file.txt
<file.txt pytemplate output.asc 1 > output.asc
sfdd <output.asc form=native type=float
```

## Instalação

Este repositório deve ser instalado dentro da pasta '$RSFSRC/user' da sua instalação local do pacote Madagascar. Após a instalação,
você poderá utilizar o script 'SConstruct' na raíz deste repositório para realizar a compilação dos programas templates. Basta
rodar o script 'SConstruct' com o comando a seguir:

```
scons
```

Após a compilação, você poderá instalar os programas templates deste repositório na sua instalação local do Madagascar. Basta
utilizar o comando a seguir:

```
sudo scons install
```

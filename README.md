# Bot Jubesvaldo  

O bot jubesvaldo foi criado com o intuito de poder exercer multiplas funções no **Servidor do Becario**, como moderação, funções de conversa, funções para jogos e funções para estudo.  

Caso queira testar este projeto em um servidor privado, você pode encontraralgumas instruções de como fazê-lo neste [parágrafo](#testando-o-projeto).

> [!IMPORTANT]  
Este bot ainda não está pronto, e pode não conter todas as funções necessárias e também pode conter erros que ainda serão corrigidos

## Sobre o bot
### Funções de moderação

O bot jubesvaldo tem duas funções de moderação caracterizadas como eventos.

A primeira função identifica menssagens que contenham algum palavrão e a segunda função identifica menssagens que tenham sido editadas e contenham algum palavrão.

Mesmo que o palavrão utilizado seja composto por mais de uma palavra ele ainda será identificado pois é utilizado regex para transformar cada termo da lista dentro do código em um padrão que o código pode identificar um palavrão dentro da menssagem.

> [!WARNING]  
> A lista que pode ser encontrada dentro do código pode estar incompleta e pode não identificar todos os palavrões.

## Testando o projeto
### Bibliotecas necessárias

Para testar este projeto será necessário instalar as bibliotecas do discord, do postgreSQL e do python-dotenv e para isso será necessário rodar em seu terminal este comando: `pip install -r requirements.txt`
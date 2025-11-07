# Bot Jubesvaldo  

O bot jubesvaldo foi criado com o intuito de poder exercer multiplas funções no **Servidor do Becario**, como moderação, funções de conversa, funções para jogos e funções para estudo.  

Caso queira testar este projeto em um servidor privado, você pode encontrar algumas instruções de como fazê-lo neste [parágrafo](#testando-o-projeto).

> [!IMPORTANT]  
> Este bot ainda não está pronto e pode não conter todas as funções necessárias para plena execução de seus objetivos e também pode conter erros que ainda serão corrigidos.

## Sobre o bot
### Funções de moderação

O bot jubesvaldo tem duas funções de moderação caracterizadas como eventos.

A primeira função identifica menssagens que foram enviadas no servidor que contenham algum palavrão e a segunda função identifica menssagens no servidor que tenham sido editadas e contenham algum palavrão.

Mesmo que o palavrão utilizado seja composto por mais de uma palavra ele ainda será identificado pois é utilizado regex para transformar cada termo da lista dentro do código em um padrão que o código possa identificar um palavrão dentro da menssagem.

> [!WARNING]  
> A lista que pode ser encontrada dentro do código pode estar incompleta e pode não identificar todos os palavrões possiveis.

### Testando o projeto

### Ferramentas necessárias
O bot utiliza um banco de dados postgresSQL, então será necessário ter instalado em sua máquina o postgreSQL.

### Bibliotecas necessárias

Para testar este projeto será necessário instalar as bibliotecas do discord, do postgreSQL e do python-dotenv e para isso será necessário rodar em seu terminal este comando: `pip install -r requirements.txt`

### Arquivo necessário

Para testar o projeto também é necessário ter um arquivo .env onde seram armazenados o token do bot, o id do servidor, o id de uma categoria do servidor, os ids dos canais que seram utilizados e o id do usuário do discord.

Basta criar um arquivo chamado **.env** na raíz do projeto e adicionar uma estrutura como a apresentada abaixo:
``` 
DISCORD_TOKEN = "token do bot"
ADM_ID = "id do usuário"
GUILD_ID = "id so servidor"
CATEGORY_ID = "id da categoria"
CONVERSATION_ID = "id do canal"
WELCOME_CHANNEL_ID = "id do canal"
```

> [!IMPORTANT]  
> Caso esteja testando em um sistema linux também será importante colocar nesse arquivo o usuário, a senha e a porta do seu banco de dados.
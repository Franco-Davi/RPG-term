# RPG-Term
Este é um projeto de estudos de objeto em python, criei isso como uma forma de testar e aprender os meus conhecimentos com classes, objetos e algumas bibliotecas interessantes sobre as quais havia lido, Argparse e Rich.

## O que é?

Se trata de um RPG de texto estilo aqueles antigos jogos de pc, quando ainda não não tinhamos interfaces gráficas. Claro, este projeto conta com algumas modernidades que facilitam e muito a sua criação.

## Como surgiu a ideia?

Tive essa ideia apartir de um vídeo que vi uma vez sobre um mestre do famoso D&D que havia inventado uma forma de criar "loot boxes" dentro do jogo, criando itens aleatórios com tabelas. Logo tive a ideia de criar uma forma de automatizar esse processo pois era muito demorado gerar os itens em mesa. Algum tempo depois conheci o jogo Four Against Darkness, um RPG solo muito interessante que me deu a ideia de transformar meu gerador de itens em um rogue like (genero de jogos eletrônicos do qual sou muito fã). E por fim, logo antes de começar este projeto da forma como está sendo executado hoje tive a ideia de transformar o antigo explorador de dungeons em um rpg completo, com cidades, castelos, NPCs, masmorras, itens encantados para colecionar e criaturas terríveis para enfrentar.

Ainda quero deixar este código de certa forma "modular", permitindo que outras histórias possam ser contadas apartir dessa mesma forma de narrar.

## To-Do

- [x] Sistema de leitura de comandos com argumentos usando Argparse;
- [x] Comandos básicos para teste como 'quit', 'screen' e 'echo';
- [x] Sistema de log;
- [x] Sistema de escolha de layout para diferentes momentos do jogo;
- [x] Criação da classe Player para armazenar os atributos do jogador e os metodos para ações;
- [x] Sistema de salvamente e carregamento com json;
- [x] Adição de um comando 'help' para ajudar na utilização do jogo sem consulta externa;
- [ ] Criação de um sistema de inventário com lista;
- [ ] Sistema de progressão de jogo estilo livro-jogo apartir da leitura de um json;
- [ ] Criação de um sistema de combate;
- [ ] Adicionar a possibilidade de itens com efeitos, desde simples proteção de armadura, até resistências e outras vantagens mágicas;
- [ ] Adicionar sistema de magia.
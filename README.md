# Zoom Archive Downloader
> Realiza o download de arquivos do zoom através da sua API, ele pode realizar o download de diversos usuários dentro de uma única sessão e os downloads são designados para pastas específicas com o nome/e-mail dos usuários.  

[![NPM Version][npm-image]][npm-url]
[![Build Status][travis-image]][travis-url]

## Compilar o projeto
Primeiro faça um clone desse repositório em algum local no seu computador
```
git clone https://github.com/LucasPanao/downZoom.git
```

Quando o clone estiver terminado, apenas execute o comando abaixo para instalar todas as dependências
```
npm install
```

## Exemplo de uso

Esse código foi feito para pessoas ou empresas que contém diversos usuários cadastrados no Zoom Cloud Meeting e desejam baixar os arquivos, para um possível backup local ou hospedar em outros servidores.  

## Configuração para Desenvolvimento

Deve se ter instalado em sua máquina o python e o navegador a ser utilizado deve ser o Google Chrome.  Ao baixar/utilizar o projeto existem 2 arquivos .txt, esses serão os arquivos que o bot irá ler e executar as requisições. 

Dentro do arquivo list_ids.txt devem ser colocados as IDs de todos os usuários que deseja extrair os arquivos de reuniões do zoom. Essas ids serão usadas dentro da requisão GET. 

```sh
[UserId1]
[UserId2]
```

Dentro do arquivo list_emails.txt devem ser colocados os e-mails ou nomes de todos os usuários que deseja extrair os arquivos de reuniões do zoom. Lembrando que deve estar alinhados a sequencia de usuários do list_ids.txt, esses nomes serão usados para criar as pastas da qual as gravações serão encaminhadas. 

```sh
[EmailUsuario1]
[EmailUsuario2]
```


## Histórico de lançamentos

* 1.0.1
    * MUDANÇA: Atualização de docs (código do módulo permanece inalterado)
* 1.0.0
    * O primeiro lançamento adequado

## Meta

Lucas Panão – [@LucasPanao](https://www.linkedin.com/in/lucas-panao/) – contato@panao.com.br

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

[https://github.com/LucasPanao]

## Contributing

1. Faça o _fork_ do projeto (<https://github.com/yourname/yourproject/fork>)
2. Crie uma _branch_ para sua modificação (`git checkout -b feature/fooBar`)
3. Faça o _commit_ (`git commit -am 'Add some fooBar'`)
4. _Push_ (`git push origin feature/fooBar`)
5. Crie um novo _Pull Request_

[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/seunome/seuprojeto/wiki

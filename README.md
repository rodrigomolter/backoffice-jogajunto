# Backoffice JogaJunto 🛒

<div align="center">
  <picture>
    <source srcset="https://www.jogajuntoinstituto.org/image/Logo_about.png" media="(prefers-color-scheme: light)">
    <img title="Instituto Joga Junto" alt="Instituto Joga Junto" href="https://www.jogajuntoinstituto.org/" src="https://github.com/rodrigomolter/qa-institutojogajunto/assets/57466763/acf43fcb-f91a-450d-9291-90b479b07064" width="400px">   
  </picture>
</div>
<br>

O sistema de controle de estoque do Instituto Joga Junto tem como objetivo tornar a experiência de colaboradores o mais intuitiva possível. Fazendo com que os produtos sejam catalogados em uma ordem que faça sentido e seja de simples navegação, tanto para cadastro de colaboradores quanto de produtos.

Este repositório conta com a suíte de **testes automatizados** para o Backoffice JogaJunto.

# Arquitetura
Os testes automatizados foram desenvolvidos utilizando `Python`, `Selenium Webdriver` e `Behave`.<br>
A utilização do Behave nos permite que os casos de testes estejam em Gherkin

Dividídos entre testes **E2E** e testes de **API**, a modelagem propõem o encapsulamento das funcionalidades em métodos e classes bem definidos. Por isso, se optou por utilizar o design patter `Page Objects` para auxiliar no desenvolvimento e principalmente manutenção dos testes.

## Testes E2E
Foram desenvolvidos testes automatizados apenas para o *happy path*[^1] das funcionalidades mais críticas do sistema, dentro do fluxo de:
 - Criação de Usuário
 - Login
 - Cadastro de Produto

## Testes de API
Os testes de API seguem o mesmo fluxo de testar o *happy path*[^1], mas também contam com **testes de contrato**:

 - Criação de Usuário
 - Login
 - Cadastro de Produto
 - Visualização de todos os produtos cadastrados

### Testes no Postman
Para complementar os testes automatizados, foi criada uma collection no Postman que cobre todos os fluxos possíveis da API, tanto positivos quanto negativos.

<a href="https://app.getpostman.com/run-collection/29423847-be72a8cb-9dac-49d5-acda-af47c2667dcb?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D29423847-be72a8cb-9dac-49d5-acda-af47c2667dcb%26entityType%3Dcollection%26workspaceId%3D634d18e6-9a9f-45a7-a562-69e352023655">
  <img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">
</a><br>

# Executando o projeto
Abaixo, um passo-a-passo de como executar os testes localmente.

## Pré-requisitos 📋
- [Python 3.x](https://www.python.org/downloads/) (Eu utilizei a versão `3.11.2` enquanto desenvolvia esse projeto).
- WebDriver do seu navegador (veja mais abaixo).

## WebDrivers
Para executar os testes você precisa instalar a versão do webdriver para o seu navegador.
- [ChromeDriver](https://chromedriver.chromium.org/downloads) for Google Chrome
- [Geckodriver](https://github.com/mozilla/geckodriver/releases/latest) for Firefox.
  
ChromeDriver e geckodriver devem estar presentes no [system path](https://en.wikipedia.org/wiki/PATH_(variable)).

## Virtual Environment 🌲
É recomendado a utilização de um ambiente virtual para a instalação de dependencias. <br>
Dentro da pasta do backoffice-jogajunto execute `python -m venv venv` para criar um ambiente virtual:
```bash
python -m venv venv
```

### Ative o ambiente virtual:

- Windows

```bash
venv\Scripts\activate
```
- Linux/MacOs
  
```bash
venv/bin/activate
```

## Instalação 🏗️
Instale todos os requisitos:
```bash
pip install -r requirements.txt
```

## Configs ⚙️
As configurações como **navegador** e **endpoints** da aplicação podem ser configuradas dentro do arquivo `behave.ini`

Os navegadores suportados são, ambos também no modo `headless`:
- Firefox
- Chrome

Lembrando que é necessário o `webdriver` do navegador escolhido, como citado nos **Pré-requisitos**

##  Rodadando os testes ✔️
Para executar os testes, basta utilizar o comando `behave`

```bash
behave
```

Você também pode executar um `feature file` específico, ou uma pasta
```bash
behave features\API\login.feature
```

## Apoie o projeto 🙌

Se você quiser apoiar o projeto, deixe uma ⭐.

## Aspirantes da Automação 🚀
Desenvolvido pela Squad Aspirantes da Automação durante o módulo avançado do curso **Bugou? QA TA ON** do [Instituto Joga Junto](https://www.jogajuntoinstituto.org/)

[Diogo Reis](https://www.linkedin.com/in/diogorreis/) • 
[George Neres](https://www.linkedin.com/in/george-neres-gsneres/)  • 
[Isadora Silva](https://www.linkedin.com/in/isadorarsilva/)  • 
[Julia Bragada](https://www.linkedin.com/in/juliabragada/)  • 
[Rodrigo Molter](https://www.linkedin.com/in/rodrigo-molter/)

[^1]: Happy Path, ou caminho feliz, são os fluxos que completam com sucesso algum tipo de transação, como por exemplo, um login bem sucedido, a finalização de uma compra em um sistema de e-commerce ou a criação de uma nova conta no sistema.

___
Made with ❤️ by Squad Aspirantes da Automação. <br>

# Consulta-CNPJ
Projeto utilizando API do site 'receitaws' para visualizar algumas informações contidas no CNPJ consultado.

Apenas uma aplicação simples utilizando o módulo TKinter para apresentar as informações.

[![Build Status](https://travis-ci.org/wherculano/Consulta-CNPJ.svg?branch=master)](https://travis-ci.org/wherculano/Consulta-CNPJ)
[![Updates](https://pyup.io/repos/github/wherculano/Consulta-CNPJ/shield.svg)](https://pyup.io/repos/github/wherculano/Consulta-CNPJ/)
[![Python 3](https://pyup.io/repos/github/wherculano/Consulta-CNPJ/python-3-shield.svg)](https://pyup.io/repos/github/wherculano/Consulta-CNPJ/)
[![codecov](https://codecov.io/gh/wherculano/Consulta-CNPJ/branch/master/graph/badge.svg)](https://codecov.io/gh/wherculano/Consulta-CNPJ)

Para instalar o projeto basta efetuar o clone do mesmo:
```console
git close https://github.com/wherculano/Consulta-CNPJ.git
```
criar um ambiente virtual dentro da pasta do projeto:
```console
cd Consulta-CNPJ
python -m venv .venv
```
E depois instalar as depedências do projeto.
Há três formas:
1. Instalando via requirements:
    ```console
    pip install -r requirements.txt
    ```
1. Instalando via setup.py
    ```console
    pip install -e .
    ```
1. Instalando via pacote zip:
    ```console
    pip install https://github.com/wherculano/Consulta-CNPJ/archive/0.1.zip
   ```
   
 A interface gráfica do programa é bem intuitiva.    
 Basta digita o CNPJ desejado que as informações irão aparecer na tela após clicar em 'OK' ou pressionar 'ENTER'

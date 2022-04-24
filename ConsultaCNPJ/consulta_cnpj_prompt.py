import random
import time
from datetime import datetime

import requests
import json

URL = 'https://www.receitaws.com.br/v1/cnpj/'


class ConsultaCNPJ:
    def __init__(self, cnpj):
        self.cnpj = ''.join([n for n in cnpj if n.isnumeric()])

    def consulta(self) -> dict or str:
        time.sleep(random.random() + random.randint(20, 25))
        print('Efetuando a consulta do CNPJ')
        req = requests.get(URL + self.cnpj)
        if req.status_code == 200:
            content = req.text
            result = json.loads(content)

            try:
                resultado = {
                    'CNPJ': result['cnpj'],
                    'Razao Social': result['nome'].upper(),
                    'Nome Fantasia': result['fantasia'].upper(),
                    'Telefone': result['telefone'],
                    'email': result['email'],
                    'CEP': result['cep'].replace('.', ''),
                    'Endereco': result['logradouro'],
                    'Numero': result['numero'],
                    'Complemento': result['complemento'],
                    'Bairro': result['bairro'],
                    'Municipio': result['municipio'],
                    'Estado': result['uf'],
                    'Porte': result['porte'],
                    'Natureza': result['natureza_juridica'],
                    'Abertura': result['abertura'],
                    'Situacao': result['situacao'],
                    'Data Situacao': result['data_situacao'],
                    'Motivo Situacao': result['motivo_situacao'],
                    'Situacao Especial': result['situacao_especial'],
                    'Ultima Atualizacao': result['ultima_atualizacao'],
                    'Atividade Principal': f"{result['atividade_principal'][0]['code']}:"
                                           f" {result['atividade_principal'][0]['text']}",
                    'Atividades Secundarias': [f"{v['code']}: {v['text']}" for v in result['atividades_secundarias']],
                    'Capital Social': result['capital_social'],
                    'Socios': result['qsa'],
                }
                if resultado['Ultima Atualizacao'] != '':
                    resultado['Ultima Atualizacao'] = datetime.strptime(
                        resultado['Ultima Atualizacao'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%d/%m/%Y %H:%M:%S')
                print('Consulta realizada com sucesso!')
                return resultado
            except KeyError:
                return f"ERRO: {result['message']}"


if __name__ == '__main__':
    numero = input('CNPJ: ')
    c = ConsultaCNPJ(numero)
    c.consulta()

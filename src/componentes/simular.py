import csv
import random
from faker import Faker
from datetime import datetime, timedelta
 
NOME_ARQUIVO = 'leads.csv' 
DATA_INICIAL = datetime(2024, 1, 1)
DATA_FINAL = datetime.now()

ETAPAS_FUNIL = ['Lead', 'Qualificação', 'Proposta', 'Negociação', 'Fechamento Ganho']
PESOS_ETAPAS = [0.40, 0.25, 0.15, 0.10, 0.05]

def gerar_dados(NUMERO_DE_LEADS):
    fake = Faker('pt_BR')
    dados = []
    total_dias = (DATA_FINAL - DATA_INICIAL).days

    for i in range(1, NUMERO_DE_LEADS + 1):
        nome_completo = fake.name()
        primeiro_nome = nome_completo.split()[0].lower()
        ultimo_nome = nome_completo.split()[-1].lower()

        data_aleatoria = DATA_INICIAL + timedelta(days=random.randint(0, total_dias))
        
        lead = {
            'id_lead': i,
            'nome_contato': nome_completo,
            'email': f'{primeiro_nome}.{ultimo_nome}@{fake.free_email_domain()}',
            'empresa': fake.company(),
            'data_criacao': data_aleatoria.strftime('%Y-%m-%d'),
            'etapa_funil': random.choices(ETAPAS_FUNIL, weights=PESOS_ETAPAS, k=1)[0],
            'valor_estimado': round(random.uniform(1500.0, 75000.0), 2)
        }
        dados.append(lead)
    
    return dados

def salvar_csv(dados, nome_arquivo):
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            if dados:
                fieldnames = dados[0].keys()
                writer = csv.DictWriter(arquivo_csv, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(dados)
        print(f" O arquivo '{nome_arquivo}' foi criado com {len(dados)} leads.")
    except Exception as e:
        print(f" Erro ao salvar o arquivo: {e}")

if __name__ == '__main__':
    dados_gerados = gerar_dados(300)
    salvar_csv(dados_gerados, NOME_ARQUIVO)
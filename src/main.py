from componentes.gerenciador import GerenciadorLeads
from componentes.vizualizacao import plotar_funil, plotar_valor_por_etapa
from componentes.simular import gerar_dados, salvar_csv

import datetime
import os
import datetime
# Define as etapas válidas do funil para facilitar a validação
ETAPAS_FUNIL = ['Lead', 'Qualificação', 'Proposta', 'Negociação', 'Fechamento Ganho']

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    print("\n--- Sistema de Funil de Vendas ---")
    print("1. Adicionar Novo Lead")
    print("2. Avançar Lead de Etapa")
    print("3. Listar Todos os Leads")
    print("4. Gerar Relatório Visual")
    print("5. Sair")
    print("6. Gerar Dados Simulados")
    return input("Escolha uma opção: ")

def adicionar_novo_lead(gerenciador):
    limpar_tela()
    print("--- Adicionar Novo Lead ---")
    try:
        nome = input("Nome do Contato: ")
        email = input("Email: ")
        empresa = input("Empresa: ")
        valor_str = input("Valor Estimado (ex: 5000): ")
        valor = float(valor_str)

        novo_lead = {
            'nome_contato': nome,
            'email': email,
            'empresa': empresa,
            'data_criacao': datetime.date.today().isoformat(),
            'etapa_funil': 'Lead', 
            'valor_estimado': valor
        }
        gerenciador.adicionar_lead(novo_lead)
        
    except ValueError:
        print("\nErro: Valor estimado inválido. Por favor, insira um número.")
    except Exception as e:
        print(f"\nOcorreu um erro: {e}")
        
    input("\nPressione Enter para continuar...")

def avancar_lead(gerenciador):
    """Avança um lead para a próxima etapa do funil."""
    limpar_tela()
    print("--- Avançar Lead de Etapa ---")
    
    print("\nLeads Atuais:")
    print(gerenciador.listar_leads())
    
    try:
        id_lead_str = input("\nDigite o ID do lead que deseja avançar: ")
        id_lead = int(id_lead_str)

        if id_lead not in gerenciador.df_leads['id_lead'].values:
            print("\nErro: ID do lead não encontrado.")
            input("\nPressione Enter para continuar...")
            return

        print("\nEtapas disponíveis:")
        for i, etapa in enumerate(ETAPAS_FUNIL):
            print(f"{i+1}. {etapa}")
        
        etapa_idx_str = input("Escolha o número da nova etapa: ")
        etapa_idx = int(etapa_idx_str) - 1

        if 0 <= etapa_idx < len(ETAPAS_FUNIL):
            nova_etapa = ETAPAS_FUNIL[etapa_idx]
            gerenciador.atualizar_etapa(id_lead, nova_etapa)
        else:
            print("\nErro: Opção de etapa inválida.")

    except ValueError:
        print("\nErro: ID ou número da etapa inválido. Por favor, insira um número.")
    except Exception as e:
        print(f"\nOcorreu um erro: {e}")
        
    input("\nPressione Enter para continuar...")

def gerar_relatorios(gerenciador):
    """Gera e exibe os gráficos do funil de vendas."""
    limpar_tela()
    print("--- Gerando Relatórios Visuais ---")
    df_leads = gerenciador.listar_leads()
    
    if df_leads.empty:
        print("Não há dados suficientes para gerar relatórios.")
    else:
        print("Exibindo o funil de vendas... (Feche a janela do gráfico para continuar)")
        plotar_funil(df_leads)
        
        print("Exibindo o valor por etapa... (Feche a janela do gráfico para continuar)")
        plotar_valor_por_etapa(df_leads)

    input("\nPressione Enter para continuar...")

def main():
        
    gerenciador = GerenciadorLeads('data/leads.csv')

    while True:
        limpar_tela()
        opcao = exibir_menu()

        if opcao == '1':
            adicionar_novo_lead(gerenciador)
        elif opcao == '2':
            avancar_lead(gerenciador)
        elif opcao == '3':
            limpar_tela()
            print("--- Lista de Leads ---")
            print(gerenciador.listar_leads())
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == '4':
            gerar_relatorios(gerenciador)
        elif opcao == '5':
            print("Saindo do sistema. Até logo!")
            break
        elif opcao == '6':
            numero_dados = input("Quantos leads deseja gerar? ")
            dados_gerados = gerar_dados(int(numero_dados))
            salvar_csv(dados_gerados, 'data/leads.csv')
            print(f"Dados simulados gerados e salvos em 'data/leads.csv'.")
        else:
            print("\nOpção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
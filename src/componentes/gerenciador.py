import pandas as pd

class GerenciadorLeads:
    # Construtor que inicializa o gerenciador de leads com um arquivo CSV
    def __init__(self, caminho_arquivo):
        # Armazena o caminho do arquivo CSV
        self.caminho_arquivo = caminho_arquivo
        try:
            # Incializa o DataFrame a partir do arquivo CSV
            self.df_leads = pd.read_csv(self.caminho_arquivo)
        # Exeption para lidar com o caso em que o arquivo não existe
        except FileNotFoundError:
            print(f'arquivo {self.caminho_arquivo} não encontrado')
            # TODO: criar o arquivo com as colunas necessárias

    def adicionar_lead(self, new_lead_info):
        # Captura o valor do maior ID e incrementa um para o ID da nova lead
        new_id = self.df_leads['id_lead'].max() + 1 if not self.df_leads.empty else 1
        # Atribui o ID gerado ao dicionário de informações da lead
        new_lead_info['id_lead'] = new_id
        # Cria um DataFrame com as informações da nova lead
        new_lead = pd.DataFrame([new_lead_info])
        # Adiciona a nova lead ao DataFrame existente e salva os dados no arquivo CSV
        self.df_leads = pd.concat([self.df_leads, new_lead], ignore_index=True)
        self.salvar_dados()
        print(f"Lead '{new_lead_info['nome_contato']}' adicionado com sucesso!")

    def atualizar_etapa(self, id_lead, nova_etapa):
        # Procura a lead passada no DataFrame
        if id_lead in self.df_leads['id_lead'].values:
            # Atualiza a etapa do funil da lead encontrada e salva as alterações
            self.df_leads.loc[self.df_leads['id_lead'] == id_lead, 'etapa_funil'] = nova_etapa
            self.salvar_dados()
            # Obtendo o nome da lead : at[inice_dataframe, coluna]
            nome_lead = self.df_leads.at[self.df_leads.index[self.df_leads['id_lead'] == id_lead][0], 'nome_contato']
            print(f"Etapa do lead {nome_lead} atualizada para '{nova_etapa}'.")
        else:
            print(f"Lead com ID {id_lead} não encontrado.")

    def salvar_dados(self):
        # Salva o DataFrame atualizado de leads no arquivo CSV
        self.df_leads.to_csv(self.caminho_arquivo, index=False)

    def listar_leads(self):
        return self.df_leads
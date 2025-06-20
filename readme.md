* Esse projeto implementa um funil de vendas.
* Com ele, você poderá gerenciar e analisar o fluxo de potenciais leads através das diferentes etapas do processo de venda.
## Conceitual de um Funil de Vendas:

* Leads (Prospects): O topo do funil, onde você identifica potenciais clientes.
* Qualificação (Qualification): A fase em que você determina se um lead tem o perfil e o interesse para se tornar um cliente.
* Proposta (Proposal): O momento em que você apresenta uma oferta comercial ao lead qualificado.
* Negociação (Negotiation): A etapa de ajuste de detalhes da proposta, como preço e escopo.
* Fechamento (Closing): A fase final, que pode resultar em "Ganha" (venda concluída) ou "Perdida".

## Como rodar
* Criando ambiente virtual
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```
* Instalando as dependências
  ```
  pip install -r requirements.txt
  ```
* Crie um arquivo leads.csv com base em leads_exemplo.csv dentro da pasta src/data
* Rodando
  ```
  cd src
  python3 main.py
  ```
  

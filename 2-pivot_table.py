import pandas as pd

# 1 - Importando dados
data = pd.read_excel("data/VendaCarros.xlsx")
# print(type(data))

# 2 - Selecionando colunas especificas do dataframe
df = data[["Fabricante", "ValorVenda", "Ano"]]
print(df)

# Criando a tabela pivô
pivot_table = df.pivot_table(
    index="Ano",
    columns="Fabricante",
    values="ValorVenda",
    aggfunc="sum"
)
print(pivot_table)

# Exportar tabela pivô em arquivo excel
pivot_table.to_excel("data/pivot_table.xlsx", "Relatorio")
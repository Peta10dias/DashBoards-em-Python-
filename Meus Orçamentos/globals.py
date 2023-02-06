import pandas as pd
import os

if("df_despesas.csv" in os.listdir()) and ("df_receitas.csv" in os.listdir()):
    df_despesas = pd.read_csv("df_despesas.csv", sep=",", index_col=0, parse_dates= True)
    df_receitas = pd.read_csv("df_receitas.csv", sep=",", index_col=0, parse_dates= True)
    df_despesas["Data"] = pd.to_datetime(df_despesas["Data"])
    df_receitas["Data"] = pd.to_datetime(df_receitas["Data"])
    df_despesas["Data"] = df_despesas["Data"].apply(lambda x: x.date())
    df_receitas["Data"] = df_receitas["Data"].apply(lambda x: x.date())    

else: 
    data_stucture = {
        'Valor':[],
        'Recebido':[],
        'Fixo':[],
        'Data':[],
        'Categoria':[],
        'Descrição':[],}   
    df_receitas = pd.DataFrame(data_stucture)
    df_despesas = pd.DataFrame(data_stucture)     
    df_despesas.to_csv('df_despesas.csv')
    df_receitas.to_csv('df_receitas.csv')    

if ("df_cat_despesas.csv" in os.listdir()) and ("df_cat_receitas.csv" in os.listdir()):
    df_cat_despesas = pd.read_csv("df_cat_despesas.csv", sep=",", index_col=0)
    df_cat_receitas = pd.read_csv("df_cat_receitas.csv", sep=",", index_col=0)
    cat_receita = df_cat_receitas.values.tolist()
    cat_despesa = df_cat_despesas.values.tolist()

else:
    cat_receita = {'Categoria': ["Sálario", "Investimento", "Comissão"]}
    cat_despesa = {'Categoria': ["Alimentação", "Aluguel", "Saúde","Lazer"]}
    df_cat_receitas = pd.DataFrame(cat_receita)
    df_cat_despesas = pd.DataFrame(cat_despesa)     
    df_cat_despesas.to_csv("df_cat_despesas.csv")
    df_cat_receitas.to_csv("df_cat_receitas.csv")       
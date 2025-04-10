# SCORE DE CREDITO BOM OK OU RUIM
import pandas as pd
tabela = pd.read_csv("clientes.csv")
#passo 2 preparar a base de dados para a IA
from sklearn.preprocessing import LabelEncoder
#profissao
codificador1 = LabelEncoder()
tabela["profissao"] = codificador1.fit_transform(tabela["profissao"])


codificador2 = LabelEncoder()
tabela["mix_credito"] = codificador2.fit_transform(tabela["mix_credito"])

codificador3 = LabelEncoder()
tabela["comportamento_pagamento"] = codificador3.fit_transform(tabela["comportamento_pagamento"])

#separar as informações para a IA
#separar em X e Y
#y -> quem eu quero prever (coluna score_credito)
#X -> o que eu tenho para prever (todas as outras colunas)
y = tabela["score_credito"]
x = tabela.drop(columns=["score_credito","id_cliente"])
#separa em dados de treino e de teste
from sklearn.model_selection import train_test_split
x_treino, x_teste, y_treino, y_teste = train_test_split(x,y,text_size=0.2)
#passo 3: criar o modelo
# tres passos importar o modelo, criar o modelo, treinar o modelo
#árvore de decisão -> RandomForest
#vizinhos Proximos -> KNN

#importar o modelo
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
#criar o modelo
modelo_arvore_decisao = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()
#treinar o modelo .fit
modelo_arvore_decisao.fit(x_treino,y_treino)
modelo_knn.fit(x_treino,y_treino)
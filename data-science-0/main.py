#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[3]:


#data_frame_female = black_friday.query("Gender == 'F' & Age == '26-35' ")
#data_frame_female.head()

#black_friday.groupby('Gender')['Age'].value_counts()[0] #49348

#mulheres = black_friday['Gender'] == 'F'
#idade_base = black_friday['Age'] == '26-35'
#black_friday[mulheres & idade_base].shape[0] #49348

#black_friday.select_dtypes(["int64", "float64","object"]).sum()

#black_friday.info()


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[4]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return black_friday.shape # 537577 linhas e 12 colunas
    pass


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[5]:


def q2():
    # Retorne aqui o resultado da questão 2.
    mulheres = black_friday['Gender'] == 'F'
    faixa_etaria = black_friday['Age'] == '26-35'
    return black_friday[mulheres & faixa_etaria].shape[0] #49348 mulheres entre 26 e 35 anos
    pass


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[6]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return black_friday['User_ID'].nunique() #5891 usuários únicos
    pass


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[7]:


def q4():
    # Retorne aqui o resultado da questão 4.
    return black_friday.dtypes.nunique() # 3 tipos de dados diferentes
    pass


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[8]:


def q5():
    # Retorne aqui o resultado da questão 5.
    #Verificando dados faltantes Null
    print(black_friday.isnull().sum())

    #Converter Null em Nan para não gerar erro de float
    black_friday.fillna(value=np.nan, inplace=True)

    #Retornando a porcentagem de valores Null entre 0 e 1
    return 1 - len(black_friday.dropna()) / len(black_friday) #0.69
    pass


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[9]:


def q6():
    # Retorne aqui o resultado da questão 6.
    return int(black_friday.isnull().sum().sort_values(ascending = False)[0])
    pass


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[10]:


def q7():
    # Retorne aqui o resultado da questão 7.
    return black_friday['Product_Category_3'].value_counts().index[0]
    pass


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[11]:


def q8():
    # Retorne aqui o resultado da questão 8.
    
    # O menor valor de compra
    minimo = black_friday['Purchase'].min()
    
    # O maior valor de compra
    maximo = black_friday['Purchase'].max()
    
    #retorna a média da coluna Purchase depois da normalização
    return float(((black_friday['Purchase'] - minimo)/(maximo - minimo)).mean())
    
    pass


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[12]:


def q9():
    # Retorne aqui o resultado da questão 9.
    
    #Padronizar a coluna Purchase
    padronizacao = ((black_friday['Purchase'] - black_friday['Purchase'].mean())/black_friday['Purchase'].std())

    #Retorna o número de ocorrências entre -1 e 1
    return int(((padronizacao < 1) & (padronizacao > -1)).sum())
    
    pass


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[13]:


def q10():
    # Retorne aqui o resultado da questão 10.
    #Verificando se uma observação em Product_Category_2 é null
    se_nulo = black_friday[black_friday['Product_Category_2'].isna()]
    #Verificando se a observação de Product_Category_2 é nula em Product_Category 3
    return bool((se_nulo['Product_Category_3'].isnull().sum() == len(se_nulo)))
    pass


# In[ ]:





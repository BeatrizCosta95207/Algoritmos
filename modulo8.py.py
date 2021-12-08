#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Módulo que permite ler, listar e analisar datasets
# 2021-12-05
# Beatriz Costa a95207


#Funções que permitem percorrer o ficheiro de texto e criar uma base de dados (lista)
# a base de dados é uma lista com vários campos
def getEMD(texto):
    novoTexto=texto.replace('\n','')
    EMD=[]
    dados=novoTexto.split(",")
    for i in range(len(dados)):
        EMD.append(dados[i])
    EMD.pop(1)
    return EMD
    
    
def lerDataset(fnome):
    f = open(fnome, encoding="utf-8")
    bd = []
    f=open(fnome, encoding="utf-8")
    bd = []
    f.readline()
    for linha in f:
        bd.append(getEMD(linha))
    for i in range(len(bd)):
        bd[i][0]='emd'+str(i+1)
    return bd


#Imprime uma tabela com algumas das informações dos atletas, ordenos por ordem cronológica decrescente
def chaveORD(a):
    return a[1]
def listarDataset(bd):
    bd.sort(key=chaveORD, reverse=True)
    print('_id      dataEMD    nome          apto')
    print('______________________________________')
    for elem in bd:
        
        print(elem[0] + " | "  + elem [1] + "|" + elem[2]+ "  " + elem[3] + " | " + elem[11])

        
#permite consultar um atleta através do seu id        
def consultarDataset(bd, id):
    for elem in bd:
        if elem[0]== id:
            print(elem)
id=input("Que id deseja consultar? ")

# retorna uma lista com todas as modalidades existentes 
def Modalidades(bd):
    mod=[]
    for elem in bd:
        if elem[7] not in mod:
            mod.append(elem[7])
    mod.sort()
    return mod

def distribPorModalidade(bd):
    distribuição={}
    for elem in bd:
        if elem[7] not in distribuição:
            distribuição[elem[7]]= 1
        else:
            distribuição[elem[7]]= distribuição[elem[7]] +1
    return distribuição


def distribPorClube(bd):
    distribuição={}
    for elem in bd:
        if elem[8] not in distribuição:
            distribuição[elem[8]] = 1
        else:
            distribuição[elem[8]] = distribuição[elem[8]] + 1
    return distribuição


def distribPorAno(bd):
    distribuição={}
    for elem in bd:
        data= elem[1].split("-")
        ano= data[0]
        if ano not in distribuição:
            distribuição[ano]=1
        else:
            distribuição[ano]= distribuição[ano]+1
    return distribuição

#faz a distribuição por qualquer campo 
def distrib(bd):
    print( " 1-data   4-idade  5-género   7-modalidade  8-clube 10-federado 11-resultado" )
    indice=input("Qual o campo que deseja consultar? ")
    i=int(indice)
    distribuição={}
    if i==1:
        for elem in d:
            if elem[1][:4] in distribuição.keys():
                distribuição[elem[1][:4]]= distribuição[elem[1][:4]]+1
            else:
                distribuição[elem[1][:4]]=1
    
    else:    
        for elem in bd:
            if elem[i] not in distribuição:
                distribuição[elem[i]]= 1
            else:
                distribuição[elem[i]]= 1 + distribuição[elem[i]]
    
    return distribuição
distrib(BD)



import matplotlib.pyplot as plt

def plotDistribPorModalidade(bd):
    a=distribPorModalidade(bd)
    tuplo=a.items()
    height=[]
    left=[]
    label=[]
    for i in range(len(tuplo)):
        left.append(i)
    for elem in tuplo:
        height.append(elem[1])
        label.append(elem[0])
    plt.bar(left,height, label=label,
           width=0.8, color=["pink"])
    plt.xticks(range(len(label)),label, rotation = 'vertical')
    plt.xlabel("Modalidade")
    plt.title("Distribuição por Modalidade")
   
    plt.show()

#faz o gráfico da distribuição por qualquer campo
def distrib(bd,indice):
    i=int(indice)
    distribuição={}
    if i==1:
        for elem in d:
            if elem[1][:4] in distribuição.keys():
                distribuição[elem[1][:4]]= distribuição[elem[1][:4]]+1
            else:
                distribuição[elem[1][:4]]=1
    
    else:    
        for elem in bd:
            if elem[i] not in distribuição:
                distribuição[elem[i]]= 1
            else:
                distribuição[elem[i]]= 1 + distribuição[elem[i]]
    return distribuição

def plotDistrib(bd,indice):
    a=distrib(bd,indice)
    tuplo=a.items()
    height=[]
    left=[]
    label=[]
    for u in range(len(tuplo)):
        left.append(u)
    for elem in tuplo:
        height.append(elem[1])
        label.append(elem[0])
    plt.bar(left,height, label=label,
           width=0.8, color=["pink"])
    plt.xticks(range(len(label)),label, rotation = 'vertical')
    if indice==1:
        plt.xlabel("Data")
        plt.title("Distribuição por data")
    elif indice== 4:
        plt.xlabel("Idade")
        plt.title("Distribuição por Idade")
    elif indice==5:
        plt.xlabel("Género")
        plt.title("Distribuição por Género")
    elif indice==7:
        plt.xlabel("Modalidade")
        plt.title("Distribuição por Modalidade")
    elif indice==8:
        plt.xlabel("Clube")
        plt.title("Distribuição por Clube")
    elif indice==10:
        plt.xlabel("Federado")
        plt.title("Distribuição por Federado/ não Federado")
    elif indice==11:
        plt.xlabel("Resultado")
        plt.title("Distribuição por Resultado")
        
        
   
    plt.show()


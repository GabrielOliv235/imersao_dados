import numpy as np
import pandas as pd
print(pd.__version__)
df = pd.read_csv("https://raw.githubusercontent.com/GabrielOliv235/imersao_dados/refs/heads/main/pandas_imersao/salaries.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.shape)
linhas, colunas = df.shape
print(f'| LINHAS: {linhas:>5} | COLUNAS: {colunas:>5} |')
print(df.columns)
novos_nomes = {
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}
df.rename(columns=novos_nomes, inplace=True)
print(df.columns)
print(df['senioridade'].value_counts())
print(df['contrato'].value_counts())
print(df['remoto'].value_counts())
print(df['tamanho_empresa'].value_counts())
senioridade = {
    'SE': 'senior',
    'MI': 'pleno',
    'EN': 'junior',
    'EX': 'executivo'
}
df['senioridade'] = df['senioridade'].replace(senioridade)
print(df['senioridade'].value_counts())
contrato = {
    'FT': 'integral',
    'PT': 'parcial',
    'CT': 'contrato',
    'FL': 'freelancer'
}
df['contrato'] = df['contrato'].replace(contrato)
print(df['contrato'].value_counts())
tamanho_empresa = {
    'L': 'grande',
    'S': 'pequena',
    'M':	'media'
}
df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)
print(df['tamanho_empresa'].value_counts())
mapa_trabalho = {
    0: 'presencial',
    100: 'remoto',
    50: 'hibrido'
}
df['remoto'] = df['remoto'].replace(mapa_trabalho)
print(df['remoto'].value_counts())
print(df.head(30))
print(df.isnull().sum())

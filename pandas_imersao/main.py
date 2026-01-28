import pandas as pd
print(pd.__version__)
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.shape)
linhas, colunas = df.shape
print(f'| LINHAS: {linhas:>5} | COLUNAS: {colunas:>5} |')

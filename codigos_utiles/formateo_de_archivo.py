import pandas as pd

# Leer los datos
df = pd.read_csv('../problema_de_formateo.csv')

# Procesar los datos
strategy_index = df[df['estrategia'].notna()].index
dfs = []
for i in range(len(strategy_index) - 1):
    dfs.append(df.loc[strategy_index[i]:strategy_index[i + 1] - 1])
dfs.append(df.loc[strategy_index[-1]:])


dfs_out = []
for df in dfs:
    for cdc in df['cuenta_de_cobro'].dropna().unique():
        df = df.fillna(method='ffill')
        df['cuenta_de_cobro'] = cdc
        dfs_out.append(df)

df_out = pd.concat(dfs_out)

# Guardar los datos en un archivo nuevo
df_out.drop_duplicates().to_csv('ready.csv', index=False)

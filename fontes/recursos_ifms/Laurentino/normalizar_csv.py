import pandas as pd

# Caminho do arquivo original
input_path = 'fontes/recursos_ifms/Laurentino/Atividades Diversificadas (respostas) - Laurentino - Respostas_ao_formulario_1.csv'
output_path = 'fontes/recursos_ifms/Laurentino/Atividades_Diversificadas_normalizado.csv'

# Carregar CSV
df = pd.read_csv(input_path)

# 1. Padronizar nomes de colunas
df.columns = [col.strip().lower().replace(' ', '_').replace('ç', 'c').replace('ã', 'a') for col in df.columns]

# 2. Padronizar datas
if 'data' in df.columns:
    df['data'] = pd.to_datetime(df['data'], errors='coerce').dt.strftime('%Y-%m-%d')

# 3. Unificar respostas similares
if 'atividade' in df.columns:
    df['atividade'] = df['atividade'].str.lower().str.strip().replace({'palestras': 'palestra', 'palestra ': 'palestra'})

# 4. Preencher valores ausentes
df = df.fillna('NULL')

# 5. Remover duplicatas
df = df.drop_duplicates()

# 6. Salvar CSV normalizado
df.to_csv(output_path, index=False)

print('Normalização concluída. Arquivo salvo em:', output_path)
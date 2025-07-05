import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 


df = pd.read_csv('dados.csv')

media_vendas = df['vendas'].mean()

print('media das vendas: ', media_vendas)
maior = df.loc[df['vendas'].idxmax()]
print('maior venda: ', maior)


menor = df.loc[df['vendas'].idxmin()]
print('menor venda: ', menor)

plt.figure(figsize=(10, 6))
sns.lineplot(x='mes', y='vendas', data=df, marker='o', linewidth=1.5)

plt.title('analise de vendas', fontsize=34, pad=20)
plt.xlabel('meses de venda', fontsize=12)
plt.ylabel('vendas', fontsize=12)
plt.grid(True)


for i, row in df.iterrows():
    plt.text(row['mes'], row['vendas'], f'R${row['vendas']}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()

plt.xticks(rotation=30)

plt.savefig('vendas_mes.png', dpi=300, bbox_inches='tight')

plt.show()
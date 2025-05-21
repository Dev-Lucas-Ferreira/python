import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('vendedores.xlsx')
vendas_por_vendedor = df.groupby('Vendedor')['Valor da Venda'].sum().reset_index()
top_5 = vendas_por_vendedor.sort_values(by='Valor da Venda', ascending=False).head(5)
top_10 = vendas_por_vendedor.sort_values(by='Valor da Venda', ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.bar(top_10['Vendedor'], top_10['Valor da Venda'], color='skyblue')
plt.xticks(rotation=45)
plt.title('Top 10 Vendedores por Faturamento')
plt.tight_layout()
plt.savefig('grafico_vendedores.png')

with pd.ExcelWriter('ranking_vendedores.xlsx', engine='openpyxl') as writer:
    top_10.to_excel(writer, sheet_name='Ranking', index=False)
    from openpyxl import load_workbook
    from openpyxl.drawing.image import Image
    writer.book = load_workbook('ranking_vendedores.xlsx')
    sheet = writer.book['Ranking']
    img = Image('grafico_vendedores.png')
    sheet.add_image(img, 'E2')
    writer.book.save('ranking_vendedores.xlsx')

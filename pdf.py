from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def gerar_pdf(caminho_arquivo):
    c = canvas.Canvas(caminho_arquivo, pagesize=letter)
    largura, altura = letter

    # Adicionar título
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, altura - 50, "Fatura de Cartão de Crédito")

    # Adicionar dados da fatura
    c.setFont("Helvetica", 12)
    c.drawString(100, altura - 100, "Nome do Titular: João da Silva")
    c.drawString(100, altura - 120, "Número do Cartão: **** **** **** 1234")
    c.drawString(100, altura - 140, "Data de Vencimento: 30/07/2024")

    # Adicionar tabela de transações
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, altura - 180, "Data        Descrição                       Parcela/Total  Valor")

    c.setFont("Helvetica", 12)
    c.drawString(100, altura - 200, "10/06      EBN *SONYPLAYST01/03  01/03       R$ 20,61")
    c.drawString(100, altura - 220, "11/06      REDE SUPERMERCADO      01/03       R$ 115,25")
    c.drawString(100, altura - 240, "12/06      CAFETERIA BARISTA      01/03       R$ 7,90")
    c.drawString(100, altura - 260, "13/06      LOJA ELETRONICA        02/03       R$ 199,99")
    c.drawString(100, altura - 280, "14/06      POSTO DE GASOLINA      02/03       R$ 45,70")
    c.drawString(100, altura - 300, "15/06      ALIMENTAÇÃO RIO DE JANEIRO  02/03  R$ 89,50")
    c.drawString(100, altura - 320, "16/06      BAZAR FLOR DO ACRE LTD   03/03    R$ 35,00")
    c.drawString(100, altura - 340, "17/06      SUPERMERCADO CENTRAL     03/03    R$ 120,85")
    c.drawString(100, altura - 360, "18/06      RESTAURANTE DELICIA     03/03    R$ 60,00")
    c.drawString(100, altura - 380, "19/06      CASAS PEDRO - CT        01/03    R$ 29,08")

    # Adicionar total
    total = 20.61 + 115.25 + 7.90 + 199.99 + 45.70 + 89.50 + 35.00 + 120.85 + 60.00 + 29.08
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, altura - 420, f"Total: R$ {total:.2f}")

    # Salvar o PDF
    c.save()

# Caminho para salvar o PDF
caminho_arquivo = r'C:\Users\ernst\Downloads\fatura_simples.pdf'
gerar_pdf(caminho_arquivo)
print(f"PDF gerado com sucesso em {caminho_arquivo}")

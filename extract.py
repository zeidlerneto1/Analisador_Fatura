import pdfplumber

def extrair_texto(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        texto = ''
        for pagina in pdf.pages:
            texto += pagina.extract_text() + '\n'
    return texto



import re
from datetime import datetime

def analisartexto(texto):
    compras = []
    regex_transacao = re.compile(
        r'(\d{1,2}/\d{1,2})\s*(.*?)\s*(\d{2}/\d{2})\s*R\$\s*([\d,]+)'
    )
    
    for match in regex_transacao.finditer(texto):
        data_str, descricao, parcela_str, valor_str = match.groups()
        valor = float(valor_str.replace(',', '.'))
        try:
            data = datetime.strptime(data_str, '%d/%m')
            data = data.replace(year=datetime.now().year)
        except ValueError:
            print('Erro ao converter data')
            data = datetime.now()

        try:
            parcela_numero, total_parcelas = parcela_str.split('/')
            parcela_numero = int(parcela_numero)
            total_parcelas = int(total_parcelas)
        except ValueError:
            parcela_numero, total_parcelas = 'N/A', 'N/A'

        compras.append({
            'data': data,
            'estabelecimento': descricao.strip(),
            'valor': valor,
            'parcela': f'{parcela_numero}/{total_parcelas}'
        })
    return compras
         
            
    
def listarcomprasordernas(compras):
    return sorted(compras, key=lambda x: x ['valor'], reverse=True)

def listarparcelasproximas(compras):
    parcelas = []
    for compra in compras:
        if compra['parcela'] != 'N/A':
            try:
                parcela_numero, total_parcelas = compra['parcela'].split('/')
                parcela_numero = int(parcela_numero)
                total_parcelas = int(total_parcelas)
                parcelas_restantes = total_parcelas - parcela_numero
                
                if parcelas_restantes == 1:
                    parcelas.append({
                        'data_transacao': compra['data'],
                        'estabelecimento': compra['estabelecimento'],
                        'valor': compra['valor'],
                        'parcela': compra['parcela']
                    })
            except ValueError:
                continue
        
    proximas = sorted(parcelas, key=lambda x: x['data_transacao'])
    return proximas

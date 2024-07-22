import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from extract import extrair_texto
from process import analisartexto, listarparcelasproximas

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Analisador de Faturas')
        self.setGeometry(100, 100, 900, 600)

        self.layout = QVBoxLayout()
        
        self.titulo = QLabel('Analisador de Faturas de Cartão de Crédito')
        self.titulo.setFont(QFont('Arial', 18, QFont.Weight.Bold))
        self.titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.titulo)
        
        self.botao_carregar = QPushButton('Carregar PDF')
        self.botao_carregar.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px; padding: 10px; border-radius: 5px;")
        self.botao_carregar.clicked.connect(self.carregar_pdf)
        
        self.botao_layout = QHBoxLayout()
        self.botao_layout.addWidget(self.botao_carregar)
        self.layout.addLayout(self.botao_layout)
        
        self.texto_resultado = QTextEdit()
        self.texto_resultado.setReadOnly(True)
        self.texto_resultado.setStyleSheet("background-color: #f1f1f1; border: 1px solid #ddd; padding: 10px;")
        self.layout.addWidget(self.texto_resultado)
        
        self.widget_central = QWidget()
        self.widget_central.setLayout(self.layout)
        self.setCentralWidget(self.widget_central)
    
    def carregar_pdf(self):
        pdf_path, _ = QFileDialog.getOpenFileName(self, 'Selecionar arquivo PDF', '', 'Arquivos PDF (*.pdf)')
        if pdf_path:
            texto = extrair_texto(pdf_path)
                        
            if texto:
                compras = analisartexto(texto)
                parcelas_proximas = listarparcelasproximas(compras)
                
                if parcelas_proximas:
                    resultado = "Parcelas próximas de terminar:\n\n"
                    for parcela in parcelas_proximas:
                        resultado += (f"Data da Transação: {parcela['data_transacao'].strftime('%d/%m/%Y')}\n"
                                      f"Estabelecimento: {parcela['estabelecimento']}\n"
                                      f"Valor: R$ {parcela['valor']:.2f}\n"
                                      f"Parcela: {parcela['parcela']}\n\n")
                else:
                    resultado = "Nenhuma parcela próxima de terminar encontrada."
                
                self.texto_resultado.setText(resultado)
            else:
                self.texto_resultado.setText("Nenhum texto foi extraído do PDF.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

from pdf2docx import Converter
import os

# Caminho absoluto do arquivo PDF de entrada
input_pdf = os.path.abspath('C:/Users/robso/OneDrive/Área de Trabalho/Faculdade/coverte/converter/Profile.pdf')

# Verifica se o arquivo existe
if not os.path.exists(input_pdf):
    print(f"Arquivo não encontrado: {input_pdf}")
else:
    # Caminho do arquivo Word de saída
    output_docx = os.path.abspath('C:/Users/robso/OneDrive/Área de Trabalho/Faculdade/coverte/convertido/Trabalho.docx')

    # Cria um conversor
    cv = Converter(input_pdf)

    # Converte o PDF para Word
    cv.convert(output_docx, start=0, end=None)

    # Fecha o conversor
    cv.close()

    print("Conversão concluída!")

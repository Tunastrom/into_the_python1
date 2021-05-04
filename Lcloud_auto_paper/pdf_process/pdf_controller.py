from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import copy


def pdf_controller():
    dir_path = 'C:/Lcloud_auto_paper/maintenence_pdf/202104/'
    # 각각의 pdf파일 불러오기
    for file_name in os.listdir(dir_path):

    # file_name = os.listdir(dir_path)[0]
        print(file_name)
        file_path = dir_path + file_name
        pdfReader = PdfFileReader(open(file_path, 'rb'))
        pdfReader.documentInfo
        print(pdfReader.numPages)
        print_obj = pdfReader.getPage(0)
        print(print_obj.extractText())


print(globals())
if __name__ == '__main__':
    pdf_controller()

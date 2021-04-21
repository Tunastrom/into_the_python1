import PyPDF2
import os


def pdf_controller():
    dir_path = 'C:/Lcloud_auto_paper/maintenence_pdf/'
    for file_name in os.listdir(dir_path):
        print(file_name)
        # file_path = dir_path + file_name
    # PyPDF2.PdfFileReader(open)
    pass


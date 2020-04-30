from PyPDF2 import PdfFileMerger,PdfFileReader,PdfFileWriter
from PyQt5.QtWidgets import QApplication,QFileDialog,QWidget
from Ui_PDF import Ui_Form
import sys

class pdf_w (QWidget,Ui_Form):
    def __init__(self):
        super(pdf_w,self).__init__()
        self.setupUi(self)
        # self.show()
        self.pushButton.clicked.connect(QFileDialog.getExistingDirectory)

if __name__ == "__main__":
    app= QApplication(sys.argv)
    qw =pdf_w()
    qw.show()
    app.exec()






   
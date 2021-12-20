from tika import parser


class ParsePDF:

    def __init__(self, fileLoc, save_name: str):
        self.fileLoc = fileLoc
        self.save_name = save_name

    def parse_pdf_and_write(self):
        parsedPDF = parser.from_file(self.fileLoc)
        self.data = parsedPDF['content']

        output_file = self.save_name+".txt"
        f = open(output_file, "w")
        f.write(self.data)
        f.close()


if __name__ == '__main__':

    pdfPath1= "pdf_files/Tez-1.pdf"
    pdfPath2 = "pdf_files/Tez-2.pdf"
    pdfPath3 = "pdf_files/Tez-3.pdf"
    pdfPath4 = "pdf_files/Tez-4.pdf"
    
    t1=pdfPath1.split("/")[1].split(".")[0]
    t2=pdfPath2.split("/")[1].split(".")[0]
    t3=pdfPath3.split("/")[1].split(".")[0]
    t4=pdfPath4.split("/")[1].split(".")[0]

    a = ParsePDF(pdfPath1,t1)
    b = ParsePDF(pdfPath2,t2)
    c = ParsePDF(pdfPath3,t3)
    d=ParsePDF(pdfPath4,t4)
    
    a.parse_pdf_and_write()
    b.parse_pdf_and_write()
    c.parse_pdf_and_write()
    d.parse_pdf_and_write()
    
    
    
    
    
    

from tika import parser


class ParsePDF:

    def __init__(self, fileLoc,):
        self.fileLoc = fileLoc

    def parse_pdf_and_write(self):
        parsedPDF = parser.from_file(self.fileLoc)  # buffer olarak değişecek
        self.data = parsedPDF['content']
        return self.data

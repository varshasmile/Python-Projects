from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import sys

input_file = sys.argv[1]
wtr_file = sys.argv[2]

with open(input_file, 'rb') as input_file, open(wtr_file, 'rb') as wtr_file:
	readfile = PdfFileReader(input_file)
	readfile2 = PdfFileReader(wtr_file)
	watermark_page = readfile2.getPage(0)
	output = PdfFileWriter()
	for i in range(readfile.getNumPages()):
	    pdf_page = readfile.getPage(i)
	    pdf_page.mergePage(watermark_page)
	    output.addPage(pdf_page)

	with open("WatermarkedPDF.pdf", "wb") as wtrpdf_file:
	        output.write(wtrpdf_file)
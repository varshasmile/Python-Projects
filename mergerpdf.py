import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_lists):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_lists:
		print(pdf)
		merger.append(pdf)
	merger.write("MergedPDFs.pdf")


pdf_combiner(inputs)
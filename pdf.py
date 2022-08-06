import PyPDF2

with open("dummy.pdf", 'r') as file:
	print(file)

with open("dummy.pdf", 'rb') as file:
	readfile = PyPDF2.PdfFileReader(file)
	print(readfile.numPages)
	print(readfile.getPage(0))
	page = readfile.getPage(0)
	page.rotateCounterClockwise(90)
	writefile = PyPDF2.PdfFileWriter()
	writefile.addPage(page)
	with open("tilt.pdf", 'wb') as new_file:
		writefile.write(new_file)
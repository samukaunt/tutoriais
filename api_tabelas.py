import requests 

#usando PDFtables API para conveter PDF em tabelas e transformar PDF em CSV, Excel e etc
def pdfToTable(PDFfilename, apiKey, fileExt, downloadDir):
	fileData = (PDFfilename, open(PDFfilename, 'rb'))
	files = {'f': fileData}
	postUrl = "https://pdftables.com/api?key={0}&format={1}".format(apiKey, fileExt)
	response = requests.post(postUrl, files=files)
	response.raise_for_status()
	with open(downloadDir, "wb") as f:
    	f.write(response.content)
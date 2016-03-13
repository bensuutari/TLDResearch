from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfdevice import PDFDevice
import sys
from cStringIO import StringIO
from nltk import *
from nltk.stem.porter import *



reload(sys)  
sys.setdefaultencoding('utf8')


class pdfread(object):

	def __init__(self,path):
		self.path=path
	def pdf2text(self):
		rsrcmgr = PDFResourceManager()
		retstr = StringIO()
		codec = 'utf-8'
		laparams = LAParams()
		device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
		fp = file(self.path, 'rb')
		interpreter = PDFPageInterpreter(rsrcmgr, device)
		password = ""
		maxpages = 0
		caching = True
		pagenos=set()

		for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
			interpreter.process_page(page)

		self.text = retstr.getvalue()

		fp.close()
		device.close()
		retstr.close()
		self.cleantext()




	    
	def cleantext(self):
		self.cleanedtext=self.text.replace('\n',' ')

		
	'''


	textprac=pdf2text('/home/ben/Desktop/Project Idea Lit/Owen/nature12330.pdf')
	#print textprac


	text_sent_token=sent_tokenize(textprac)
	for sent in text_sent_token[0:9]:
		print sent.strip().split()
	
	print text_sent_token[0:9]
	text_word_token=word_tokenize(textprac)
	text_word_token_freq=FreqDist(textprac)


	pos_word_token=pos_tag(text_word_token)

	nouns=list()
	for i in range(0,len(pos_word_token)-1):
		if pos_word_token[i][1]=='NN':
			nouns.append(pos_word_token[i][0])


	#print nouns

	nounsfreq=FreqDist(nouns)
	nounsfreqMC=nounsfreq.most_common(50)
	for j in range(0,10):
		print str(nouns[j])+':'+str(nounsfreqMC[j][1])



	print nouns[2].split()
	print nouns[9].split()
	print nouns[2]==nouns[9]
	'''


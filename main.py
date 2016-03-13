
from PDF_open import *
from summarize import *
import sys
sys.setdefaultencoding('utf8')
print "Type the path to the pdf you'd like to summarize:"
filepath=raw_input()

pdftext=pdfread(filepath)


pdftext.pdf2text()

#print pdftext.cleanedtext[0:9]

cleantext=pdftext.cleanedtext
summtext=summtext(cleantext)
'''
for j in range(0,49):
	print str(summtext.nounsfreq[j][0])+':'+str(summtext.nounsfreq[j][1])

'''

print('\n-----\n'.join(summtext.sent[0:10]))

stemmer = PorterStemmer()

stemmednouns=[stemmer.stem(noun) for noun in summtext.nouns[0:29]]

#print stemmednouns


sortedsentscore=sorted(summtext.sentscore, key=lambda yy: yy[1],reverse=True)
for h in range(0,14):
	print sortedsentscore[h][0]
	print '\n----------\n'








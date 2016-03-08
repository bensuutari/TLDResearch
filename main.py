
from PDF_open import *
from summarize import *


print "Type the path to the pdf you'd like to summarize:"
filepath=raw_input()

pdftext=pdfread(filepath)

print "Would you like the text cleaned? (y/n)"
rawclean=raw_input()

while (rawclean is not 'y') and (rawclean is not 'n'):

	print 'sorry, thats not a valid input. Type y or n for clean text'
	print "Would you like the text cleaned? (y/n)"
	rawclean=raw_input()

pdftext.pdf2text(rawclean)

print pdftext.cleanedtext[0:9]

cleantext=pdftext.cleanedtext
summtext=summtext(cleantext)

for j in range(0,49):
	print str(summtext.nouns[j])+':'+str(summtext.nounsfreq[j][1])







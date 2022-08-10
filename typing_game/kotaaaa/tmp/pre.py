# https://tuxdoc.com/download/ielts-4000-academic-word-listpdf-4_pdf
f = open("../testdata/ielts_words_orig.txt","r")
fw = open("../testdata/ielts_words_wr2.txt","w")
for i in f.readlines():
  if ":" in i:
    fw.write("\n"+i.strip())
  else:
    fw.write(" "+ i.strip())



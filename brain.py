import csvreader
import organizer

data = csvreader.datagetter()

data.loadData()

contentlist = data.getContent()
titlelist = data.getTitle()

print(contentlist[1])

o = organizer.organize()
o.tokenizing(contentlist[1])
o.graghprinter()
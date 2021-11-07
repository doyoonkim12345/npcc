import csv


class datagetter:

    def __init__(self):
        self.datasheet = []

    def getRawData(self):
        return self.datasheet

    def getData(self, address, type):
        return self.datasheet[address][type]

    def loadData(self):
        a = 0
        temp = 0
        with open('petitionlist.csv', "r", encoding='UTF8') as file:
            while 1:
                line = file.readline()
                if not line :
                    break
                line = line.split(",")
                if not len(line) == 6:
                    a = a+1
                self.datasheet.append(line)

    def getTitle(self):
        titlelist = []
        for templist in self.datasheet:
            titlelist.append(templist[0])
        return titlelist

    def getContent(self):
        contentList = []
        for templist in self.datasheet:
            contentList.append(templist[4])
        return contentList

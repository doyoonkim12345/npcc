import csv

petitioncontent = open('petitionlist.csv', 'w', encoding='UTF8', newline="")

csvwriter = csv.writer(petitioncontent)

def csvWrite(title, category, startdate, enddate, content, uploader):
    title = title.replace('\"', "").replace(",","")
    category = category.replace('\"', "").replace(",","")
    startdate = startdate.replace('\"', "").replace(",","")
    enddate = enddate.replace('\"', "").replace(",","")
    content = content.replace('\"', "").replace(",","")
    uploader = uploader.replace('\"', "").replace(",","")
    csvwriter.writerow([title, category, startdate, enddate, content,uploader])


def specialwrite(llist):
    csvwriter.writerow(llist)
#petitioncontent.close()

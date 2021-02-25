import csv  
def getTitles():  # csv파일로부터 기사 제목을 읽어 배열에 저장한후 배열을 반환하는 함수
    file = open('articles.csv','r',encoding='utf-8')
    rdr = csv.reader(file)
    titles = []
 
    for line in rdr:
        titles.append(line[0])

    file.close()
    return titles

def getContents(): # csv파일로부터 기사 내용을 읽어 배열에 저장한후 배열을 반환하는 함수
    file = open('articles.csv','r',encoding='utf-8')
    rdr = csv.reader(file)

    contents = []
    for line in rdr:
        contents.append(line[1])

    file.close()
    return contents

def getSummaries(): # csv파일로부터 기사 요약 내용을 읽어 배열에 저장한후 배열을 반환하는 함수
    file = open('summaries.csv','r',encoding='utf-8')
    rdr = csv.reader(file)
    summaries = []
    for line in rdr:
      summaries.append(line[0])
    file.close()
    return summaries
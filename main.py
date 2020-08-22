import split
import Cosine_Similarity
import Frequency
import os

TOTAL_PAGE = 20 # number of the printed page
TOTAL = 1000 # number of articles

def printTitleList(page, list_title):
    for i in range(int(TOTAL / TOTAL_PAGE) * (page - 1), int(TOTAL / TOTAL_PAGE) * (page)):
        print(str(i + 1) + ' : ' + list_title[i])

if __name__ == "__main__":
    list_title = split.splitArticles('title')
    list_contents = split.splitArticles('contents')
    page = 1
    os.system('cls')
    while True:
        printTitleList(page, list_title)
        print("----------------------------------------------------------------------------------------------\n")
        print("                      '>' : Next Page                '<' : Previous Page                      \n")
        print("----------------------------------------------------------------------------------------------\n")
        data = input("Please Input Data : ")
        if data == '>':
            if page < TOTAL_PAGE:
                page += 1
            os.system('cls')
        elif data == '<':
            if page > 1:
                page -= 1
            os.system('cls')
        elif data in list_title:
            index = list_title.index(data)
            os.system('cls')
            print('<' + list_title[index] + '>' + '\n')
            print(list_contents[index])
            list_sim = Cosine_Similarity.get_similar(list_title[index])
            print("\n\n<Similar Articles>\n")
            for i in range(0, len(list_sim)):
                print(str(i + 1) + ". " + list_sim[i])
            print("\n\n<High Frequency Word>\n")
            rank_word = Frequency.get_FrequencyWord(index)
            for i in range(0, len(rank_word)):
                print(str(i + 1) + ". " + rank_word[i])
            print("\n\n")
            data = input("Move Main Page or Exit Program? (Enter Yes or Exit) : ")
            if data.lower() == 'yes'.lower():
                page = 1
                os.system('cls')
            elif data.lower() == 'exit'.lower():
                break
        elif ' ' not in data:
            os.system('cls')
            rank_title = Frequency.get_FrequencyTitle(data)
            print("<Articles that '" + data + "' appeared a lot>\n")
            for i in range(0, len(rank_title)):
                print(str(i + 1) + ". " + rank_title[i])
            print("\n\n")
            data = input("Move Main Page or Exit Program? (Enter Yes or Exit) : ")
            if data.lower() == 'yes'.lower():
                page = 1
                os.system('cls')
            elif data.lower() == 'exit'.lower():
                break
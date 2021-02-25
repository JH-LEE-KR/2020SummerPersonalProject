from flask import Flask, render_template, request
from Cosine_Similarity import get_similar
from Frequency import get_FrequencyTitle, get_FrequencyWord
from readCsv import getTitles,getContents,getSummaries



summaries = getSummaries()
titles= getTitles()
contents = getContents()


app = Flask('')

@app.route('/')
def home(): #현재 페이지
  current_page =1
  return render_template('index.html',t = titles, c = contents,current_page = current_page,len = len(titles))

@app.route('/next')
def next():
  current_page = int(request.args.get('page'))

  return render_template('next.html',t = titles, c = contents, current_page = current_page, len = len(titles))

@app.route('/document')
def doc():
  idx = int(request.args.get('title'))
  similar_articles = get_similar(titles[idx],titles,contents)
  index = []
  for article in similar_articles:
      index.append(titles.index(article))
  print(type(index[0]))
  top_rank_words = get_FrequencyWord(idx)


  return render_template('document.html',title = titles[idx], content = contents[idx],curr_page = int(idx/20)+1,similar_articles = similar_articles,top_rank_words=top_rank_words, summary= summaries[idx],index=index)

@app.route("/word")
def word():
  keyword = request.args.get('word')
  result = get_FrequencyTitle(keyword)

  return render_template("word.html",titles=titles,keyword=keyword,result=result, n =len(result))

app.run()

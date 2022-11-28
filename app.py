import pickle
import numpy as np
from flask import Flask, render_template, request
popular = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_score = pickle.load(open('similarity_score.pkl', 'rb'))
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html',
                           book_name= list(popular['Book-Title'].values),
                           author = list(popular['Book-Author'].values),
                           image=list(popular['Image-URL-M'].values),
                           votes=list(popular['num_rating'].values),
                           rating=list(popular['avg_rating'].values))
@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/about')
def about_ui():
    return render_template('about.html')

@app.route('/recommend_books', methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    distances = similarity_score[index]
    similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]
    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(temp_df.drop_duplicates('Book-Title')['Book-Title'].values)
        item.extend(temp_df.drop_duplicates('Book-Title')['Book-Author'].values)
        item.extend(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values)

        data.append(item)

    print(data)
    return render_template('recommend.html', data=data)
if __name__ == '__main__':
     app.run(debug=True)
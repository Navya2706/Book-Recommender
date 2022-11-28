from flask import Flask, render_template
# popular = pickle.load(open('popular.pkl', 'rb'))
app= Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html'
                           # book_name= list(popular['Book-Title'].values),
                           # author = list(popular['Book-Author'].values),
                           # image=list(popular['Image-URL-M'].values),
                           # votes=list(popular['num-rating'].values),
                           # rating=list(popular['avg-rating'].values)
                           )

    if __name__ == '__main__':
         app.run(debug=True) 
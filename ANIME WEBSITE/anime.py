from flask import Flask, render_template
from database import load_data_from_db

app = Flask(__name__)

@app.route('/')
def index():
    my_videos = load_data_from_db("Movies")
    my_episodes = load_data_from_db("Episodes")
    return render_template('anime.html',
                           movies=my_videos,
                           episodes=my_episodes,
                           company_name='Meta')

if __name__ == '__main__': 
    app.run(debug=True)
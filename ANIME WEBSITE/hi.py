from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Video URL
    video_url = "https://eplayvid.net/watch/0d2a14cd8081fd2"

    # Ad URL (replace this with the actual ad URL)
    ad_url = "https://eplayvid.net/watch/0d2a14cd8081fd2"

    return render_template('anime.html', video_url=video_url, ad_url=ad_url)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, abort
import os
import markdown

app = Flask(__name__)

POSTS_DIR = "posts"

def get_all_posts():
    posts = []
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            path = os.path.join(POSTS_DIR, filename)
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
                html = markdown.markdown(content)
                title = content.split('\n')[0].replace("#", "").strip()
                slug = filename.replace(".md", "")
                posts.append({
                    "title": title,
                    "slug": slug,
                    "content": html
                })
    return posts

@app.route("/")
def home():
    posts = get_all_posts()
    return render_template("home.html", posts=posts)

@app.route("/post/<slug>")
def post(slug):
    file_path = os.path.join(POSTS_DIR, f"{slug}.md")
    if not os.path.exists(file_path):
        abort(404)

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        html = markdown.markdown(content)

    title = content.split('\n')[0].replace("#", "").strip()
    return render_template("post.html", title=title, content=html)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


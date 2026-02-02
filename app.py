from flask import Flask, render_template, abort
import os
import markdown2
import re
from flask import send_from_directory


app = Flask(__name__)

POSTS_DIR = "posts"


def get_all_posts():
    posts = []

    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            path = os.path.join(POSTS_DIR, filename)

            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
                # Extract date from frontmatter
                date_match = re.search(r'date:\s*(\d{4}-\d{2}-\d{2})', content)
                post_date = date_match.group(1) if date_match else "1970-01-01"

                # Extract first image
                image_match = re.search(r'!\[.*?\]\((.*?)\)', content)
                image_url = image_match.group(1) if image_match else None

                # Extract title (first markdown heading)
                title_match = re.search(r'^#\s+(.*)', content, re.MULTILINE)
                title = title_match.group(1).strip() if title_match else "Untitled Post"

                # Convert markdown to HTML (enable common extras)
                html = markdown2.markdown(
    content,
    extras=[
        "fenced-code-blocks",
        "tables",
        "strike",
        "task_list",
        "code-friendly",
        "cuddled-lists"
    ]
)


                slug = filename.replace(".md", "")

                posts.append({
                    "title": title,
                    "slug": slug,
                    "content": html,
                    "image": image_url,
                    "date": post_date
})
    posts.sort(key=lambda x: x["date"], reverse=True)
    return posts

@app.route("/")
def home():
    posts = get_all_posts()
    return render_template("home.html", posts=posts)

@app.route("/post/<slug>")
def post(slug):
    file_path = os.path.join("posts", f"{slug}.md")

    if not os.path.exists(file_path):
        abort(404)

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Extract title from markdown
    title_match = re.search(r'^#\s+(.*)', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Untitled Post"

    # Convert markdown to HTML (enable common extras)
    html = markdown2.markdown(
        content,
        extras=["fenced-code-blocks", "tables", "code-friendly", "metadata"],
    )

    return render_template("post.html", title=title, content=html)

@app.route('/google7fd7bebf24bb122c.html')
def gsc_verification():
    return send_from_directory('.', 'google7fd7bebf24bb122c.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


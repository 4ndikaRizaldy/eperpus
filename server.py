from flask import Flask, send_from_directory

app = Flask(__name__)

# Folder PDF
BOOKS_DIR = "books"

@app.route('/books/<filename>')
def get_book(filename):
    return send_from_directory(BOOKS_DIR, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)


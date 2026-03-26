from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id": 1, "title": "DevOps Handbook"},
    {"id": 2, "title": "Kubernetes Up and Running"}
]

@app.route("/")
def home():
    return "Bookstore API Running"

@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)

@app.route("/books", methods=["POST"])
def add_book():
    data = request.json
    books.append(data)
    return jsonify({"message": "Book added"}), 201

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "q": "Bạn coi trọng điều gì nhất?",
        "options": [("Gryffindor", "Lòng dũng cảm 🦁"),
                    ("Ravenclaw", "Sự thông thái 🦅"),
                    ("Hufflepuff", "Sự trung thành 🦡"),
                    ("Slytherin", "Tham vọng 🐍")]
    },
    {
        "q": "Bạn thích hoạt động nào nhất?",
        "options": [("Gryffindor", "Phiêu lưu, mạo hiểm"),
                    ("Ravenclaw", "Đọc sách, tìm tòi kiến thức"),
                    ("Hufflepuff", "Giúp đỡ bạn bè, làm việc nhóm"),
                    ("Slytherin", "Lãnh đạo, đạt thành công lớn")]
    },
    {
        "q": "Nếu có quyền chọn một vật phẩm phép thuật, bạn chọn gì?",
        "options": [("Gryffindor", "Thanh kiếm Gryffindor"),
                    ("Ravenclaw", "Quyển sách bí thuật cổ"),
                    ("Hufflepuff", "Chiếc chén chữa lành"),
                    ("Slytherin", "Đũa phép quyền năng nhất")]
    },
    {
        "q": "Bạn muốn bạn bè nhớ đến mình như người…?",
        "options": [("Gryffindor", "Gan dạ"),
                    ("Ravenclaw", "Thông minh"),
                    ("Hufflepuff", "Tốt bụng"),
                    ("Slytherin", "Quyền lực")]
    },
    {
        "q": "Con vật nào bạn thích nhất?",
        "options": [("Gryffindor", "Sư tử 🦁"),
                    ("Ravenclaw", "Đại bàng 🦅"),
                    ("Hufflepuff", "Lửng 🦡"),
                    ("Slytherin", "Rắn 🐍")]
    }
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        scores = {"Gryffindor": 0, "Ravenclaw": 0, "Hufflepuff": 0, "Slytherin": 0}
        
        for i in range(len(questions)):
            answer = request.form.get(f"q{i}")
            if answer:
                scores[answer] += 1
        
        house = max(scores, key=scores.get)
        return render_template("result.html", house=house, scores=scores)
    
    return render_template("index.html", questions=questions)

if __name__ == "__main__":
    app.run(debug=True)

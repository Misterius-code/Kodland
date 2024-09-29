from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key

# Define your questions and their correct answers
questions = [
    {
        "question": "What is the most popular Python library for AI development?",
        "options": ["TensorFlow", "Django", "Pandas", "Keras"],
        "answer": "TensorFlow"
    },
    {
        "question": "Which Python library is used for Natural Language Processing?",
        "options": ["Numpy", "NLTK", "Requests", "spaCy"],
        "answer": "NLTK"
    },
    {
        "question": "What is the common application of computer vision in AI?",
        "options": ["Image Recognition", "Data Mining", "Web Scraping", "Text Analysis"],
        "answer": "Image Recognition"
    },
    {
        "question": "Which library is primarily used in Python for image processing and computer vision?",
        "options": ["Matplotlib", "OpenCV", "Requests", "Pillow"],
        "answer": "OpenCV"
    },
    {
        "question": "What does the acronym CNN stand for in the context of deep learning?",
        "options": ["Central Neural Network", "Convolutional Neural Network", "Core Network Node", "Convolutional Neural Net"],
        "answer": "Convolutional Neural Network"
    }
]

# Define the quiz route
@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        user_answers = []
        for i in range(len(questions)):
            # Fetch the answer for each question using the dynamic name (e.g., question_1, question_2)
            selected_answer = request.form.get(f"question_{i}")
            user_answers.append(selected_answer)

        # Calculate the score
        score = sum(1 for i, q in enumerate(questions) if user_answers[i] == q['answer'])
        session['score'] = score

        if 'best_score' not in session or session['best_score'] < score:
            session['best_score'] = score

        return redirect(url_for('result'))

    best_score = session.get('best_score', 0)
    total_questions = len(questions)
    return render_template('quiz.html', questions=questions, best_score=best_score, total_questions=total_questions,enumerate=enumerate)

# Define the result route
@app.route("/result")
def result():
    score = session.get('score', 0)
    best_score = session.get('best_score', 0)
    total_questions = len(questions)
    return render_template('result.html', score=score, best_score=best_score, total_questions=total_questions)

if __name__ == "__main__":
    app.run(debug=True)

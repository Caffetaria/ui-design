from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load lesson and quiz data from JSON files
with open('lessons.json') as f:
    lessons = json.load(f)

with open('quiz.json') as f:
    quiz = json.load(f)

# In-memory storage for user progress (not suitable for production)
user_progress = {
    'last_lesson': None,
    'quiz_answers': {}
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/learn/<int:lesson_id>')
def learn(lesson_id):
    lesson = lessons.get(str(lesson_id))
    if lesson:
        user_progress['last_lesson'] = lesson_id
        return render_template('learn.html', lesson=lesson)
    return "Lesson not found", 404

@app.route('/quiz/<int:question_id>', methods=['GET', 'POST'])
def quiz_route(question_id):
    if request.method == 'POST':
        answer = request.form.get('answer')
        user_progress['quiz_answers'][question_id] = answer
        next_question_id = question_id + 1
        if str(next_question_id) in quiz:
            return jsonify(success=True, next_question=next_question_id)
        else:
            return jsonify(success=True, next_question=None)

    question = quiz.get(str(question_id))
    if question:
        return render_template('quiz.html', question=question, question_id=question_id, total_questions=len(quiz))
    return "Question not found", 404

@app.route('/result')
def result():
    # Calculate results based on user_progress data
    correct_answers = 0
    for q_id, q_data in quiz.items():
        if user_progress['quiz_answers'].get(int(q_id)) == q_data['correct']:
            correct_answers += 1
    return render_template('result.html', score=correct_answers, total=len(quiz))

if __name__ == '__main__':
    app.run(debug=True) 
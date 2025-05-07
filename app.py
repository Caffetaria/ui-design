from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import json
import os

app = Flask(__name__)
app.secret_key = 'tripletakesecretkey'  # For session management

# Load lesson and quiz data from JSON files
def load_json_data():
    with open('lessons.json') as f:
        lessons = json.load(f)

    with open('quiz.json') as f:
        quiz = json.load(f)
        
    return lessons, quiz

lessons, quiz = load_json_data()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/learn/<int:lesson_id>')
def learn(lesson_id):
    if str(lesson_id) in lessons:
        lesson = lessons[str(lesson_id)]
        next_id = lesson_id + 1
        prev_id = lesson_id - 1
        
        # Check if next/prev lessons exist
        has_next = str(next_id) in lessons
        has_prev = str(prev_id) in lessons
        
        return render_template('learn.html', 
                               lesson=lesson, 
                               lesson_id=lesson_id,
                               next_id=next_id if has_next else None,
                               prev_id=prev_id if has_prev else None)
    return "Lesson not found", 404

@app.route('/practice')
def practice():
    return render_template('practice.html')

@app.route('/quiz')
def quiz_start():
    # Reset quiz state
    if 'quiz_answers' in session:
        session.pop('quiz_answers')
    if 'current_question' in session:
        session.pop('current_question')
    
    # Start with question 1
    session['quiz_answers'] = {}
    session['current_question'] = 1
    
    return render_template('quiz_start.html', total_questions=len(quiz))

@app.route('/quiz/<int:question_id>', methods=['GET', 'POST'])
def quiz_question(question_id):
    if request.method == 'POST':
        answer = request.form.get('answer')
        
        # Make sure we have a quiz_answers dictionary
        if 'quiz_answers' not in session:
            session['quiz_answers'] = {}
        
        # Store this answer
        quiz_answers = session['quiz_answers']
        quiz_answers[str(question_id)] = answer
        session['quiz_answers'] = quiz_answers
        
        # Debug output to verify the answer is stored
        print(f"Storing answer for question {question_id}: {answer}")
        print(f"Current quiz_answers: {session['quiz_answers']}")
        
        next_question_id = question_id + 1
        if str(next_question_id) in quiz:
            session['current_question'] = next_question_id
            return redirect(url_for('quiz_question', question_id=next_question_id))
        else:
            # Force the session to be saved before redirecting
            session.modified = True
            return redirect(url_for('quiz_result'))

    question = quiz.get(str(question_id))
    if question:
        # Debug output for images
        if 'image_a' in question or 'image_b' in question:
            print(f"Question {question_id} images:")
            if 'image_a' in question:
                print(f"Image A: {question.get('image_a')}")
            if 'image_b' in question:
                print(f"Image B: {question.get('image_b')}")
            
        return render_template('quiz.html', 
                              question=question, 
                              question_id=question_id, 
                              total_questions=len(quiz))
    return "Question not found", 404

@app.route('/quiz/result')
def quiz_result():
    # Calculate results based on session data
    if 'quiz_answers' not in session:
        return redirect(url_for('quiz_start'))
    
    # Debug output to check what answers were recorded
    print("Final quiz_answers in session:")
    print(session['quiz_answers'])
    
    correct_answers = 0
    for q_id, q_data in quiz.items():
        user_answer = session['quiz_answers'].get(q_id)
        correct = q_data['correct']
        
        print(f"Question {q_id}: User answered '{user_answer}', correct is '{correct}'")
        
        if user_answer == correct:
            correct_answers += 1
    
    # Calculate percentage
    total_questions = len(quiz)
    score_percentage = int((correct_answers / total_questions) * 100)
    
    return render_template('result.html', 
                          score=correct_answers, 
                          total=total_questions,
                          percentage=score_percentage)

@app.route('/explore')
def explore():
    return render_template('explore.html')

if __name__ == '__main__':
    app.run(debug=True)

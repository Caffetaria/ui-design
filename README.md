# Triple Take: Photography Rule of Thirds App

Triple Take is a web application designed to teach photography enthusiasts about the Rule of Thirds composition technique. The app includes interactive lessons, practice exercises, and quizzes to help users master this fundamental photography principle.

## Features

- **Learn**: Step-by-step lessons explaining the Rule of Thirds with visual examples
- **Practice**: Interactive tool to practice applying the Rule of Thirds to different images
- **Quiz**: Test your knowledge with a series of questions about the technique
- **Explore**: View gallery of example photos showcasing effective use of the Rule of Thirds

## Installation and Setup

### Prerequisites

- Python 3.7 or higher
- Flask web framework

### Setting Up the Environment

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/triple-take.git
   cd triple-take
   ```

2. _Optional_ Create a virtual environment and activate it:

   ```
   python -m venv venv

   # On Windows:
   venv\Scripts\activate

   # On macOS/Linux:
   source venv/bin/activate
   ```

### Running the Application

1. Start the Flask application:

   ```
   python app.py
   ```

2. Open your web browser and navigate to:

   ```
   http://127.0.0.1:5000/
   ```

3. You should now see the Triple Take homepage and can begin your learning journey!

## Application Structure

The application is organized as follows:

```
triple-take/
├── app.py                 # Main Flask application
├── lessons.json           # Lesson content data
├── quiz.json              # Quiz questions and answers
├── requirements.txt       # Python dependencies
├── static/                # Static assets
│   ├── css/               # CSS styles
│   │   └── style.css      # Main stylesheet
│   └── img/               # Image placeholders (not included in repo)
└── templates/             # HTML templates
    ├── home.html          # Homepage template
    ├── learn.html         # Lesson page template
    ├── practice.html      # Practice page template
    ├── quiz.html          # Quiz question template
    ├── quiz_start.html    # Quiz start page template
    ├── result.html        # Quiz results template
    └── explore.html       # Gallery page template
```

## Usage Instructions

1. **Home Page**: Start by clicking "Start Learning" to begin the lessons or choose another section from the navigation bar.

2. **Learn Section**: Progress through lessons using the "Next Lesson" and "Previous Lesson" buttons. Each lesson builds on concepts from previous ones.

3. **Practice Section**: Use the interactive tool to apply the Rule of Thirds:

   - Drag the red grid overlay to position it over the image
   - Place important elements at intersection points
   - Click "Check Composition" to receive feedback
   - Adjust your approach based on feedback

4. **Quiz Section**: Test your knowledge by answering multiple-choice questions. Some questions include image examples where you need to identify correct application of the Rule of Thirds.

5. **Results**: After completing the quiz, you'll receive a score and feedback on your understanding.

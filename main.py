from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Убираем host и port из app.run(), так как Render сам управляет этим
@app.route('/')
def index():
    feedback_success = request.args.get('feedback_success', False)
    return render_template('index.html', feedback_success=feedback_success)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    name = request.form.get('name')
    email = request.form.get('email')
    rating = request.form.get('rating')
    message = request.form.get('message')
    
    print(f"Received feedback from {name} ({email}), rating: {rating}, message: {message}")
    return redirect(url_for('index', feedback_success=True))
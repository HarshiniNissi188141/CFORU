import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from flask import Flask, render_template, request, redirect, url_for, session, send_file
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)
app.secret_key = 'harshini_sigma_founder_key'

# --- 📧 EMAIL CONFIGURATION ---
# Replace these with your actual details for the email to work
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password" 

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            points INTEGER DEFAULT 0,
            final_score INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

# Run DB setup immediately
init_db()

# --- ROUTES ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('fullname')
    email = request.form.get('email')
    try:
        conn = sqlite3.connect('database.db')
        conn.execute("INSERT INTO users (name, email, points) VALUES (?, ?, 0)", (name, email))
        conn.commit()
        conn.close()
    except:
        pass # Ignore if user already exists
        
    session['user'] = {'name': name, 'email': email, 'points': 0, 'final_score': 0}
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    if 'user' not in session: return redirect(url_for('home'))
    
    # Fetch fresh data from DB
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email=?", (session['user']['email'],))
    data = cur.fetchone()
    conn.close()
    
    if data:
        session['user']['points'] = data[3]
        session['user']['final_score'] = data[4]
        session['user']['name'] = data[1]
        
    return render_template('dashboard.html', user=session['user'])

@app.route('/workspace/<category>')
def workspace(category):
    if 'user' not in session: return redirect(url_for('home'))
    return render_template('editor.html', category=category, user=session['user'])

@app.route('/update_points', methods=['POST'])
def update_points():
    if 'user' in session:
        conn = sqlite3.connect('database.db')
        conn.execute("UPDATE users SET points = points + 50 WHERE email = ?", (session['user']['email'],))
        conn.commit()
        conn.close()
    return "success"

@app.route('/quiz')
def quiz():
    if 'user' not in session: return redirect(url_for('home'))
    test_type = request.args.get('type', 'mockA')
    return render_template('quiz.html', test_type=test_type)

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    if 'user' not in session: return redirect(url_for('home'))

    score = int(request.form.get('score'))
    test_type = request.form.get('test_type')
    
    # --- SCORING CONFIGURATION ---
    # Final Exam = 40 Questions
    # Mock Tests = 20 Questions
    # Practice = 10 Questions
    max_score = 40 if test_type == 'final' else 20
    if test_type == 'practice': max_score = 10 

    percentage = (score / max_score) * 100
    
    # --- RANKING LOGIC ---
    rank = "Needs Improvement"
    color = "#ff3333" # Red
    msg = f"You scored {score}/{max_score}. Keep practicing!"

    if percentage >= 90:
        rank = "Elite Achiever 🏆"
        color = "#00ff00" # Green
        msg = "Flawless Victory! You are a master."
    elif percentage >= 75:
        rank = "Certified Professional"
        color = "#00ffff" # Cyan
        msg = "Congratulations! You passed the assessment."
    elif percentage >= 50:
        rank = "Intermediate"
        color = "#ffcc00" # Yellow
        msg = "Good attempt, but you need 75% to certify."

    # --- FINAL EXAM HANDLING ---
    if test_type == 'final':
        conn = sqlite3.connect('database.db')
        conn.execute("UPDATE users SET final_score = ? WHERE email = ?", (score, session['user']['email']))
        conn.commit()
        conn.close()
        
        # Update session immediately
        session['user']['final_score'] = score
        
        # Send Certificate ONLY if they pass (>= 75%)
        # 75% of 40 is 30 marks.
        if percentage >= 75:
            cert_path = generate_cert(session['user']['name'], score)
            send_email(session['user']['email'], session['user']['name'], cert_path)
            return redirect(url_for('certificate_sent'))

    return render_template('results.html', score=score, max=max_score, rank=rank, color=color, msg=msg)

@app.route('/certificate_sent')
def certificate_sent():
    return render_template('certificate_sent.html')

@app.route('/download/<filename>')
def download_file(filename):
    if 'user' not in session: return redirect(url_for('home'))
    
    # Security Check: Did they pass?
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT final_score FROM users WHERE email=?", (session['user']['email'],))
    result = cur.fetchone()
    conn.close()
    
    if result and result[0] >= 30: # 30 is 75% of 40
        return send_file(os.path.join('static', filename), as_attachment=True)
    else:
        return "<h1>Access Denied. Score 75% in Final Exam to Unlock.</h1>"

# --- HELPER FUNCTIONS ---

def generate_cert(name, score):
    save_path = os.path.join('static', 'generated_cert.png')
    try:
        img = Image.open(os.path.join('static', 'template.png'))
        draw = ImageDraw.Draw(img)
        
        # Use default font to avoid errors if arial isn't found
        font_L = ImageFont.load_default() 
        font_S = ImageFont.load_default()

        # Draw Text (Adjust coordinates 400,350 based on your image)
        draw.text((400, 350), name.upper(), fill="black", font=font_L)
        draw.text((550, 500), f"{score}/40", fill="black", font=font_S)
        draw.text((650, 750), "Harshini R. (Founder)", fill="black", font=font_S)
        
        img.save(save_path)
    except Exception as e:
        print(f"Cert Error: {e}")
    return save_path

def send_email(to_email, name, cert_path):
    print(f"Sending email to {to_email}...")
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = to_email
        msg['Subject'] = "🏆 You Passed! C FOR U Certification"
        
        body = f"Congratulations {name}!\n\nYou scored above 75%! Attached are your Certificate, Mind Map, and Revision Notes."
        msg.attach(MIMEText(body, 'plain'))
        
        # List of files to attach
        files = [cert_path, 'static/mindmap.pdf', 'static/revision.pdf']
        
        for f in files:
            if os.path.exists(f):
                part = MIMEBase('application', 'octet-stream')
                with open(f, 'rb') as file: part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(f)}')
                msg.attach(part)
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()
        print("✅ Email Sent Successfully!")
    except Exception as e:
        print(f"❌ Email Failed: {e}")

if __name__ == '__main__':
    app.run(debug=True)
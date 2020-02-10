from flask import Flask, render_template, redirect, url_for, request
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/email', methods=["GET", "POST"])
def email():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    fromaddr = "marcus.er.bader@gmail.com"
    toaddr = "marcusbader@hotmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject

    body = "Message sent from: " + name + "\n To reach " + name + " reply to this email address: " + email + "\n" + message
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, 'Cobcob94')
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)

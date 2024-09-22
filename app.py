from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib  # Biblioteca para enviar e-mails usando o protocolo SMTP
from email.mime.text import MIMEText  # Classe para criar o corpo do e-mail em texto

app = Flask(__name__)
app.secret_key = 'segredo_super_secreto'  # Necessário para utilizar flash messages

@app.route('/')
def index():
    return render_template('email_form.html')  # Renderiza o formulário HTML

@app.route('/send_email', methods=['POST'])
def send_email():
    # Obtém os dados do formulário
    usuario = request.form['remetente']
    senha = request.form['senha']
    destinatario = request.form['destinatario']
    assunto = request.form['assunto']
    corpo = request.form['corpo']

    # Configurações do servidor SMTP do Gmail
    smtp_servidor = 'smtp.gmail.com'
    smtp_porta = 587

    # Configurar a mensagem
    mensagem = MIMEText(corpo)
    mensagem['From'] = usuario
    mensagem['To'] = destinatario
    mensagem['Subject'] = assunto

    try:
        # Conectar ao servidor SMTP e enviar o e-mail
        with smtplib.SMTP(smtp_servidor, smtp_porta) as servidor:
            servidor.starttls()
            servidor.login(usuario, senha)
            servidor.sendmail(usuario, destinatario, mensagem.as_string())
            flash("Seu e-mail foi enviado com sucesso!", "success")
    except Exception as e:
        flash(f"Erro ao enviar e-mail: {e}", "danger")
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox

def send_email():
    try:
        from_email = entry_from.get()
        to_email = entry_to.get()
        password = entry_password.get()
        subject = entry_subject.get()
        message = text_message.get("1.0", tk.END)

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()

        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
root = tk.Tk()
root.title("Email Sender")

tk.Label(root, text="From Email:").grid(row=0, column=0)
tk.Label(root, text="Password:").grid(row=1, column=0)
tk.Label(root, text="To Email:").grid(row=2, column=0)
tk.Label(root, text="Subject:").grid(row=3, column=0)
tk.Label(root, text="Message:").grid(row=4, column=0)

entry_from = tk.Entry(root)
entry_password = tk.Entry(root, show="*")
entry_to = tk.Entry(root)
entry_subject = tk.Entry(root)
text_message = tk.Text(root, height=10, width=30)

entry_from.grid(row=0, column=1)
entry_password.grid(row=1, column=1)
entry_to.grid(row=2, column=1)
entry_subject.grid(row=3, column=1)
text_message.grid(row=4, column=1)

tk.Button(root, text="Send", command=send_email).grid(row=5, column=1)

root.mainloop()

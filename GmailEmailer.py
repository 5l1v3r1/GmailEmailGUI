from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.application import MIMEApplication
from email.MIMEBase import MIMEBase
import smtplib
class MyDialog:
	def __init__(self, parent):
		self.var = IntVar()
		#https://myaccount.google.com/lesssecureapps
		Label(root, text="You must enable Less Secure Apps in gmail! Browse here to do so:").pack()
#		Label(root, text="Browse here to do so:").pack()
		Label(root, text="https://myaccount.google.com/lesssecureapps").pack()
		Label(root, text="Enter your email address (must be gmail):").pack()
		self.a = Text(root, height=1, width=30)
		self.a.pack(padx=15)
		Label(root, text="Enter your gmail password:").pack()
		self.b = Entry(root, show="*", width=30) #Passord dots
		self.b.pack()
		Label(root, text="Email address's with spaces seperating them:").pack()
		self.c = Text(root, height=5, width=40)
		self.c.pack(padx=15)
		Label(root, text="Type Subject here:").pack()
		self.e = Text(root, height=2, width=40)
		self.e.pack(padx=15)
		Label(root, text="Type email body here (can paste from another document):").pack()
		self.f = Text(root, height=20, width=60)
		self.f.pack(padx=15)
		self.g = Checkbutton(root, text="Attachments", variable=self.var) #, command=self.send
		self.g.pack()
		self.datbutton = Button(root, text="Press to send!", command=self.send)
		self.datbutton.pack(pady=15)
	def send(self):
		self.datbutton.configure(state=DISABLED) # Turns button grey to prevent double sending
		count = 0
		T = Text(root, bg="grey93", borderwidth=0, height=1, width=33)
		T.pack(padx=5)
		T.insert(END, "Sending now, please wait...")
		if self.var.get() == 1: # checking the box sets "var" variable to 1, which indicates an attachment
			reco = tkFileDialog.askopenfilename()
			os.path.split(reco)
			beco = os.path.split(reco)[1]
		toaddy = self.c.get("1.0", "end-1c")
		for line in toaddy.split(): # for every email address, do a seperate send
			fromaddy = self.a.get("1.0", "end-1c")
			passwordz = self.b.get() 
			subject = self.e.get("1.0", "end-1c")
			bodyz = self.f.get("1.0", "end-1c")
			sendto = line # Who are you sending to?
			password = passwordz  # Password
			fromaddr = fromaddy
			toaddr = sendto
			msg = MIMEMultipart()
			msg['From'] = fromaddr
			msg['To'] = str(toaddr)
			msg['Subject'] = subject
			body = ''.join(bodyz)
			msg.attach(MIMEText(body, 'plain'))
			if self.var.get() == 1: # checking the box sets "var" variable to 1, which indicates an attachment
				part = MIMEBase('application', "octet-stream")
				part.set_payload(open(reco, "rb").read())
				part.add_header('Content-Disposition', 'attachment; filename=' + beco)
				msg.attach(part)
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls()
			server.login(fromaddr, password)
			text = msg.as_string()
			server.sendmail(fromaddr, toaddr, text)
			server.quit()
			count = count + 1 #to print amount sent at the end
		T = Text(root, bg="grey93", borderwidth=0, height=1, width=33)
		T.pack(padx=5)
		T.insert(END, "Sent to " + str(count) + " email address's!")
root = Tk()
root.title("Mass Gmail Emailer")
#root.withdraw() #hides second window
MyDialog(root)
root.wait_window() #removed d.top (second window)

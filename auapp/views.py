from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from random import randrange
from django.core.mail import send_mail
from todo_project.settings import DEFAULT_FROM_EMAIL

# Use Maileroo domain as sender
SENDER_EMAIL = DEFAULT_FROM_EMAIL

def usignup(request):
	if request.method=="POST":
		un=request.POST.get("un")
		em=request.POST.get("em")
		try:
			usr=User.objects.get(username=un)
			return render(request,'usignup.html',{'msg':'username already taken'})
		except User.DoesNotExist:
			try:
				usr=User.objects.get(email=em)
				return render(request,'usignup.html',{'msg':'email already registered'})
			except User.DoesNotExist:
				text="1234567890abcdefghojglmnopqrstuvwxyz"
				pw=""
				for i in range(6):
					pw= pw + text[randrange(len(text))]
				
				html_message = f"""
				<!DOCTYPE html>
				<html>
				<head>
					<style>
						body {{ font-family: 'Arial', sans-serif; background-color: #f4f4f4; margin: 0; padding: 0; }}
						.email-container {{ max-width: 600px; margin: 40px auto; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
						.header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 40px 20px; text-align: center; color: white; }}
						.header h1 {{ margin: 0; font-size: 28px; }}
						.content {{ padding: 40px 30px; }}
						.welcome {{ font-size: 18px; color: #333; margin-bottom: 20px; }}
						.credentials {{ background: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #667eea; }}
						.credential-item {{ margin: 10px 0; font-size: 16px; }}
						.credential-label {{ color: #666; font-weight: 600; }}
						.credential-value {{ color: #667eea; font-weight: bold; font-size: 18px; }}
						.button {{ display: inline-block; background: #667eea; color: white !important; padding: 15px 40px; text-decoration: none; border-radius: 5px; margin: 20px 0; font-weight: bold; box-shadow: 0 4px 6px rgba(102, 126, 234, 0.3); }}
						.button:hover {{ background: #5568d3; }}
						.footer {{ background: #f8f9fa; padding: 20px; text-align: center; color: #666; font-size: 14px; }}
					</style>
				</head>
				<body>
					<div class="email-container">
						<div class="header">
							<h1>🎯 Welcome to TaskFlow!</h1>
						</div>
						<div class="content">
							<p class="welcome">Hi <strong>{un}</strong>! 👋</p>
							<p>Your account has been created successfully. We're excited to have you on board!</p>
							
							<div class="credentials">
								<div class="credential-item">
									<span class="credential-label">Username:</span><br>
									<span class="credential-value">{un}</span>
								</div>
								<div class="credential-item">
									<span class="credential-label">Password:</span><br>
									<span class="credential-value">{pw}</span>
								</div>
							</div>
							
							<p style="color: #666; font-size: 14px;">
								<strong>⚠️ Important:</strong> Please save your password securely. You can change it after logging in.
							</p>
							
							<center>
								<a href="http://127.0.0.1:8000/ulogin/" class="button">Login to TaskFlow →</a>
							</center>
							
							<p style="color: #999; font-size: 13px; margin-top: 30px;">
								If you didn't create this account, please ignore this email.
							</p>
						</div>
						<div class="footer">
							Made with ❤️ by TaskFlow<br>
							© 2025 TaskFlow. All rights reserved.
						</div>
					</div>
				</body>
				</html>
				"""
				
				plain_message = f"Hi {un}!\n\nWelcome to TaskFlow!\n\nYour login credentials:\nUsername: {un}\nPassword: {pw}\n\nLogin at: http://127.0.0.1:8000/ulogin/\n\nBest regards,\nTaskFlow Team"
				
				from django.core.mail import EmailMultiAlternatives
				email = EmailMultiAlternatives(
					"Welcome to TaskFlow - Your Account is Ready! 🎉",
					plain_message,
					SENDER_EMAIL,
					[em]
				)
				email.attach_alternative(html_message, "text/html")
				email.send(fail_silently=False)
				
				usr=User.objects.create_user(username=un,password=pw,email=em)
				usr.save()
				return redirect('ulogin')
	else:
		return render(request,'usignup.html')

def ulogin(request):
	if request.method=="POST":
		un=request.POST.get('un')
		pw=request.POST.get("pw")
		remember_me=request.POST.get('remember_me')
		usr=authenticate(username=un,password=pw)
		if usr is None:
			return render(request,'ulogin.html',{'msg':'Invalid Credentials'})
		else:
			login(request,usr)
			# Set session expiry based on remember me checkbox
			if not remember_me:
				# Session expires when browser closes (default is 2 weeks)
				request.session.set_expiry(0)
			else:
				# Session expires after 30 days
				request.session.set_expiry(2592000)  # 30 days in seconds
			return redirect('home')
	else:
		return render(request,'ulogin.html')

def ulogout(request):
	logout(request)
	return redirect('ulogin')

def guest_login(request):
	"""Guest login with demo account"""
	# Create guest user if it doesn't exist
	guest_username = "guest_demo"
	guest_password = "demo123"
	
	try:
		guest_user = User.objects.get(username=guest_username)
	except User.DoesNotExist:
		guest_user = User.objects.create_user(
			username=guest_username,
			password=guest_password,
			email="guest@taskflow.demo"
		)
		guest_user.save()
	
	# Authenticate and login
	user = authenticate(username=guest_username, password=guest_password)
	if user:
		login(request, user)
		# Set session to expire when browser closes for guest
		request.session.set_expiry(0)
		return redirect('home')
	else:
		return redirect('ulogin')

def uresetpassword(request):
	if request.method=="POST":
		un=request.POST.get("un")
		em=request.POST.get("em")
		try:
			usr=User.objects.get(username=un) and User.objects.get(email=em)
			text="1234567890abcdefghojglmnopqrstuvwxyz"
			pw=""
			for i in range(6):
				pw= pw + text[randrange(len(text))]
			
			# Beautiful HTML email for password reset
			html_message = f"""
			<!DOCTYPE html>
			<html>
			<head>
				<style>
					body {{ font-family: 'Arial', sans-serif; background-color: #f4f4f4; margin: 0; padding: 0; }}
					.email-container {{ max-width: 600px; margin: 40px auto; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
					.header {{ background: linear-gradient(135deg, #f59e0b 0%, #dc2626 100%); padding: 40px 20px; text-align: center; color: white; }}
					.header h1 {{ margin: 0; font-size: 28px; }}
					.content {{ padding: 40px 30px; }}
					.welcome {{ font-size: 18px; color: #333; margin-bottom: 20px; }}
					.credentials {{ background: #fef3c7; padding: 20px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #f59e0b; }}
					.credential-item {{ margin: 10px 0; font-size: 16px; }}
					.credential-label {{ color: #666; font-weight: 600; }}
					.credential-value {{ color: #dc2626; font-weight: bold; font-size: 18px; }}
					.button {{ display: inline-block; background: #dc2626; color: white !important; padding: 15px 40px; text-decoration: none; border-radius: 5px; margin: 20px 0; font-weight: bold; box-shadow: 0 4px 6px rgba(220, 38, 38, 0.3); }}
					.button:hover {{ background: #b91c1c; }}
					.footer {{ background: #f8f9fa; padding: 20px; text-align: center; color: #666; font-size: 14px; }}
					.warning {{ background: #fef2f2; border-left: 4px solid #dc2626; padding: 15px; margin: 20px 0; border-radius: 5px; }}
				</style>
			</head>
			<body>
				<div class="email-container">
					<div class="header">
						<h1>🔐 Password Reset</h1>
					</div>
					<div class="content">
						<p class="welcome">Hi <strong>{un}</strong>! 👋</p>
						<p>Your password has been reset successfully.</p>
						
						<div class="credentials">
							<div class="credential-item">
								<span class="credential-label">Username:</span><br>
								<span class="credential-value">{un}</span>
							</div>
							<div class="credential-item">
								<span class="credential-label">New Password:</span><br>
								<span class="credential-value">{pw}</span>
							</div>
						</div>
						
						<div class="warning">
							<strong>⚠️ Security Tip:</strong> Please change this password after logging in for better security.
						</div>
						
						<center>
							<a href="http://127.0.0.1:8000/ulogin/" class="button">Login Now →</a>
						</center>
						
						<p style="color: #999; font-size: 13px; margin-top: 30px;">
							If you didn't request this password reset, please contact us immediately.
						</p>
					</div>
					<div class="footer">
						Made with ❤️ by TaskFlow<br>
						© 2025 TaskFlow. All rights reserved.
					</div>
				</div>
			</body>
			</html>
			"""
			
			plain_message = f"Hi {un}!\n\nYour password has been reset.\n\nNew credentials:\nUsername: {un}\nPassword: {pw}\n\nLogin at: http://127.0.0.1:8000/ulogin/\n\nBest regards,\nTaskFlow Team"
			
			from django.core.mail import EmailMultiAlternatives
			email = EmailMultiAlternatives(
				"TaskFlow - Password Reset Successful 🔐",
				plain_message,
				SENDER_EMAIL,
				[em]
			)
			email.attach_alternative(html_message, "text/html")
			email.send(fail_silently=False)
			
			usr.set_password(pw)
			usr.save()
			return redirect('ulogin')
		except User.DoesNotExist:
			return render(request,'uresetpassword.html',{'msg':'Invalid Credentials'})

	else:
		return render(request,'uresetpassword.html')

import praw
from datetime import datetime
from time import sleep

start_time = datetime.now()
update_counter = 1

while 1: #run this on the cloud indefinitely until you stop it manually

	###################################
	""" Scraping Reddit with PRAW """
	###################################
	reddit = praw.Reddit(client_id='your_client_id', \
	                     client_secret='your_client_secret', \
	                     user_agent='your_user_agent', \
	                     username='your_username ', \
	                     password='your_password')
	subreddit = reddit.subreddit('bapcsalescanada') # this is the subreddit I am monitoring
	frequency = 1800 # every 30 mins
	link_dict = {}
	reddit_url = 'https://www.reddit.com'
	for submission in subreddit.new(limit=30):
		# I am watching for "SSD" posts during the last _frequency_ secondes
	    if (datetime.now().timestamp() - submission.created_utc < frequency) and ("SSD" in submission.title.upper()) :
	        link_dict[(submission.title.encode('utf-8')).decode('utf-8')] = ((reddit_url+submission.permalink).encode('utf-8')).decode('utf-8')
	# formatting the titles and links
	new_links = '\n'.join('[{}] - {}: {}'.format(i+1,key,val) for i, (key,val) in enumerate(link_dict.items()))
	print (new_links)

	##########################
	""" Sending the email """ 
	##########################
	import smtplib, ssl

	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = "sender_email@gmail.com"  # Enter your address
	receiver_email = "receiver_email@gmail.com"  # Enter receiver address
	password = "your_sender_email_password"
	if len(link_dict)>0:
		msg = f"Here, check the latest submissions in the r/{subreddit.display_name} during the last {frequency//60} minutes:\n{new_links}. "
		message = f"""\
		Subject: Update r/{subreddit.display_name}

		Hi there

		{msg}"""

		message = message.encode("ascii", errors="ignore") # Avoid ascii code errors due to special characters

		context = ssl.create_default_context()
		with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		    server.login(sender_email, password)
		    server.sendmail(sender_email, receiver_email, message)

	tdiff = datetime.now() - start_time
	print(f"Update number {update_counter} after {tdiff.seconds//3600} hours and {tdiff.seconds//60-tdiff.seconds//3600*60} minutes") # watch progress
	update_counter += 1
	sleep(frequency)	#Executing every _frequency_ seconds
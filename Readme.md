# Monitoring a subreddit for SSD deals

I was waiting for a good deal to upgrade my HDD to SDD. Last Black Friday, I missed quite good SSD deals. The reason: I come few our later and find out that the item is already out of stock due to huge demand. I was so frustrated it happened twice in the same day so I wrote this code to do the monitoring for me!

My source for tech deals was [this subreddit](https://www.reddit.com/r/bapcsalescanada/).
The idea consists of three main components:
- __Scrapping relevent posts from the subreddit__: For this purpose, you should create an App on your Reddit account to have credential allowing you to access the Reddit API. It is simple and you can check this tutorial [here](http://www.storybench.org/how-to-scrape-reddit-with-python/) which detaills the process step by step.
- __Sending notifications__: Using _smtplib_, an email is sent to notify you that a deal has been detected
- __Hosting the code on the cloud__: At first, I ran the code in the background on my smartphone. Then I just hosted the code on [pythonanywhere.com](https://www.pythonanywhere.com/) which grant you ressources to run your code even with free account :) .

Result: I was able to snatch a great deal for a 1GB Crucial MX500!
# amazonPriceTracker
A Python script that checks the price for a product on Amazon and sends you an Email if the price is below the given constant.
### Constants
- EMAIL: Your Email adress, set as environment variable
- PASSWORD: Password of your Email account, set as environment variable
- SMTP: SMTP Server of your Email provider, change in main.py if you're not using Gmail
- URL: URL to the Amazon product you want to track
- BUY_AT: If the current price is lower than this, you'll receive an Email

Make sure you've enabled less secure apps if you are sending from a Gmail account.<br>
You may have to change the request headers, you can ckeck yours on http://myhttpheader.com/.

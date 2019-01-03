# EmailBodyRetriever
This project's main aim is to remove the unnecessary text like From, To, BCC, CC etc and capture main body of the email
## Summary
What Email Body Retriever does is that it captures the body of the last email to an on-going email thread.

for example, the following is the forwarded message from some consultants:
```
---------- Forwarded message ---------
From: CANADA-Be Best! <canada.bebestconsultants@gmail.com>
Date: Mon, 26 Nov 2018, 13:25
Subject: Re: Suggest universities for MS in Computer Science
To: Thiruthuvaraj Rajasekhar <trsekhar.123@gmail.com>, BBC Helpdesk <helpdesk@bebestconsultants.com>, Karam Kaur <Karam@bebestconsultants.com>



Dear Rajsekhar

PFA  xcel of canada list of universities
Kindly please confirm the universities


Please find the bank details to transfer the amount.

Thanks and regards,
Samyuktha
```
The email conversation consists of unnecessary information like Forwaded message, From, Date etc. The main message is:
```
PFA xcel of canada list of universities
Kindly please confirm the universities

Please find the bank details to transfer the amount.

```


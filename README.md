# EmailBodyRetriever
This project's main aim is to remove the unnecessary text like From, To, BCC, CC etc and capture main body of the email
## Summary
What Email Body Retriever does is that it captures the body of the last email to an on-going email thread.

for example, the following is the forwarded message from some consultants:
```
---------- Forwarded message ---------
From: CANADA-Be Best! <canada.bebestcosadasdas@gmail.com>
Date: Mon, 26 Nov 2018, 13:25
Subject: Re: Suggest universities for MS in Computer Science
To: Ram Kumar <trram.12332@gmail.com>, BBC Helpdesk <helpdesk@bebestcsdassdants.com>, Karam Kaur <Karam@asdasdas.com>



Dear Ram

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


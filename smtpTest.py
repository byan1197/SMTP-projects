import smtplib

gmailSMTP = smtplib.SMTP('smtp.gmail.com', 587)
gmailSMTP.ehlo()
gmailSMTP.starttls()
account = #GMAIL ACCOUNT
gmailSMTP.login (account, #PASSWORD)

recip = #INSERT RECIPIENT HERE

for i in range (1,10):
    gmailSMTP.sendmail (account, recip, 'Subject: TEST #' +str(i) +'.\nHello this is a test to see if my SMTP server is working dont respond jen. Sincerely, Bond')

gmailSMTP.quit()

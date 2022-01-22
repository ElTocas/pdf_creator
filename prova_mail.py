import webbrowser
import yagmail

def open_mail_old(receiver,subject,body):
    webbrowser.open('mailto:?to=' + receiver + '&subject=' + subject + '&body=' + body, new=1)

def open_mail(sender,receiver,subject,body):

    yag = yagmail.SMTP(sender)
    yag.send(
        to=receiver,
        subject="Yagmail test with attachment",
        contents=body, 
        #attachments=filename,
    )
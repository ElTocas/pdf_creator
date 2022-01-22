import webbrowser

def open_mail(receiver,subject,body):
    webbrowser.open('mailto:?to=' + receiver + '&subject=' + subject + '&body=' + body, new=1)

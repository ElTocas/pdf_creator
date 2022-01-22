import webbrowser
import yagmail
import streamlit as st

def open_mail_old(receiver,subject,body):
    webbrowser.open('mailto:?to=' + receiver + '&subject=' + subject + '&body=' + body, new=1)

def open_mail(sender,receiver,subject,body):
    #
    password = st.text_input("Enter a password", type="password")
    if st.button("send"):
        yagmail.register(sender,password)
        yag = yagmail.SMTP(sender,password)
        yag.send(
            to=receiver,
            subject="Yagmail test with attachment",
            contents=body, 
            #attachments=filename,
        )
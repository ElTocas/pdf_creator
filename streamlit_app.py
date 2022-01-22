import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date, timedelta, datetime
import streamlit as st
from streamlit.components.v1 import iframe

import prova_mail as u


st.set_page_config(layout="centered", page_icon="🎓", page_title="British Generator")
st.title("British PDF Generator")

st.write(
    "Questa App genera un foglio PDF che potrai inviarci per aiutare la scuola ad organizzare il corso migliore per te"
)

def ok_gen(campo):
    if campo:
        campo = " O "
    else:
        campo = "   "
    return campo



env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template2.html")


st.info("Per favore completa tutti i campi richiesti:")
form = st.form("template_form")
Nome = form.text_input("Nome:",autocomplete ="given-name")
Cognome = form.text_input("Cognome:",autocomplete ="family-name")
indirizzo_mail = form.text_input("E-mail",autocomplete ="email")
telefono = form.text_input("Telefono",autocomplete ="tel")


course = form.selectbox(
    "Scegli il livello del corso che vorresti seguire",
    ["A2", "A1","B2", "B1","C2", "C1"],
    index=3,
)
course_type = form.selectbox(
    "Scegli che tipologia di corso vorresti seguire",
    ["Individuale", "Semi-individuale","Gruppo"],
    index=1,
)
course_presenza = form.selectbox(
    "Scegli la tipologia delle lezioni",
    ["Solo Online", "Ibrido (online e in presenza)","Solo in presenza"],
    index=1,
)


today = date.today()
tomorrow = today + timedelta(days=30)

start_date = form.date_input('Scegli quando dovrebbe partire il corso', today + timedelta(7),min_value=today,help="E' solo una data indicativa, non preoccuparti se non potrai rispettarla")
end_date = form.date_input('Scegli quando dovrebbe finire il corso', tomorrow + timedelta(7),help="E' solo una data indicativa, non preoccuparti se non potrai rispettarla")

#if start_date > end_date:
#    form.error('Error: End date must fall after start date.')

form.info("Per favore seleziona i giorni e le ore indicative in cui preferiresti avere le lezioni")
lun, mar, mer, giov, ven, sab = form.columns(6)
lun.caption("Lunedì")
lu1 = lun.checkbox("Mattina",key="lun mat")
lu2 = lun.checkbox("Pomeriggio",key="lun pom")
lu3 = lun.checkbox("Sera",key="lun ser")

mar.caption("Martedì")
ma1 = mar.checkbox("Mattina",key="mar mat")
ma2 = mar.checkbox("Pomeriggio",key="mar pom")
ma3 = mar.checkbox("Sera",key="mar ser")

mer.caption("Mercoledì")
me1 = mer.checkbox("Mattina",key="mer mat")
me2 = mer.checkbox("Pomeriggio",key="mer pom")
me3 = mer.checkbox("Sera",key="mer ser")

giov.caption("Giovedì")
gi1 = giov.checkbox("Mattina",key="giov mat")
gi2 = giov.checkbox("Pomeriggio",key="giov pom")
gi3 = giov.checkbox("Sera",key="giov ser")

ven.caption("Venerdì")
ve1 = ven.checkbox("Mattina",key="ven mat")
ve2 = ven.checkbox("Pomeriggio",key="ven pom")
ve3 = ven.checkbox("Sera",key="ven ser")

sab.caption("Sabato")
sa1 = sab.checkbox("Mattina",key="sab mat")

submit = form.form_submit_button("Generate PDF")


lu1 = ok_gen(lu1);lu2 = ok_gen(lu2);lu3 = ok_gen(lu3)
ma1 = ok_gen(ma1);ma2 = ok_gen(ma2);ma3 = ok_gen(ma3)
me1 = ok_gen(me1);me2 = ok_gen(me2);me3 = ok_gen(me3)
gi1 = ok_gen(gi1);gi2 = ok_gen(gi2);gi3 = ok_gen(gi3)
ve1 = ok_gen(ve1);ve2 = ok_gen(ve2);ve3 = ok_gen(ve3)
sa1 = ok_gen(sa1)
if submit:
    html = template.render(
        nome=Nome,
        cognome=Cognome,
        indirizzo_mail = indirizzo_mail,
        telefono = telefono,
        course=course,
        course_type = course_type,
        course_presenza = course_presenza,
        start_date = start_date,
        end_date = end_date,
        lu1=lu1, lu2=lu2, lu3=lu3,
        ma1=ma1, ma2=ma2, ma3=ma3,
        me1=me1, me2=me2, me3=me3,
        gi1=gi1, gi2=gi2, gi3=gi3,
        ve1=ve1, ve2=ve2, ve3=ve3,
        sa1=sa1,
        date=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        
    )

    pdf = pdfkit.from_string(html, False)
    st.balloons()

    st.success("🎉 Your PDF was generated!")
    # st.write(html, unsafe_allow_html=True)
    # st.write("")
    nome_file_pdf = Nome + "_" + Cognome + "_" + date + ".pdf"

    st.download_button(
        "⬇️ Download PDF",
        data=pdf,
        file_name=nome_file_pdf,
        mime="application/octet-stream",
    )

    if st.button("INVIA MAIL (beta):"):
        subject = "Info Iscrizione  " + Nome + " " + Cognome + " Precompiled"
        body = "Ciao"
        u.open_mail("to.martire@gmail.com",subject,body)
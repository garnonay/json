
  
import streamlit as st
import pandas as pd

st.title('Conversor de R4DA - Pre')

slack = st.text_area('Pega la respuesta de Slack sin incluir **New purchase created**')

st.write("")
st.write("")

slack2 = slack.replace("type", "operation")
slack3 = slack2.replace("status: approved\n", "")
slack4 = slack3.replace("asset: Bitcoin\n", "")
slack5 = slack4.replace("asset: Ethereum\n", "")
slack6 = slack5.replace("\n", ",\n")
slack7 = slack6.replace("operation", "\"operation\"")
slack7 = slack7.replace("netAmount", "\"netAmount\"")
slack7 = slack7.replace("amount", "\"amount\"")
slack7 = slack7.replace("fee", "\"fee\"")
slack7 = slack7.replace("rate", "\"rate\"")
slack7 = slack7.replace("id: ", "\"id\": \"")
slack7 = slack7.replace("purchased", "\"purchased\"")
slack7 = slack7.replace("buy", "\"buy\"")
slack7 = slack7.replace("sell", "\"sell\"")
if slack7 != "":
    slack7 = "{\n" + slack7 + "\"" + "\n }"
    st.code(slack7, language='json')
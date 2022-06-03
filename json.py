import streamlit as st
import pandas as pd

st.header('Conversor de R4DA - Pre')

slack = st.text_area('Pega la respuesta de slack')

st.write("")
st.write("")

slack2 = slack.replace("type", "operation")
slack3 = slack2.replace("status: approved\n", "")
slack4 = slack3.replace("asset: Bitcoin\n", "")
slack5 = slack4.replace("\n", ",\n")
slack6 = slack5.replace("operation", "\"operation\"")
slack6 = slack6.replace("netAmount", "\"netAmount\"")
slack6 = slack6.replace("amount", "\"amount\"")
slack6 = slack6.replace("fee", "\"fee\"")
slack6 = slack6.replace("rate", "\"rate\"")
slack6 = slack6.replace("id: ", "\"id\": \"")
slack6 = slack6.replace("purchased", "\"purchased\"")
slack6 = slack6.replace("buy", "\"buy\"")
slack6 = slack6.replace("sell", "\"sell\"")
slack6 = slack6 + "\""


st.code(slack6, language='json')
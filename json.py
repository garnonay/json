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
slack6 = slack5.replace("asset: Polkadot\n", "")
slack7 = slack6.replace("asset: Cardano\n", "")
slack8 = slack7.replace("asset: Chainlink\n", "")
slack9 = slack8.replace("asset: Solana\n", "")
slack10 = slack9.replace("asset: Uniswap\n", "")
slack11= slack10.replace("asset: Polygon\n", "")
slack12 = slack11.replace("\n", ",\n")
slack13 = slack12.replace("operation", "\"operation\"")
slack13 = slack13.replace("netAmount", "\"netAmount\"")
slack13 = slack13.replace("amount", "\"amount\"")
slack13 = slack13.replace("fee", "\"fee\"")
slack13 = slack13.replace("rate", "\"rate\"")
slack13 = slack13.replace("id: ", "\"id\": \"")
slack13 = slack13.replace("purchased", "\"purchased\"")
slack13 = slack13.replace("buy", "\"buy\"")
slack13 = slack13.replace("sell", "\"sell\"")
if slack13 != "":
    slack13 = "{\n" + slack13 + "\"" + "\n }"
    st.code(slack13, language='json')
import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Gerenciador de Sócios Famil")

@st.cache_data
def extrair_dados():
    dados = pd.DataFrame({
        "Nome": ["João", "Maria"],
        "Idade": [20, 30]
    })
    return dados

df = extrair_dados()


with st.expander("Editação manual"):
    novo_df = st.data_editor(
        df,
        num_rows="dynamic",
        use_container_width=True
    )

    if st.button("💾 Salvar"):
        novo_df.to_csv("dados.csv", index=False)
        st.success("Alterações salvas!")

'''
st.markdown("""  """)
st.image(image, caption=None)
st.metric(label=""
    value=""
    delta=""
    )

st.plotly.chart()

st.text_input()

st.number_input()

st.selectbox(
    "Texto",
    options=
    )

st.multiselect(
    "Texto",
    options=
    )

    st.slider(
    label="",
    min_value=1,
    max_value=1,
    )
    minimo = faixa[0]
    maximo = faixa[1]

    st.sidebar

    col1,col2,col3 = st.columns
'''

'''
https://gerenciador-de-socios-famil-cqkgmp9oplyhpbiyrrcury.streamlit.app/

https://gitmoji.dev/
'''

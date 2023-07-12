import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home")


#image_path ='logo_cury_company.png'
image = Image.open('logo.png')
st.sidebar.image(image, width=120)

st.sidebar.markdown('# Cury Company')
st.sidebar.markdown('## Fastest Delivery in Town')
st.sidebar.markdown("""---""")

st.write("# Curry Company Growth Dashboard")

st.markdown(
    """
    Growth Dashboard foi construido para acompanhar as métricas de cresceimento dos Entregadores e Restaurantes.
    ### Como utilizar esse Growth Dahboard?
    - Visão Empresa:
        - Visão Gerencial: Metricas gerais de comportamento.
        - Visão Tática: Indicadores semanais de crescimento.
        - Visão Geográfica: Insights de geolocalização.
    - Visão Entregador:
        - Acompanhamento dos indicadores semanais de crescimento.
    - Visão Restaurante:
        - Indicadores semanais de crescimento dos restaurantes.
""")

    
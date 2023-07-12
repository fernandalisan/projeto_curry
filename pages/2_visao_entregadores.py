#=========================================
# Importação dos arquivos
#=========================================

import pandas as pd
import io
import plotly.express as px
from PIL import Image
import streamlit as st
from datetime import datetime
from streamlit_folium import folium_static
import folium



st.set_page_config(page_title='Visão Entregadores', page_icon='🚚', layout='wide')

#=========================================
# Funções
#=========================================

# 1-Função para limpeza de dados do DataFrame

def clean_code(df1):
    """Esta função tem a responsabilidade de limpar o dataframe.
        Tipos de limpeza:
        1-Conversões - Tipos de dados
        2-Excluindo NaN
        3-Tirando os espaços das células nas colunas
        4-Limpeza da coluna tempo (time taken : tirando o (min))
        
        imput: dataframe
        output: dataframe
    """    
    ###Início da limpeza de dados###
    #Excluindo 'NaN ' da coluna Age:
    linhas_selecionadas = df1['Delivery_person_Age'] != 'NaN '
    #Localizando as linhas que contém NaN
    #df1 = df1.loc[linhas, colunas]
    df1 = df1.loc[linhas_selecionadas, :].copy()

    #conversões:
    #Delivery_person_Age - conversão de Object(str) para int
    df1['Delivery_person_Age'] = df1['Delivery_person_Age'].astype(int)

    #coluna Delivery_person_Ratings - conversão de Object(str) para float
    df1['Delivery_person_Ratings'] = df1['Delivery_person_Ratings'].astype(float)

    #coluna Order_Date - conversão de Object(str) para data
    df1['Order_Date'] = pd.to_datetime( df1['Order_Date'], format = '%d-%m-%Y' )

    ###Excluindo 'NaN ' da coluna 'multiple_deliveries':
    linhas_selecionadas = df1['multiple_deliveries'] != 'NaN '
    df1 = df1.loc[linhas_selecionadas, :].copy()

    ###Excluindo 'NaN ' da coluna 'City':
    linhas_selecionadas = df1['City'] != 'NaN '
    df1 = df1.loc[linhas_selecionadas, :].copy()

    ###Excluindo 'NaN ' da coluna 'Road_traffic_density':
    linhas_selecionadas = df1['Road_traffic_density'] != 'NaN '
    df1 = df1.loc[linhas_selecionadas, :].copy()

    ###Excluindo 'NaN ' da coluna 'Weatherconditions':
    linhas_selecionadas = df1['Weatherconditions'] != 'NaN '
    df1 = df1.loc[linhas_selecionadas, :].copy()

    ###Excluindo 'NaN ' da coluna 'Festival':
    linhas_selecionadas = df1['Festival'] != 'NaN '
    df1 = df1.loc[linhas_selecionadas, :].copy()

    ###Excluindo 'NaN ' da coluna 'Delivery_person_Age':
    linhas_selecionadas = df1['Delivery_person_Age'] != 'NaN '
    df1 = df1.loc[linhas_selecionadas, :].copy()

    #coluna multiple_deliveries - conversão de Object(str) para int
    df1['multiple_deliveries'] = df1['multiple_deliveries'].astype(int)

    #tirando os espaços das células nas colunas:
    df1.loc[:, 'ID'] =  df1.loc[:, 'ID'].str.strip()
    df1.loc[:, 'Road_traffic_density'] =  df1.loc[:, 'Road_traffic_density'].str.strip()
    df1.loc[:, 'Type_of_order'] =  df1.loc[:, 'Type_of_order'].str.strip()
    df1.loc[:, 'Type_of_vehicle'] =  df1.loc[:, 'Type_of_vehicle'].str.strip()
    df1.loc[:, 'City'] =  df1.loc[:, 'City'].str.strip()
    df1.loc[:, 'Festival'] =  df1.loc[:, 'Festival'].str.strip()

    #limpando a coluna time taken : tirando o (min)
    df1['Time_taken(min)'] = df1['Time_taken(min)'].apply(lambda x: x.split( '(min)')[1])

    #coluna 'Time_taken(min)' - conversão de Object(str) para int
    df1['Time_taken(min)'] = df1['Time_taken(min)'].astype(int)

    return df1


    
def top_delivers(df1, top_asc):
#7- Os 10 entregadores mais lentos por cidade    
    df2 = df1.loc[:, ['Time_taken(min)', 'Delivery_person_ID','City' ]].groupby(['City', 'Delivery_person_ID']).max().sort_values(['City', 'Time_taken(min)'], ascending = top_asc).reset_index()
    df_aux01 = df2.loc[df2['City'] == 'Metropolitian', :].head(10)
    df_aux02 = df2.loc[df2['City'] == 'Urban', :].head(10)
    df_aux03 = df2.loc[df2['City'] == 'Semi-Urban', :].head(10)
    df3 = pd.concat([df_aux01, df_aux02, df_aux03]).reset_index(drop = True)
    return df3


    







#### Fim da limpeza de dados ###

#======================================
#Tratamento do Dataframe
#======================================

#carregando o arquivo csv
arquivo = pd.read_csv(r'pages/train.csv')

#transformar o arquivo em um DataFrame
df = pd.DataFrame(arquivo)

# Limpando o arquivo 
df1 = clean_code(df)





#===========================
####Fim da limpeza de dados
#===========================


###================================
### Início - Menu lateral
###================================


#imagem - logo (menu lateral)
#image_path ='logo_cury_company.png'
image = Image.open('logo.png')
st.sidebar.image(image, width=120)

#Cabeçalhos (menu lateral)
st.sidebar.markdown('# Cury Company')
st.sidebar.markdown('## Fastest Delivery in Town')
st.sidebar.markdown("""---""")

#Barra de seleção por rolagem  (menu lateral)
data_slider = st.sidebar.slider('Selecione a data limite',
                  value=datetime(2022, 4, 13),
                  min_value=datetime(2022, 2, 11),
                  max_value=datetime(2022, 4, 6),
                  format='DD-MM-YYYY')
st.sidebar.markdown("""---""")

#Barra por seleção (menu lateral)
opcoes_trafego = st.sidebar.multiselect(
    'Selecione a condição de trânsito',
    ['Low','Medium','High','Jam'],
    default=['Low', 'Medium', 'High', 'Jam'])

#Rodapé (menu lateral)
st.sidebar.markdown("""---""")
st.sidebar.markdown('#### Powered by Fernanda Lima')

#Cabeçalho (página inicial) 
st.header('Marketplace - Visão Entregadores')

#lincando filtros de data do menu lateral com os gráficos
linhas_selecionadas = df1['Order_Date'] < data_slider
df1 = df1.loc[linhas_selecionadas, :]


#lincando filtros de transito do menu lateral com os gráficos
linhas_selecionadas = df1['Road_traffic_density'].isin(opcoes_trafego)
df1 = df1.loc[linhas_selecionadas, :]


###===============================
###   Fim - menu lateral 
###===============================

#=================================
#Layout no Streamlit
#================================= 

#=================================
###Pagina principal
#=================================

#Abas - Configuração (página inicial)
tab1, tab2, tab3 = st.tabs(['Visão Gerencial', '_', '_'])

#configurando as abas

with tab1:
    with st.container():
        st.title('Métricas Gerais')
        
        col1, col2, col3, col4 = st.columns(4, gap = 'large')
        with col1:
#1 A menor e a maior idade dos entregadores
            maior_idade = df1.loc[:, 'Delivery_person_Age'].max()
            col1.metric('Maior de idade', maior_idade)

        with col2:
#1 A menor e a maior idade dos entregadores
            menor_idade = df3 = df1.loc[:, 'Delivery_person_Age'].min()
            col2.metric('Menor de idade', menor_idade)

        with col3:
#2 A pior e a melhor condição de veículos
            melhor_condicao = df2 = df1.loc[:, 'Vehicle_condition'].max()
            col3.metric('Melhor condição', melhor_condicao)
            
        with col4:
#2 A pior e a melhor condição de veículos
            pior_condicao = df3 = df1.loc[:, 'Vehicle_condition'].min()
            col4.metric('Pior condição',pior_condicao)
            
#########Bloco 1 container            
            
    with st.container():
        st.markdown("""___""")
        st.markdown('# Avaliações')
        col1, col2 = st.columns(2)
        with col1:
#3 Avaliação média por entregador
            st.markdown('##### Avaliação média por entregador')
            avaliacoes_media_por_entragador = df1.loc[:, ['Delivery_person_Ratings', 'Delivery_person_ID']].groupby('Delivery_person_ID').count().reset_index()
            st.dataframe(avaliacoes_media_por_entragador)
            
            
        with col2:
#4 A avaliação média e o desvio padrão por tipo de tráfego
            st.markdown('##### Avaliação média por trânsito')
            avaliacao_med_desv_trafego = df1.loc[:, ['Delivery_person_Ratings', 'Road_traffic_density']].groupby('Road_traffic_density').agg({'Delivery_person_Ratings':['mean', 'std']})
            avaliacao_med_desv_trafego.columns = ['avaliacao_media', 'avaliacao_desvio_padrao']
            avaliacao_med_desv_trafego.reset_index()
            st.dataframe(avaliacao_med_desv_trafego)

#5 Avaliação média e o desvio padrão por condições climáticas            
            st.markdown('##### Avaliação média por clima')
            avaliacao_med_desv_climatica = df1.loc[:, ['Delivery_person_Ratings', 'Weatherconditions']].groupby('Weatherconditions').agg({'Delivery_person_Ratings':['mean', 'std']})
            avaliacao_med_desv_climatica.columns = ['avaliacao_media', 'avaliacao_desvio_padrao']
            avaliacao_med_desv_climatica.reset_index()
            st.dataframe(avaliacao_med_desv_climatica)
            
            
######Bloco 2 conteiner        
        
    with st.container():
        st.markdown("""___""")
        st.title('Velocidade de entrega')
        col1, col2 = st.columns(2)
        
        
        with col1:
#6- Os 10 entreagdores mais rápidos por cidade.            
            st.markdown(' ##### Top entregadores mais rápidos')
            df3 = top_delivers(df1, top_asc=True)
            st.dataframe(df3)

            
        with col2:
#7- Os 10 entregadores mais lentos por cidade
            st.markdown('##### Top entregadores mais lentos')
            df3 = top_delivers(df1, top_asc=False)
            st.dataframe(df3)
            


             
      
        
        
        
        
#importar o arquivo
import pandas as pd
import io
import plotly.express as px
from PIL import Image
import streamlit as st
from datetime import datetime
import numpy as np
from haversine import haversine
from streamlit_folium import folium_static
import plotly.graph_objects as go

#carregando o arquivo csv
arquivo = pd.read_csv(r'/Users/fernanda/Documents/repos/ftc/arquivos_baixados/train.csv')

#transformar o arquivo em um DataFrame
df = pd.DataFrame(arquivo)

#cópia do arquivo original
df1 = df.copy()

#####limpeza dos dados####

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


#===========================
####Fim da limpeza de dados
#===========================


###================================
### Início - Menu lateral
###================================
#imagem - logo (menu lateral)
from PIL import Image
image_path ='logo_cury_company.png'
image = Image.open(image_path)
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
st.header('Marketplace - Visão Restaurantes')

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

with tab1:
    with st.container():
        st.markdown('____')
        st.title('Métricas Gerais')
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
#1 - A quantidade de entregadores únicos.
            entregadores_unicos = len(df1.loc[:,'Delivery_person_ID'].unique())
            col1.metric('Entregadores únicos', entregadores_unicos)
        
        with col2:
#2 - A distância média dos restaurantes e dos locais de entrega.
            colunas = ['Restaurant_latitude', 'Restaurant_longitude', 'Delivery_location_latitude', 'Delivery_location_longitude']
            df1['distancia'] = df1.loc[:, colunas].apply(lambda x: haversine(  (x['Restaurant_latitude'], x[ 'Restaurant_longitude']), (x['Delivery_location_latitude'], x['Delivery_location_longitude'])), axis=1)
            media_distancia = np.round(df1['distancia'].mean(), 2)
            col2.metric('Distância média das entregas', media_distancia)
            
            
            
            
            
        with col3:
#6- O tempo médio de entrega durante os Festivais.
            df2 = df1.loc[:, ['Time_taken(min)', 'Festival']].groupby(['Festival']).agg( {'Time_taken(min)' : 'mean'} )
            df2.columns = ['media_entrega']
            df2 = df2.reset_index()
            df2 = np.round(df2.loc[df2['Festival'] == 'Yes', 'media_entrega'], 2)
            col3.metric('Tempo médio de entrega com Festival', df2)
            
            
            
        with col4:
#6- O desvio padrão de entrega durante os Festivais.
            df2 = df1.loc[:, ['Time_taken(min)', 'Festival']].groupby(['Festival']).agg( {'Time_taken(min)' : 'std'} )
            df2.columns = ['media_entrega']
            df2 = df2.reset_index()
            df2 = np.round(df2.loc[df2['Festival'] == 'Yes', 'media_entrega'], 2)
            col4.metric('Desvio padrão de entrega com Festival', df2)
            
            
        
        with col5:
#6- O tempo médio de entrega sem Festivais.
            df2 = df1.loc[:, ['Time_taken(min)', 'Festival']].groupby(['Festival']).agg( {'Time_taken(min)' : 'mean'} )
            df2.columns = ['media_entrega']
            df2 = df2.reset_index()
            df2 = np.round(df2.loc[df2['Festival'] == 'No', 'media_entrega'], 2)
            col5.metric('Tempo médio de entrega sem Festival', df2)           


 
        with col6:
#6- O desvio padrão de entrega sem Festivais.
            df2 = df1.loc[:, ['Time_taken(min)', 'Festival']].groupby(['Festival']).agg( {'Time_taken(min)' : 'std'} )
            df2.columns = ['media_entrega']
            df2 = df2.reset_index()
            df2 = np.round(df2.loc[df2['Festival'] == 'No', 'media_entrega'], 2)
            col6.metric('Desvio padrão de entrega sem Festival', df2)
            
        
            
    
    with st.container():
        st.markdown('____')
        st.title('Tempo médio de entrega por cidade')
        col1, col2 = st.columns(2)
        
        with col1:
#3- O tempo médio e o desvio padrão de entrega por cidade (em gráfico de colunas)
            df2 = df1.loc[:, ['Time_taken(min)', 'City']].groupby('City').agg( {'Time_taken(min)' : ['mean', 'std']} )
            df2.columns = ['media_entrega', 'desvio_padrao_entrega']
            df2 = df2.reset_index()
                #gráfico
            fig = go.Figure()
            fig.add_trace(go.Bar(name = 'Control', x=df2['City'], y= df2['media_entrega'], error_y=dict(type='data', array = df2['desvio_padrao_entrega'])))
            fig.update_layout(barmode= 'group')
            st.plotly_chart(fig)
            
        with col2:
#4- O tempo médio e o desvio padrão de entrega por cidade e por tipo de pedido.
            st.title('Distribuição da distância')
            df2 = df1.loc[:, ['Time_taken(min)', 'City', 'Type_of_order']].groupby(['City', 'Type_of_order']).agg( {'Time_taken(min)' : ['mean', 'std']} )
            df2.columns = ['media_entrega', 'desvio_padrao_entrega']
            df2 = df2.reset_index()
            st.dataframe(df2)


    
    
    
    with st.container():
        st.markdown('____')
        st.title('Distribuição do tempo')
        col1, col2 = st.columns(2)
        
        with col1:
#2 - A distância média dos restaurantes e dos locais de entrega (em gráfico pizza)
            colunas = ['Restaurant_latitude', 'Restaurant_longitude', 'Delivery_location_latitude', 'Delivery_location_longitude']
            df1['distancia'] = df1.loc[:, colunas].apply(lambda x: haversine(  (x['Restaurant_latitude'], x[ 'Restaurant_longitude']), (x['Delivery_location_latitude'], x['Delivery_location_longitude'])), axis=1)
            media_distancia = df1.loc[:, ['City', 'distancia']].groupby('City').mean().reset_index()
            #gráfico
            fig = go.Figure(data=[ go.Pie (labels = media_distancia['City'],values= media_distancia['distancia'], pull=[0, 0.1, 0])])
            st.plotly_chart(fig)
            

        with col2:
#5- O tempo médio e o desvio padrão de entrega por cidade e tipo de tráfego( em gráfico de pizza)
            df2 = df1.loc[:, ['Time_taken(min)', 'City', 'Road_traffic_density']].groupby(['City', 'Road_traffic_density']).agg( {'Time_taken(min)' : ['mean', 'std']} )
            df2.columns = ['media_entrega', 'desvio_padrao_entrega']
            df2 = df2.reset_index()
            #gráfico 
            fig = px.sunburst(df2, path = ['City', 'Road_traffic_density' ], values= 'media_entrega', color = 'desvio_padrao_entrega', color_continuous_scale= 'RdBu', color_continuous_midpoint=np.average(df2['desvio_padrao_entrega']))
            st.plotly_chart(fig)

         

    
        


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

st.set_page_config(page_title='Visão Empresa', page_icon='📊', layout='wide')






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

#### Fim da limpeza de dados ###





def order_metric(df1):
#1- quantidade de pedidos por dia
    colunas = ['ID', 'Order_Date']
    df2 = df1.loc[:, colunas].groupby(['Order_Date']).count().reset_index()
    ######Criação do gráfico######
    fig = px.bar(df2, x= 'Order_Date', y= 'ID') 
    return fig


def traffic_order_share(df1):    
#3 Distribuição dos pedidos por tipo de tráfego.(em %)
    colunas = ['ID', 'Road_traffic_density']
    df2 = df1.loc[:, colunas].groupby(['Road_traffic_density']).count().reset_index()
    df2['entregas_perc'] = df2['ID'] / df2['ID'].sum()
    ######Criação do gráfico######
    fig = px.pie(df2, values = 'entregas_perc', names= 'Road_traffic_density')       
    return fig 


def traffic_order_city(df1):
#4 Comparação do volume de pedidos por cidade e tipo de tráfego 
    colunas = ['ID', 'City', 'Road_traffic_density']
    df2 = df1.loc[:,colunas].groupby(['City', 'Road_traffic_density']).count().reset_index()     ######Criação do gráfico######
    fig = px.scatter(df2, x='City', y='Road_traffic_density', size= 'ID', color= 'City')
    return fig 


def order_by_week(df1):
#2 Quantidade de pedidos por semana.        
    df1['week_of_year'] = df1['Order_Date'].dt.strftime('%U')
    df01 = df1.loc[:, ['ID', 'week_of_year']].groupby('week_of_year').count().reset_index()
    df02 = df1.loc[:, ['Delivery_person_ID', 'week_of_year']].groupby('week_of_year').nunique().reset_index()
    df03 = pd.merge(df01, df02, how= 'inner')
    df03['Oder_by_deliver'] = df03['ID'] / df03['Delivery_person_ID']
    ######Criação do gráfico######
    fig = px.line(df03, x='week_of_year', y='Oder_by_deliver')
    return fig 


def order_share_by_week(df1):       
#5 Quantidade de pedido por entregador e por semana.
    df01 = df1.loc[:, ['ID', 'week_of_year']].groupby('week_of_year').count().reset_index()
    df02 = df1.loc[:, ['Delivery_person_ID', 'week_of_year']].groupby('week_of_year').nunique().reset_index()
    df03 = pd.merge(df01, df02, how= 'inner')
    df03['Oder_by_deliver'] = df03['ID'] / df03['Delivery_person_ID']
    ######Criação do gráfico###### 
    fig = px.line(df03, x='week_of_year', y='Oder_by_deliver')
    return fig 
        

def country_maps(df1):
#6 A localização central de cada cidade por tipo de tráfego.
    df2 = df1.loc[:, ['Delivery_location_latitude', 'Delivery_location_longitude', 'City', 'Road_traffic_density']].groupby(['City', 'Road_traffic_density']).median().reset_index()
    #criando o gráfico de mapa
    map = folium.Map()
    for index, location_info in df2.iterrows():
        folium.Marker([location_info['Delivery_location_latitude'],
                      location_info['Delivery_location_longitude']],
                      popup=location_info[['City', 'Road_traffic_density']]).add_to(map)
    folium_static(map, width=1024, height=600)


    
    
    
    

#======================================
#Tratamento do Dataframe
#======================================

#carregando o arquivo csv
arquivo = pd.read_csv(r'pages/train.csv')

#transformar o arquivo em um DataFrame
df = pd.DataFrame(arquivo)

# Limpando o arquivo 
df1 = clean_code(df)





#=================================
#Layout no Streamlit
#=================================

###================================
### Menu lateral
###================================

#imagem - logo (menu lateral)
from PIL import Image
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
st.header('Visão Empresa')

#lincando filtros de data do menu lateral com os gráficos
linhas_selecionadas = df1['Order_Date'] < data_slider
df1 = df1.loc[linhas_selecionadas, :]


#lincando filtros de transito do menu lateral com os gráficos
linhas_selecionadas = df1['Road_traffic_density'].isin(opcoes_trafego)
df1 = df1.loc[linhas_selecionadas, :]


###================================
### Página Principal Visão Empresa
###================================



#Abas - Configuração (página inicial)
tab1, tab2, tab3 = st.tabs(['Visão Gerencial', 'Visão Tática', 'Visão Geográfica'])

#Aba - Visão Gerencial (tab1)
with tab1:
    with st.container():
        st.markdown('# Distribuição dos pedidos por tipo de tráfego') #título
        fig = order_metric(df1)  #função que chama a figura
        st.plotly_chart(fig, use_contanier_width=True) #plota o gráfico        
               
        
    with st.container():
        coluna1, coluna2 = st.columns(2)
        
        with coluna1:
            st.markdown('# Distribuição dos pedidos por tipo de tráfego')
            fig = traffic_order_share(df1)
            st.plotly_chart(fig, use_contanier_width=True)
             
        with coluna2:
            st.markdown('# Distribuição dos pedidos por cidade')
            fig = traffic_order_city(df1)
            st.plotly_chart(fig, use_contanier_width=True)
            
                

#Aba - Visão Tática(tab2)
with tab2:
    with st.container():
        st.markdown('# Pedidos por semana')
        fig = order_by_week(df1)
        st.plotly_chart(fig, use_contanier_width=True)
        
    with st.container():
        st.markdown('# Pedidos por entregador e por semana')
        fig = order_share_by_week(df1)
        st.plotly_chart(fig, use_contanier_width=True)
        

         
#Aba - Visão Geográfica (tab3)
with tab3:
    st.markdown('# Localização central de cada cidade por tipo de tráfego')
    fig = country_maps(df1)
    
    

         
   
    



















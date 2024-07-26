import pandas as pd 
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import folium
from streamlit_folium import st_folium
from PIL import Image
import webbrowser


df=pd.read_csv(r"C:\Users\USER\Desktop\airbnb_new\Airbnb_new.csv")


st.set_page_config(layout="wide")
st.title("AIRBNB DATA ANALYSIS ")
with st.sidebar:
    select=option_menu("select the options",["HOME","DATA EXPLORATION"])
if select=="HOME":
    
    st.image(r"C:\Users\USER\Desktop\airbnb_new\image-airbnb.jpg")
    st.header("About Airbnb")
    st.write("")
    st.write('''***Airbnb is an online marketplace that connects people who want to rent out
              their property with people who are looking for accommodations,
              typically for short stays. Airbnb offers hosts a relatively easy way to
              earn some income from their property.Guests often find that Airbnb rentals
              are cheaper and homier than hotels.***''')
    st.write("")
    st.write('''***Airbnb Inc (Airbnb) operates an online platform for hospitality services.
                  The company provides a mobile application (app) that enables users to list,
                  discover, and book unique accommodations across the world.
                  The app allows hosts to list their properties for lease,
                  and enables guests to rent or lease on a short-term basis,
                  which includes vacation rentals, apartment rentals, homestays, castles,
                  tree houses and hotel rooms. The company has presence in China, India, Japan,
                  Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy,
                  Norway, Portugal, Russia, Spain, Sweden, the UK, and others.
                  Airbnb is headquartered in San Francisco, California, the US.***''')
    
    st.header("Background of Airbnb")
    st.write("")
    st.write('''***Airbnb was born in 2007 when two Hosts welcomed three guests to their
              San Francisco home, and has since grown to over 4 million Hosts who have
                welcomed over 1.5 billion guest arrivals in almost every country across the globe.***''')
    
    tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8=st.tabs(["Popular","Arts and Culture","Outdoors","Mountains","Beach","Unique stays","Categories","Things to do"])
    with tab1:

        col1,col2,col3,col4=st.columns(4)

        with col1:
            col11,col21=st.columns(2)
            with col11:
                if st.button("Canmore"):         
                    webbrowser.open("https://www.airbnb.co.in/canmore-canada/stays/pet-friendly")               
            with col21:
                if st.button("Jasper"):
                    webbrowser.open("https://www.airbnb.co.in/benalmadena-spain/stays")
        with col2:  
            col12,col22=st.columns(2)          
            with col12:            
                if st.button("Marbella"):
                    webbrowser.open("https://www.airbnb.co.in/marbella-spain/stays/houses")       
            with col22:
                if st.button("Mijas"):
                    webbrowser.open("https://www.airbnb.co.in/mijas-spain/stays")

        
        
    with tab2:

        col1,col2,col3,col4=st.columns(4)

        with col1:
            col11,col21=st.columns(2)
            with col11:
                if st.button("Phoenix"):         
                    webbrowser.open("https://www.airbnb.co.in/phoenix-az/stays/villas")               
            with col21:
                if st.button("York"):
                    webbrowser.open("https://www.airbnb.co.in/york-united-kingdom/stays")
        with col2:  
            col12,col22=st.columns(2)          
            with col12:            
                if st.button("London"):
                    webbrowser.open("https://www.airbnb.co.in/london-united-kingdom/stays/apartments")       
            with col22:
                if st.button("Paris"):
                    webbrowser.open("https://www.airbnb.co.in/paris-france/stays/pools")

    with tab3:

        col1,col2,col3,col4=st.columns(4)

        with col1:
            col11,col21=st.columns(2)
            with col11:
                if st.button("Banff"):         
                    webbrowser.open("https://www.airbnb.co.in/banff-canada/stays/condos")               
            with col21:
                if st.button("Nerja"):
                    webbrowser.open("https://www.airbnb.co.in/nerja-spain/stays/apartments")
        with col2:  
            col12,col22=st.columns(2)          
            with col12:            
                if st.button("Greer"):
                    webbrowser.open("https://www.airbnb.co.in/greer-az/stays")       
            with col22:
                if st.button("Victoria"):
                    webbrowser.open("https://www.airbnb.co.in/victoria-canada/stays/apartments")                
    
    
    
if select=="DATA EXPLORATION":
    tab1,tab2,tab3,tab4 =st.tabs(["PRICE ANALYSIS","AVAILABLITY ANALYSIS","LOCATION BASED ANALYSIS","GEOSPATIAL ANALYSIS"])
    with tab1:
        st.title("price analysis")
        df1=pd.DataFrame(df.groupby("country")["price"].mean().round())
        df1.reset_index(inplace=True)
        df2=pd.DataFrame(df.groupby(["country","room_type"])["price"].mean().round())
        df2.reset_index(inplace=True)
        
        option=st.radio("select the options",["AVERAGE PRICE FOR EACH COUNTRY ","AVERAGE PRICE FOR EACH COUNTRY ACCORDING TO THE ROOM TYPE"])
            
        if option=="AVERAGE PRICE FOR EACH COUNTRY ":
            fig_df1=px.bar(df1,x="country",y="price",title="AVERAGE PRICE FOR EACH COUNTRY ",color_discrete_sequence=px.colors.sequential.Agsunset,hover_name="price")
            st.plotly_chart(fig_df1)
        if option=="AVERAGE PRICE FOR EACH COUNTRY ACCORDING TO THE ROOM TYPE":   
            fig_df2=px.bar(df2,x="country",y="price",title="AVERAGE PRICE FOR EACH COUNTRY ACCORDING TO THE PROPERTY TYPE",color="room_type",color_discrete_sequence=px.colors.sequential.Agsunset,hover_name="price")
            st.plotly_chart(fig_df2)

        col1,col2=st.columns(2)    
        with col1:
            select_c=st.selectbox("SELECT THE COUNTRY",df["country"].unique())
            df3=df[df["country"]==select_c]
            df3.reset_index(drop=True,inplace=True)           
            select=st.selectbox("SELECT THE ROOM TYPE",df["room_type"].unique())
            df4=df3[df3["room_type"]==select]         
            df4.reset_index(drop=True,inplace=True)
            df_bar=pd.DataFrame(df4.groupby("property_type")[["price","review_scores","number_of_reviews"]].mean().round()) 
            df_bar.reset_index(inplace=True) 
            fig=px.bar(df_bar,x="property_type",y="price",title="AVERAGE PRICE FOR PROPERTY TYPES",
                        hover_data=["review_scores","number_of_reviews"],
                        color_discrete_sequence=px.colors.sequential.Aggrnyl)
            st.plotly_chart(fig) 

        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            select=st.selectbox("SELECT THE PROPERTY TYPE",df4["property_type"].unique())  
            df5=df4[df4["property_type"]==select]  
            df5.reset_index(drop=True,inplace=True)            
            df_pie= pd.DataFrame(df5.groupby("host_response_time")[["price","bedrooms"]].mean().round())
            df_pie.reset_index(inplace= True)
            fig_pi= px.pie(df_pie, values="price", names= "host_response_time",
                            hover_data=["bedrooms"],
                            color_discrete_sequence=px.colors.sequential.BuPu_r,
                            title="AVERAGE PRICE DIFFERENCE BASED ON HOST RESPONSE TIME",
                            )
            st.plotly_chart(fig_pi)


        col1,col2=st.columns(2)
        with col1:
            select=st.selectbox("SELECT THE HOST RESPONSE TIME",df3["host_response_time"].unique())
            df6=df5[df5["host_response_time"]==select] 
            df6.reset_index(drop=True,inplace=True)  

            df_bar = pd.DataFrame(df6.groupby("bed_type")[["minimum_nights", "maximum_nights", "price"]].mean().round())

            df_bar.reset_index(inplace= True)

            fig_bar = px.bar(df_bar, x='bed_type', y=['minimum_nights', 'maximum_nights'], 
            title='AVERAGE PRICE FOR MINIMUM NIGHTS AND MAXIMUM NIGHTS',hover_data=["price"],
            barmode='group',color_discrete_sequence=px.colors.sequential.Aggrnyl, width=600, height=500)
            st.plotly_chart(fig_bar)
        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            df_bar=pd.DataFrame(df4.groupby("bed_type")[["bedrooms","beds","accommodates","price"]].mean().round())
            df_bar.reset_index(inplace= True)

            fig_bar = px.bar(df_bar, x='bed_type', y=["bedrooms","beds","accommodates"], 
            title='AVERAGE PRICE FOR BEDROOMS,BEDS AND ACCOMMODATES',hover_data=["price"],
            barmode='group',color_discrete_sequence=px.colors.sequential.Aggrnyl, width=600, height=500)
            st.plotly_chart(fig_bar)
                

    with tab2:
        st.title("availablity analysis")
        df=pd.read_csv(r"C:\Users\USER\Desktop\airbnb_new\Airbnb_new.csv")
        select_a=st.selectbox("SELECT THE COUNTRY ",df["country"].unique())
        df1=df[df["country"]==select_c]
        df1.reset_index(drop=True,inplace=True)           
        select=st.selectbox("SELECT THE PROPERTY TYPE ",df["property_type"].unique())
        df2=df1[df1["property_type"]==select]         
        df2.reset_index(drop=True,inplace=True)
        df3=pd.DataFrame(df2.groupby(["room_type","bed_type","is_location_exact"])["availability_30"].mean().round())
        df3.reset_index(inplace=True)
        #st.dataframe(df3)
        df_a_sunb_30= px.sunburst(df3, path=["room_type","bed_type","is_location_exact"], values="availability_30",width=900,height=600,title=st.write("AVERAGE AVAILABLITY (AVAILABLITY_30) BY ROOM TYPE, BED TYPE, AND LOCATION  PRECISION (exact or not)"),color_discrete_sequence=px.colors.sequential.Peach_r,color="room_type",color_discrete_map={'Private room':' #008080', 'Entire home/apt':'#c0c0c0', 'Shared room':'#33FF99'})
        button=st.button("!")
        if button:
            st.write("***This sunburst chart visualizes the average availability how many days out of the next 30 a listing is available for different room types (private, entire home/apt, shared), bed types, and location precision (exact or not). It allows you to explore availability trends within a specific country and property type selected from the dropdowns above.***")
        st.plotly_chart(df_a_sunb_30)
        
        df4=pd.DataFrame(df2.groupby(["room_type","bed_type","is_location_exact"])["availability_60"].mean().round())
        df4.reset_index(inplace=True)
        #st.dataframe(df4)
        df_a_sunb_60= px.sunburst(df4, path=["room_type","bed_type","is_location_exact"], values="availability_60",width=900,height=600,title=st.write("AVERAGE AVAILABLITY (AVAILABLITY_60) BY ROOM TYPE, BED TYPE, AND LOCATION  PRECISION (exact or not)"),color_discrete_sequence=px.colors.sequential.Peach_r,color="room_type",color_discrete_map={'Private room':' #008080', 'Entire home/apt':'#c0c0c0', 'Shared room':'#33FF99'})
        button=st.button("  !")
        if button:
            st.write("***This sunburst chart visualizes the average availability how many days out of the next 60 a listing is available for different room types (private, entire home/apt, shared), bed types, and location precision (exact or not). It allows you to explore availability trends within a specific country and property type selected from the dropdowns above.***")
        st.plotly_chart(df_a_sunb_60)

        df5=pd.DataFrame(df2.groupby(["room_type","bed_type","is_location_exact"])["availability_90"].mean().round())
        df5.reset_index(inplace=True)
        #st.dataframe(df5)
        df_a_sunb_90= px.sunburst(df5, path=["room_type","bed_type","is_location_exact"], values="availability_90",width=900,height=600,title=st.write("AVERAGE AVAILABLITY (AVAILABLITY_90) BY ROOM TYPE, BED TYPE, AND LOCATION  PRECISION (exact or not)"),color_discrete_sequence=px.colors.sequential.Peach_r,color="room_type",color_discrete_map={'Private room':' #008080', 'Entire home/apt':'#c0c0c0', 'Shared room':'#33FF99'})
        button=st.button("! ")
        if button:
            st.write("***This sunburst chart visualizes the average availability how many days out of the next 90 a listing is available for different room types (private, entire home/apt, shared), bed types, and location precision (exact or not). It allows you to explore availability trends within a specific country and property type selected from the dropdowns above.***")
        st.plotly_chart(df_a_sunb_90)
               
        df6=pd.DataFrame(df2.groupby(["room_type","bed_type","is_location_exact"])["availability_365"].mean().round())
        df6.reset_index(inplace=True)
        #st.dataframe(df6)
        df_a_sunb_365= px.sunburst(df6, path=["room_type","bed_type","is_location_exact"], values="availability_365",width=900,height=600,title=st.write("AVERAGE AVAILABLITY (AVAILABLITY_365) BY ROOM TYPE, BED TYPE, AND LOCATION  PRECISION (exact or not)"),color_discrete_sequence=px.colors.sequential.Peach_r,color="room_type",color_discrete_map={'Private room':' #008080', 'Entire home/apt':'#c0c0c0', 'Shared room':'#33FF99'})
        button=st.button(" ! ")
        if button:
            st.write("***This sunburst chart visualizes the average availability how many days out of the next 365 a listing is available for different room types (private, entire home/apt, shared), bed types, and location precision (exact or not). It allows you to explore availability trends within a specific country and property type selected from the dropdowns above.***")
        st.plotly_chart(df_a_sunb_365)

        roomtype_a= st.selectbox("SELECT THE ROOM TYPE.", df2["room_type"].unique())
        df7= df2[df2["room_type"] == roomtype_a]
        df_mul_bar_a= pd.DataFrame(df7.groupby("host_response_time")[["availability_30","availability_60","availability_90","availability_365","price"]].mean().round())
        df_mul_bar_a.reset_index(inplace= True)
        fig_df_mul_bar_a = px.bar(df_mul_bar_a, x='host_response_time', y=['availability_30', 'availability_60', 'availability_90', "availability_365"], 
        title='AVERAGE AVAILABILITY BASED ON HOST RESPONSE TIME',hover_data="price",
        barmode='group',color_discrete_sequence=px.colors.sequential.Blugrn_r,width=1000)
        st.plotly_chart(fig_df_mul_bar_a)

    with tab3:
        st.title("location based analysis")
        df=pd.read_csv(r"C:\Users\USER\Desktop\airbnb_new\Airbnb_new.csv")
        select_a=st.selectbox("SELECT THE COUNTRY NAME. ",df["country"].unique())
        df1=df[df["country"]==select_a]
        df1.reset_index(drop=True,inplace=True)           
        select=st.selectbox("SELECT THE PROPERTY TYPE.",df1["property_type"].unique())
        df2=df1[df1["property_type"]==select]         
        df2.reset_index(drop=True,inplace=True)
        #st.dataframe(df2["suburb"].unique())
        df6=pd.DataFrame(df2.groupby(["room_type","suburb"])[["price","review_scores"]].mean().round())
        df6.reset_index(inplace=True)
        #st.dataframe(df6)
        fig_df_loc_bar_a = px.bar(df6, x='suburb',y= "price", 
        title="LOCATION-BASED ANALYSIS FOR ROOM TYPE,PRICE AND REVIEW SCORE",hover_data=["room_type","review_scores"],
        barmode='group',width=1000,color="room_type",color_discrete_sequence=px.colors.sequential.Agsunset)
        st.plotly_chart(fig_df_loc_bar_a)



        select_sub=st.selectbox("select the suburb",df1["suburb"].unique())
        df7=df1[df1["suburb"]==select_sub]
        df7.reset_index(drop=True,inplace=True)
        #st.dataframe(df7)
        df_7=pd.DataFrame(df7.groupby(["street","government_area","market"])["price"].mean())
        #st.dataframe(df_7)
        df_7.reset_index(inplace=True)
        fig_s = px.bar(df_7, x='street',y= "price", 
        title="LOCATION BASED ANALYSIS OF STREET,GOVERNMENT-AREA,MARKET AND AVERAGE PRICE",hover_data=["government_area","market"],
        barmode='group',width=1000,color="government_area",color_discrete_sequence=px.colors.sequential.Agsunset)
        st.plotly_chart(fig_s)

        df8 =pd.DataFrame( df7.groupby(["host_location","host_neighbourhood","host_name","is_location_exact","host_is_superhost"])["price"].mean())
        df8.reset_index(inplace=True)
        #st.dataframe(df8)

        fig_h = px.bar(df8, x='host_neighbourhood',y= "price", 
        title="AVERAGE PRICE BY NEIGHBOURHOOD,HOST-LOCATION,AND LOCATION PRECISION",hover_data=["is_location_exact","host_location","host_name"],
        barmode='group',width=1000,color="host_is_superhost",color_discrete_sequence=px.colors.sequential.Agsunset)      
        st.plotly_chart(fig_h)


    with tab4:


        df=pd.read_csv(r"C:\Users\USER\Desktop\airbnb_new\Airbnb_new.csv")
        select_a=st.selectbox("SELECT THE COUNTRY NAME . ",df["country"].unique())
        df1=df[df["country"]==select_a]
        df1.reset_index(drop=True,inplace=True)           
        select=st.selectbox("SELECT THE PROPERTY TYPE .",df1["property_type"].unique())
        df2=df1[df1["property_type"]==select]         
        df2.reset_index(drop=True,inplace=True)
        #st.dataframe(df2)
       

        st.title("Geospatial visualization")
        map_select=st.radio("SELECT THE MAP ",["BASED ON LISTINGS","BASED ON HOST"])

        tile_types = ["OpenStreetMap", "CartoDB Positron", "CartoDB Voyager","OpenStreetMap.CH","OpenTopoMap","Stadia.AlidadeSatellite","Stadia.StamenTerrain"]
        selected_tile_type = st.selectbox("SELECT THE TILE TYPE", tile_types)

        if map_select=="BASED ON LISTINGS":
            st.subheader("based on listings details")
            m = folium.Map(location=[df2["latitude"].mean(), df2["longitude"].mean()], zoom_start=13,tiles=f"{selected_tile_type}")

            for idx, row in df2.iterrows():
                image_html = f"""
                                <div>
                                    <img src="{row['images']}" alt="Image" width="250">
                                    <br>
                                    <span>"{row['name']}"</span>
                                </div>
                                """
                folium.Marker(
                    [row["latitude"], row["longitude"]],
                    tooltip=f"Price: ${row['price']} \nRating: {row['review_scores']}",popup=image_html
                ).add_to(m)

            st_folium(m, width=900, height=700)    

        if map_select=="BASED ON HOST":

            st.subheader("based on host details")
            m_1 = folium.Map(location=[df2["latitude"].mean(), df2["longitude"].mean()], zoom_start=13,tiles=f"{selected_tile_type}")

            for idx, row in df2.iterrows():
                image_html_host = f"""
                                <div>
                                    <img src="{row['host_picture_url']}" alt="Image" width="250">
                                    <br>
                                    <span>"'response rate:'{row['host_response_rate']}',super host:'{row['host_is_superhost']}"</span>
                                </div>
                                """
                folium.Marker(
                    [row["latitude"], row["longitude"]],
                    tooltip=f"name: ${row['host_name']} \n,location: {row['host_location']}",popup=image_html_host,Icon='flag'
                ).add_to(m_1)

            st_folium(m_1, width=900, height=700)

        

      


        

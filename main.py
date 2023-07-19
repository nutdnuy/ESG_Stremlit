import streamlit as st
import pandas as pd   
import numpy as np
import requests


st.title(' ESG & Portfolio Emission :national_park:')

st.write(":monkey_face: ปัจจัยด้านสิ่งแวดล้อม สังคม และธรรมาภิบาล (ESG) และการปล่อยมลพิษจากพอร์ตโฟลิโอมีความสำคัญในการตัดสินใจลงทุน เนื่องจากเป็นปัจจัยชี้วัดความยั่งยืนของบริษัท ผลกระทบทางสังคม และการเปลี่ยนแปลงสภาพภูมิอากาศ ช่วยลดความเสี่ยงที่เกี่ยวข้องกับความเสียหายต่อสิ่งแวดล้อม ความไม่สงบในสังคม หรือธรรมาภิบาลที่ไม่ดี ยิ่งไปกว่านั้น บริษัทที่ให้ความสำคัญกับปัจจัยเหล่านี้มักแสดงให้เห็นถึงประสิทธิภาพในระยะยาวที่ดีกว่าเนื่องจากรูปแบบธุรกิจที่ยั่งยืน การปฏิบัติตามกฎระเบียบก็มีความสำคัญเช่นกัน เนื่องจากหน่วยงานบังคับใช้การรายงาน ESG และการลดการปล่อยมลพิษมากขึ้น นอกจากนี้ มาตรการเหล่านี้ยังตอบสนองความต้องการที่เพิ่มขึ้นในหมู่นักลงทุนสำหรับการลงทุนที่รับผิดชอบต่อสังคมและการมีส่วนร่วมในความพยายามลดการเปลี่ยนแปลงสภาพภูมิอากาศ ดังนั้น ESG และการพอร์ตโฟลิโอ Emission จึงมีความสำคัญต่อประสิทธิภาพทางการเงิน ความพร้อมด้านกฎระเบียบ ความรับผิดชอบต่อสังคม และการต่อสู้กับการเปลี่ยนแปลงสภาพภูมิอากาศ :monkey_face:")



Investment_Amount = st.number_input('Investment Amount')



st.subheader('Asset Allocation ')


col1, col2, col3 = st.columns(3)


with col2:
    st.subheader('')
    


df = pd.read_csv('ESG_Score.csv')

df['dummy_W'] = np.where(df['ESG Combined Score']  > 0, 1, 0)

df_emission = pd.read_csv("Mar_Emission.csv")

df_emission["Scope_1"] = df_emission["CO2 Equivalent Emissions Direct, Scope 1"] / df_emission["Company Market Cap"]
df_emission["Scope_2"] = df_emission["CO2 Equivalent Emissions Indirect, Scope 2"] / df_emission["Company Market Cap"]


list_AssetClass =  [""] + df["ธรแาพ"].tolist()


with col1:
    Asset_1 = st.selectbox('Stock 1:',(list_AssetClass ))
    Asset_2 = st.selectbox('Stock 2:',(list_AssetClass ))
    Asset_3 = st.selectbox('Stock 3:',(list_AssetClass ))
    Asset_4 = st.selectbox('Stock 4:',(list_AssetClass ))
    Asset_5 = st.selectbox('Stock 5:',(list_AssetClass ))  
 
    
        
with col3:
    Aweight_1 = st.number_input('weight 1', min_value=0, max_value=100)
    Aweight_2 = st.number_input('weight 2', min_value=0, max_value=100)
    Aweight_3 = st.number_input('weight 3', min_value=0, max_value=100)
    Aweight_4 = st.number_input('weight 4', min_value=0, max_value=100)
    Aweight_5 = st.number_input('weight 5', min_value=0, max_value=100)



# ปุ่ม run

show_btn = st.button("Simulation!")





if show_btn:
    #df[df['Company Common Name'] == Asset_1 ]["ESG Combined Score"].tolist()[0] * Aweight_1  /100


    ESG_Score = 0
    ESG_Score_E = 0 
    ESG_Score_S = 0 
    ESG_Score_G = 0 
    ESG_W = 0
    
    Scop1_CO2 = 0
    Scop2_CO2 = 0




    if Asset_1 in df["ธรแาพ"].tolist() :
        if df[df["ธรแาพ"] == Asset_1 ]["ESG Combined Score"].tolist()[0] * Aweight_1  /100  > 0:
            ESG_Score += df[df["ธรแาพ"] == Asset_1 ]["ESG Combined Score"].tolist()[0] * Aweight_1  
            ESG_Score_E += df[df["ธรแาพ"] == Asset_1 ]["Environmental Pillar Score"].tolist()[0] * Aweight_1  
            ESG_Score_S += df[df["ธรแาพ"] == Asset_1 ]["Social Pillar Score"].tolist()[0] * Aweight_1 
            ESG_Score_G += df[df["ธรแาพ"] == Asset_1 ]["Governance Pillar Score"].tolist()[0] * Aweight_1 
            ESG_W += Aweight_1 
            
            Scop1_CO2 += df_emission[df_emission["Instrument"] == Asset_1]["Scope_1"].tolist()[0] * Aweight_1 /100
            Scop2_CO2 += df_emission[df_emission["Instrument"] == Asset_1]["Scope_2"].tolist()[0] * Aweight_1 /100




    if Asset_2 in df["ธรแาพ"].tolist() :
        if df[df["ธรแาพ"] == Asset_2 ]["ESG Combined Score"].tolist()[0] * Aweight_2  /100  > 0:
            ESG_Score += df[df["ธรแาพ"] == Asset_2 ]["ESG Combined Score"].tolist()[0] * Aweight_2 
            ESG_Score_E += df[df["ธรแาพ"] == Asset_2 ]["Environmental Pillar Score"].tolist()[0] * Aweight_2
            ESG_Score_S += df[df["ธรแาพ"] == Asset_2 ]["Social Pillar Score"].tolist()[0] * Aweight_2 
            ESG_Score_G += df[df["ธรแาพ"] == Asset_2 ]["Governance Pillar Score"].tolist()[0] * Aweight_2 
            ESG_W += Aweight_2
            
            Scop1_CO2 += df_emission[df_emission["Instrument"] == Asset_2]["Scope_1"].tolist()[0] * Aweight_2 /100
            Scop2_CO2 += df_emission[df_emission["Instrument"] == Asset_2]["Scope_2"].tolist()[0] * Aweight_1 /100



    if Asset_3 in df["ธรแาพ"].tolist() :
        if df[df["ธรแาพ"] == Asset_3 ]["ESG Combined Score"].tolist()[0] * Aweight_3  /100  > 0:
            ESG_Score += df[df["ธรแาพ"] == Asset_3 ]["ESG Combined Score"].tolist()[0] * Aweight_3  
            ESG_Score_E += df[df["ธรแาพ"] == Asset_3 ]["Environmental Pillar Score"].tolist()[0] * Aweight_3
            ESG_Score_S += df[df["ธรแาพ"] == Asset_3 ]["Social Pillar Score"].tolist()[0] * Aweight_3
            ESG_Score_G += df[df["ธรแาพ"] == Asset_3 ]["Governance Pillar Score"].tolist()[0] * Aweight_3
            ESG_W += Aweight_3
            Scop1_CO2 += df_emission[df_emission["Instrument"] == Asset_3]["Scope_1"].tolist()[0] * Aweight_3 /100
            Scop2_CO2 += df_emission[df_emission["Instrument"] == Asset_3]["Scope_2"].tolist()[0] * Aweight_1 /100





    if Asset_4 in df["ธรแาพ"].tolist() :
        if df[df["ธรแาพ"] == Asset_4 ]["ESG Combined Score"].tolist()[0] * Aweight_4  /100  > 0:
            ESG_Score += df[df["ธรแาพ"] == Asset_4 ]["ESG Combined Score"].tolist()[0] * Aweight_4  
            ESG_Score_E += df[df["ธรแาพ"] == Asset_4 ]["Environmental Pillar Score"].tolist()[0] * Aweight_4
            ESG_Score_S += df[df["ธรแาพ"] == Asset_4 ]["Social Pillar Score"].tolist()[0] * Aweight_4 
            ESG_Score_G += df[df["ธรแาพ"] == Asset_4 ]["Governance Pillar Score"].tolist()[0] * Aweight_4
            ESG_W += Aweight_4
            Scop1_CO2 += df_emission[df_emission["Instrument"] == Asset_4]["Scope_1"].tolist()[0] * Aweight_4 /100
            Scop2_CO2 += df_emission[df_emission["Instrument"] == Asset_4]["Scope_2"].tolist()[0] * Aweight_1 /100




    if Asset_5 in df["ธรแาพ"].tolist() :
        if df[df["ธรแาพ"] == Asset_5 ]["ESG Combined Score"].tolist()[0] * Aweight_5  /100  > 0:
            ESG_Score += df[df["ธรแาพ"] == Asset_5 ]["ESG Combined Score"].tolist()[0] * Aweight_5  
            ESG_Score_E += df[df["ธรแาพ"] == Asset_5 ]["Environmental Pillar Score"].tolist()[0] * Aweight_5
            ESG_Score_S += df[df["ธรแาพ"] == Asset_5 ]["Social Pillar Score"].tolist()[0] * Aweight_5
            ESG_Score_G += df[df["ธรแาพ"] == Asset_5 ]["Governance Pillar Score"].tolist()[0] * Aweight_5
            ESG_W += Aweight_5
            
            Scop1_CO2 += df_emission[df_emission["Instrument"] == Asset_5]["Scope_1"].tolist()[0] * Aweight_5 /100
            Scop2_CO2 += df_emission[df_emission["Instrument"] == Asset_5]["Scope_2"].tolist()[0] * Aweight_1 /100
        
        
    ESGScore_Port = ESG_Score / ESG_W 
    
    Scop1_CO2_all = Scop1_CO2 * Investment_Amount
    Scop2_CO2_all = Scop2_CO2 * Investment_Amount
    
    
    
    tab1, tab2 = st.tabs(["Portfolio ESG Score", "Portfolio Emission"])
    
    with tab1:
    
        col0, col1 = st.columns(2)
        
        if ESG_W > 0:

            with col0:
                st.title(' ESG Port :national_park:  ')
                st.title('   ')
                st.title(int(ESGScore_Port))
                st.title('   ')
                st.subheader('Environmental Pillar Score')
                st.subheader(' ')
                st.subheader('Social Pillar Score')
                st.subheader(' ')
                st.subheader('Governance Pillar Score')
                st.subheader(' ')
                st.subheader(' ')

            with col1:
                st.title('%Port cal ESG ')
                st.title('   ')
                st.title(int(ESG_W) )
                st.title('   ')

                st.subheader(int(ESG_Score_E  / ESG_W ))
                st.subheader(' ')
                st.subheader(int(ESG_Score_S  / ESG_W) )
                st.subheader(' ')
                st.subheader(int(ESG_Score_G / ESG_W ))
                st.subheader(' ')
                st.subheader(' ')
        else :
            st.title(' Error ไม่มี Score  ')
            

    
    
    with tab2:
        st.header("CO2 Emission Scope 1" )
        st.subheader(str(int(Scop1_CO2_all)) + " T.")
        st.header("CO2 Emission Scope 2" )
        st.subheader( str(int(Scop2_CO2_all)) + "  T.")


    

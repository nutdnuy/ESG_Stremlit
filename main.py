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



list_AssetClass =  [""] + df["Company Common Name"].tolist()


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

show_btn = st.button("Show code!")
if show_btn:
    #df[df['Company Common Name'] == Asset_1 ]["ESG Combined Score"].tolist()[0] * Aweight_1  /100

    ESG_Score = 0
    ESG_W = 0

    if Asset_1 in df["Company Common Name"].tolist() :
        if df[df['Company Common Name'] == Asset_1 ]["ESG Combined Score"].tolist()[0] * Aweight_1  /100  > 0:
            ESG_Score += df[df['Company Common Name'] == Asset_1 ]["ESG Combined Score"].tolist()[0] * Aweight_1   
            ESG_W += Aweight_1 




    if Asset_2 in df["Company Common Name"].tolist() :
        if df[df['Company Common Name'] == Asset_2 ]["ESG Combined Score"].tolist()[0] * Aweight_2  /100  > 0:
            ESG_Score += df[df['Company Common Name'] == Asset_2 ]["ESG Combined Score"].tolist()[0] * Aweight_2  
            ESG_W += Aweight_2



    if Asset_3 in df["Company Common Name"].tolist() :
        if df[df['Company Common Name'] == Asset_3 ]["ESG Combined Score"].tolist()[0] * Aweight_3  /100  > 0:
            ESG_Score += df[df['Company Common Name'] == Asset_3 ]["ESG Combined Score"].tolist()[0] * Aweight_3  
            ESG_W += Aweight_3





    if Asset_4 in df["Company Common Name"].tolist() :
        if df[df['Company Common Name'] == Asset_4 ]["ESG Combined Score"].tolist()[0] * Aweight_4  /100  > 0:
            ESG_Score += df[df['Company Common Name'] == Asset_4 ]["ESG Combined Score"].tolist()[0] * Aweight_4  
            ESG_W += Aweight_4




    if Asset_5 in df["Company Common Name"].tolist() :
        if df[df['Company Common Name'] == Asset_5 ]["ESG Combined Score"].tolist()[0] * Aweight_5  /100  > 0:
            ESG_Score += df[df['Company Common Name'] == Asset_5 ]["ESG Combined Score"].tolist()[0] * Aweight_5  
            ESG_W += Aweight_5


    ESGScore_Port = ESG_Score / ESG_W 

    st.title(' ESG Port :national_park:  ')
    st.title('   ')
    st.title(ESGScore_Port)
    st.title('   ')
    st.title(' นำ้หนักที่คำนวณ :national_park:  ')
    st.title('   ')
    st.title(ESG_W )

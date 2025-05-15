import streamlit as st
from streamlit_option_menu import option_menu
with st.sidebar:
    select=option_menu(
        menu_title="Intenship",
        options=["Intenship","About","contact"],
        icons=['book','file-person','telephone']
    )
if select=="Intenship":
    st.title("Intenship")
elif select=="About":
    st.title("About")
elif select=="contact":
    st.title("contact")
    st.balloons()
"""st.title("Vinsup Infotech")
st.header("Dhaarani")
st.subheader("Akalya")
st.text("Baladharshini")
st.write("🟢Subashini")
st.badge("add",color="green")
st.metric("python","20","-20%")


st.divider()
st.text_input("name:")
st.number_input("age:",min_value=0)
st.selectbox("gender",["male","female"])
st.multiselect("skills",["HTML","CSS","JS","PYTHON"])
st.radio("state",["TN","KL","KA"])
st.checkbox("agree to terms and conditons")
st.button("submit")
st.button("click")

col1,col2=st.columns(2)
with col1:
    st.text_input("username")
with col2:
    st.image("https://th.bing.com/th/id/R.78a13c9eb31108addb76f77ada4589ff?rik=b%2fIodCIvyGbxCA&riu=http%3a%2f%2ffiles.all-free-download.com%2fdownloadfiles%2fwallpapers%2f1920_1080%2fpeaceful_lake_wallpaper_landscape_nature_1208.jpg&ehk=6EYMLnN48Cs4mGNjCqvvjwaPz6MF2KRLIUOhJG57Z8g%3d&risl=&pid=ImgRaw&r=0") 
with st.sidebar:
    st.write("My Side bar") """  
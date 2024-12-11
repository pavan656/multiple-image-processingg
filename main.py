import streamlit as st
from streamlit_option_menu import option_menu
import img_Compressor,about,contact

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        with st.sidebar:        
            app = option_menu(
                menu_title="Main Menu",
                options=['IMG Compressor','About','Contact Us'],
                icons=['image','book','envelope'],
                menu_icon='cast',
                default_index=0
                
                )

        
        if app == "IMG Compressor":
            img_Compressor.app()
        if app == "About":
            about.app()
        if app == "Contact Us":
            contact.app()    
 
    run()            
         

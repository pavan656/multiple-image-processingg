import streamlit as st

def app():
    st.markdown(
    "<h1 style='font-size: 5em;text-align: center; border: solid #2B1B3D; border-radius: 10px;'>Contact Us</h1>",
    unsafe_allow_html=True,
    )
    st.write("")
    st.write("---")
    st.header(":mailbox: Get In Touch With Us..!")
    st.write("")

    contact_form = """
        <form action="https://formsubmit.co/pavan.s.diwakar@gmail.com" method="POST">
            <input type="hidden" name="_autoresponse" value="Your Message has been recorded.">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Details about the issue"></textarea>
            <button type="submit">Send</button>
        </form>
        """
    
    st.markdown(contact_form, unsafe_allow_html=True)

    def local_css(file_name):
         with open(file_name) as f:
              st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    local_css("assets/style.css")

import streamlit as st

st.title("Hello Streamlit-er 👋")
st.markdown(
    """ 
    This is a playground for you to try Streamlit and have fun. 

    **There's :rainbow[so much] you can build!**
    
    We prepared a few examples for you to get started. Just 
    click on the buttons above and discover what you can do 
    with Streamlit. 
    """
)

if st.button("Send balloons!"):
    st.balloons()

tabs = st.tabs(['Me', 'My projects'])
with tabs[0]:
    st.markdown("Hi, I'm Ioana")

    cv_button = st.expander("View CV")

    with st.container(border=True):
        with cv_button:
            st.markdown("I went to Imperial")

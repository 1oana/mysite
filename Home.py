import streamlit as st

st.title("Ioana's Portfolio")


tabs = st.tabs(['Me', 'My projects'])
with tabs[0]:
    st.markdown(""" 
    My name is [Ioana](https://www.linkedin.com/in/ioana-ioana/)
    and I made this website as a little portfolio.
    My name can be confusing to pronounce,
    so I usually tell people it 'rhymes with iguana', hence the URL.
    
    Since I graduated from Imperial College London in 2022
    I've been working at the University of Oxford as a Data Scientist/Research Assistant.
    I've been working on projects in global and public health, as well as with education data.
    
    What has excited me most about my work has been the variety: of data, of challenges, of people...
    I enjoy the challenge of cleaning messy data and using it to find answers (or even just more questions) .
    I also enjoy the process of communicating my findings to others,
    whether it's through writing reports, giving presentations, or creating visualizations.
    I am passionate about using data to make a positive impact in the world,
    and I believe that data science has the potential to do just that.
    """)

    cv_button = st.expander("View a brief CV")

    with st.container():
        with cv_button:
            st.markdown("""**Experience**
                
            Data Scientist/Research Assistant at University of Oxford (2022 - Present)
            - Projects in global and public health and education data
            - Passionate about data-driven impact
                        
                        """)

import streamlit as st

st.title("Ioana's Portfolio")


tabs = st.tabs(["Me", "My projects"])
with tabs[0]:
    st.markdown(""" 
    My name is [Ioana](https://www.linkedin.com/in/ioana-duta/)
    and I made this website as a little portfolio.
    My name can be confusing to pronounce,
    so I usually tell people it 'rhymes with iguana', hence the URL.
    
    Since I graduated from Imperial College London in 2022
    I've been working at the University of Oxford as a Data Scientist/Research Assistant.
    I've been working on projects in global and public health, as well as with education data.
    
    What has excited me most about my work has been the variety: of data, of challenges, of collaborators...
    I enjoy the challenge of cleaning messy data and using it to find answers (or even just more questions) .
    I also enjoy the process of communicating my work to a diverse audience and the opportunity to
    collaborate with and learn from a wide range of people.
    I am especially passionate about using the resources available to us in the global north to make 
    a positive impact around the world.
    """)

    cv_button = st.expander("View a brief CV")

    with cv_button:
        st.markdown("""**Experience**

- **Project Administrator**, January 2025-present; _Doctoral Training Centre, University of Oxford, UK_
- **Data Scientist**, October 2022-April 2025; _Nuffield Department of Clinical Neuroscience/Oxford Martin Programme on Global Epilepsy, University of Oxford, UK_
- **Research Assistant (AI)**, October 2023-December 2024; _Nuffield Department of Women's and Reproductive Health, University of Oxford, UK_
                    """)

        st.markdown("""**Education**
- **MSci in Mathematics**, 2018-2022; _Imperial College London, UK_
    - First Class Honours (combined Bachelor's and Master's degree)
    - Thesis: _The Spread of Information about COVID-19 on Twitter_
""")
    with tabs[1]:
        st.markdown("### Projects")

        thesis_expander = st.expander(
            "**Master's project: [_The Spread of Information about COVID-19 on Twitter_](https://github.com/1oana/Masters_thesis)**"
        )
        with thesis_expander:
            st.markdown("""
                _Adapted abstract_:
                Social media acts as a forum for the exchange of ideas on a level of accessibility
                and equalisation unprecedented in human history. Twitter in particular has become a
                mainstay of socio-political communication. Thus, conversations on Twitter are a
                microcosm of the spread of ideas through the population as a whole, both as a
                mirror to information spread via other means, and as a medium of spread in and of
                itself. The results from analysis of tweet reply networks as a conversation medium
                reveals that it is possible to use measures of the size, depth and virality of
                reply cascades to predict classify conversations as to whether they are or are not
                about COVID, as well as to differentiate between accounts according to their
                purpose and influence. Investigations of user interaction networks revealed how
                both verified public figures and ordinary people have the power to influence
                conversations and become central in conversational communities.
                
                Technique and methods:
                - Data collection: Twitter API, web scraping
                - Data analysis: Python
                - Data visualisation: Gephi, PyPlot, Seaborn
                - Machine learning: Scikit-learn
                - Network analysis: NetworkX, Gephi

                The project was supervised by [Dr. Prasun K Ray](https://profiles.imperial.ac.uk/p.ray/) and
                submitted as part of my Master's degree in Mathematics at Imperial College London.

                The code and writeup is available on my [GitHub](https://github.com/1oana/Masters_thesis).
            """)

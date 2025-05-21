import streamlit as st
import pages.project_1 as p1
import subsections as sub

st.title("Ioana's Portfolio")

tabs = st.tabs(["Me", "Papers & Thesis"])
with st.sidebar:
    st.markdown("## Contact me")
    st.markdown("### [LinkedIn](https://www.linkedin.com/in/ioana-duta/)")
    st.markdown("### [GitHub](https://githib.com/1oana)")
with tabs[0]:
    sub.bio()

    cv_button = st.expander("View a brief CV")

    with cv_button:
        sub.cv()

with tabs[1]:
    st.markdown("### Projects")

    st.markdown("""
            My Google Scholar profile is available
            [here](https://scholar.google.co.uk/citations?user=d-2LGu4AAAAJ&hl=en).
    """)

    thesis_expander = st.expander(
        "**Master's project 2022: [_The Spread of Information about COVID-19 \
            on Twitter_](https://github.com/1oana/Masters_thesis)**"
    )
    with thesis_expander:
        st.markdown("""
            _Adapted abstract_:
            Social media acts as a forum for the exchange of ideas on a level of
            accessibility and equalisation unprecedented in human history. Twitter in
            particular has become a mainstay of socio-political communication. Thus,
            conversations on Twitter are a microcosm of the spread of ideas through the
            population as a whole, both as a mirror to information spread via other means,
            and as a medium of spread in and of itself. The results from analysis of tweet
            reply networks as a conversation medium reveals that it is possible to use
            measures of the size, depth and virality of reply cascades to predict classify
            conversations as to whether they are or are not about COVID, as well as to
            differentiate between accounts according to their purpose and influence.
            Investigations of user interaction networks revealed how both verified public
            figures and ordinary people have the power to influence conversations and
            become central in conversational communities.

            Technique and methods:
            - Data collection: Twitter API, web scraping
            - Data analysis: Python
            - Data visualisation: Gephi, PyPlot, Seaborn
            - Machine learning: Scikit-learn
            - Network analysis: NetworkX, Gephi

            The project was supervised by
            [Dr. Prasun K Ray](https://profiles.imperial.ac.uk/p.ray/)
            and submitted as part of my Master's degree in Mathematics
            at Imperial College London.

            The code and writeup is available on my
            [GitHub](https://github.com/1oana/Masters_thesis).
        """)

    gen_paper_expander = st.expander(
        "**Paper: [_Evaluating the generalisability of region-naïve machine learning\
            algorithms for the identification of epilepsy in \
                low-resource settings_](https://doi.org/10.1371/journal.pdig.0000491)**"
    )

    with gen_paper_expander:
        st.markdown("""
            Duta I, Kariuki SM, Ngugi AK, Mwesige AK, Masanja H, et al. (2025)
            Evaluating the generalisability of region-naïve machine learning algorithms for
            the identification of epilepsy in low-resource settings.
            PLOS Digital Health 4(2): e0000491. https://doi.org/10.1371/journal.pdig.0000491

            _Authors' Summary_:
            Epilepsy disproportionately affects people in low to middle income countries
            (LMICs). Socioeconmic disadvantages make it hard to access diagnosis and
            treatment as these rely on resources, personnel and time. Machine learning
            models may be able to provide cheap, accessible options for diagnosis and
            screening. Our previous work has demonstrated that such models can perform well.
            It is, however, crucial that tools are robust, safe, and responsibly deployed,
            especially in LMICs where poor models may more easily result in adverse impacts.

            Models must be trained on data, which are necessarily sourced from certain
            regions. Models show reduced performance when applied in regions that were not
            included in the training data. They may also have different optimal parameters,
            including the thresholds used to determine whether someone is a positive case.

            There can also be a trade-off, whereby a model that performs better in regions
            not included in the training data may perform worse in regions that were, but
            could make the model more robust.

            We recommend applying models in target regions and updating them as necessary.
            We also caution against generic deployment of models developed and tested in
            one region into a new area without careful, thorough testing and authentication.
        """)

    gpt_paper_expander = st.expander(
        "**Paper: [_Exploring the capabilities of ChatGPT in women's health:\
            obstetrics and gynaecology_](https://doi.org/10.1038/s44294-024-00028-w)**"
    )

    with gpt_paper_expander:
        st.markdown("""
            Bachmann, M., Duta, I., Mazey, E. et al. Exploring the capabilities of ChatGPT
            in women's health: obstetrics and gynaecology.
            npj Womens Health 2, 26 (2024). https://doi.org/10.1038/s44294-024-00028-w

            _Abstract_:
            Artificial Intelligence (AI) is transforming healthcare, with Large Language
            Models (LLMs) like ChatGPT offering novel capabilities. This study evaluates
            ChatGPT's performance in interpreting and responding to the UK Royal College of
            Obstetricians and Gynaecologists MRCOG Part One and Two examinations --
            international benchmarks for assessing knowledge and clinical reasoning in
            Obstetrics and Gynaecology. We analysed ChatGPT's domain-specific accuracy, the
            impact of linguistic complexity, and its self-assessment confidence. A dataset
            of 1824 MRCOG questions was curated, ensuring minimal prior exposure to ChatGPT
            ChatGPT's responses were compared to known correct answers, and linguistic
            complexity was assessed using token counts and Type-Token ratios. Confidence
            scores were assigned by ChatGPT and analysed for self-assessment accuracy.
            ChatGPT achieved 72.2% accuracy on Part One and 50.4% on Part Two, performing
            better on Single Best Answer (SBA) than Extended Matching (EMQ) Questions. The
            findings highlight the potential and significant limitations of ChatGPT in
            clinical decision-making in women's health.
        """)

    oxmat_preprint_expander = st.expander(
        "**Preprint: [_The OxMat dataset: a multimodal resource for the\
        development of AI-driven technologies in maternal and newborn \
        child health_](https://arxiv.org/abs/2404.08024)**"
    )

    with oxmat_preprint_expander:
        st.markdown("""
            Khan M Jaleed, Duta I, et al. The OxMat dataset: a multimodal resource for the
            development of AI-driven technologies in maternal and newborn child health.
            Preprint. https://doi.org/10.48550/arXiv.2404.08024

            _Abstract_:
            The rapid advancement of Artificial Intelligence (AI) in healthcare presents
            a unique opportunity for advancements in obstetric care, particularly through
            the analysis of cardiotocography (CTG) for fetal monitoring. However, the
            effectiveness of such technologies depends upon the availability of large,
            high-quality datasets that are suitable for machine learning. This paper
            introduces the Oxford Maternity (OxMat) dataset, the world's largest curated
            dataset of CTGs, featuring raw time series CTG data and extensive clinical data
            for both mothers and babies, which is ideally placed for machine learning.
            The OxMat dataset addresses the critical gap in women's health data by
            providing over 177,211 unique CTG recordings from 51,036 pregnancies, carefully
            curated and reviewed since 1991. The dataset also comprises over 200 antepartum,
            intrapartum and postpartum clinical variables, ensuring near-complete data for
            crucial outcomes such as stillbirth and acidaemia. While this dataset also
            covers the intrapartum stage, around 94% of the constituent CTGs are antepartum.
            This allows for a unique focus on the underserved antepartum period, in which
            early detection of at-risk fetuses can significantly improve health outcomes.
            Our comprehensive review of existing datasets reveals the limitations of
            current datasets: primarily, their lack of sufficient volume, detailed clinical
            data and antepartum data. The OxMat dataset lays a foundation for future
            AI-driven prenatal care, offering a robust resource for developing and testing
            algorithms aimed at improving maternal and fetal health outcomes.

        """)
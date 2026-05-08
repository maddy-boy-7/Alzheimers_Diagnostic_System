import streamlit as st


def home_page():
      st.title("Alzheimer's Diagnostic System")

    st.markdown("""
            <div style="background:rgba(139,92,246,0.15); border:1px solid rgba(139,92,246,0.4);
                                border-radius:10px; padding:20px; margin-bottom:20px;">
                                            <h3 style="color:#c4b5fd;">About Alzheimer's Disease</h3>
                                                        <p style="color:#e5e7eb; line-height:1.8;">
                                                                        Alzheimer's disease (AD) is a progressive neurodegenerative disease that affects memory,
                                                                                        thinking, and behavior. It is the most common cause of dementia, accounting for
                                                                                                        60-80% of cases. Early detection is crucial for better management and treatment outcomes.
                                                                                                                    </p>
                                                                                                                            </div>
                                                                                                                                """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
              st.markdown("""
                          <div style="background:rgba(34,197,94,0.1); border:1px solid #22c55e;
                                                  border-radius:10px; padding:16px; text-align:center;">
                                                                  <h2 style="color:#22c55e; margin:0;">55M+</h2>
                                                                                  <p style="color:#9ca3af; margin:4px 0 0; font-size:0.85rem;">People affected worldwide</p>
                                                                                              </div>
                                                                                                      """, unsafe_allow_html=True)
          with col2:
                    st.markdown("""
                                <div style="background:rgba(245,158,11,0.1); border:1px solid #f59e0b;
                                                        border-radius:10px; padding:16px; text-align:center;">
                                                                        <h2 style="color:#f59e0b; margin:0;">1 in 3</h2>
                                                                                        <p style="color:#9ca3af; margin:4px 0 0; font-size:0.85rem;">Seniors die with Alzheimer's</p>
                                                                                                    </div>
                                                                                                            """, unsafe_allow_html=True)
                with col3:
                          st.markdown("""
                                      <div style="background:rgba(239,68,68,0.1); border:1px solid #ef4444;
                                                              border-radius:10px; padding:16px; text-align:center;">
                                                                              <h2 style="color:#ef4444; margin:0;">$321B</h2>
                                                                                              <p style="color:#9ca3af; margin:4px 0 0; font-size:0.85rem;">Annual cost of care (US)</p>
                                                                                                          </div>
                                                                                                                  """, unsafe_allow_html=True)

    st.write("")
    st.subheader("How This System Works")
    st.markdown("""
            This diagnostic system provides **two prediction pathways**:

                    | Method | Input | Output |
                            |--------|-------|--------|
                                    | Clinical Prediction | Age, MMSE, APOE gene, demographics | CN / LMCI / AD |
                                            | MRI CNN Analysis | Brain MRI scan image | 4-stage dementia classification |

                                                    **Navigate to "Predict Alzheimer's"** from the sidebar to begin.
                                                        """)

    st.write("")
    st.info("""
            Disclaimer: This system is for educational and research purposes only.
                    Always consult a qualified healthcare professional for medical diagnosis.
                        """)

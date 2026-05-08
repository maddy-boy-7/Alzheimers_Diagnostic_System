import streamlit as stiimport numpy as np
def model_accuracy_page():
      st.markdown("""
          <div style="background:linear-gradient(135deg,rgba(109,40,217,0.3),rgba(5,5,30,0.7)); border:1px solid rgba(139,92,246,0.5); border-radius:16px; padding:40px; text-align:center; margin-bottom:30px;">
                  <h1 style="color:#fff; font-size:2.2rem; margin:0 0 8px; letter-spacing:2px;">
                              Model Performance Dashboard
                                      </h1>
                                              <p style="color:#c4b5fd; font-size:1rem; margin:0;">
                                                          CNN + Logistic Regression - Training Results, Architecture and Metrics
                                                                  </p>
                                                                      </div>
                                                                          """, unsafe_allow_html=True)
  

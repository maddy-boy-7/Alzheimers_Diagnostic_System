import streamlit as st
from config import HF_EMAIL, HF_PASS, BASE_PROMPT


def _smart_response(prompt: str) -> str:
      p = prompt.lower().strip()

    if any(w in p for w in ["hello", "hi", "hey", "good morning", "good evening"]):
              return ("Hello! I'm your Alzheimer's AI assistant. I can help you with information about "
                                      "Alzheimer's disease, its symptoms, prevention strategies, treatment options, "
                                      "caregiving tips, and more. What would you like to know?")

    if any(w in p for w in ["symptom", "sign", "what is alzheimer", "how to know"]):
              return ("**Common Symptoms of Alzheimer's Disease:**\n\n"
                                      "Early Stage: Memory loss affecting daily life, difficulty planning or solving problems.\n\n"
                                      "Middle Stage: Increasing memory loss, difficulty recognizing family/friends.\n\n"
                                      "Late Stage: Loss of ability to communicate verbally, complete dependence on others.\n\n"
                                      "If you notice these signs, please consult a neurologist for proper evaluation.")

    if any(w in p for w in ["cause", "risk", "why", "apoe", "genetic", "gene"]):
              return ("**Causes & Risk Factors:**\n\n"
                                      "APOE-e4 gene: The strongest known genetic risk factor.\n\n"
                                      "Age: Risk doubles every 5 years after age 65.\n\n"
                                      "Medical conditions: Cardiovascular disease, diabetes, high blood pressure.\n\n"
                                      "Family history: Having a parent or sibling with Alzheimer's increases your risk.")

    if any(w in p for w in ["prevent", "avoid", "reduce risk", "protect"]):
              return ("**Ways to Reduce Your Alzheimer's Risk:**\n\n"
                                      "Exercise regularly: 150 min/week of aerobic exercise.\n\n"
                                      "Eat a brain-healthy diet: Mediterranean or MIND diet.\n\n"
                                      "Stay mentally active: Puzzles, reading, learning new skills.\n\n"
                                      "Get quality sleep: Brain clears toxic proteins during sleep.\n\n"
                                      "Manage cardiovascular  health: Control blood pressure and cholesterol.")

    if any(w in p for w in ["treat", "cure", "medication", "drug", "therapy"]):
              return ("**Alzheimer's Treatment Options:**\n\n"
                                      "FDA-Approved Medications:\n"
                                      "- Cholinesterase inhibitors (donepezil, rivastigmine) for early/middle stages\n"
                                      "- Memantine for moderate to severe Alzheimer's\n"
                                      "- Lecanemab (Leqembi) - newer drug that slows progression\n\n"
                                      "There is currently no cure, but early treatment can significantly slow progression.")

    if any(w in p for w in ["stage", "progression", "mild", "moderate", "severe"]):
              return ("**Stages of Alzheimer's Disease:**\n\n"
                                      "Stage 1 - Preclinical: Brain changes occurring but no noticeable symptoms.\n\n"
                                      "Stage 2 - MCI: Slight memory decline, not severe enough to interfere with daily life.\n\n"
                                      "Stage 3 - Mild: Mild memory loss, can still live independently.\n\n"
                                      "Stage 4 - Moderate: Needs help with daily activities.\n\n"
                                      "Stage 5 - Severe: Full-time care required.")

    if any(w in p for w in ["diagnos", "test", "detect", "mmse", "scan", "mri"]):
              return ("**Diagnosing Alzheimer's Disease:**\n\n"
                                      "Clinical Assessment: MMSE and standardized cognitive tests.\n\n"
                                      "Brain Imaging: MRI and PET scans to detect amyloid plaques.\n\n"
                                      "Biomarker Tests: Blood tests for amyloid and tau proteins.\n\n"
                                      "This prediction system uses clinical data (age, MMSE, APOE genotype) to assess risk.")

    if any(w in p for w in ["caregiv", "care for", "support", "nursing"]):
              return ("**Caregiving Tips:**\n\n"
                                      "Create a safe environment: Remove fall hazards, lock medications.\n\n"
                                      "Establish routines: Consistent schedules reduce confusion.\n\n"
                                      "Communicate clearly: Simple sentences, speak slowly.\n\n"
                                      "Alzheimer's Association Helpline: 1-800-272-3900 (24/7)")

    if any(w in p for w in ["statistic", "how many", "prevalence", "million"]):
              return ("**Alzheimer's Disease - Key Statistics:**\n\n"
                                      "Over 55 million people worldwide live with dementia.\n\n"
                                      "In the US: approximately 6.9 million Americans age 65+ have Alzheimer's.\n\n"
                                      "Every 3 seconds, someone develops dementia.\n\n"
                                      "Alzheimer's is the 7th leading cause of death in the United States.")

    if any(w in p for w in ["bye", "goodbye", "thank", "thanks"]):
              return ("Thank you for using the Alzheimer's Prediction System!\n\n"
                                      "Remember: early detection saves lives. If you have concerns, "
                                      "please consult a healthcare professional. Stay healthy!")

    return ("I can help you with:\n\n"
                        "- Symptoms of Alzheimer's\n"
                        "- Causes & Risk Factors\n"
                        "- Prevention strategies\n"
                        "- Treatment options\n"
                        "- Disease stages\n"
                        "- How to get diagnosed\n"
                        "- Caregiving tips\n"
                        "- Global statistics\n\n"
                        "Try asking me about any of these topics!")



def chat_bot():
      st.title("Alzheimer's Assistant ChatBot")
      st.write("Ask me anything about Alzheimer's disease  - symptoms, prevention, treatment, and more.")
      st.write("---")

    if "messages" not in st.session_state:
              st.session_state.messages = [
                            {"role": "assistant", "content": "Hi! I'm your Alzheimer's AI assistant. How can I help you today?"}
              ]

    for msg in st.session_state.messages:
              with st.chat_message(msg["role"]):
                            st.markdown(msg["content"])

          user_input = st.chat_input("Type your question here...")

    if user_input:
              st.session_state.messages.append({"role": "user", "content": user_input})
              with st.chat_message("user"):
                            st.markdown(user_input)

              with st.chat_message("assistant"):
                            with st.spinner("Thinking..."):
                                              original_input = user_input
                                              response = None

                                if HF_EMAIL and HF_PASS:
                                                      try:
                                                                                from hugchat import hugchat
                                                                                from hugchat.login import Login
                                                                                sign = Login(HF_EMAIL, HF_PASS)
                                                                                cookies = sign.login()
                                                                                chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
                                                                                hf_query = user_input
                                                                                if not st.session_state.get("_base_sent"):
                                                                                                              st.session_state["_base_sent"] = True
                                                                                                              hf_query = BASE_PROMPT + user_input
                                                                                                          response = str(chatbot.chat(hf_query)).strip("`")
except Exception:
                        response = None

                if not response:
                                      response = _smart_response(original_input)

            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})


import streamlit as st
from config import TEAM_MEMBERS, COLLEGE, DEPT, CITY


def team_members():
      st.title("Team Members")

    st.markdown("""
            <div style="background:rgba(139,92,246,0.15); border:1px solid rgba(139,92,246,0.4);
                                border-radius:10px; padding:20px; margin-bottom:20px; text-align:center;">
                                            <h3 style="color:#c4b5fd; margin:0;">B.Tech Final Year Project</h3>
                                                        <p style="color:#9ca3af; margin:8px 0 0;">Alzheimer's Diagnostic System</p>
                                                                </div>
                                                                    """, unsafe_allow_html=True)

    cols = st.columns(len(TEAM_MEMBERS))
    for col, member in zip(cols, TEAM_MEMBERS):
              with col:
                            st.markdown(f\"\"\"
                                <div style=\"background:rgba(0,0,0,0.4); border:1px solid rgba(139,92,246,0.3);
                                            border-radius:12px; padding:20px; text-align:center;\">
                                    <div style=\"font-size:3rem; margin-bottom:10px;\">User</div>
                                    <h3 style=\"color:#c4b5fd; margin:0 0 4px;\">{member['name']}</h3>
                                    <p style=\"color:#a78bfa; font-size:0.85rem; margin:0 0 8px;\">{member['role']}</p>
                                    <p style=\"color:#9ca3af; font-size:0.8rem; margin:0 0 4px;\">{member['dept']}</p>
                                    <p style=\"color:#9ca3af; font-size:0.75rem; margin:0 0 8px;\">{member['college']}</p>
                                    <p style=\"color:#9ca3af; font-size:0.75rem; margin:0;\">{member['city']}</p>
                                    <hr style=\"border-color:rgba(139,92,246,0.2); margin:12px 0;\">
                                    <p style=\"color:#60a5fa; font-size:0.8rem; margin:0;\">Email {member['email']}</p>
                                </div>
                            \"\"\", unsafe_allow_html=True)

          st.write(\"\")
                       st.markdown(f\"\"\"
                           <div style=\"background:rgba(0,0,0,0.3); border:1px solid rgba(139,92,246,0.2);
                    border-radius:10px; padding:16px; text-align:center; margin-top:10px;\">
            <p style=\"color:#9ca3af; margin:0; font-size:0.9rem;\">
                <strong style=\"color:#c4b5fd;\">{COLLEGE}</strong><br>
                {DEPT} | {CITY}
            </p>
        </div>
    \"\"\", unsafe_allow_html=True)

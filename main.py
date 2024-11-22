import streamlit as st

st.set_page_config(
    page_title = "MenoCare | Wellness Through Menopause",
    page_icon = "images/favicon.ico"
)

st.markdown(
    """
    <style>
        .stImage img {
            position: absolute;
            top: -50px;  
            right: -400px; 
            width: 150px; 
            z-index: 1000; 
        }
        .block-container {
            padding-top: 100px;
        }
        .custom-paragraph {
            margin-bottom: 28px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.image("images/MenoCare.png", width=350, caption=None)
    
st.title("Welcome to MENOCARE")
st.write('<p class="custom-paragraph">Your personalized wellness support through menopause</p>', unsafe_allow_html=True)



@st.fragment()
def personal_data_form():
    with st.form("personal_data"):
        st.header("Profile Information")
        
        name = st.text_input("Name")
        
        age = st.number_input(
            "Age", 
            min_value=1, 
            max_value=120, 
            step=1
        )
        
        weight = st.number_input(
            "Weight (kg)", 
            min_value=0.0, 
            max_value=300.0, 
            step=0.1
        )
        
        height = st.number_input(
            "Height (cm)", 
            min_value=0.0, 
            max_value=250.0, 
            step=0.1
        )
        
        activities = (
            "Sedentary",
            "Lightly Active",
            "Moderately Active",
            "Very Active",
            "Super Active",
        )
        activity_level = st.selectbox("Activity Level", activities)
        
        symptoms = (
            "Hot Flashes",
            "Night Sweats",
            "Mood Swings",
            "Brain Fog",
            "Weight Gain",
            "Fatigue",
            "Sleep Disturbances",
            "Joint Pain",
            "Bone Density Loss",
        )
        menopause_symptoms = st.multiselect("Menopause Symptoms", symptoms)
        
        personal_data_submit = st.form_submit_button("Save")
        if personal_data_submit:
            if all(name, age, weight, height, activity_level, menopause_symptoms):
                with st.spinner():
                    # TODO:SAVE THE DATA
                    st.success("Your information has been saved.")
            else:
                st.warning("Please fill in all of the required information.")
                


def forms():
    personal_data_form()
    
if __name__ == "__main__":
    forms()
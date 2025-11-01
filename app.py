import streamlit as st
import psycopg2

# --- Database Connection Function ---
# THIS IS THE FINAL, CORRECT FUNCTION
def get_db_connection():
    try:
        # This function now READS from st.secrets and adds SSL
        conn = psycopg2.connect(
            host=st.secrets["db_host"],
            database=st.secrets["db_database"],
            user=st.secrets["db_user"],
            password=st.secrets["db_password"],
            port=int(st.secrets["db_port"]),
            sslmode="require"  # <-- THIS FIXES THE "insecure connection" ERROR
        )
        return conn
    except Exception as e:
        st.error(f"Error connecting to the database: {e}")
        return None

# --- Custom CSS for Styling ---
# This function injects custom CSS to make the app look good.
def load_css():
    st.markdown(
        """
        <style>
        
        /* --- Base App Styling (Formal Dark Background) --- */
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #1a2938 0%, #2c3e50 100%);
            color: #eBf5eB; /* Faint Green Text Color */
            font-size: 16px; 
        }

        /* --- Logo Styling (REMOVED) --- */
        
        /* --- Title (Centered) --- */
        .stTitle {
            font-family: 'Arial', sans-serif;
            font-weight: bold;
            color: #eBf5eB; /* Faint Green Text Color */
            font-size: 3rem; 
            text-align: center; 
            border: 2px solid #5c9dff; 
            border-radius: 15px;      
            padding: 10px;            
            width: 70%;               
            margin: 10px auto;        
        }
        
        /* --- Subheader (Centered) --- */
        .st-emotion-cache-1jicfab.e115fcil1 {
            font-size: 1.75rem; 
            text-align: center; 
            color: #eBf5eB; /* Faint Green Text Color */
        }

        /* --- Step Headers (Centered) --- */
        .st-emotion-cache-1jicfab { 
             color: #eBf5eB; /* Faint Green Text Color */
             font-family: 'Arial', sans-serif;
             font-size: 2rem; 
             text-align: center; 
             padding-top: 1rem;
        }
        
        /* --- Section Markdown Headers (e.g., Personal Details) --- */
        [data-testid="stForm"] h3 {
            font-size: 1.9rem; /* INCREASED FONT SIZE */
            font-weight: bold;
            color: #eBf5eB; /* Faint Green Text Color */
        }

        /* --- Frosted Glass Form Container --- */
        [data-testid="stForm"] {
            background: rgba(255, 255, 255, 0.05); 
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3); 
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
            transition: transform 0.3s ease;
        }
        [data-testid="stForm"]:hover {
            transform: scale(1.01);
            box-shadow: 0 0 20px #5c9dff; 
        }

        /* --- Input Labels (e.g., "Roll No") --- */
        .st-emotion-cache-1n76e7f { 
            color: #eBf5eB; /* Faint Green Text Color */
            font-weight: bold;
            font-size: 1.25rem; 
        }

        /* --- Style all input boxes (Dark Mode) --- */
        [data-testid="stTextInput"] input,
        [data-testid="stNumberInput"] input,
        [data-testid="stTextArea"] textarea {
            background-color: rgba(255, 255, 255, 0.1); 
            color: #eBf5eB; /* Faint Green Text Color (for user typing) */
            font-size: 1.1rem; 
            border: 1px solid rgba(255, 255, 255, 0.5);
            border-radius: 5px;
            transition: all 0.3s ease;
        }

        /* --- Input box focus effect --- */
        [data-testid="stTextInput"] input:focus,
        [data-testid="stNumberInput"] input:focus,
        [data-testid="stTextArea"] textarea:focus {
            border-color: #5c9dff; 
            box-shadow: 0 0 10px #5c9dff;
            background-color: rgba(255, 255, 255, 0.15);
        }

        /* --- Submit Button Container --- */
        .stButton {
            display: flex;
            justify-content: center; 
        }

        /* --- Submit Button --- */
        .stButton > button {
            background: #0068c9; 
            color: white; 
            border: none;
            border-radius: 10px;
            padding: 12px 20px; 
            font-weight: bold;
            font-size: 1.25rem; 
            width: 50%; 
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            background: #007fff; 
            box-shadow: 0 0 15px #5c9dff;
            transform: scale(1.02);
        }
        
        /* --- Info Box (for selected year) --- */
        [data-testid="stInfo"] {
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            border: none;
            font-size: 1.1rem; 
            color: #eBf5eB; /* Faint Green Text Color */
        }
        
        /* --- Container for Year Selection --- */
        .st-emotion-cache-q8sbsg { 
             background-color: rgba(255, 255, 255, 0.05); 
             border: 1px solid rgba(255, 255, 255, 0.3); 
             border-radius: 15px; 
             padding: 20px;
        }
        
        /* --- Selectbox (Year) Text --- */
        .st-emotion-cache-1629p8f {
            font-size: 1.2rem; 
        }
        .st-emotion-cache-q8sbsg .st-emotion-cache-1n76e7f {
             font-size: 1.25rem !important; 
             color: #eBf5eB !important; /* Faint Green Text Color */
             font-weight: bold !important;
        }


        /* --- START: EXPLICIT LIGHT THEME OVERRIDES --- */
        
        body[data-theme="light"] [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #e0e0e0 0%, #f0f0f0 100%); /* Lighter background */
            color: #333333; /* Darker text for readability */
        }

        body[data-theme="light"] [data-testid="stForm"] h3 {
            color: #013220 !important; /* Dark Green (blakish) */
        }

        body[data-theme="light"] .stTitle,
        body[data-theme="light"] .st-emotion-cache-1jicfab.e115fcil1,
        body[data-theme="light"] .st-emotion-cache-1jicfab,
        body[data-theme="light"] .st-emotion-cache-1n76e7f,
        body[data-theme="light"] .st-emotion-cache-q8sbsg .st-emotion-cache-1n76e7f {
            color: #2c3e50 !important; /* Dark blue/grey for other headers/labels */
        }

        body[data-theme="light"] [data-testid="stTextInput"] input,
        body[data-theme="light"] [data-testid="stNumberInput"] input,
        body[data-theme="light"] [data-testid="stTextArea"] textarea {
            background-color: #ffffff; /* White background for inputs */
            color: #333333; /* Dark text for inputs */
            border: 1px solid #cccccc; /* Light border */
        }

        body[data-theme="light"] [data-testid="stForm"] {
            background: rgba(255, 255, 255, 0.8); /* Slightly transparent white form */
            border: 1px solid #e0e0e0;
            box-shadow: 0 4px 16px 0 rgba(0, 0, 0, 0.1);
        }
        
        body[data-theme="light"] [data-testid="stInfo"] {
            background-color: rgba(200, 200, 200, 0.8); /* Light grey info box */
            color: #333333;
        }
        
        /* --- END: LIGHT THEME OVERRIDES --- */


        /* --- MEDIA QUERY FOR MOBILE PHONES --- */
        @media (max-width: 768px) {
            
            /* Make fonts smaller */
            .stTitle {
                font-size: 2.2rem; 
                width: 90%; 
            }
            .st-emotion-cache-1jicfab.e115fcil1 {
                font-size: 1.4rem; 
            }
            .st-emotion-cache-1jicfab { 
                 font-size: 1.6rem; 
            }
            [data-testid="stForm"] h3 {
                font-size: 1.5rem; /* Increased mobile size */
            }
            .st-emotion-cache-1n76e7f { 
                font-size: 1.1rem; 
            }
            .stButton > button {
                font-size: 1.1rem; 
                width: 80%; 
            }
            
            /* Reduce padding to save space */
            [data-testid="stForm"] {
                padding: 15px;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# --- Main Application ---
st.set_page_config(
    page_title="AI&DS Student Portal",
    page_icon="🤖",  # AI emoji as tab icon
    layout="wide"
    # The 'theme="dark"' argument is removed to prevent the error
)

# Call the CSS function to apply styles
load_css()

# --- DEBUGGING CODE IS NOW REMOVED ---


# --- 1. Header with Title (Centered) ---
# st.image("AI.webp", width=150) # Image is removed
st.title("AI & DS Department 🧠")
st.subheader("Student Data Entry Portal")


# --- 2. CHOOSE THE YEAR (in its own container) ---
with st.container(border=True):
    st.header("Step 1: Select Student Year 🎓")
    year_option = st.selectbox(
        "In which year you are?", 
        ("Second Year", "Third Year", "Final Year")
    )

# This converts the user-friendly name to the actual table name
if year_option == "Second Year":
    table_name = "second_year"
elif year_option == "Third Year":
    table_name = "third_year"
else:
    table_name = "final_year"

st.info(f"You are currently entering data for: **{table_name}**")

# --- 3. CREATE THE DATA ENTRY FORM ---
st.header("Step 2: Fill in Student Details 📝")

with st.form(key="student_form", clear_on_submit=True):
    
    # We use st.columns to make the form layout cleaner
    # On mobile, these will automatically stack.
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 👤 Personal Details")
        roll_no = st.text_input("🆔 Roll No (e.g., 21BIT001)", help="This is the Primary Key and must be unique.")
        name = st.text_input("👤 Full Name")
        email_id = st.text_input("✉️ Email ID")
        phone_no = st.text_input("📞 Phone No")
        class_teacher = st.text_input("🧑‍🏫 Class Teacher Name")

    with col2:
        st.markdown("### 📚 Academic Details")
        mark_10th = st.number_input("🔟 10th Mark (%)", min_value=0.0, max_value=100.0, format="%.2f")
        mark_12th_or_diploma = st.number_input("🎓 12th/Diploma Mark (%)", min_value=0.0, max_value=100.0, format="%.2f")
        cgpa = st.number_input("📈 Current CGPA", min_value=0.0, max_value=10.0, format="%.2f")
        attendance_percentage = st.number_input("📊 Attendance (%)", min_value=0.0, max_value=100.0, format="%.2f")
    
    # Add a visual separator
    st.markdown("---") 
    
    st.markdown("### 💡 Career & Feedback")
    col3, col4 = st.columns(2)

    with col3:
        career_aspirations = st.text_area("🚀 Career Aspirations")
        certifications = st.text_area("📜 Certifications (one per line)")
        achievements = st.text_area("🏆 Achievements (one per line)")
    
    with col4:
        interested_area = st.text_area("🛰️ Interested Areas (e.g., AI, Web, Data Science)")
        career_help_needed = st.text_area("🤝 For Career, Need Help From Dept")
        suggestion_feedback = st.text_area("📬 Suggestions / Feedback")

    # --- 4. SUBMIT BUTTON ---
    st.markdown("<br>", unsafe_allow_html=True) # Adds a little space
    submit_button = st.form_submit_button(label="Click Here to Submit Data") 

# --- 5. LOGIC TO RUN WHEN FORM IS SUBMITTED ---
# This part is unchanged and will work perfectly.
if submit_button:
    # Basic validation
    if not roll_no or not name or not email_id:
        st.warning("Please fill in at least Roll No, Name, and Email ID.")
    else:
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                sql_query = f"""
                INSERT INTO {table_name} (
                    roll_no, name, email_id, phone_no, mark_10th, 
                    mark_12th_or_diploma, cgpa, career_aspirations, 
                    attendance_percentage, class_teacher, certifications, 
                    achievements, interested_area, career_help_needed, 
                    suggestion_feedback
                ) 
                VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s, %s, %s
                )
                """
                
                # Make sure your variable name matches the one in st.number_input
                data_to_insert = (
                    roll_no, name, email_id, phone_no, mark_10th,
                    mark_12th_or_diploma, cgpa, career_aspirations,
                    attendance_percentage, class_teacher, certifications,
                    achievements, interested_area, career_help_needed,
                    suggestion_feedback
                )
                
                cursor.execute(sql_query, data_to_insert)
                conn.commit() 
                
                st.success(f"Successfully added student {name} ({roll_no}) to the {table_name} table!")
                
                cursor.close()
                conn.close()
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.info("Tip: Check if the 'Roll No' already exists. It must be unique.")
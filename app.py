import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Functions for "1ergest"
def add_nine_months_nine_days(date):
    try:
        # Add 9 months and 9 days to the input date
        new_date = date + relativedelta(months=9, days=9)
        # Format the new date back to a string in D M YYYY format
        new_date_str = new_date.strftime('%d %m %Y')
        return new_date_str
    except ValueError:
        return "Invalid date format or non-existent date. Please enter the date as D M YYYY (e.g., 27 3 2004)."

# Functions for "2uerdgd"
def add_thirty_six_months(date):
    try:
        # Add 36 months to the input date
        new_date = date + relativedelta(months=36)
        # Format the new date back to a string in D M YYYY format
        new_date_str = new_date.strftime('%d %m %Y')
        return new_date_str
    except ValueError:
        return "Invalid date format or non-existent date. Please enter the date as D M YYYY (e.g., 27 3 2004)."

def add_fifty_months(date):
    try:
        # Add 50 months to the input date
        new_date = date + relativedelta(months=50)
        # Format the new date back to a string in D M YYYY format
        new_date_str = new_date.strftime('%d %m %Y')
        return new_date_str
    except ValueError:
        return "अवैध तारीख स्वरूप किंवा अस्तित्वात नसलेली तारीख. कृपया D M YYYY म्हणून तारीख प्रविष्ट करा (उदा. 27 3 2004)."

# Streamlit app
st.title("तारीख गणना")

# Display "Select an option" as a title in the sidebar
st.sidebar.markdown("## एक पर्याय निवडा")

# Display "1ergest" and "2uerdgd" options directly on the sidebar
calc_option = st.sidebar.radio("", ["नऊ महिने नऊ दिवसांनी", "अनुदान"])

st.header("जन्म तारीख निवडा")
year = st.selectbox("वर्ष", list(range(2023, 2051)), index=18)
month = st.selectbox("महिना", list(range(1, 13)), index=3)
day = st.selectbox("दिवस", list(range(1, 32)), index=5)

try:
    input_date = datetime(year, month, day)
    if calc_option == "नऊ महिने नऊ दिवसांनी":
        new_date_str = add_nine_months_nine_days(input_date)
        st.markdown(f"### नऊ महिने नऊ दिवसांनी: **:blue[{new_date_str}]**")
    else:  # 2uerdgd
        period_option = st.selectbox("निवडा गाय किंवा म्हैस", ["गाय", "म्हैस"])
        if period_option == "गाय":
            new_date_str = add_thirty_six_months(input_date)
            st.markdown(f"### 36 महिन्यांनंतर: **:blue[{new_date_str}]**")
        else:
            new_date_str = add_fifty_months(input_date)
            st.markdown(f"### 50 महिन्यांनंतर: **:blue[{new_date_str}]**")
except ValueError:
    st.markdown("### **:red[अवैध तारीख. कृपया वैध तारीख निवडा.]**")

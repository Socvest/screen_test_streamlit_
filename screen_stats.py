import streamlit as st
from st_screen_stats import st_screen_data
from custom_sidebar_icons import Set_Nav_Emojis as set_Nav
st.set_page_config(layout="wide")

js = f"""
            <script>
                stDecoration = parent.document.querySelectorAll('[data-testid="stDecoration"]')
                stDecoration[0].remove();
                stFooter = parent.document.querySelectorAll('footer');
                stFooter[0].remove();

                removeElstDecoration = parent.document.querySelectorAll('iframe[srcdoc*="stDecoration[0].remove()"]')[0].parentNode;
                removeElstDecoration.style = 'display:none;'
                
            </script>

            """
st.components.v1.html(js, height=0, width=0)

# st.write(st_screen_data())

screen_size_Dashboard = st_screen_data(key="screen_size_Dashboard")
# with st.spinner("loading..."):
#     time.sleep(2)
    # if screen_size_Dashboard == None:
    #     st.markdown("""
    #                     <meta http-equiv="refresh" content="0; URL=http://localhost:8501" />
    #                 """, unsafe_allow_html=True)


st.write(st.session_state["screen_size_Dashboard"])

if "user_authorized_status" not in st.session_state:
    st.session_state["user_authorized_status"] = None
if "sessionCookie" not in st.session_state:
    st.session_state["sessionCookie"] = None

def cookies_check():

    headers = _get_websocket_headers()
    if "Cookie" in headers:
        cookies_set = [{o[0].strip(): o[1].strip()} for o in [ i.split("=") for i in headers.get("Cookie").split(";") if i != ""] ]
        auth_cookie = [i for i in cookies_set if i.get("optumGamerSession") != None]
        if len(auth_cookie) > 0:
            st.session_state["sessionCookie"] = auth_cookie[0]["optumGamerSession"]
            verify_session = requests.get(base_url + soft_user_login_path, params={"sessionId":auth_cookie[0]["optumGamerSession"]})
            if verify_session.status_code == 200:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
st.session_state["user_authorized_status"] = True# cookies_check() 

if st.session_state["user_authorized_status"] == False:

    st.write("Need to authenticate")

else:

    emojis_list = [
        {"emojiLibrary":"remix_icon", "iconName":"ri-dashboard-fill", "emojiObject":{}, "style":"", "elementID":""},
        {"emojiLibrary":"remix_icon", "iconName":"ri-tools-line", "style":"", "elementID":""},
    ]

    emojisOrender = set_Nav(emojis_list)
    emojisOrender.show_me_the_icons_Render() 

    if "dashboard_page_sel" not in st.session_state:
        st.session_state["dashboard_page_sel"] = 1
    if "filter_form_status_msg" not in st.session_state:
        st.session_state["filter_form_status_msg"] = None
    if "filter_data_results_search" not in st.session_state:
        st.session_state["filter_data_results_search"] = None
    if "filter_data_results_filter" not in st.session_state:
        st.session_state["filter_data_results_filter"] = []
    if "filter_has_been_selected" not in st.session_state:
        st.session_state["filter_has_been_selected"] = None

    if "filtered_data_" not in st.session_state:
        st.session_state["filtered_data_"] = []

    if "edit_dashboard" not in st.session_state:
        st.session_state['edit_dashboard'] = False

    if "edit_dashboard_btn_name" not in st.session_state:
        st.session_state['edit_dashboard_btn_name'] = "Edit Dashboard"
    if "edit_dashboard_tooltip" not in st.session_state:
        st.session_state['edit_dashboard_tooltip'] = ""
    if "dashboard_data" not in st.session_state:
        st.session_state['dashboard_data'] = None

    if "filter_dashboard_" not in st.session_state:
        st.session_state["filter_dashboard"] = None
    if "filter_options_" not in st.session_state:
        st.session_state["filter_options_"] = None
    if "filter_options_select" not in st.session_state: 
        st.session_state["filter_options_select"] = None
    if "filter_options_radio" not in st.session_state:
        st.session_state["filter_options_radio"] = None 
    if "tablet_mobile_sx" not in st.session_state:
        st.session_state["tablet_mobile_sx"] = None
    if "mobile_sx" not in st.session_state:
        st.session_state["mobile_sx"] = None

    def delete_dashboard_card(saved_card_comp):
        st.toast("Deleting...")
                
    def update_dashboard_cards(saved_card_comp):
        st.toast("Updating...")

    def remove_duplicates_from_filtered_data(data):

        new_d = []
        index_ = []
        for x in data:
            if x['unique_id'] not in index_:
                index_.append(x["unique_id"])
                new_d.append(x)
        return new_d

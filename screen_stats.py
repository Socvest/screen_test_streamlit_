import streamlit as st
from st_screen_stats import st_screen_data
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


st.write(st_screen_data())

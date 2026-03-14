src = open(r'C:\Users\BoulePiou\cockpit-raphael\app.py', encoding='utf-8').read()

# Trouver la fin du bloc import streamlit
debut = src.index('import streamlit as st')
fin = src.index('\nimport db_wrapper')

nouveau_bloc = """import streamlit as st
import html

if not hasattr(st, "_original_markdown"):
    st._original_markdown = st.markdown
    def patched_markdown(body, unsafe_allow_html=False, **kwargs):
        if isinstance(body, str):
            import html as _html
            body = _html.unescape(body)
        return st._original_markdown(body, unsafe_allow_html=unsafe_allow_html, **kwargs)
    st.markdown = patched_markdown

if "sidebar_state" not in st.session_state:
    st.session_state.sidebar_state = "collapsed"

COMMON_BTN_CSS = "position:fixed!important;top:1rem!important;left:1rem!important;width:2.5rem!important;height:2.5rem!important;background-color:#1a0a12!important;border:2px solid #FFD060!important;color:#FFD060!important;padding:0!important;z-index:999999!important;display:flex!important;align-items:center!important;justify-content:center!important;border-radius:0.5rem!important;font-size:1.2rem!important;font-weight:bold!important;line-height:1!important;"

if st.session_state.sidebar_state == "collapsed":
    st.markdown(f\'\'\'<style>
    header[data-testid="stHeader"]{{display:none!important;}}
    section[data-testid="stSidebar"]{{display:none!important;}}
    div[data-testid="stMainBlockContainer"]>div:first-child div[data-testid="stButton"] button{{{COMMON_BTN_CSS}}}
    </style>\'\'\', unsafe_allow_html=True)
    if st.button("❯", key="btn_open"):
        st.session_state.sidebar_state = "expanded"
        st.rerun()
else:
    st.markdown(f\'\'\'<style>
    header[data-testid="stHeader"]{{display:none!important;}}
    section[data-testid="stSidebar"]{{display:block!important;visibility:visible!important;transform:translateX(0)!important;}}
    @media(max-width:768px){{section[data-testid="stSidebar"]{{position:fixed!important;width:100vw!important;min-width:100vw!important;z-index:999998!important;}}}}
    section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"]>div:first-child div[data-testid="stButton"] button{{{COMMON_BTN_CSS}}}
    </style>\'\'\', unsafe_allow_html=True)
    with st.sidebar:
        if st.button("❮", key="btn_close"):
            st.session_state.sidebar_state = "collapsed"
            st.rerun()
"""

src = src[:debut] + nouveau_bloc + src[fin:]
open(r'C:\Users\BoulePiou\cockpit-raphael\app.py', 'w', encoding='utf-8').write(src)
print("OK")

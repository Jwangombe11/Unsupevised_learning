import streamlit as st
import re
import sys
import sys
from streamlit import cli as stcli

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "clt_demo.py"]
    sys.exit(stcli.main())

st.write('Hello World')

streamlit run clt_demo.py 
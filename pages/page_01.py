import streamlit as st

import numpy as np
import pandas as pd

st.markdown("""# This is a header
## This is a sub header
This is text

- list1
- list2
- list3
""")


col1, col2, col3 = st.columns(3)
col1.metric("SPDR S&P 500", "$437.8", "-$1.25")
col2.metric("FTEC", "$121.10", "0.46%")
col3.metric("BTC", "$46,583.91", "+4.87%")



if st.button('click me'):
    # print is visible in the server output, not in the page
    print('button clicked!')
    st.write('I was clicked 🎉')
    st.write('Further clicks are not visible but are executed')
else:
    st.write('I was not clicked 😞')


df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})


# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

# and used to select the displayed lines
head_df = df.head(line_count)
st.write(head_df)

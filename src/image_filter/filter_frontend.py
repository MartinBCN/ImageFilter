import streamlit as st
from PIL import Image

from filter import Filter

st.title('Image Filter')

# --- User Inputs ---
BW = {'Yes': True, 'No': False}
bw = st.sidebar.radio(label='Black/White', options=list(BW.keys()))
bw_bool = BW[bw]

blur = st.sidebar.slider(label='Blur [%]', min_value=0, max_value=100, step=1)

# --- Uploaded Image ---

uploaded_file = st.file_uploader("Choose an image...", type="png")
if uploaded_file is not None:
    image = Image.open(uploaded_file)

    if bw_bool:
        image = Filter.black_white(image)

    image = Filter().blurry(image, blur / 100)

    st.image(image, caption='Uploaded Image.', use_column_width=True)

from PIL import Image
import streamlit as st

from src.image_filter.filter import Filter


def show_image(image: Image, bw_bool: bool, blur: int) -> None:
    if bw_bool:
        image = Filter.black_white(image)

    image = Filter().blurry(image, blur / 100)

    st.image(image, caption='Uploaded Image.', use_column_width=True)

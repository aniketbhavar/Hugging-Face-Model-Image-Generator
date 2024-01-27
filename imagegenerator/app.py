# streamlit_app.py
import streamlit as st
import requests
from PIL import Image
import io

API_URL = "               "
headers = {"Authorization": " api-your "}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

def main():
    st.title("Hugging Face Model Image Generator")

    # Sidebar for user input
    user_input = st.text_input("Enter your input:")
    if st.button("Generate Image"):
        image_bytes = query({"inputs": user_input})
        if image_bytes:
            # Display the image
            image = Image.open(io.BytesIO(image_bytes))
            st.image(image, caption="Generated Image", use_column_width=True)

            # Save the image to a file
            image_path = 'downloaded_image.jpg'
            image.save(image_path)

            # Provide a download link
            st.markdown(f"### [Download Resulting Image]({image_path})")

if __name__ == "__main__":
    main()
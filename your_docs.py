import streamlit as st
from PIL import Image
from fpdf import FPDF
import os
from pdf2image import convert_from_path


def convert_image_to_pdf(image_file, pdf_path):
    image = Image.open(image_file)
    pdf = FPDF()
    pdf.add_page()
    pdf.image(image_file, 0, 0, pdf.w, pdf.h)
    pdf.output(pdf_path, "F")


def convert_pdf_to_image(pdf_path, image_path):
    images = convert_from_path(pdf_path)
    for i, image in enumerate(images):
        image.save(f"{image_path}_{i}.jpg", "JPEG")
        

def main():
    st.title("Image ↔️ PDF Converter")

    conversion_type = st.radio("Select Conversion:", ("Image to PDF", "PDF to Image"))

    if conversion_type == "Image to PDF":
        st.subheader("Convert Image to PDF")
        image_file = st.file_uploader("Upload Image (JPEG only):", type=["jpg", "jpeg"])
        if image_file is not None:
            st.write("Image uploaded successfully!")
            st.image(image_file, caption="Uploaded Image", use_column_width=True)
            if st.button("Convert"):
                with st.spinner("Converting..."):
                    convert_image_to_pdf(image_file, "output.pdf")
                st.success("Conversion successful! You can download the PDF file below.")
                st.download_button("Download PDF", "output.pdf", label="Click here to download")

    elif conversion_type == "PDF to Image":
        st.subheader("Convert PDF to Image")
        pdf_file = st.file_uploader("Upload PDF:", type=["pdf"])
        if pdf_file is not None:
            st.write("PDF uploaded successfully!")
            if st.button("Convert"):
                with st.spinner("Converting..."):
                    convert_pdf_to_image(pdf_file, "output.jpg")
                st.success("Conversion successful! You can download the JPEG image below.")
                st.download_button("Download JPEG", "output.jpg", label="Click here to download")


if __name__ == "__main__":
    main()

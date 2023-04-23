# 1041-1050
import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

from colour_analysis import *
from texture_analysis import *

# Get the images from folder
parent_folder = "FacialExpression/"
subfolder_names = ["happy", "neutral", "sad"]

if __name__ == '__main__':
    st.title("Image Processing")
    st.write("Program ini meliputi analisis warna dan tekstur dari suatu gambar")
    st.write("---")

    ## Menampilkan daftar gambar apa saja yang ada
    st.header("List Gambar")
    df = pd.DataFrame(columns=['Image Name', 'Category'])
    df_list = []
    for subfolder in subfolder_names:
        subfolder_path = os.path.join(parent_folder, subfolder)
        image_list = os.listdir(subfolder_path)
        image_names = [os.path.splitext(image)[0] for image in image_list]
        category = [subfolder] * len(image_names)
        image_df = pd.DataFrame(
            {"Image Name": image_names, "Category": category})
        df_list.append(image_df)
    df = pd.concat(df_list, ignore_index=True)
    st.dataframe(df, width=800, height=300)
    
    ## Memuat keseluruhan gambar yang nantinya digunakan pada widget multiselect
    img_list = []
    for subfolder in subfolder_names:
        subfolder_path = os.path.join(parent_folder, subfolder)
        img_list += os.listdir(subfolder_path)
    st.write("Pilih Gambar yang Ingin Dianalisis")
    selected_img = st.multiselect(label="Ketentuan : 3 Gambar Happy, Neutral, dan Sad", options=img_list, default=None)
    
    ## Memproses gambar yang dipilih
    if(st.button("Proses") and selected_img):
        counter = 1
        for img in selected_img:
            for subfolder in subfolder_names:
                subfolder_path = os.path.join(parent_folder, subfolder)
                img_path = os.path.join(subfolder_path, img)
                if os.path.isfile(img_path):
                    st.write("---")
                    st.write(f"## Gambar #{counter}")
                    st.write("Gambar yang dipilih : ", img)
                    st.write("Kategori : ", subfolder)
                    # Colour Analysis
                    st.write("## #1 Analisis Warna")

                    ## 1. Mengubah gambar menjadi pixel
                    st.write("### A. Mengubah Gambar Menjadi Pixel")
                    img_pixel = img_to_pixels(img_path) ## Mengubah gambar menjadi pixel
                    st.image(img_pixel, caption="Gambar Asli", width=300)
                    st.dataframe(pd.DataFrame(img_pixel), width=800, height=300)
                    
                    ## 2. Menghitung histogram
                    st.write("### B. Visualisasi Histogram")
                    img_hist = get_colour_histogram(img_pixel) ## Menghitung histogram gambar
                    st.pyplot(img_hist)
                    
                    ## 3. Menghitung first order statistics
                    st.write("### C. Menghitung First Order Statistics")
                    img_stats = first_order_statistics(img_pixel) ## Menghitung statistik gambar
                    st.dataframe(pd.DataFrame(img_stats, index=["Mean", "Variance", "Skewness", "Kurtosis", "Entropy"], columns=["Value"]), width=800)

                    # Texture Analysis
                    st.write("## #2 Analisis Tekstur")

                    ## 1. Menghitung GLCM
                    st.write("### A. Menghitung GLCM")
                    metric_texture = ['dissimilarity', 'correlation', 'homogeneity', 'contrast', 'ASM', 'energy']
                    glcm_matrix = glcm(img_pixel, metric_texture)
                    st.dataframe(pd.DataFrame(glcm_matrix, index=metric_texture, columns=["0", "45", "90", "135"]), width=800)

                    ## 2. Visualisasi Histogram
                    st.write("### B. Visualisasi Histogram")
                    img_hist_texture = get_texture_histogram(glcm_matrix, metric_texture)
                    st.pyplot(img_hist_texture)

                    counter += 1
                    break;
    else:
        st.error("Tidak ada gambar yang dipilih")
            

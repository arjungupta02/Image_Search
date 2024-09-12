import streamlit as st
from bs4 import BeautifulSoup
# import requests
import ssl
from urllib.request import urlopen
# div:bugb2->figure->imgsrc:SpgDA
# imgsrc: https://plus.unsplash.com/premium_photo-1713110640802-28de8804e163
# https://www.webfx.com/tools/emoji-cheat-sheet/

st.set_page_config(page_title="Download Images",page_icon=":camping:",layout="wide")

st.markdown("<h1 style='text-align: center;'>Search Images</h1>",unsafe_allow_html=True)



if 'image_set' not in st.session_state:
    st.session_state.image_set = set()
if 'image_dict' not in st.session_state:
    st.session_state.image_dict = dict()
# image_dict = dict()

context = ssl._create_unverified_context()
with st.form("Search"):
    keyword = st.text_input("Enter your Keyword").replace(" ","-")
    search = st.form_submit_button("Search")
    print(keyword)

if search:
    st.session_state.image_set.clear()
    st.session_state.image_dict.clear()
    page = urlopen(f'https://unsplash.com/s/photos/{keyword}',context= context).read()
    soup = BeautifulSoup(page,'html.parser')
    # rows = soup.find_all('div',class_ = 'bugb2')

    img = soup.find_all('img',srcset = True,sizes = True)


    for i in img:
        st.session_state.image_set.add(i['srcset'].split(',')[3].strip())
        st.session_state.image_dict[i['srcset'].split(',')[3].strip()] = i['srcset'].split('?')[0].strip()

        # for row in rows:
        #     figures = row.find_all('figure',recursive = False)

        #     for figure in figures:
        #         img = figure.find_all('img',srcset = True,sizes = True)

        #         for i in img:
        #             image_set.add(i['srcset'].split(',')[2].strip())

placeholder = st.empty()
columns= placeholder.columns(4)

image_list = list(st.session_state.image_set)
for index, image_ in enumerate(image_list):
    col = columns[index % 4]  # Cycle through the four columns
    col.image(image_)
    col.markdown(f"[Download]({st.session_state.image_dict[image_]})", unsafe_allow_html=True)
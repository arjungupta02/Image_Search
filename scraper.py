import streamlit as st
from bs4 import BeautifulSoup
import requests
import ssl
from urllib.request import urlopen

# div:bugb2->figure->imgsrc:SpgDA
# imgsrc: https://plus.unsplash.com/premium_photo-1713110640802-28de8804e163

st.markdown("<h1 style='text-align: center;'>Search Images</h1>",unsafe_allow_html=True)

image_set = set()

context = ssl._create_unverified_context()
with st.form("Search"):
    keyword = st.text_input("Enter your Keyword").replace(" ","-")
    search = st.form_submit_button("Search")
    print(keyword)

if search:
    # page = requests.get(f'https://unsplash.com/s/photos/{keyword}')
    page = urlopen(f'https://unsplash.com/s/photos/{keyword}',context= context).read()
    soup = BeautifulSoup(page,'html.parser')
    # rows = soup.find_all('div',class_ = 'bugb2')
    
    img = soup.find_all('img',srcset = True,sizes = True)

    for i in img:
        image_set.add(i['srcset'].split(',')[2].strip())

    # for row in rows:
    #     figures = row.find_all('figure',recursive = False)

    #     for figure in figures:
    #         img = figure.find_all('img',srcset = True,sizes = True)

    #         for i in img:
    #             image_set.add(i['srcset'].split(',')[2].strip())

    placeholder = st.empty()
    col1,col2,col3= placeholder.columns(3)

    image_list = list(image_set)
    for index in range(len(image_list)):
        if index % 3 == 0:
            col3.image(image_list[index])
        elif index % 2 == 0:
            col2.image(image_list[index])
        else:
            col1.image(image_list[index])


# # https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=100&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 100w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=200&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 200w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=300&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 300w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 400w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 500w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 600w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 700w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 800w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 900w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=1000&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 1000w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=1200&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 1200w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=1400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 1400w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=1600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 1600w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=1800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 1800w, https://plus.unsplash.com/premium_photo-1667126447968-f02d4cb36114?w=2000&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJlZXN8ZW58MHx8MHx8fDA%3D 2000w

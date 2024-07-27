import streamlit as st
import requests


API_KEY = st.secrets["api_key"]

def get_gifs(query):
    url = f"https://api.giphy.com/v1/gifs/search?api_key={API_KEY}&q={query}&limit=2"
    response = requests.get(url)
    gifs = response.json()['data']
    return [gif['images']['downsized']['url'] for gif in gifs]

def main():
    st.title('Giphy Search App')

    query = st.text_input('Enter a search term:')
    if query:
        gifs = get_gifs(query)
        for gif in gifs:
            st.image(gif, use_column_width=True)

if __name__ == '__main__':
    main()
    # st.write(st.secrets['some_key'])

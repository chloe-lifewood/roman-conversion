# app.py

import streamlit as st
from pypinyin import pinyin, Style
from korean_romanizer.romanizer import Romanizer
import cutlet
from unidecode import unidecode

def convert_text(language, text):
    
    if language == 'Chinese':
        result = pinyin(text, style=Style.NORMAL)
        return ' '.join([item[0] for item in result])
    
    elif language == 'Korean':
        return Romanizer(text).romanize()

    elif language == 'Japanese':
        katsu = cutlet.Cutlet()
        result = katsu.romaji(text)
        return result
    elif language == 'Hebrew':
        return unidecode(text)
    
def main():
    st.title('Name Romanizer')
    st.write('Convert names to Roman characters.')

     
    language = st.selectbox('Select language:', ['Chinese', 'Korean', 'Japanese', 'Hebrew'])

    # User input
    user_input = st.text_area("Enter the name/text to convert:")

    if st.button('Convert'):
        result = convert_text(language, user_input)

        st.subheader('Converted Result')
        st.info(result)

if __name__ == '__main__':
    main()

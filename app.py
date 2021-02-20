import streamlit as st
import decipher


cypher_list = ['Atbash Cypher', 'Ceaser Cipher']

def dec_wrap(func, *arg, **kwargs):
    """
    A wrapper to check for value errors. I don't know if this is a good design choice, but it allows me to 
    1. decouple error decipher error handling from streamlit error reporting
    2. avoid repeating the same try-except four times

    """
    try:
        return func(*arg, **kwargs)
    except ValueError:
        st.warning("Make sure your secret message only includes numbers, letters, and punctuation!")


def run():
    """
    Main run method.

    """
    st.header("🔑 Decipher")

    st.write("Decipher any string using a Atbash or Ceasarian cipher!")

    str_in = st.text_input("String to decipher", "Ifmmp!")

    dec_cypher = st.selectbox("Cypher to use", cypher_list, key= "dec")

    if dec_cypher == 'Ceaser Cipher':
        st.write("The rotation refers to the rotation used to encrypt. Thus, if you select 3, you are trying to undo a rotation of 3, which means you want to decrypt 'd' into 'a'")
        rot = st.slider("Cipher Rotation", 0, 26, 13, 1, key='dec')

    decrypt = st.button("Decipher!")

    if decrypt:
        if dec_cypher == 'Atbash Cypher':
                output = dec_wrap(decipher.dec_atbash, str_in) 
                st.write(f"Deciphered text: {output}") 

        elif dec_cypher == "Ceaser Cipher":
                output = dec_wrap(decipher.dec_ceaser, str_in, 26 - rot)
                st.write(f"Deciphered text: {output}")

        
    st.header("🔒 Encrypt")

    st.write("Encrypt any string using a Atbash or Ceasarian cipher!")

    str_in = st.text_input("String to encrypt", "Hello!")

    enc_cypher = st.selectbox("Cypher to use", cypher_list, key = "enc")

    if enc_cypher == "Atbash Cipher":
        st.write("The Atbash Cipher maps the alphabet to it's reverse, so 'a' becomes 'z' and vice versa. This implementation preserves case in its mapping, does not map numbers, spaces, or punctuation, and will not map any non-Ascii character.")

    if enc_cypher == 'Ceaser Cipher':
        st.write("The Ceaser Cipher maps the alphabet to a 'rotation' of the alphabet. In this way, with a Ceaser cipher with rotation of 3 would map 'a' to 'd'. This implementation preserves case, does not map numbers, spaces, or punctuation, and will not map any non-Ascii character. ")

        rot = st.slider("Cipher Rotation", 0, 26, 13, 1, key='enc')

    encrypt = st.button("Encrypt!")

    if encrypt:
        if enc_cypher == 'Atbash Cypher':
                output = dec_wrap(decipher.dec_atbash, str_in)
                st.write(f"Encrypted text: {output}")

        elif enc_cypher == "Ceaser Cipher":

                output = dec_wrap(decipher.dec_ceaser, str_in, rot) 
                st.write(f"Encrypted text: {output}")




if __name__ == "__main__":
    run()
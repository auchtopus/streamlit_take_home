import streamlit as st
import decipher

def run():
    """
    Main run method

    """
    st.header("Decipher")

    st.write("Decipher any string using a Atbash or Ceasarian cipher!")

    str_in = st.text_input("String to decipher", "Ifmmp!")

    cypher = st.selectbox("Cypher to use", ['Atbash Cypher', 'Ceaser Cipher'])

    if cypher == 'Ceaser Cipher':
        rot = st.slider("Cipher Rotation", 0, 26, 13, 1)

    activate = st.button("Decipher!")

    if activate:
        if cypher == 'Atbash Cypher':
            output = decipher.dec_atbash(str_in)
            st.write(f"Deciphered text: {output}")
        elif cypher == "Ceaser Cipher":
            output = decipher.dec_ceaser(str_in, rot)
            st.write(f"Deciphered text: {output}")

        





if __name__ == "__main__":
    run()
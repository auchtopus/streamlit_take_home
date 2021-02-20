"""
App interface. This is entirely frontend; all encryption logic is called from the decipher module

"""
import streamlit as st
import decipher


cipher_list = ['Atbash Cipher', 'Ceasar Cipher']


def dec_wrap(func: callable, *arg, **kwargs) -> str:
    """
    A wrapper to check for value errors. I don't know if this is a good design choice, but it allows me to 
    1. decouple error decipher error handling from streamlit error reporting
    2. avoid repeating the same try-except four times

    Args:
        func: cipher function to call and wrap
        *args: args to pass to the cipher function
        **kwargs: keyword args to pass to the cipher function

    Returns:
        The decrypted or encrypted string

    """
    try:
        return func(*arg, **kwargs)
    except ValueError:
        st.warning(
            "Make sure your secret message only includes numbers, letters, and punctuation!")


def run():
    """
    Main run method. 
    """
    st.header("🔑 Decrypt a secret message...")

    st.subheader("Decrypt any string using an Atbash or Ceasarean cipher!")
    st.write("Enter your encrypted text and hit enter.")
    str_in = st.text_input("String to decrypt", "Svool!")

    dec_cipher = st.selectbox("Cipher to use", cipher_list, key="dec")

    if dec_cipher == cipher_list[0]:
        output = dec_wrap(decipher.dec_atbash, str_in)
        st.write(f"🔑 Decrypted text: **{output}**")

    if dec_cipher == cipher_list[1]:
        st.write("The rotation refers to the rotation used to encrypt. Thus, if you select 3, you are trying to undo a rotation of 3, which means you want to decrypt 'd' into 'a'")
        rot = st.slider("Cipher Rotation", 0, 26, 13, 1, key='dec')
        # 26-rot gives the corresponding decryption to rot
        output = dec_wrap(decipher.dec_ceasar, str_in, 26 - rot)
        st.write(f"🔑 Decrypted text: **{output}**")

    st.header("🔒 Encrypt a secret message...")

    st.subheader("Encrypt any string using an Atbash or Ceasarean cipher!")
    st.write("Enter the message you want to encrypt, and hit enter.")
    str_in = st.text_input("String to encrypt", "Hello!")

    enc_cipher = st.selectbox("Cipher to use", cipher_list, key="enc")

    if enc_cipher == cipher_list[0]:
        st.write("The Atbash Cipher maps the alphabet to it's reverse, so 'a' becomes 'z' and vice versa. This implementation preserves case in its mapping, does not map numbers, spaces, or punctuation, and will not map any non-Ascii character.")
        output = dec_wrap(decipher.dec_atbash, str_in)
        st.write(f"🔒 Encrypted text: **{output}**")

    if enc_cipher == cipher_list[1]:
        st.write("The Ceasar Cipher maps the alphabet to a 'rotation' of the alphabet. In this way, with a Ceasar cipher with rotation of 3 would map 'a' to 'd'. This implementation preserves case, does not map numbers, spaces, or punctuation, and will not map any non-Ascii character.")

        rot = st.slider("Cipher Rotation", 0, 26, 13, 1, key='enc')

        output = dec_wrap(decipher.dec_ceasar, str_in, rot)
        st.write(f"🔒 Encrypted text: **{output}**")


if __name__ == "__main__":
    run()

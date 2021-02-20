# Streamlit Decryption


This is a basic streamlit app that can be used to decrypt and encrypt secret messages using the Atbash and Caesarean ciphers. 

## Setup

Running this app requires python, pip, and streamlit.

Python can be installed [here](https://www.python.org/downloads/). Any version can be used to run the app locally, but deployment requires Python 3.8.7.

Pip should be automatically installed along with Python; if for some reason it is not, go [here](https://pip.pypa.io/en/stable/installing/) to rectify that.

Streamlit is the sole python module required to run the app. 

It can be installed with 

```
pip install streamlit
```
or
```
pip install -r requirements.txt
```

## Startup

To start the app, ensure that streamlit is installed in whatever python environment you are using. Then, nagivate to this directory in your shell and run
```
streamlit run app.py
```

## Usage
The app is a single page app with the decryption utility on top and encryption on the bottom.

To decrypt a message:
1. enter the text you wish to decrypt in the textbox
2. select the appropriate cipher. If you are using the Caeserean cipher, you will be prompted to select the appropriate rotation. The default is 13, which is what is used to decrypt the spec.
3. Hit enter and see your decrypted secret message!

To encrypt a message:
1. enter the text you wish to encrypt in the text box
2. select the appropriate cipher. If you are using the Caeserean cipher, you will be prompted to select the appropriate rotation. The default is 13, which is what is used to decrypt the spec.
3. Hit enter and see your newly encrypted secret message!
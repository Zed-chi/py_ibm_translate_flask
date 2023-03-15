# py_ibm_translate_flask
This is simple server for translating text in french/english.
Based on flask

Hello guys, due to accout activation problem i've made it with "translators" package instead. 
Thank you)

### Requirements:
* python 3.7

### Installation:
`pip install -r requirements.txt`

### Starting:
`python3 server.py`

So API consist two routes:
* `/englishToFrench`
* `/frenchToEnglish`

All you have to do is to push POST request with `{"text":...}` data.

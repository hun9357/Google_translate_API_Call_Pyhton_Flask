import os
from google.cloud import translate_v2 as translate
from flask import Flask,request,jsonify

app = Flask(__name__)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\hun93\Desktop\TranslationAPI\tough-canto-289818-edd52a549c0f.json"


@app.route('/api',methods=['GET'])
def translate_word():
   translate_client = translate.Client()

   d={}

   text = str(request.args['Word'])
   target = 'ko'

   output = translate_client.translate(
       text,
       target_language=target
   )
   d[text] = str(output)

   return jsonify(d)

if __name__ == '__main__':
    app.run()
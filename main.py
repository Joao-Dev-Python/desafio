from flask import Flask,jsonify,request
from flask_restful import reqparse
from flask_cors import CORS
import  os, base64

message = "Em terra de quem tem um olho e rei"
print(message)
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')
print(base64_message)



path_params = reqparse.RequestParser()
path_params.add_argument('r', type=str)
app = Flask(__name__)
CORS(app)

@app.route("/pro",methods = ['GET'])
def pro():
    return jsonify({
        "instrucao" : """Preste muita atencao 'vc tera que descriptografar a mensagem da chave DESAFIO com base64 corrigi-la e manda de volta no endpoint  ?r=  encriptografada em base64' na rota \resp. Antes de encriptografar removatodos todos os espacos e nao use caracter especial caso contrario retornara um erro """,
        
        "DESAFIO": base64_message})
    
    
    

@app.route('/resp', methods=["GET"])
def resp():
    data =   path_params.parse_args()
    if(data["r"] == "RW10ZXJyYWRlY2Vnb3F1ZW10ZW11bW9saG9lcmVp"):
        return jsonify({
            "message" : "muito bem aguarde o proximo desafio",
            "resp" : data["r"]
            }), 201
    return jsonify({
        "message" : "Vc nao fez correto"
    })
    



if __name__== '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host="0.0.0.0",port=port)
#,host="0.0.0.0"






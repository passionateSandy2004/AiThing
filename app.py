from flask import Flask, request, jsonify, send_file
from TextGen import GenText2
from pptMake import GenPPT
from PPTPicker import PickPPT
from DefaultData import SetDefaultData
import FilterSearch
import os 
import WebMaker

# Initialize Flask app
app = Flask(__name__)

@app.route('/generate_ppt', methods=['POST'])
def generate_ppt():
    data = request.json  # Get the input data from POST request
    user_input = data.get('user_input', '')
    style=data.get('Style', '')
    topic=data.get('Topic', '')
    tm1=data.get('TeamM1','')
    tm2=data.get('TeamM2','')
    tm3=data.get('TeamM3','')
    adderss=data.get('Address','')
    mail=data.get('Contact mail','')
    #PPT Picker(style) and get the PPT
    ppt,slideInfo=PickPPT(style)  
    
    outputFile=os.path.join(os.getcwd(), "temp.pptx")
    if not user_input:
        return jsonify({"error": "No user input provided."}), 400
    details=SetDefaultData(GenText2(user_input,slideInfo["Blength"],slideInfo["Clength"]),topic,tm1,tm2,tm3,adderss,mail)
    genrated=GenPPT(ppt,outputFile,details)
    if genrated:
        return send_file(outputFile, as_attachment=True, download_name="updated_pitch_deck.pptx")
    else:
        return False
@app.route("/getInvestor",methods=['POST'])
def getInvestor():
    data = request.json  # Get the input data from POST request
    user_input = data.get('user_input', '')
    matches=FilterSearch.generate_funding_recommendation(user_input)
    return matches

@app.route("/makeWeb",methods=['POST'])
def makeWeb():
    data = request.json  # Get the input data from POST request
    user_input = data.get('user_input', '')
    outputFile=os.path.join(os.getcwd(), "index.html")
    code=WebMaker.makeBody(outputFile,user_input)
    return send_file(outputFile, as_attachment=True, download_name="index.html")

if __name__ == '__main__':
    # Run the app
    app.run(debug=True, port=5001)

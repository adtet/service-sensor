import json
from flask import Flask,jsonify,request
from sqllib import input_data_sensor

app = Flask(__name__)

@app.route('/sensor/input/data',methods=['POST'])
def data_input():
    json_data = request.json
    if json_data==None:
        result = {"message": "process failed"}
        resp = jsonify(result)
        return resp, 400
    else:
        if 'A' not in json_data or 'B' not in json_data or 'C' not in json_data or 'D' not in json_data or 'E' not in json_data or 'F' not in json_data or 'G' not in json_data or 'H' not in json_data or 'I' not in json_data or 'J' not in json_data or 'K' not in json_data or 'L' not in json_data or 'M' not in json_data or 'N' not in json_data or 'O' not in json_data or 'P' not in json_data or 'Q' not in json_data or 'R' not in json_data:
            result = {"message": "error request"}
            resp = jsonify(result)
            return resp, 401
        else:
            A = json_data['A']
            B = json_data['B']
            C = json_data['C']
            D = json_data['D']
            E = json_data['E']
            F = json_data['F']
            G = json_data['G']
            H = json_data['H']
            I = json_data['I']
            J = json_data['J']
            K = json_data['K']
            L = json_data['L']
            M = json_data['M']
            N = json_data['N']
            O = json_data['O']
            P = json_data['P']
            Q = json_data['Q']
            R = json_data['R']
            input_data_sensor(A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R)
            result = {"message": "Input Success"}
            resp = jsonify(result)
            return resp, 202


if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=5000)
    app.run(port=5000, debug=True)
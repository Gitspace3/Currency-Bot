from flask import Flask,request,jsonify
import requests

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']


    final_amount = fetch_conversion_factor(source_currency,target_currency,amount)

    response = {
        'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,final_amount,target_currency)
    }
    return jsonify(response)


def fetch_conversion_factor(source,target,amount):
    url = "https://api.fastforex.io/convert?from={}&to={}&amount={}&api_key=80d3951200-d9a5d66ca0-sjg0k9".format(source,target,amount)

    response = requests.get(url)
    response = response.json()
    return response['result']['{}'.format(target)]


if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0', port=5000)

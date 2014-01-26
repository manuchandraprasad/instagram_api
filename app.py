from flask import Flask, jsonify, request, make_response
import requests,urllib,re
from kombu import Connection, Exchange, Queue

app = Flask(__name__)

CLIENT_ID = 'e52abe5fd68349ffa7a7ef3d3d7c84bf'
REGEX_IMAGE = re.compile('\.com\/(.+\.jpg)')
blog_exchange = Exchange('instagram', 'direct', durable=True)
url_queue = Queue('instagram', exchange=blog_exchange, routing_key='instagram')

@app.route("/", methods=['POST', 'GET'])
def hello():
    try:
        print request.json
        print request.content_type
        return jsonify({'post': 'Success'})
    except:
        return jsonify({'post': 'Fail'})


@app.route("/url", methods=['GET', 'POST'])
def verify():
    if request.method == 'GET':
        d = request.args.get('hub.challenge')
        return make_response(d)
    else:
        events = request.json
        add_to_queue(events)           
        return jsonify({'data': 'Success'})

def add_to_queue(data):
    with Connection('redis://192.168.1.8//') as conn:
        producer = conn.Producer(serializer='json')
        producer.publish(data, exchange=blog_exchange, routing_key='instagram',
                        declare=[url_queue])

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5678)

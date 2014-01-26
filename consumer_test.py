from kombu import Connection, Exchange, Queue
import requests,urllib,re
from pprint import pprint
CLIENT_ID = 'e52abe5fd68349ffa7a7ef3d3d7c84bf'
REGEX_IMAGE = re.compile('\.com\/(.+\.jpg)')

blog_exchange = Exchange('instagram', 'direct', durable=True)
url_queue = Queue('instagram', exchange=blog_exchange, routing_key='instagram')

def download_image(body, message):
    for event in body:
        url = 'https://api.instagram.com/v1/%(object)ss/%(object_id)s/media/recent?client_id=%(client_id)s' % {
            'client_id': CLIENT_ID, 'object_id': event['object_id'],'object':event['object']}
        pprint(event)
        api_data = requests.get(url)
        data = api_data.json()['data']
        for item in data:
            img_url = item['images']['standard_resolution']['url']
            filename = REGEX_IMAGE.findall(img_url)
            print "[DOWNLOADING] %s"%filename
            urllib.urlretrieve(img_url,'images/%s'%filename[0])
    message.ack()

# connections
with Connection('redis://192.168.1.8//') as conn:
    with conn.Consumer(url_queue, callbacks=[download_image]) as consumer:
        # Process messages and handle events on all channels
        while True:
            conn.drain_events()
curl -F 'client_id=e52abe5fd68349ffa7a7ef3d3d7c84bf' \
     -F 'client_secret=c0243b601d3446629215b580c43bb983' \
     -F 'object=user' \
     -F 'aspect=media' \
     -F 'verify_token=myVerifyToken' \
     -F 'callback_url=http://chat.quadloops.com:5678/url' \
     https://api.instagram.com/v1/subscriptions/


curl -F 'client_id=e52abe5fd68349ffa7a7ef3d3d7c84bf' \
     -F 'client_secret=c0243b601d3446629215b580c43bb983' \
     -F 'object=geography' \
     -F 'aspect=media' \
     -F 'lat=35.657872' \
     -F 'lng=139.70232' \
     -F 'radius=1000' \
     -F 'callback_url=http://chat.quadloops.com:5678/url' \
     https://api.instagram.com/v1/subscriptions/

curl -F 'client_id=e52abe5fd68349ffa7a7ef3d3d7c84bf' \
     -F 'client_secret=c0243b601d3446629215b580c43bb983' \
     -F 'object=tag' \
     -F 'aspect=media' \
     -F 'object_id=nofilter' \
     -F 'callback_url=http://chat.quadloops.com:5678/url' \
     https://api.instagram.com/v1/subscriptions/
     
curl -X DELETE 'https://api.instagram.com/v1/subscriptions?client_secret=c0243b601d3446629215b580c43bb983&object=all&client_id=e52abe5fd68349ffa7a7ef3d3d7c84bf'
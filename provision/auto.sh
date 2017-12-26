vagrant up --provider=azure

fab -i key.pem -H ubuntu@DNS instalacion
fab -i key.pem -H ubuntu@DNS servicios


from APISureConnector.apisureconnector import APISureConnector
import json
from datetime import datetime
from pprint import pp

if __name__ == '__main__':
    connector = APISureConnector(client_id="gAtxkHbIAwDOHnSTajn0p0tN4V6Yhk1B",
                                 client_secret="80OdKmebSkWlpkGP")

    url = 'https://api.apisure.io/mapi_base/v1/Guarantee/Guarantee/Apply'
    filename = 'guarantee_sample.json'

    with open(filename) as file:
        data = json.load(file)

    data["GuaranteeApplicationDetails"]["PartyReference"]["ApplicantReference"] = datetime.now().strftime("%m%d%Y")

    response = connector.send_request(url=url, data=data)

    print(response)
    pp(response.json())

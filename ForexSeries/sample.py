import oandapyV20
import oandapyV20.endpoints.forexlabs as labs
import oandapyV20.endpoints.pricing as pricing
import json

accountID = "101-002-7031957-001"
token = "aa7bb80db50d544e569084df3ab7796c-6c1595a45cf1ce91755298f21cb4153b"

api = oandapyV20.API(access_token=token)

params = {
    "instruments": "EUR_USD,EUR_JPY"
}

r = pricing.PricingStream(accountID=accountID, params=params)
rv = api.request(r)
maxrecs = 100
for ticks in rv:
    print (json.dumps(ticks, indent=4),",")
    if maxrecs == 0:
        r.terminate("maxrecs records received")
# print (rv)
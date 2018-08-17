import oandapyV20
import oandapyV20.endpoints.forexlabs as labs
import oandapyV20.endpoints.pricing as pricing
import oandapyV20.endpoints.instruments as instruments
import json


accountID = "101-002-7031957-001"
token = "aa7bb80db50d544e569084df3ab7796c-6c1595a45cf1ce91755298f21cb4153b"

api = oandapyV20.API(access_token=token)

params = {
  "count": 2,
  "granularity": "H1"
}

r = instruments.InstrumentsCandles(instrument="DE30_EUR",
                                   params=params)

api.request(r)
print (r.response['candles'])
# for candle in r.response['candles']:
#     print (candle['mid']['c'])
# print (json.dumps(r.response.candles.mid, indent=2))



# def SMA(n):
#     return 
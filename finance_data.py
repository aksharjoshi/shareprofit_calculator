from yahoo_finance import Share
import datetime
import requests
import sys
from decimal import Decimal

def get_symbol(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)

    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        if x['symbol'] == symbol:
            return x['name']


def get_info_share(symbol):
	#print symbol
	#symbol = sys.argv[1]
	share1 = Share(symbol)
	try:
		share1.get_info()
		if not share1:# is None:
			print symbol," is not a valid share symbol. \nPlease re-run the program with correct share symbol"
		else:
			#print "here"
			print(datetime.datetime.now())
			company = get_symbol(symbol)
			print company
			print share1.get_price()
			print share1.get_change()
			#print share1.get_short_ratio()
			open = share1.get_open()
			price = share1.get_price()
			percChange = float(Decimal(price) - Decimal(open))/float(Decimal(open))
			print "%f" % percChange +"%" 
			
	except Exception as e:
		print symbol," is not a valid share symbol. \nPlease re-run the program with correct share symbol"
	except AttributeError as ae: 
		print "att error"
	except yahoo_finance.YQLQueryError as ye:
			print symbol," is not a valid share symbol in ye error. \nPlease re-run the program with correct share symbol"



if __name__ == "__main__":
	get_info_share()

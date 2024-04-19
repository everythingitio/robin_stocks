import robin_stocks.robinhood as r
import os
import json

rs_email = os.getenv('rh_email')
rh_pass = os.getenv('rh_pass')
print('rs_email:', rs_email)
print('rh_pass: ****')
login = r.login(os.getenv('rh_email'),os.getenv('rh_pass'))
print(json.dumps(login, indent=4))

symbol='SINT'
quantity=1
time_in_force='gfd'

# order = r.order_buy_market(symbol, quantity, jsonify=True)
# print(json.dumps(order, indent=4))
# buy_market_order_id = order['id']
# buy_market_order_price = order['price']

print(json.dumps(r.get_stock_order_info('6622cddc-0f26-4c2f-96a7-576516ac3683'), indent=4))

# print(json.dumps(r.get_all_open_stock_orders(), indent=4))

# print(json.dumps(r.cancel_stock_order('6622cddc-0f26-4c2f-96a7-576516ac3683'), indent=4))

# order = r.order_sell_stop_loss(symbol, quantity, 0.0414, account_number=None, timeInForce='gfd', extendedHours=False, jsonify=True)
# print(json.dumps(order, indent=4))

# order_sell = r.order_sell_market(symbol, quantity, timeInForce='gfd', jsonify=True)
# print(json.dumps(order_sell, indent=4))


# limitPrice = r.get_latest_price_adjusted(symbol, 0.02, priceType=None, includeExtendedHours=True)
# order_buy_limit_ext = r.order_buy_limit(symbol, quantity, limitPrice[0], timeInForce='gfd', extendedHours=True, jsonify=True,  market_hours='extended_hours')
# print(json.dumps(order_buy_limit_ext, indent=4))

limitPrice = r.get_latest_price_adjusted(symbol, -0.02, priceType=None, includeExtendedHours=True)
order_sell_limit_ext =  r.order_sell_limit(symbol, quantity, limitPrice[0], account_number=None, timeInForce='gfd', extendedHours=True, jsonify=True, market_hours='extended_hours')
print(json.dumps(order_sell_limit_ext, indent=4))



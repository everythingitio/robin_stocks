```
cd /Users/oketo/Downloads/robin_stocks_fix/robin_stocks

virtualenv /Users/oketo/Downloads/robin_stocks_fix/env
source /Users/oketo/Downloads/robin_stocks_fix/env/bin/activate

cd /Users/oketo/Downloads/robin_stocks_fix/robin_stocks

pip install -r requirements.txt 

use HTTP Toolkit instead of Fiddler

python


import robin_stocks.robinhood as r
login = r.login('','')

r.build_holdings()
{'SINT': {'price': '0.044200', 'quantity': '1.00000000', 'average_buy_price': '0.0400', 'equity': '0.04', 'percent_change': '10.50', 'intraday_percent_change': '10.50', 'equity_change': '0.004200', 'type': 'stock', 'name': 'SiNtx', 'id': '921be484-02df-485a-9c67-12ab6ee36783', 'pe_ratio': '-0.020000', 'percentage': '10.94'}}


def order_sell_stop_loss(symbol, quantity, stopPrice, account_number=None, timeInForce='gtc', extendedHours=False, jsonify=True):
    """Submits a stop order to be turned into a market order once a certain stop price is reached.


r.order_sell_stop_loss('SINT', 1, 0.04, account_number=None, timeInForce='gtc', extendedHours=False, jsonify=True)
TypeError: can only concatenate str (not "float") to str

r.order(symbol, quantity, "sell", account_number, None, stopPrice, timeInForce, extendedHours, jsonify)

r.order('SINT', 1, "sell", None, None, 0.04, timeInForce='gtc', extendedHours=False, jsonify=True)
TypeError: can only concatenate str (not "float") to str

@login_required
def order(symbol, quantity, side, limitPrice=None, stopPrice=None, account_number=None, timeInForce='gtc', extendedHours=False, jsonify=True, market_hours='regular_hours'):
    """A generic order function.

{'non_field_errors': ['Stop limit order requested, but no stop price provided.']}


stop sell

{
  "account": "https://api.robinhood.com/accounts/5RZ07024/",
  "ask_price": "0.045100",
  "bid_ask_timestamp": "2024-04-19T17:25:59Z",
  "bid_price": "0.045000",
  "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
  "quantity": "1",
  "market_hours": "regular_hours",
  "order_form_version": 4,
  "ref_id": "70973b95-1db1-4a1f-baab-9164ec7f21b2",
  "side": "sell",
  "symbol": "SINT",
  "time_in_force": "gfd",
  "trigger": "stop",
  "type": "market",
  "stop_price": "0.0400"
}

code 

sell stop loss order

{
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "symbol": "SINT",
    "price": null,
    "quantity": 1,
    "ref_id": "f52f1800-f053-4396-a277-303947071ecb",
    "type": "market",
    "stop_price": 0.04,
    "time_in_force": "gtc",
    "trigger": "stop",
    "side": "sell",
    "market_hours": "regular_hours",
    "extended_hours": false,
    "order_form_version": 4
}
{
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "symbol": "SINT",
    "quantity": 1,
    "ref_id": "f52f1800-f053-4396-a277-303947071ecb",
    "type": "market",
    "time_in_force": "gtc",
    "trigger": "stop",
    "side": "sell",
    "market_hours": "regular_hours",
    "order_form_version": 4
}

after fixing. {'detail': 'Not enough shares to sell.'}

market_order

{
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "symbol": "SINT",
    "price": 0.0435,
    "quantity": 1,
    "ref_id": "026dbdfe-0564-4942-9ced-74edf7d3ab54",
    "type": "market",
    "stop_price": null,
    "time_in_force": "gtc",
    "trigger": "immediate",
    "side": "buy",
    "market_hours": "regular_hours",
    "extended_hours": false,
    "order_form_version": 4
}

{
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "symbol": "SINT",
    "price": 0.0435,
    "quantity": 1,
    "ref_id": "026dbdfe-0564-4942-9ced-74edf7d3ab54",
    "type": "limit",
    "stop_price": null,
    "time_in_force": "gtc",
    "trigger": "immediate",
    "side": "buy",
    "market_hours": "regular_hours",
    "order_form_version": 4,
    "preset_percent_limit": "0.05"
}


{'id': '6622bc70-c063-4d68-b33e-0ab27a28ce97', 'ref_id': '026dbdfe-0564-4942-9ced-74edf7d3ab54', 'url': 'https://api.robinhood.com/orders/6622bc70-c063-4d68-b33e-0ab27a28ce97/', 'account': 'https://api.robinhood.com/accounts/5RZ07024/', 'user_uuid': '2f6cd410-6d32-4a58-9376-eea3c55a5f9c', 'position': 'https://api.robinhood.com/positions/5RZ07024/921be484-02df-485a-9c67-12ab6ee36783/', 'cancel': 'https://api.robinhood.com/orders/6622bc70-c063-4d68-b33e-0ab27a28ce97/cancel/', 'instrument': 'https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/', 'instrument_id': '921be484-02df-485a-9c67-12ab6ee36783', 'cumulative_quantity': '0.00000000', 'average_price': None, 'fees': '0.00', 'state': 'unconfirmed', 'pending_cancel_open_agent': None, 'type': 'limit', 'side': 'buy', 'time_in_force': 'gtc', 'trigger': 'immediate', 'price': '0.04350000', 'stop_price': None, 'quantity': '1.00000000', 'reject_reason': None, 'created_at': '2024-04-19T18:48:16.284479Z', 'updated_at': '2024-04-19T18:48:16.284500Z', 'last_transaction_at': '2024-04-19T18:48:16.284479Z', 'executions': [], 'extended_hours': False, 'market_hours': 'regular_hours', 'override_dtbp_checks': False, 'override_day_trade_checks': False, 'response_category': None, 'stop_triggered_at': None, 'last_trail_price': None, 'last_trail_price_updated_at': None, 'last_trail_price_source': None, 'dollar_based_amount': None, 'total_notional': {'amount': '0.05', 'currency_code': 'USD', 'currency_id': '1072fc76-1862-41ab-82c2-485837590762'}, 'executed_notional': None, 'investment_schedule_id': None, 'is_ipo_access_order': False, 'ipo_access_cancellation_reason': None, 'ipo_access_lower_collared_price': None, 'ipo_access_upper_collared_price': None, 'ipo_access_upper_price': None, 'ipo_access_lower_price': None, 'is_ipo_access_price_finalized': False, 'is_visible_to_user': True, 'has_ipo_access_custom_price_limit': False, 'is_primary_account': True, 'order_form_version': 4, 'preset_percent_limit': '0.050000', 'order_form_type': 'all_day_trading_v1_2', 'last_update_version': -1, 'placed_agent': 'user'}


--------

print(json.dumps(r.get_stock_order_info('6622bc70-c063-4d68-b33e-0ab27a28ce97'), indent=4))

{
    "id": "6622bc70-c063-4d68-b33e-0ab27a28ce97",
    "ref_id": "026dbdfe-0564-4942-9ced-74edf7d3ab54",
    "url": "https://api.robinhood.com/orders/6622bc70-c063-4d68-b33e-0ab27a28ce97/",
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "user_uuid": "2f6cd410-6d32-4a58-9376-eea3c55a5f9c",
    "position": "https://api.robinhood.com/positions/5RZ07024/921be484-02df-485a-9c67-12ab6ee36783/",
    "cancel": null,
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "instrument_id": "921be484-02df-485a-9c67-12ab6ee36783",
    "cumulative_quantity": "1.00000000",
    "average_price": "0.04000000",
    "fees": "0.00",
    "state": "filled",
    "pending_cancel_open_agent": null,
    "type": "limit",
    "side": "buy",
    "time_in_force": "gtc",
    "trigger": "immediate",
    "price": "0.04350000",
    "stop_price": null,
    "quantity": "1.00000000",
    "reject_reason": null,
    "created_at": "2024-04-19T18:48:16.284479Z",
    "updated_at": "2024-04-19T18:48:16.672741Z",
    "last_transaction_at": "2024-04-19T18:48:16.476000Z",
    "executions": [
        {
            "price": "0.04349900",
            "quantity": "1.00000000",
            "rounded_notional": "0.04000000",
            "settlement_date": "2024-04-23",
            "timestamp": "2024-04-19T18:48:16.476000Z",
            "id": "6622bc70-99f7-4f9d-ab30-9bef818e5740",
            "ipo_access_execution_rank": null,
            "trade_execution_date": "2024-04-19"
        }
    ],
    "extended_hours": false,
    "market_hours": "regular_hours",
    "override_dtbp_checks": false,
    "override_day_trade_checks": false,
    "response_category": null,
    "stop_triggered_at": null,
    "last_trail_price": null,
    "last_trail_price_updated_at": null,
    "last_trail_price_source": null,
    "dollar_based_amount": null,
    "total_notional": {
        "amount": "0.05",
        "currency_code": "USD",
        "currency_id": "1072fc76-1862-41ab-82c2-485837590762"
    },
    "executed_notional": {
        "amount": "0.04",
        "currency_code": "USD",
        "currency_id": "1072fc76-1862-41ab-82c2-485837590762"
    },
    "investment_schedule_id": null,
    "is_ipo_access_order": false,
    "ipo_access_cancellation_reason": null,
    "ipo_access_lower_collared_price": null,
    "ipo_access_upper_collared_price": null,
    "ipo_access_upper_price": null,
    "ipo_access_lower_price": null,
    "is_ipo_access_price_finalized": false,
    "is_visible_to_user": true,
    "has_ipo_access_custom_price_limit": false,
    "is_primary_account": true,
    "order_form_version": 4,
    "preset_percent_limit": "0.050000",
    "order_form_type": "all_day_trading_v1_2",
    "last_update_version": 2,
    "placed_agent": "user"
}

--------
print(json.dumps(r.cancel_stock_order('6622bc70-c063-4d68-b33e-0ab27a28ce97'), indent=4))



Order 6622bc70-c063-4d68-b33e-0ab27a28ce97 cancelled
{
    "detail": "Order cannot be cancelled at this time."
}

-------

fixed but other triggered too

symbol='SINT'
quantity=1
time_in_force='gfd'
order = r.order_buy_market(symbol, quantity, jsonify=True)
print(order)
buy_market_order_id = order['id']
buy_market_order_price = order['price']



{
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "symbol": "SINT",
    "price": 0.0424,
    "quantity": 1,
    "ref_id": "a268eb93-4cad-4d12-85af-09888f87b91a",
    "type": "market",
    "stop_price": null,
    "time_in_force": "gtc",
    "trigger": "immediate",
    "side": "buy",
    "market_hours": "regular_hours",
    "extended_hours": false,
    "order_form_version": 4
}
{
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "symbol": "SINT",
    "price": 0.0424,
    "quantity": 1,
    "ref_id": "a268eb93-4cad-4d12-85af-09888f87b91a",
    "type": "limit",
    "time_in_force": "gtc",
    "trigger": "immediate",
    "side": "buy",
    "market_hours": "regular_hours",
    "order_form_version": 4,
    "preset_percent_limit": "0.05"
}


{'id': '6622c2f1-4937-4f9b-8f1c-54fab3fddf9f', 'ref_id': 'a268eb93-4cad-4d12-85af-09888f87b91a', 'url': 'https://api.robinhood.com/orders/6622c2f1-4937-4f9b-8f1c-54fab3fddf9f/', 'account': 'https://api.robinhood.com/accounts/5RZ07024/', 'user_uuid': '2f6cd410-6d32-4a58-9376-eea3c55a5f9c', 'position': 'https://api.robinhood.com/positions/5RZ07024/921be484-02df-485a-9c67-12ab6ee36783/', 'cancel': 'https://api.robinhood.com/orders/6622c2f1-4937-4f9b-8f1c-54fab3fddf9f/cancel/', 'instrument': 'https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/', 'instrument_id': '921be484-02df-485a-9c67-12ab6ee36783', 'cumulative_quantity': '0.00000000', 'average_price': None, 'fees': '0.00', 'state': 'unconfirmed', 'pending_cancel_open_agent': None, 'type': 'limit', 'side': 'buy', 'time_in_force': 'gtc', 'trigger': 'immediate', 'price': '0.04240000', 'stop_price': None, 'quantity': '1.00000000', 'reject_reason': None, 'created_at': '2024-04-19T19:16:01.853705Z', 'updated_at': '2024-04-19T19:16:01.853718Z', 'last_transaction_at': '2024-04-19T19:16:01.853705Z', 'executions': [], 'extended_hours': False, 'market_hours': 'regular_hours', 'override_dtbp_checks': False, 'override_day_trade_checks': False, 'response_category': None, 'stop_triggered_at': None, 'last_trail_price': None, 'last_trail_price_updated_at': None, 'last_trail_price_source': None, 'dollar_based_amount': None, 'total_notional': {'amount': '0.05', 'currency_code': 'USD', 'currency_id': '1072fc76-1862-41ab-82c2-485837590762'}, 'executed_notional': None, 'investment_schedule_id': None, 'is_ipo_access_order': False, 'ipo_access_cancellation_reason': None, 'ipo_access_lower_collared_price': None, 'ipo_access_upper_collared_price': None, 'ipo_access_upper_price': None, 'ipo_access_lower_price': None, 'is_ipo_access_price_finalized': False, 'is_visible_to_user': True, 'has_ipo_access_custom_price_limit': False, 'is_primary_account': True, 'order_form_version': 4, 'preset_percent_limit': '0.050000', 'order_form_type': 'all_day_trading_v1_2', 'last_update_version': -1, 'placed_agent': 'user'}

Status filled

{
    "id": "6622c2f1-4937-4f9b-8f1c-54fab3fddf9f",
    "ref_id": "a268eb93-4cad-4d12-85af-09888f87b91a",
    "url": "https://api.robinhood.com/orders/6622c2f1-4937-4f9b-8f1c-54fab3fddf9f/",
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "user_uuid": "2f6cd410-6d32-4a58-9376-eea3c55a5f9c",
    "position": "https://api.robinhood.com/positions/5RZ07024/921be484-02df-485a-9c67-12ab6ee36783/",
    "cancel": null,
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "instrument_id": "921be484-02df-485a-9c67-12ab6ee36783",
    "cumulative_quantity": "1.00000000",
    "average_price": "0.04000000",
    "fees": "0.00",
    "state": "filled",
    "pending_cancel_open_agent": null,
    "type": "limit",
    "side": "buy",
    "time_in_force": "gtc",
    "trigger": "immediate",
    "price": "0.04240000",
    "stop_price": null,
    "quantity": "1.00000000",
    "reject_reason": null,
    "created_at": "2024-04-19T19:16:01.853705Z",
    "updated_at": "2024-04-19T19:16:02.274544Z",
    "last_transaction_at": "2024-04-19T19:16:02.123000Z",
    "executions": [
        {
            "price": "0.04220000",
            "quantity": "1.00000000",
            "rounded_notional": "0.04000000",
            "settlement_date": "2024-04-23",
            "timestamp": "2024-04-19T19:16:02.123000Z",
            "id": "6622c2f2-8c99-491b-b476-a0caa90334b9",
            "ipo_access_execution_rank": null,
            "trade_execution_date": "2024-04-19"
        }
    ],
    "extended_hours": false,
    "market_hours": "regular_hours",
    "override_dtbp_checks": false,
    "override_day_trade_checks": false,
    "response_category": null,
    "stop_triggered_at": null,
    "last_trail_price": null,
    "last_trail_price_updated_at": null,
    "last_trail_price_source": null,
    "dollar_based_amount": null,
    "total_notional": {
        "amount": "0.05",
        "currency_code": "USD",
        "currency_id": "1072fc76-1862-41ab-82c2-485837590762"
    },
    "executed_notional": {
        "amount": "0.04",
        "currency_code": "USD",
        "currency_id": "1072fc76-1862-41ab-82c2-485837590762"
    },
    "investment_schedule_id": null,
    "is_ipo_access_order": false,
    "ipo_access_cancellation_reason": null,
    "ipo_access_lower_collared_price": null,
    "ipo_access_upper_collared_price": null,
    "ipo_access_upper_price": null,
    "ipo_access_lower_price": null,
    "is_ipo_access_price_finalized": false,
    "is_visible_to_user": true,
    "has_ipo_access_custom_price_limit": false,
    "is_primary_account": true,
    "order_form_version": 4,
    "preset_percent_limit": "0.050000",
    "order_form_type": "all_day_trading_v1_2",
    "last_update_version": 2,
    "placed_agent": "user"
}

----------

stop sell

quantity=2
order = r.order_sell_stop_loss(symbol, quantity, 0.0414, account_number=None, timeInForce='gtc', extendedHours=False, jsonify=True)
print(json.dumps(order, indent=4))

"state": "unconfirmed",

{
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "symbol": "SINT",
    "price": null,
    "quantity": 2,
    "ref_id": "5453da6a-8e2f-4fa0-b60f-1e55d0edc2f3",
    "type": "market",
    "stop_price": 0.0414,
    "time_in_force": "gtc",
    "trigger": "stop",
    "side": "sell",
    "market_hours": "regular_hours",
    "extended_hours": false,
    "order_form_version": 4
}
{
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "symbol": "SINT",
    "quantity": 2,
    "ref_id": "5453da6a-8e2f-4fa0-b60f-1e55d0edc2f3",
    "type": "market",
    "stop_price": 0.0414,
    "time_in_force": "gtc",
    "trigger": "stop",
    "side": "sell",
    "market_hours": "regular_hours",
    "order_form_version": 4
}
{
    "id": "6622c93f-9f22-4610-b6b4-1e42fe560433",
    "ref_id": "5453da6a-8e2f-4fa0-b60f-1e55d0edc2f3",
    "url": "https://api.robinhood.com/orders/6622c93f-9f22-4610-b6b4-1e42fe560433/",
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "user_uuid": "2f6cd410-6d32-4a58-9376-eea3c55a5f9c",
    "position": "https://api.robinhood.com/positions/5RZ07024/921be484-02df-485a-9c67-12ab6ee36783/",
    "cancel": "https://api.robinhood.com/orders/6622c93f-9f22-4610-b6b4-1e42fe560433/cancel/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "instrument_id": "921be484-02df-485a-9c67-12ab6ee36783",
    "cumulative_quantity": "0.00000000",
    "average_price": null,
    "fees": "0.00",
    "state": "unconfirmed",
    "pending_cancel_open_agent": null,
    "type": "market",
    "side": "sell",
    "time_in_force": "gtc",
    "trigger": "stop",
    "price": null,
    "stop_price": "0.04140000",
    "quantity": "2.00000000",
    "reject_reason": null,
    "created_at": "2024-04-19T19:42:55.694395Z",
    "updated_at": "2024-04-19T19:42:55.694407Z",
    "last_transaction_at": "2024-04-19T19:42:55.694395Z",
    "executions": [],
    "extended_hours": false,
    "market_hours": "regular_hours",
    "override_dtbp_checks": false,
    "override_day_trade_checks": false,
    "response_category": null,
    "stop_triggered_at": null,
    "last_trail_price": null,
    "last_trail_price_updated_at": null,
    "last_trail_price_source": null,
    "dollar_based_amount": null,
    "total_notional": null,
    "executed_notional": null,
    "investment_schedule_id": null,
    "is_ipo_access_order": false,
    "ipo_access_cancellation_reason": null,
    "ipo_access_lower_collared_price": null,
    "ipo_access_upper_collared_price": null,
    "ipo_access_upper_price": null,
    "ipo_access_lower_price": null,
    "is_ipo_access_price_finalized": false,
    "is_visible_to_user": true,
    "has_ipo_access_custom_price_limit": false,
    "is_primary_account": true,
    "order_form_version": 4,
    "preset_percent_limit": null,
    "order_form_type": "all_day_trading_v1_2",
    "last_update_version": -1,
    "placed_agent": "user"
}

 "state": "confirmed",

{
    "id": "6622c93f-9f22-4610-b6b4-1e42fe560433",
    "ref_id": "5453da6a-8e2f-4fa0-b60f-1e55d0edc2f3",
    "url": "https://api.robinhood.com/orders/6622c93f-9f22-4610-b6b4-1e42fe560433/",
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "user_uuid": "2f6cd410-6d32-4a58-9376-eea3c55a5f9c",
    "position": "https://api.robinhood.com/positions/5RZ07024/921be484-02df-485a-9c67-12ab6ee36783/",
    "cancel": "https://api.robinhood.com/orders/6622c93f-9f22-4610-b6b4-1e42fe560433/cancel/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "instrument_id": "921be484-02df-485a-9c67-12ab6ee36783",
    "cumulative_quantity": "0.00000000",
    "average_price": null,
    "fees": "0.00",
    "state": "confirmed",
    "pending_cancel_open_agent": null,
    "type": "market",
    "side": "sell",
    "time_in_force": "gtc",
    "trigger": "stop",
    "price": null,
    "stop_price": "0.04140000",
    "quantity": "2.00000000",
    "reject_reason": null,
    "created_at": "2024-04-19T19:42:55.694395Z",
    "updated_at": "2024-04-19T19:42:56.256373Z",
    "last_transaction_at": "2024-04-19T19:42:55.912000Z",
    "executions": [],
    "extended_hours": false,
    "market_hours": "regular_hours",
    "override_dtbp_checks": false,
    "override_day_trade_checks": false,
    "response_category": null,
    "stop_triggered_at": null,
    "last_trail_price": null,
    "last_trail_price_updated_at": null,
    "last_trail_price_source": null,
    "dollar_based_amount": null,
    "total_notional": null,
    "executed_notional": null,
    "investment_schedule_id": null,
    "is_ipo_access_order": false,
    "ipo_access_cancellation_reason": null,
    "ipo_access_lower_collared_price": null,
    "ipo_access_upper_collared_price": null,
    "ipo_access_upper_price": null,
    "ipo_access_lower_price": null,
    "is_ipo_access_price_finalized": false,
    "is_visible_to_user": true,
    "has_ipo_access_custom_price_limit": false,
    "is_primary_account": true,
    "order_form_version": 4,
    "preset_percent_limit": null,
    "order_form_type": "all_day_trading_v1_2",
    "last_update_version": 1,
    "placed_agent": "user"
}

  "state": "filled",

{
    "id": "6622c93f-9f22-4610-b6b4-1e42fe560433",
    "ref_id": "5453da6a-8e2f-4fa0-b60f-1e55d0edc2f3",
    "url": "https://api.robinhood.com/orders/6622c93f-9f22-4610-b6b4-1e42fe560433/",
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "user_uuid": "2f6cd410-6d32-4a58-9376-eea3c55a5f9c",
    "position": "https://api.robinhood.com/positions/5RZ07024/921be484-02df-485a-9c67-12ab6ee36783/",
    "cancel": null,
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "instrument_id": "921be484-02df-485a-9c67-12ab6ee36783",
    "cumulative_quantity": "2.00000000",
    "average_price": "0.04000000",
    "fees": "0.00",
    "state": "filled",
    "pending_cancel_open_agent": null,
    "type": "market",
    "side": "sell",
    "time_in_force": "gtc",
    "trigger": "stop",
    "price": "0.04140000",
    "stop_price": "0.04140000",
    "quantity": "2.00000000",
    "reject_reason": null,
    "created_at": "2024-04-19T19:42:55.694395Z",
    "updated_at": "2024-04-19T19:45:29.986022Z",
    "last_transaction_at": "2024-04-19T19:45:29.834000Z",
    "executions": [
        {
            "price": "0.04140000",
            "quantity": "2.00000000",
            "rounded_notional": "0.08000000",
            "settlement_date": "2024-04-23",
            "timestamp": "2024-04-19T19:45:29.834000Z",
            "id": "6622c9d9-8d59-4293-8d3f-22b6ef458e55",
            "ipo_access_execution_rank": null,
            "trade_execution_date": "2024-04-19"
        }
    ],
    "extended_hours": false,
    "market_hours": "regular_hours",
    "override_dtbp_checks": false,
    "override_day_trade_checks": false,
    "response_category": null,
    "stop_triggered_at": "2024-04-19T19:45:29.833000Z",
    "last_trail_price": null,
    "last_trail_price_updated_at": null,
    "last_trail_price_source": null,
    "dollar_based_amount": null,
    "total_notional": {
        "amount": "0.08",
        "currency_code": "USD",
        "currency_id": "1072fc76-1862-41ab-82c2-485837590762"
    },
    "executed_notional": {
        "amount": "0.08",
        "currency_code": "USD",
        "currency_id": "1072fc76-1862-41ab-82c2-485837590762"
    },
    "investment_schedule_id": null,
    "is_ipo_access_order": false,
    "ipo_access_cancellation_reason": null,
    "ipo_access_lower_collared_price": null,
    "ipo_access_upper_collared_price": null,
    "ipo_access_upper_price": null,
    "ipo_access_lower_price": null,
    "is_ipo_access_price_finalized": false,
    "is_visible_to_user": true,
    "has_ipo_access_custom_price_limit": false,
    "is_primary_account": true,
    "order_form_version": 4,
    "preset_percent_limit": null,
    "order_form_type": "all_day_trading_v1_2",
    "last_update_version": 3,
    "placed_agent": "user"
}

------------------


order = r.order_buy_market(symbol, quantity, jsonify=True)
print(json.dumps(order, indent=4))
buy_market_order_id = order['id']
buy_market_order_price = order['price']

{
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "symbol": "SINT",
    "price": 0.042,
    "quantity": 1,
    "ref_id": "1a4d1344-eed9-4e46-b132-433600519915",
    "type": "market",
    "stop_price": null,
    "time_in_force": "gtc",
    "trigger": "immediate",
    "side": "buy",
    "market_hours": "regular_hours",
    "extended_hours": false,
    "order_form_version": 4
}
{
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "symbol": "SINT",
    "price": 0.042,
    "quantity": 1,
    "ref_id": "1a4d1344-eed9-4e46-b132-433600519915",
    "type": "limit",
    "time_in_force": "gtc",
    "trigger": "immediate",
    "side": "buy",
    "market_hours": "regular_hours",
    "order_form_version": 4,
    "preset_percent_limit": "0.05"
}
{
    "id": "6622cadd-ca75-48d2-a41f-7d5a545a7978",
    "ref_id": "1a4d1344-eed9-4e46-b132-433600519915",
    "url": "https://api.robinhood.com/orders/6622cadd-ca75-48d2-a41f-7d5a545a7978/",
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "user_uuid": "2f6cd410-6d32-4a58-9376-eea3c55a5f9c",
    "position": "https://api.robinhood.com/positions/5RZ07024/921be484-02df-485a-9c67-12ab6ee36783/",
    "cancel": "https://api.robinhood.com/orders/6622cadd-ca75-48d2-a41f-7d5a545a7978/cancel/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "instrument_id": "921be484-02df-485a-9c67-12ab6ee36783",
    "cumulative_quantity": "0.00000000",
    "average_price": null,
    "fees": "0.00",
    "state": "unconfirmed",
    "pending_cancel_open_agent": null,
    "type": "limit",
    "side": "buy",
    "time_in_force": "gtc",
    "trigger": "immediate",
    "price": "0.04200000",
    "stop_price": null,
    "quantity": "1.00000000",
    "reject_reason": null,
    "created_at": "2024-04-19T19:49:49.546166Z",
    "updated_at": "2024-04-19T19:49:49.546179Z",
    "last_transaction_at": "2024-04-19T19:49:49.546166Z",
    "executions": [],
    "extended_hours": false,
    "market_hours": "regular_hours",
    "override_dtbp_checks": false,
    "override_day_trade_checks": false,
    "response_category": null,
    "stop_triggered_at": null,
    "last_trail_price": null,
    "last_trail_price_updated_at": null,
    "last_trail_price_source": null,
    "dollar_based_amount": null,
    "total_notional": {
        "amount": "0.05",
        "currency_code": "USD",
        "currency_id": "1072fc76-1862-41ab-82c2-485837590762"
    },
    "executed_notional": null,
    "investment_schedule_id": null,
    "is_ipo_access_order": false,
    "ipo_access_cancellation_reason": null,
    "ipo_access_lower_collared_price": null,
    "ipo_access_upper_collared_price": null,
    "ipo_access_upper_price": null,
    "ipo_access_lower_price": null,
    "is_ipo_access_price_finalized": false,
    "is_visible_to_user": true,
    "has_ipo_access_custom_price_limit": false,
    "is_primary_account": true,
    "order_form_version": 4,
    "preset_percent_limit": "0.050000",
    "order_form_type": "all_day_trading_v1_2",
    "last_update_version": -1,
    "placed_agent": "user"
}

print(json.dumps(r.get_stock_order_info('6622cadd-ca75-48d2-a41f-7d5a545a7978'), indent=4))

{
    "id": "6622cadd-ca75-48d2-a41f-7d5a545a7978",
    "ref_id": "1a4d1344-eed9-4e46-b132-433600519915",
    "url": "https://api.robinhood.com/orders/6622cadd-ca75-48d2-a41f-7d5a545a7978/",
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "user_uuid": "2f6cd410-6d32-4a58-9376-eea3c55a5f9c",
    "position": "https://api.robinhood.com/positions/5RZ07024/921be484-02df-485a-9c67-12ab6ee36783/",
    "cancel": null,
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "instrument_id": "921be484-02df-485a-9c67-12ab6ee36783",
    "cumulative_quantity": "1.00000000",
    "average_price": "0.04000000",
    "fees": "0.00",
    "state": "filled",
    "pending_cancel_open_agent": null,
    "type": "limit",
    "side": "buy",
    "time_in_force": "gtc",
    "trigger": "immediate",
    "price": "0.04200000",
    "stop_price": null,
    "quantity": "1.00000000",
    "reject_reason": null,
    "created_at": "2024-04-19T19:49:49.546166Z",
    "updated_at": "2024-04-19T19:49:49.892562Z",
    "last_transaction_at": "2024-04-19T19:49:49.717000Z",
    "executions": [
        {
            "price": "0.04180000",
            "quantity": "1.00000000",
            "rounded_notional": "0.04000000",
            "settlement_date": "2024-04-23",
            "timestamp": "2024-04-19T19:49:49.717000Z",
            "id": "6622cadd-c157-4961-842f-84190451cff6",
            "ipo_access_execution_rank": null,
            "trade_execution_date": "2024-04-19"
        }
    ],
    "extended_hours": false,
    "market_hours": "regular_hours",
    "override_dtbp_checks": false,
    "override_day_trade_checks": false,
    "response_category": null,
    "stop_triggered_at": null,
    "last_trail_price": null,
    "last_trail_price_updated_at": null,
    "last_trail_price_source": null,
    "dollar_based_amount": null,
    "total_notional": {
        "amount": "0.05",
        "currency_code": "USD",
        "currency_id": "1072fc76-1862-41ab-82c2-485837590762"
    },
    "executed_notional": {
        "amount": "0.04",
        "currency_code": "USD",
        "currency_id": "1072fc76-1862-41ab-82c2-485837590762"
    },
    "investment_schedule_id": null,
    "is_ipo_access_order": false,
    "ipo_access_cancellation_reason": null,
    "ipo_access_lower_collared_price": null,
    "ipo_access_upper_collared_price": null,
    "ipo_access_upper_price": null,
    "ipo_access_lower_price": null,
    "is_ipo_access_price_finalized": false,
    "is_visible_to_user": true,
    "has_ipo_access_custom_price_limit": false,
    "is_primary_account": true,
    "order_form_version": 4,
    "preset_percent_limit": "0.050000",
    "order_form_type": "all_day_trading_v1_2",
    "last_update_version": 2,
    "placed_agent": "user"
}

----------

order sell market

def order_sell_market(symbol, quantity, account_number=None, timeInForce='gtc', extendedHours=False, jsonify=True):
    """Submits a market order to be executed immediately.

order_sell = r.order_sell_market(symbol, quantity, jsonify=True)
print(json.dumps(order_sell, indent=4))    

{
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "symbol": "SINT",
    "price": 0.0405,
    "quantity": 1,
    "ref_id": "44478e4f-52c2-4d7b-9b00-a3bd3287cf38",
    "type": "market",
    "stop_price": null,
    "time_in_force": "gtc",
    "trigger": "immediate",
    "side": "sell",
    "market_hours": "regular_hours",
    "extended_hours": false,
    "order_form_version": 4
}
{
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "symbol": "SINT",
    "quantity": 1,
    "ref_id": "44478e4f-52c2-4d7b-9b00-a3bd3287cf38",
    "type": "market",
    "time_in_force": "gtc",
    "trigger": "immediate",
    "side": "sell",
    "market_hours": "regular_hours",
    "order_form_version": 4
}
{
    "non_field_errors": [
        "Invalid Good Til Canceled order."
    ]
}


order_sell = r.order_sell_market(symbol, quantity, timeInForce='gfd', jsonify=True)
print(json.dumps(order_sell, indent=4))

{
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "symbol": "SINT",
    "price": 0.0405,
    "quantity": 1,
    "ref_id": "5d42f3ed-b7df-44f3-a40a-dedf9003cc95",
    "type": "market",
    "stop_price": null,
    "time_in_force": "gfd",
    "trigger": "immediate",
    "side": "sell",
    "market_hours": "regular_hours",
    "extended_hours": false,
    "order_form_version": 4
}
{
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "symbol": "SINT",
    "quantity": 1,
    "ref_id": "5d42f3ed-b7df-44f3-a40a-dedf9003cc95",
    "type": "market",
    "time_in_force": "gfd",
    "trigger": "immediate",
    "side": "sell",
    "market_hours": "regular_hours",
    "order_form_version": 4
}
{
    "id": "6622cddc-0f26-4c2f-96a7-576516ac3683",
    "ref_id": "5d42f3ed-b7df-44f3-a40a-dedf9003cc95",
    "url": "https://api.robinhood.com/orders/6622cddc-0f26-4c2f-96a7-576516ac3683/",
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "user_uuid": "2f6cd410-6d32-4a58-9376-eea3c55a5f9c",
    "position": "https://api.robinhood.com/positions/5RZ07024/921be484-02df-485a-9c67-12ab6ee36783/",
    "cancel": "https://api.robinhood.com/orders/6622cddc-0f26-4c2f-96a7-576516ac3683/cancel/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "instrument_id": "921be484-02df-485a-9c67-12ab6ee36783",
    "cumulative_quantity": "0.00000000",
    "average_price": null,
    "fees": "0.00",
    "state": "unconfirmed",
    "pending_cancel_open_agent": null,
    "type": "market",
    "side": "sell",
    "time_in_force": "gfd",
    "trigger": "immediate",
    "price": null,
    "stop_price": null,
    "quantity": "1.00000000",
    "reject_reason": null,
    "created_at": "2024-04-19T20:02:36.974830Z",
    "updated_at": "2024-04-19T20:02:36.974846Z",
    "last_transaction_at": "2024-04-19T20:02:36.974830Z",
    "executions": [],
    "extended_hours": false,
    "market_hours": "regular_hours",
    "override_dtbp_checks": false,
    "override_day_trade_checks": false,
    "response_category": null,
    "stop_triggered_at": null,
    "last_trail_price": null,
    "last_trail_price_updated_at": null,
    "last_trail_price_source": null,
    "dollar_based_amount": null,
    "total_notional": null,
    "executed_notional": null,
    "investment_schedule_id": null,
    "is_ipo_access_order": false,
    "ipo_access_cancellation_reason": null,
    "ipo_access_lower_collared_price": null,
    "ipo_access_upper_collared_price": null,
    "ipo_access_upper_price": null,
    "ipo_access_lower_price": null,
    "is_ipo_access_price_finalized": false,
    "is_visible_to_user": true,
    "has_ipo_access_custom_price_limit": false,
    "is_primary_account": true,
    "order_form_version": 4,
    "preset_percent_limit": null,
    "order_form_type": "all_day_trading_v1_2",
    "last_update_version": -1,
    "placed_agent": "user"
}


print(json.dumps(r.get_stock_order_info('6622cddc-0f26-4c2f-96a7-576516ac3683'), indent=4))


state queued because of market hours close at 16:00. After market is open.

{
    "id": "6622cddc-0f26-4c2f-96a7-576516ac3683",
    "ref_id": "5d42f3ed-b7df-44f3-a40a-dedf9003cc95",
    "url": "https://api.robinhood.com/orders/6622cddc-0f26-4c2f-96a7-576516ac3683/",
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "user_uuid": "2f6cd410-6d32-4a58-9376-eea3c55a5f9c",
    "position": "https://api.robinhood.com/positions/5RZ07024/921be484-02df-485a-9c67-12ab6ee36783/",
    "cancel": "https://api.robinhood.com/orders/6622cddc-0f26-4c2f-96a7-576516ac3683/cancel/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "instrument_id": "921be484-02df-485a-9c67-12ab6ee36783",
    "cumulative_quantity": "0.00000000",
    "average_price": null,
    "fees": "0.00",
    "state": "queued",
    "pending_cancel_open_agent": null,
    "type": "market",
    "side": "sell",
    "time_in_force": "gfd",
    "trigger": "immediate",
    "price": null,
    "stop_price": null,
    "quantity": "1.00000000",
    "reject_reason": null,
    "created_at": "2024-04-19T20:02:36.974830Z",
    "updated_at": "2024-04-19T20:02:36.974846Z",
    "last_transaction_at": "2024-04-19T20:02:36.974830Z",
    "executions": [],
    "extended_hours": false,
    "market_hours": "regular_hours",
    "override_dtbp_checks": false,
    "override_day_trade_checks": false,
    "response_category": null,
    "stop_triggered_at": null,
    "last_trail_price": null,
    "last_trail_price_updated_at": null,
    "last_trail_price_source": null,
    "dollar_based_amount": null,
    "total_notional": null,
    "executed_notional": null,
    "investment_schedule_id": null,
    "is_ipo_access_order": false,
    "ipo_access_cancellation_reason": null,
    "ipo_access_lower_collared_price": null,
    "ipo_access_upper_collared_price": null,
    "ipo_access_upper_price": null,
    "ipo_access_lower_price": null,
    "is_ipo_access_price_finalized": false,
    "is_visible_to_user": true,
    "has_ipo_access_custom_price_limit": false,
    "is_primary_account": true,
    "order_form_version": 4,
    "preset_percent_limit": null,
    "order_form_type": "all_day_trading_v1_2",
    "last_update_version": -1,
    "placed_agent": "user"
}

print(json.dumps(r.cancel_stock_order('6622cddc-0f26-4c2f-96a7-576516ac3683'), indent=4))


Order 6622cddc-0f26-4c2f-96a7-576516ac3683 cancelled
{
    "detail": "Order cannot be cancelled at this time."
}

after trying multiple times

state cancelled

{
    "id": "6622cddc-0f26-4c2f-96a7-576516ac3683",
    "ref_id": "5d42f3ed-b7df-44f3-a40a-dedf9003cc95",
    "url": "https://api.robinhood.com/orders/6622cddc-0f26-4c2f-96a7-576516ac3683/",
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "user_uuid": "2f6cd410-6d32-4a58-9376-eea3c55a5f9c",
    "position": "https://api.robinhood.com/positions/5RZ07024/921be484-02df-485a-9c67-12ab6ee36783/",
    "cancel": null,
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "instrument_id": "921be484-02df-485a-9c67-12ab6ee36783",
    "cumulative_quantity": "0.00000000",
    "average_price": null,
    "fees": "0.00",
    "state": "cancelled",
    "pending_cancel_open_agent": null,
    "type": "market",
    "side": "sell",
    "time_in_force": "gfd",
    "trigger": "immediate",
    "price": null,
    "stop_price": null,
    "quantity": "1.00000000",
    "reject_reason": null,
    "created_at": "2024-04-19T20:02:36.974830Z",
    "updated_at": "2024-04-19T20:07:42.132510Z",
    "last_transaction_at": "2024-04-19T20:07:42.068673Z",
    "executions": [],
    "extended_hours": false,
    "market_hours": "regular_hours",
    "override_dtbp_checks": false,
    "override_day_trade_checks": false,
    "response_category": null,
    "stop_triggered_at": null,
    "last_trail_price": null,
    "last_trail_price_updated_at": null,
    "last_trail_price_source": null,
    "dollar_based_amount": null,
    "total_notional": null,
    "executed_notional": null,
    "investment_schedule_id": null,
    "is_ipo_access_order": false,
    "ipo_access_cancellation_reason": "user",
    "ipo_access_lower_collared_price": null,
    "ipo_access_upper_collared_price": null,
    "ipo_access_upper_price": null,
    "ipo_access_lower_price": null,
    "is_ipo_access_price_finalized": false,
    "is_visible_to_user": true,
    "has_ipo_access_custom_price_limit": false,
    "is_primary_account": true,
    "order_form_version": 4,
    "preset_percent_limit": null,
    "order_form_type": "all_day_trading_v1_2",
    "last_update_version": 1,
    "placed_agent": "user"
}

-------------

def order_sell_limit(symbol, quantity, limitPrice, account_number=None, timeInForce='gtc', extendedHours=False, jsonify=True):
    """Submits a limit order to be executed once a certain price is reached.


limitPrice = 0.041
order_sell_limit =  r.order_sell_limit(symbol, quantity, limitPrice, account_number=None, timeInForce='gtc', extendedHours=True, jsonify=True)
print(json.dumps(order_sell_limit, indent=4))

{
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "symbol": "SINT",
    "price": null,
    "quantity": 1,
    "ref_id": "fdb2e8dd-2591-40ac-ae80-d49e067d1eb7",
    "type": "market",
    "stop_price": 0.041,
    "time_in_force": "gtc",
    "trigger": "stop",
    "side": "sell",
    "market_hours": "regular_hours",
    "extended_hours": true,
    "order_form_version": 4
}
{
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "symbol": "SINT",
    "quantity": 1,
    "ref_id": "fdb2e8dd-2591-40ac-ae80-d49e067d1eb7",
    "type": "market",
    "stop_price": 0.041,
    "time_in_force": "gtc",
    "trigger": "stop",
    "side": "sell",
    "market_hours": "regular_hours",
    "order_form_version": 4
}
{
    "id": "6622d07e-17ce-4c85-a5a2-a6ccbcb414f2",
    "ref_id": "fdb2e8dd-2591-40ac-ae80-d49e067d1eb7",
    "url": "https://api.robinhood.com/orders/6622d07e-17ce-4c85-a5a2-a6ccbcb414f2/",
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "user_uuid": "2f6cd410-6d32-4a58-9376-eea3c55a5f9c",
    "position": "https://api.robinhood.com/positions/5RZ07024/921be484-02df-485a-9c67-12ab6ee36783/",
    "cancel": "https://api.robinhood.com/orders/6622d07e-17ce-4c85-a5a2-a6ccbcb414f2/cancel/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "instrument_id": "921be484-02df-485a-9c67-12ab6ee36783",
    "cumulative_quantity": "0.00000000",
    "average_price": null,
    "fees": "0.00",
    "state": "unconfirmed",
    "pending_cancel_open_agent": null,
    "type": "market",
    "side": "sell",
    "time_in_force": "gtc",
    "trigger": "stop",
    "price": null,
    "stop_price": "0.04100000",
    "quantity": "1.00000000",
    "reject_reason": null,
    "created_at": "2024-04-19T20:13:50.547791Z",
    "updated_at": "2024-04-19T20:13:50.547802Z",
    "last_transaction_at": "2024-04-19T20:13:50.547791Z",
    "executions": [],
    "extended_hours": false,
    "market_hours": "regular_hours",
    "override_dtbp_checks": false,
    "override_day_trade_checks": false,
    "response_category": null,
    "stop_triggered_at": null,
    "last_trail_price": null,
    "last_trail_price_updated_at": null,
    "last_trail_price_source": null,
    "dollar_based_amount": null,
    "total_notional": null,
    "executed_notional": null,
    "investment_schedule_id": null,
    "is_ipo_access_order": false,
    "ipo_access_cancellation_reason": null,
    "ipo_access_lower_collared_price": null,
    "ipo_access_upper_collared_price": null,
    "ipo_access_upper_price": null,
    "ipo_access_lower_price": null,
    "is_ipo_access_price_finalized": false,
    "is_visible_to_user": true,
    "has_ipo_access_custom_price_limit": false,
    "is_primary_account": true,
    "order_form_version": 4,
    "preset_percent_limit": null,
    "order_form_type": "all_day_trading_v1_2",
    "last_update_version": -1,
    "placed_agent": "user"
}

-----------

sell extended hours

{
  "account": "https://api.robinhood.com/accounts/5RZ07024/",
  "ask_price": "0.043200",
  "bid_ask_timestamp": "2024-04-19T20:28:23Z",
  "bid_price": "0.040100",
  "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
  "quantity": "1",
  "market_hours": "extended_hours",
  "order_form_version": 4,
  "ref_id": "6f6fa21c-89c5-4979-9c3e-4096b9a743b6",
  "side": "sell",
  "symbol": "SINT",
  "time_in_force": "gfd",
  "trigger": "immediate",
  "type": "limit",
  "price": "0.0400"
}

{
  "id": "6622d430-203f-4bfb-9375-c198e3dc8b4e",
  "ref_id": "6f6fa21c-89c5-4979-9c3e-4096b9a743b6",
  "url": "https://api.robinhood.com/orders/6622d430-203f-4bfb-9375-c198e3dc8b4e/",
  "account": "https://api.robinhood.com/accounts/5RZ07024/",
  "user_uuid": "2f6cd410-6d32-4a58-9376-eea3c55a5f9c",
  "position": "https://api.robinhood.com/positions/5RZ07024/921be484-02df-485a-9c67-12ab6ee36783/",
  "cancel": "https://api.robinhood.com/orders/6622d430-203f-4bfb-9375-c198e3dc8b4e/cancel/",
  "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
  "instrument_id": "921be484-02df-485a-9c67-12ab6ee36783",
  "cumulative_quantity": "0.00000000",
  "average_price": null,
  "fees": "0.00",
  "state": "unconfirmed",
  "pending_cancel_open_agent": null,
  "type": "limit",
  "side": "sell",
  "time_in_force": "gfd",
  "trigger": "immediate",
  "price": "0.04000000",
  "stop_price": null,
  "quantity": "1.00000000",
  "reject_reason": null,
  "created_at": "2024-04-19T20:29:36.066454Z",
  "updated_at": "2024-04-19T20:29:36.066468Z",
  "last_transaction_at": "2024-04-19T20:29:36.066454Z",
  "executions": [],
  "extended_hours": true,
  "market_hours": "extended_hours",
  "override_dtbp_checks": false,
  "override_day_trade_checks": false,
  "response_category": null,
  "stop_triggered_at": null,
  "last_trail_price": null,
  "last_trail_price_updated_at": null,
  "last_trail_price_source": null,
  "dollar_based_amount": null,
  "total_notional": {
    "amount": "0.04",
    "currency_code": "USD",
    "currency_id": "1072fc76-1862-41ab-82c2-485837590762"
  },
  "executed_notional": null,
  "investment_schedule_id": null,
  "is_ipo_access_order": false,
  "ipo_access_cancellation_reason": null,
  "ipo_access_lower_collared_price": null,
  "ipo_access_upper_collared_price": null,
  "ipo_access_upper_price": null,
  "ipo_access_lower_price": null,
  "is_ipo_access_price_finalized": false,
  "is_visible_to_user": true,
  "has_ipo_access_custom_price_limit": false,
  "is_primary_account": true,
  "order_form_version": 4,
  "preset_percent_limit": null,
  "order_form_type": "all_day_trading_v1_2",
  "last_update_version": -1,
  "placed_agent": "user"
}

sell regular hours

{
  "account": "https://api.robinhood.com/accounts/5RZ07024/",
  "ask_price": "0.045100",
  "bid_ask_timestamp": "2024-04-19T17:25:59Z",
  "bid_price": "0.045000",
  "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
  "quantity": "1",
  "market_hours": "regular_hours",
  "order_form_version": 4,
  "ref_id": "70973b95-1db1-4a1f-baab-9164ec7f21b2",
  "side": "sell",
  "symbol": "SINT",
  "time_in_force": "gfd",
  "trigger": "stop",
  "type": "market",
  "stop_price": "0.0400"
}

{
  "id": "6622a92d-2a32-427e-965c-a784f3f489b2",
  "ref_id": "70973b95-1db1-4a1f-baab-9164ec7f21b2",
  "url": "https://api.robinhood.com/orders/6622a92d-2a32-427e-965c-a784f3f489b2/",
  "account": "https://api.robinhood.com/accounts/5RZ07024/",
  "user_uuid": "2f6cd410-6d32-4a58-9376-eea3c55a5f9c",
  "position": "https://api.robinhood.com/positions/5RZ07024/921be484-02df-485a-9c67-12ab6ee36783/",
  "cancel": "https://api.robinhood.com/orders/6622a92d-2a32-427e-965c-a784f3f489b2/cancel/",
  "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
  "instrument_id": "921be484-02df-485a-9c67-12ab6ee36783",
  "cumulative_quantity": "0.00000000",
  "average_price": null,
  "fees": "0.00",
  "state": "unconfirmed",
  "pending_cancel_open_agent": null,
  "type": "market",
  "side": "sell",
  "time_in_force": "gfd",
  "trigger": "stop",
  "price": null,
  "stop_price": "0.04000000",
  "quantity": "1.00000000",
  "reject_reason": null,
  "created_at": "2024-04-19T17:26:05.624736Z",
  "updated_at": "2024-04-19T17:26:05.624751Z",
  "last_transaction_at": "2024-04-19T17:26:05.624736Z",
  "executions": [],
  "extended_hours": false,
  "market_hours": "regular_hours",
  "override_dtbp_checks": false,
  "override_day_trade_checks": false,
  "response_category": null,
  "stop_triggered_at": null,
  "last_trail_price": null,
  "last_trail_price_updated_at": null,
  "last_trail_price_source": null,
  "dollar_based_amount": null,
  "total_notional": null,
  "executed_notional": null,
  "investment_schedule_id": null,
  "is_ipo_access_order": false,
  "ipo_access_cancellation_reason": null,
  "ipo_access_lower_collared_price": null,
  "ipo_access_upper_collared_price": null,
  "ipo_access_upper_price": null,
  "ipo_access_lower_price": null,
  "is_ipo_access_price_finalized": false,
  "is_visible_to_user": true,
  "has_ipo_access_custom_price_limit": false,
  "is_primary_account": true,
  "order_form_version": 4,
  "preset_percent_limit": null,
  "order_form_type": "all_day_trading_v1_2",
  "last_update_version": -1,
  "placed_agent": "user"
}

----------

buy extended hours

{
  "account": "https://api.robinhood.com/accounts/5RZ07024/",
  "ask_price": "0.042200",
  "bid_ask_timestamp": "2024-04-19T20:32:30Z",
  "bid_price": "0.042100",
  "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
  "quantity": "1",
  "market_hours": "extended_hours",
  "order_form_version": 4,
  "ref_id": "ed513bae-b8cd-41a5-a00d-0af315df5429",
  "side": "buy",
  "symbol": "SINT",
  "time_in_force": "gfd",
  "trigger": "immediate",
  "type": "limit",
  "price": "0.0422"
}

{
  "id": "6622d550-319c-4672-9178-8d33f2f3903c",
  "ref_id": "ed513bae-b8cd-41a5-a00d-0af315df5429",
  "url": "https://api.robinhood.com/orders/6622d550-319c-4672-9178-8d33f2f3903c/",
  "account": "https://api.robinhood.com/accounts/5RZ07024/",
  "user_uuid": "2f6cd410-6d32-4a58-9376-eea3c55a5f9c",
  "position": "https://api.robinhood.com/positions/5RZ07024/921be484-02df-485a-9c67-12ab6ee36783/",
  "cancel": "https://api.robinhood.com/orders/6622d550-319c-4672-9178-8d33f2f3903c/cancel/",
  "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
  "instrument_id": "921be484-02df-485a-9c67-12ab6ee36783",
  "cumulative_quantity": "0.00000000",
  "average_price": null,
  "fees": "0.00",
  "state": "unconfirmed",
  "pending_cancel_open_agent": null,
  "type": "limit",
  "side": "buy",
  "time_in_force": "gfd",
  "trigger": "immediate",
  "price": "0.04220000",
  "stop_price": null,
  "quantity": "1.00000000",
  "reject_reason": null,
  "created_at": "2024-04-19T20:34:24.979559Z",
  "updated_at": "2024-04-19T20:34:24.979573Z",
  "last_transaction_at": "2024-04-19T20:34:24.979559Z",
  "executions": [],
  "extended_hours": true,
  "market_hours": "extended_hours",
  "override_dtbp_checks": false,
  "override_day_trade_checks": false,
  "response_category": null,
  "stop_triggered_at": null,
  "last_trail_price": null,
  "last_trail_price_updated_at": null,
  "last_trail_price_source": null,
  "dollar_based_amount": null,
  "total_notional": {
    "amount": "0.05",
    "currency_code": "USD",
    "currency_id": "1072fc76-1862-41ab-82c2-485837590762"
  },
  "executed_notional": null,
  "investment_schedule_id": null,
  "is_ipo_access_order": false,
  "ipo_access_cancellation_reason": null,
  "ipo_access_lower_collared_price": null,
  "ipo_access_upper_collared_price": null,
  "ipo_access_upper_price": null,
  "ipo_access_lower_price": null,
  "is_ipo_access_price_finalized": false,
  "is_visible_to_user": true,
  "has_ipo_access_custom_price_limit": false,
  "is_primary_account": true,
  "order_form_version": 4,
  "preset_percent_limit": null,
  "order_form_type": "all_day_trading_v1_2",
  "last_update_version": -1,
  "placed_agent": "user"
}

------------

sell  extended hours

{
  "account": "https://api.robinhood.com/accounts/5RZ07024/",
  "ask_price": "0.043200",
  "bid_ask_timestamp": "2024-04-19T20:45:01Z",
  "bid_price": "0.040600",
  "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
  "quantity": "1",
  "market_hours": "extended_hours",
  "order_form_version": 4,
  "ref_id": "aa3bbdc5-c706-4f56-9fdd-2e154900632e",
  "side": "sell",
  "symbol": "SINT",
  "time_in_force": "gfd",
  "trigger": "immediate",
  "type": "limit",
  "price": "0.0400"
}

{
  "id": "6622d7da-3f09-412e-928d-8b4ebc576bd7",
  "ref_id": "aa3bbdc5-c706-4f56-9fdd-2e154900632e",
  "url": "https://api.robinhood.com/orders/6622d7da-3f09-412e-928d-8b4ebc576bd7/",
  "account": "https://api.robinhood.com/accounts/5RZ07024/",
  "user_uuid": "2f6cd410-6d32-4a58-9376-eea3c55a5f9c",
  "position": "https://api.robinhood.com/positions/5RZ07024/921be484-02df-485a-9c67-12ab6ee36783/",
  "cancel": "https://api.robinhood.com/orders/6622d7da-3f09-412e-928d-8b4ebc576bd7/cancel/",
  "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
  "instrument_id": "921be484-02df-485a-9c67-12ab6ee36783",
  "cumulative_quantity": "0.00000000",
  "average_price": null,
  "fees": "0.00",
  "state": "unconfirmed",
  "pending_cancel_open_agent": null,
  "type": "limit",
  "side": "sell",
  "time_in_force": "gfd",
  "trigger": "immediate",
  "price": "0.04000000",
  "stop_price": null,
  "quantity": "1.00000000",
  "reject_reason": null,
  "created_at": "2024-04-19T20:45:14.705708Z",
  "updated_at": "2024-04-19T20:45:14.705722Z",
  "last_transaction_at": "2024-04-19T20:45:14.705708Z",
  "executions": [],
  "extended_hours": true,
  "market_hours": "extended_hours",
  "override_dtbp_checks": false,
  "override_day_trade_checks": false,
  "response_category": null,
  "stop_triggered_at": null,
  "last_trail_price": null,
  "last_trail_price_updated_at": null,
  "last_trail_price_source": null,
  "dollar_based_amount": null,
  "total_notional": {
    "amount": "0.04",
    "currency_code": "USD",
    "currency_id": "1072fc76-1862-41ab-82c2-485837590762"
  },
  "executed_notional": null,
  "investment_schedule_id": null,
  "is_ipo_access_order": false,
  "ipo_access_cancellation_reason": null,
  "ipo_access_lower_collared_price": null,
  "ipo_access_upper_collared_price": null,
  "ipo_access_upper_price": null,
  "ipo_access_lower_price": null,
  "is_ipo_access_price_finalized": false,
  "is_visible_to_user": true,
  "has_ipo_access_custom_price_limit": false,
  "is_primary_account": true,
  "order_form_version": 4,
  "preset_percent_limit": null,
  "order_form_type": "all_day_trading_v1_2",
  "last_update_version": -1,
  "placed_agent": "user"
}

-----------


order by limit extended hours


def order_buy_limit(symbol, quantity, limitPrice, account_number=None, timeInForce='gtc', extendedHours=False, jsonify=True):
    """Submits a limit order to be executed once a certain price is reached.

order_buy_limit_ext = r.order_buy_limit(symbol, quantity, 0.04, account_number=None, timeInForce='gfd', extendedHours=True, jsonify=True)
print(json.dumps(order_buy_limit_ext, indent=4))

{
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "symbol": "SINT",
    "price": 0.04,
    "quantity": 1,
    "ref_id": "d05aac3c-0025-4d76-961c-69e6f5df48d0",
    "type": "market",
    "stop_price": 0.04,
    "time_in_force": "gfd",
    "trigger": "stop",
    "side": "buy",
    "market_hours": "regular_hours",
    "extended_hours": true,
    "order_form_version": 4
}
{
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "symbol": "SINT",
    "price": 0.04,
    "quantity": 1,
    "ref_id": "d05aac3c-0025-4d76-961c-69e6f5df48d0",
    "type": "limit",
    "stop_price": 0.04,
    "time_in_force": "gfd",
    "trigger": "stop",
    "side": "buy",
    "market_hours": "regular_hours",
    "order_form_version": 4,
    "preset_percent_limit": "0.05"
}
{
    "non_field_errors": [
        "Invalid limit order."
    ]
}

from web

{
  "account": "https://api.robinhood.com/accounts/5RZ07024/",
  "ask_price": "0.042200",
  "bid_ask_timestamp": "2024-04-19T20:32:30Z",
  "bid_price": "0.042100",
  "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
  "quantity": "1",
  "market_hours": "extended_hours",
  "order_form_version": 4,
  "ref_id": "ed513bae-b8cd-41a5-a00d-0af315df5429",
  "side": "buy",
  "symbol": "SINT",
  "time_in_force": "gfd",
  "trigger": "immediate",
  "type": "limit",
  "price": "0.0422"
}

-------------

fix order by limit extended

order_buy_limit_ext = r.order_buy_limit(symbol, quantity, 0.042, timeInForce='gfd', extendedHours=True, jsonify=True,  market_hours='extended_hours')
print(json.dumps(order_buy_limit_ext, indent=4))

{
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "symbol": "SINT",
    "price": 0.042,
    "quantity": 1,
    "ref_id": "a4a775f0-f306-4a93-8860-b906dc9a05a1",
    "type": "limit",
    "stop_price": null,
    "time_in_force": "gfd",
    "trigger": "immediate",
    "side": "buy",
    "market_hours": "extended_hours",
    "extended_hours": true,
    "order_form_version": 4
}
{
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "symbol": "SINT",
    "price": 0.042,
    "quantity": 1,
    "ref_id": "a4a775f0-f306-4a93-8860-b906dc9a05a1",
    "type": "limit",
    "time_in_force": "gfd",
    "trigger": "immediate",
    "side": "buy",
    "market_hours": "extended_hours",
    "extended_hours": true,
    "order_form_version": 4
}
{
    "id": "6622e250-55fd-4973-9588-f65308cfeaad",
    "ref_id": "a4a775f0-f306-4a93-8860-b906dc9a05a1",
    "url": "https://api.robinhood.com/orders/6622e250-55fd-4973-9588-f65308cfeaad/",
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "user_uuid": "2f6cd410-6d32-4a58-9376-eea3c55a5f9c",
    "position": "https://api.robinhood.com/positions/5RZ07024/921be484-02df-485a-9c67-12ab6ee36783/",
    "cancel": "https://api.robinhood.com/orders/6622e250-55fd-4973-9588-f65308cfeaad/cancel/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "instrument_id": "921be484-02df-485a-9c67-12ab6ee36783",
    "cumulative_quantity": "0.00000000",
    "average_price": null,
    "fees": "0.00",
    "state": "unconfirmed",
    "pending_cancel_open_agent": null,
    "type": "limit",
    "side": "buy",
    "time_in_force": "gfd",
    "trigger": "immediate",
    "price": "0.04200000",
    "stop_price": null,
    "quantity": "1.00000000",
    "reject_reason": null,
    "created_at": "2024-04-19T21:29:52.501623Z",
    "updated_at": "2024-04-19T21:29:52.501638Z",
    "last_transaction_at": "2024-04-19T21:29:52.501623Z",
    "executions": [],
    "extended_hours": true,
    "market_hours": "extended_hours",
    "override_dtbp_checks": false,
    "override_day_trade_checks": false,
    "response_category": null,
    "stop_triggered_at": null,
    "last_trail_price": null,
    "last_trail_price_updated_at": null,
    "last_trail_price_source": null,
    "dollar_based_amount": null,
    "total_notional": {
        "amount": "0.05",
        "currency_code": "USD",
        "currency_id": "1072fc76-1862-41ab-82c2-485837590762"
    },
    "executed_notional": null,
    "investment_schedule_id": null,
    "is_ipo_access_order": false,
    "ipo_access_cancellation_reason": null,
    "ipo_access_lower_collared_price": null,
    "ipo_access_upper_collared_price": null,
    "ipo_access_upper_price": null,
    "ipo_access_lower_price": null,
    "is_ipo_access_price_finalized": false,
    "is_visible_to_user": true,
    "has_ipo_access_custom_price_limit": false,
    "is_primary_account": true,
    "order_form_version": 4,
    "preset_percent_limit": null,
    "order_form_type": "all_day_trading_v1_2",
    "last_update_version": -1,
    "placed_agent": "user"
}

after adding del payload['extended_hours'] 

    "non_field_errors": [
        "Extended hours and market hours mismatch."
    ]

{
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "symbol": "SINT",
    "price": 0.042,
    "quantity": 1,
    "ref_id": "0be97206-bc34-4626-8ddb-5b7ca3fbcfbf",
    "type": "limit",
    "stop_price": null,
    "time_in_force": "gfd",
    "trigger": "immediate",
    "side": "buy",
    "market_hours": "extended_hours",
    "extended_hours": true,
    "order_form_version": 4
}
{
    "account": "https://api.robinhood.com/accounts/5RZ07024/",
    "instrument": "https://api.robinhood.com/instruments/921be484-02df-485a-9c67-12ab6ee36783/",
    "symbol": "SINT",
    "price": 0.042,
    "quantity": 1,
    "ref_id": "0be97206-bc34-4626-8ddb-5b7ca3fbcfbf",
    "type": "limit",
    "time_in_force": "gfd",
    "trigger": "immediate",
    "side": "buy",
    "market_hours": "extended_hours",
    "order_form_version": 4
}
{
    "non_field_errors": [
        "Extended hours and market hours mismatch."
    ]
}

order_sell_limit_ext =  r.order_sell_limit(symbol, quantity, 0.04, timeInForce='gfd', extendedHours=True, jsonify=True)
print(json.dumps(order_sell_limit, indent=4))


```
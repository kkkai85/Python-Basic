from flask import jsonify, request
from flask_restful import Resource
import json

# 預設資料
stores = [{
    'name': 'First store',
    'items': [{'name':'my item 1', 'price': 30 }],
    },
    {
    'name': 'Second store',
    'items': [{'name':'my item 2', 'price': 15 }],
    }
]

# 建立類別繼承Resource，方法都對應到客戶端請求所需的method
class Stores(Resource):
    def get(self):
        return jsonify(stores)

    def post(self):
        try:
            getStore = request.get_data()
            if not getStore:
                return {
                    'message' : 'No Data Inserted.'
                }, 404

            jdata = json.loads(getStore)
            stores.append(jdata)

            return jsonify(stores)
        except Exception as e:
            return str(e)
    
    def put(self):
        try:
            getStore = request.get_data()
            if not getStore:
                return {
                    'message' : 'No Data Inserted.'
                }, 404

            jdata = json.loads(getStore)
            for sname in stores:
                if sname['name'] == jdata['name']:
                    sname['items'] = jdata['items']
                    return jsonify(stores)

            return "No Found"
        except Exception as e:
            return str(e)

    def delete(self):
        try:
            getStore = request.values['name']
            if not getStore:
                return {
                    'message' : 'No Data Inserted.'
                }, 404

            for store in stores:
                if store['name'] == getStore:
                    stores.remove(store)
                    return jsonify(stores)

            return {
                    'message' : 'name not exist.'
                }, 404

        except Exception as e:
            return str(e)
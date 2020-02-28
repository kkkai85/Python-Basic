from flask import Flask, jsonify, request
import json

# 初始化Flask 類別成為instance
app = Flask(__name__)

# 使用者端會提出一個請求稱為request，
# 這些資訊都可以透過瀏灠器的開發者工具看的到，大概幾種狀況：
# 取得資訊的時候GET
# 送出資訊的時候POST
# 更新資訊的時候PUT
# 刪除資訊的時候DELETE

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

# 路由和處理函式配對
# app.route('路徑', methods = ['GET', 'POST']) 
# 第一個參數是endpoint 的路徑
# 如果需要從API 傳入參數到路徑，就需要使用<>符號
# 後面就是API 的方法，定義了API 被觸發後的動作，最終給予結果

# 取得全部store
@app.route('/store') # 若沒設定methods，預設為GET
def get_all():
    # return str(type(stores))
    return jsonify(stores) 

# 查詢store
@app.route('/store/<string:name>', methods = ['GET'])
def get_store(name):
    try:
        for sname in stores:
            if sname['name'] == name:
                return jsonify(sname)

        return "No store"
    except Exception as e:
        return str(e)

# 新增store
@app.route('/store', methods = ['POST'])
def post_store():
    try:
        getStore = request.get_data() or "No Data"
        if getStore == "No Data":
            return getStore

        jdata = json.loads(getStore)
        stores.append(jdata)

        return jsonify(stores)
    except Exception as e:
        return str(e)

# 修改store 中的item 資料
@app.route('/store', methods = ['PUT'])
def put_store():
    try:
        getStore = request.get_data() or "No Data"
        if getStore == "No Data":
            return getStore

        store = json.loads(getStore)
        for sname in stores:
            if sname['name'] == store['name']:
                sname['items'] = store['items']
                return jsonify(stores)

        return "No Found"
    except Exception as e:
        return str(e)

# 刪除store
@app.route('/store', methods = ['DELETE'])
def delete_store():
    try:
        getStore = request.values['name'] or "No Data"
        if getStore == "No Data":
            return getStore

        for store in stores:
            if store['name'] == getStore:
                stores.remove(store)
                return jsonify(stores)

        return "No Found"

    except Exception as e:
        return str(e)

# 判斷自己執行而非當作引入的模組
# 因為__name__ 這變數若被當作模組引入使用就不會是__main__
if __name__ == "__main__":
    app.debug = True
    # app.run()
    app.run(host = '0.0.0.0', port = 5000)
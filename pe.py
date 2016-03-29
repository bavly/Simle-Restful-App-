from re import search

from flask import Flask , request, jsonify
import json
app = Flask("bavly")

@app.route('/api/users/add', methods = ['POST'])
def add():
    args = request.args
    user_name = args.get("user_name")
    if user_name:
        with open(user_name, 'w') as file:
            json.dump(args , file)
        return jsonify({"response":"user added 7amada" }), 200
    else:
        return jsonify({"response": "No user name spec"}), 403



@app.route('/api/users/<user_name>')
def get(user_name):
    import os
    if os.path.exists(user_name):
        jsonify({"User name": " Exists "})
        with open(user_name, 'r') as f:
            x = json.load(f)
        return jsonify(x), 200

    return jsonify({"response": "Not found"}), 404


@app.route('/api/users/<user_name>', methods=["DELETE"])
def delete (user_name):
    import os
    if user_name:
       if os.path.exists(user_name):
           os.remove(user_name)
           return jsonify({'response': 'User deleted successfully'}), 404
       else:
           return jsonify({'response': 'no user with this user name'}), 404
    else:
        return jsonify({'response': 'You must provide a user name'}), 403




if __name__ == '__main__':
     app.run(host='0.0.0.0' , debug=True)







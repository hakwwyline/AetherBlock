from flask import Flask, request, jsonify
from blockchain import Blockchain
from transaction import Transaction

app = Flask(__name__)
blockchain = Blockchain()


@app.route('/new_transaction', methods=['POST'])
def new_transaction():
    tx_data = request.get_json()
    required_fields = ["sender", "recipient", "amount"]

    for field in required_fields:
        if not tx_data.get(field):
            return "Invalid transaction data", 400

    transaction = Transaction(
        tx_data["sender"],
        tx_data["recipient"],
        tx_data["amount"]
    )

    blockchain.add_transaction(transaction.to_dict())
    return jsonify({"message": "Transaction added"}), 201


@app.route('/mine', methods=['GET'])
def mine():
    result = blockchain.mine()
    if not result:
        return jsonify({"message": "No transactions to mine"})
    return jsonify({"message": f"Block #{result} is mined."})


@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return jsonify({
        "length": len(chain_data),
        "chain": chain_data
    })


if __name__ == '__main__':
    app.run(debug=True)

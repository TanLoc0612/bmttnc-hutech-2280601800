from flask import Flask, request, jsonify
from cipher.playfair import PlayFairCipher
app = Flask(__name__)

playfair_cipher = PlayFairCipher()

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.get_json()
    if not data or 'key' not in data:
        return jsonify({'error': 'Missing key'}), 400
    matrix = playfair_cipher.create_playfair_matrix(data['key'])
    return jsonify({'playfair_matrix': matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    if not data or 'key' not in data or 'plain_text' not in data:
        return jsonify({'error': 'Missing key or plain_text'}), 400
    matrix = playfair_cipher.create_playfair_matrix(data['key'])
    encrypted = playfair_cipher.playfair_encrypt(data['plain_text'], matrix)
    return jsonify({'encrypted_text': encrypted})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()
    if not data or 'key' not in data or 'cipher_text' not in data:
        return jsonify({'error': 'Missing key or cipher_text'}), 400
    matrix = playfair_cipher.create_playfair_matrix(data['key'])
    decrypted = playfair_cipher.playfair_decrypt(data['cipher_text'], matrix)
    return jsonify({'decrypted_text': decrypted})

if __name__ == '__main__':
    app.run(debug=True)
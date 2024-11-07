from core.storage.database import MongoDBRepository, DataService
from core.blockchain.tron import ConnectWallet
from flask_jwt_extended import create_access_token
from flask import request, jsonify, session


from core.storage.database import MongoDBRepository, DataService
from core.blockchain.tron import ConnectWallet
from flask_jwt_extended import create_access_token
from flask import request, jsonify, session

def LoginPost():
    try:
        seedPhase = []
        for index in range(1, 13):
            seedPhase.append(request.form[f'seed-{index}'])

    except KeyError as e:
        return jsonify({"error": f"Missing form field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Error processing the form: {str(e)}"}), 500

    try:
        wallet = ConnectWallet(seedPhase=seedPhase)
    except Exception as e:
        return jsonify({"error": f"Error connecting to wallet: {str(e)}"}), 500

    try:
        session['address'] = wallet.address
        access_token = create_access_token(identity=wallet.address)
    except Exception as e:
        return jsonify({"error": f"Error creating access token: {str(e)}"}), 500

    try:
        repository = MongoDBRepository(db_name="mydatabase", collection_name="auth")
        service = DataService(repository=repository)
        
        service.add_data({'address': wallet.address, 'jwt': access_token})
    except Exception as e:
        return jsonify({"error": f"Error saving data to database: {str(e)}"}), 500

    try:
        return jsonify({
            "address": wallet.address
        })
    except Exception as e:
        return jsonify({"error": f"Error generating response: {str(e)}"}), 500


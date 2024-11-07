from flask import render_template, session
from core.blockchain.eth import CreateWallet
from core.storage.database import MongoDBRepository, DataService
from flask_jwt_extended import create_access_token


def RegisterPost():
    try:
        wallet = CreateWallet() 
        session['address'] = wallet.address

    except Exception as e:
        return f"Error creating wallet: {str(e)}", 500

    try:
        access_token = create_access_token(identity=wallet.address)
    except Exception as e:
        return f"Error creating access token: {str(e)}", 500

    try:
        repository = MongoDBRepository(db_name="mydatabase", collection_name="auth")
        service = DataService(repository=repository)
        service.add_data({'address': wallet.address, 'jwt': access_token})
    except Exception as e:
        return f"Error saving data to database: {str(e)}", 500

    try:
        return render_template('register-post.html', seed=wallet.seedPhase.split())
    except Exception as e:
        return f"Error rendering the page: {str(e)}", 500
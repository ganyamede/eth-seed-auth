# eth-seed-auth
A project for registration and authentication using a seed phrase in the Ethereum network. The seed phrase is not stored; authentication is done via the Ethereum address. A JWT token is generated for API access after successful verification.

<img width="448" alt="image" src="https://github.com/user-attachments/assets/9ab16dba-fe0e-41af-b496-65888386cab7">

## Features

- **Secure Authentication:** The seed phrase is never stored. Authentication occurs via the Ethereum address derived from the seed phrase.

  <img width="752" alt="image" src="https://github.com/user-attachments/assets/d4057f6d-50f4-4c87-b564-c09ce14fbe12">
- **JWT Tokens:** After successful authentication, a JWT token is generated for secure API access.
  <img width="340" alt="image" src="https://github.com/user-attachments/assets/b6830f8d-96a0-42d1-bbcb-55926f81af2e">
- **Web3 Integration:** Built with Ethereum support for blockchain-based identity verification.

<img width="485" alt="image" src="https://github.com/user-attachments/assets/3f6f3c91-2645-4000-97d8-e54ef741e88c">


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ganyamede/eth-seed-auth.git
   ```
   
2. Go to project
   ```bash
   cd eth-seed-auth
   ```

3. Install dependencies: 
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables
  
5. Usage
   To run the application, use the following command:
   ```bash
   python3 main.py
   ```

This will start the server, and you can interact with the API for registration and authentication via seed phrase.


 **When using frontend frameworks, you will need to make a small change in the api folder, and replace render_templates with jsonify**

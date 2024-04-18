import rsa

def generate_key_pair():
    return rsa.newkeys(2048)

def encrypt_message(message, public_key):
    return rsa.encrypt(message.encode(), public_key)

def decrypt_message(encrypted_message, private_key):
    return rsa.decrypt(encrypted_message, private_key).decode()

def main():
    # Generate RSA key pairs for the bank and the client
    bank_private_key, bank_public_key = generate_key_pair()
    client_private_key, client_public_key = generate_key_pair()

    # Bank sends its public key to the client (during registration)
    bank_client_public_key = client_public_key

    # Authentication process
    # Step 1: Bank sends a challenge to the client
    challenge = "Please confirm your identity."
    encrypted_challenge = encrypt_message(challenge, bank_client_public_key)

    # Step 2: Client decrypts the challenge and sends it back encrypted with bank's public key
    decrypted_challenge = decrypt_message(encrypted_challenge, client_private_key)
    response = decrypted_challenge + " - Client's response."

    # Step 3: Bank verifies client's response
    encrypted_response = encrypt_message(response, bank_public_key)
    decrypted_response = decrypt_message(encrypted_response, bank_private_key)

    print("Decrypted response from client:", decrypted_response)

if __name__ == "__main__":
    main()

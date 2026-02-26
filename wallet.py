from ecdsa import SigningKey, SECP256k1
import binascii


class Wallet:
    def __init__(self):
        """
        Generate new wallet with private and public keys.
        """
        self.private_key = SigningKey.generate(curve=SECP256k1)
        self.public_key = self.private_key.get_verifying_key()

    def sign_transaction(self, transaction_hash):
        """
        Sign transaction hash using private key.
        """
        signature = self.private_key.sign(transaction_hash.encode())
        return binascii.hexlify(signature).decode()

    def get_address(self):
        """
        Return public key as wallet address.
        """
        return binascii.hexlify(self.public_key.to_string()).decode()

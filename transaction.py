import json
import hashlib


class Transaction:
    def __init__(self, sender, recipient, amount, signature=None):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature

    def to_dict(self):
        """
        Convert transaction to dictionary.
        """
        return self.__dict__

    def compute_hash(self):
        """
        Compute SHA-256 hash of transaction.
        """
        tx_string = json.dumps(self.to_dict(), sort_keys=True)
        return hashlib.sha256(tx_string.encode()).hexdigest()

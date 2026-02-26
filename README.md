# ⚡ AetherBlock

AetherBlock is a modular experimental blockchain framework written in Python.

It demonstrates core blockchain architecture in a clean, extensible, and developer-friendly way.

---

## 🔷 Core Features

- Proof-of-Work consensus
- Genesis block generation
- Transaction hashing
- Wallet key generation (ECDSA)
- Digital transaction signing
- Block validation
- REST API interaction
- Clean modular structure

---

## 🧱 Architecture Overview

AetherBlock consists of the following core components:

- `blockchain.py` – Core chain logic and consensus
- `transaction.py` – Transaction model and hashing
- `wallet.py` – Cryptographic key generation & signing
- `app.py` – REST API interface

The project is intentionally minimalistic to make blockchain internals transparent and easy to understand.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/aetherblock.git
cd aetherblock

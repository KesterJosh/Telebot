import requests

# Etherscan API key
ETHERSCAN_API_KEY = "P1T6WRTYS8RHXDXUAC6FKX1BIZ5TX9E8M2"

# Contract address
contract_address = "0xbD1b10DA53f82bA46b27Ac498BcaaB4d96591FBD"

# Fetch list of transactions involving the contract
contract_transactions_url = f"https://api.etherscan.io/api?module=account&action=txlist&address={contract_address}&startblock=0&endblock=99999999&apikey={ETHERSCAN_API_KEY}"
transactions_response = requests.get(contract_transactions_url)
transactions_data = transactions_response.json()

if transactions_data.get("status") == "1":
    transactions = transactions_data.get("result")

    # Create a set to store unique addresses
    unique_addresses = set()

    for tx in transactions:
        sender = tx["from"]
        receiver = tx["to"]

        if sender != contract_address and sender:
            unique_addresses.add(sender)

        if receiver != contract_address and receiver:
            unique_addresses.add(receiver)

    # Iterate through unique addresses and print them
    for address in unique_addresses:
        # Make sure address starts with "0x"
        if not address.startswith("0x"):
            address = "0x" + address
        print(f"Address: {address}")
else:
    print("Failed to fetch transactions.")

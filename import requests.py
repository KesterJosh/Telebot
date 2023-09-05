import requests
from web3 import Web3

# Etherscan API key
ETHERSCAN_API_KEY = "P1T6WRTYS8RHXDXUAC6FKX1BIZ5TX9E8M2"

# Ethereum node URL
infura_url = "https://mainnet.infura.io/v3/05e37ed816b34dc9bb71c8e0719aa081"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Contract address
contract_address = "0xbD1b10DA53f82bA46b27Ac498BcaaB4d96591FBD"

# Construct the Etherscan API URL
etherscan_api_url = f"https://api.etherscan.io/api?module=contract&action=getabi&address={contract_address}&apikey={ETHERSCAN_API_KEY}"

# Fetch the ABI using the Etherscan API
response = requests.get(etherscan_api_url)
data = response.json()

if data.get("status") == "1":
    token_abi = data.get("result")

    # Create contract instance
    token_contract = web3.eth.contract(address=contract_address, abi=token_abi)

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

            if sender != contract_address:
                unique_addresses.add(sender)

            if receiver != contract_address:
                unique_addresses.add(receiver)

        # Iterate through unique addresses and get token balance
        for address in unique_addresses:
        # Make sure address starts with "0x"
        if not address.startswith("0x"):
            address = "0x" + address
            token_balance = token_contract.functions.balanceOf(address).call()
            print(f"Token balance of address {address}: {token_balance}")
    else:
        print("Failed to fetch transactions.")
else:
    print("Failed to fetch ABI.")

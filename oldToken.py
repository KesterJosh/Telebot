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

    try:
        # Create contract instance
        token_contract = web3.eth.contract(address=contract_address, abi=token_abi)

        address_to_check = "0x6d3fd2dba53c072d272b4f9ab319b63de62618fe"

        # Convert the address to checksum format
        checksum_address = Web3.to_checksum_address(address_to_check)

        token_balance = token_contract.functions.balanceOf(checksum_address).call()

        print(f"Tokens burned from {checksum_address}: {token_balance}") 
    except Exception as e:
        print(f"An error occurred while checking balance: {e}")
        token_balance = None  # Set token_balance to None in case of an exception
else:
    print("Failed to fetch ABI.")
    token_balance = None  # Set token_balance to None if ABI fetching failed

# Now token_balance will either have a valid balance or be None in case of an exception or ABI fetching failure.

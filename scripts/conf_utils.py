from brownie import accounts, config, network

FAUCET_URL = 'https://faucet.kintsugi.themerge.dev/'

# Thanks to Patrick Collins ; inspired by his helpful_scripts
NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "ganache"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS + [
    "mainnet-fork",
    "binance-fork",
    "matic-fork",
]

def get_accounts(number=None):
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0:1]
    account = accounts.from_mnemonic(config["wallets"]["from_mnemonic"], count=2)
    return account

import sys
from brownie import FirstContract
#from brownie import * 
from scripts import conf_utils

def main():
    # accounts setup
    accounts = conf_utils.get_accounts()
    if ( accounts[0].balance() == 0):
        print(f'You should get some test ehters.\nFaucet: {conf_utils.FAUCET_URL}')
        sys.exit(1)

    # deploy a smart contract
    firstContract = FirstContract.deploy('My new contract', {"from": accounts[0]})
    print(firstContract.getMessage())
    
    # interact with the SC
    firstContract.updateMessage('My contract updated!')
    print(firstContract.getMessage())



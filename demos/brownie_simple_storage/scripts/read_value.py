from brownie import SimpleStorage, accounts, config


def read_contract():
    # -1 Gets the most recent contract deployment
    # 0 Gets the first contract deployment
    simple_storage = SimpleStorage[-1]
    # ABI
    # Address
    print(simple_storage.retrieve())


def main():
    read_contract()

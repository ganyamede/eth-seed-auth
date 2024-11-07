from eth_account import Account
from mnemonic import Mnemonic

Account.enable_unaudited_hdwallet_features()

class ConnectWallet:
    def __init__(self, seedPhase: str = None) -> None:
        if type(seedPhase).__name__ == 'list':
            seedPhase = ' '.join(map(str, seedPhase))


        print(seedPhase)
        self.seedPhase = seedPhase
        self.account = Account.from_mnemonic(self.seedPhase)
        self.address = self.account.address

class CreateWallet(ConnectWallet):
    def __init__(self) -> None:
        mnemonic = Mnemonic("english")
        self.seedPhase = mnemonic.generate(strength=128)

        super().__init__(self.seedPhase)
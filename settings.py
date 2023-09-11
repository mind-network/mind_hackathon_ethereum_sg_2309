
CONTRACT_ADDRESS_NS = '0xfE428F0949b88b74EfDAE2b79e34EeaF01eB5225'
CONTRACT_ADDRESS_MSG = '0xfE428F0949b88b74EfDAE2b79e34EeaF01eB5225'

CONTRACT_ABI_NS = [
        {
                "anonymous": False,
                "inputs": [
                        {
                                "indexed": True,
                                "internalType": "address",
                                "name": "wallet",
                                "type": "address"
                        },
                        {
                                "indexed": False,
                                "internalType": "bytes",
                                "name": "pk2",
                                "type": "bytes"
                        },
                        {
                                "indexed": False,
                                "internalType": "bytes",
                                "name": "pkb",
                                "type": "bytes"
                        }
                ],
                "name": "KeysUpdated",
                "type": "event"
        },
        {
                "inputs": [
                        {
                                "internalType": "bytes",
                                "name": "_pk2",
                                "type": "bytes"
                        },
                        {
                                "internalType": "bytes",
                                "name": "_pkb",
                                "type": "bytes"
                        }
                ],
                "name": "setPKNS",
                "outputs": [],
                "stateMutability": "nonpayable",
                "type": "function"
        },
        {
                "inputs": [
                        {
                                "internalType": "address",
                                "name": "_wallet",
                                "type": "address"
                        }
                ],
                "name": "getPKNS",
                "outputs": [
                        {
                                "internalType": "bytes",
                                "name": "pk2",
                                "type": "bytes"
                        },
                        {
                                "internalType": "bytes",
                                "name": "pkb",
                                "type": "bytes"
                        }
                ],
                "stateMutability": "view",
                "type": "function"
        }
]

CONTRACT_ABI_MSG = [
        {
                "anonymous": False,
                "inputs": [
                        {
                                "indexed": True,
                                "internalType": "address",
                                "name": "wallet",
                                "type": "address"
                        },
                        {
                                "indexed": False,
                                "internalType": "bytes",
                                "name": "C1",
                                "type": "bytes"
                        }
                ],
                "name": "KeysUpdated",
                "type": "event"
        },
        {
                "inputs": [
                        {
                                "internalType": "bytes",
                                "name": "_C1",
                                "type": "bytes"
                        }
                ],
                "name": "setMSG",
                "outputs": [],
                "stateMutability": "nonpayable",
                "type": "function"
        },
        {
                "inputs": [
                        {
                                "internalType": "address",
                                "name": "_wallet",
                                "type": "address"
                        }
                ],
                "name": "getMSG",
                "outputs": [
                        {
                                "internalType": "bytes",
                                "name": "C1",
                                "type": "bytes"
                        }
                ],
                "stateMutability": "view",
                "type": "function"
        }
]
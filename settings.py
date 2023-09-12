
CONTRACT_ADDRESS_NS = '0xd2eE09AB4917972697c8352325f7E03bA4ce2449'
CONTRACT_ADDRESS_MSG = '0x8536B1e36F10234b13Ca7f8F58965B0F85E36b68'

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
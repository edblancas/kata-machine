from src.util.local_types import BinaryNode

tree = BinaryNode(20,
                  BinaryNode(10,
                             BinaryNode(5,
                                        right=BinaryNode(7)),
                             BinaryNode(15)),
                  BinaryNode(50,
                             BinaryNode(30,
                                        BinaryNode(29),
                                        BinaryNode(45)),
                             BinaryNode(100)))

tree2 = BinaryNode(20,
                  BinaryNode(10,
                             BinaryNode(5,
                                        left=None,
                                        right=BinaryNode(7)),
                             BinaryNode(15)),
                  BinaryNode(50,
                             BinaryNode(30,
                                        BinaryNode(29,
                                                   BinaryNode(21)),
                                        BinaryNode(45,
                                                   right=BinaryNode(49))),
                             BinaryNode(100)))

from src.util.local_types import BinaryNode

tree = BinaryNode(20,
                  right=BinaryNode(50,
                                   right=BinaryNode(100),
                                    left=BinaryNode(30,
                                            right=BinaryNode(45),
                                            left=BinaryNode(29))),
                  left=BinaryNode(10,
                                  left=BinaryNode(5, left=None,
                                                     right=BinaryNode(7)),
                                  right=BinaryNode(15)))

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

from src.globals_d import BinaryNode

tree = BinaryNode(20,
                  right=BinaryNode(50,
                                   right=BinaryNode(100),
                                   left=BinaryNode(30,
                                                   right=BinaryNode(45),
                                                   left=BinaryNode(29)
                                                   )
                                   ),
                  left=BinaryNode(10,
                                  right=BinaryNode(15),
                                  left=BinaryNode(5,
                                                  right=BinaryNode(7)
                                                  )
                                  )
                  )

# Define the second tree (tree2)
tree2 = BinaryNode(20,
                   right=BinaryNode(50,
                                    left=BinaryNode(30,
                                                    left=BinaryNode(29,
                                                                    left=BinaryNode(21)
                                                                    ),
                                                    right=BinaryNode(45,
                                                                     right=BinaryNode(49)
                                                                     )
                                                    )
                                    ),
                   left=BinaryNode(10,
                                   right=BinaryNode(15),
                                   left=BinaryNode(5,
                                                   right=BinaryNode(7)
                                                   )
                                   )
                   )

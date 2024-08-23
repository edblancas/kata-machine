from src.util.linked_list import ListInterface

def test_list(self, list: ListInterface[int]) -> None:
    list.append(5)
    list.append(7)
    list.append(9)

    self.assertEqual(list.get(2), 9)
    self.assertEqual(list.remove_at(1), 7)
    self.assertEqual(list.length, 2)

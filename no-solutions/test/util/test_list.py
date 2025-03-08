from src.util.linked_list import ListInterface

def test_list(self, list: ListInterface[int]) -> None:
    list.append(5)
    list.append(7)
    list.append(9)

    self.assertEqual(list.get(2), 9)
    self.assertEqual(list.remove_at(1), 7)
    self.assertEqual(list.length, 2)

    list.append(11)
    self.assertEqual(list.remove_at(1), 9)
    self.assertEqual(list.remove(9), None)
    self.assertEqual(list.remove_at(0), 5)
    self.assertEqual(list.remove_at(0), 11)
    self.assertEqual(list.length, 0)

    list.prepend(5)
    list.prepend(7)
    list.prepend(9)

    self.assertEqual(list.get(2), 5)
    self.assertEqual(list.get(0), 9)
    self.assertEqual(list.remove(9), 9)
    self.assertEqual(list.length, 2)
    self.assertEqual(list.get(0), 7)

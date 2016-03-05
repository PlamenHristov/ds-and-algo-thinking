import unittest
from MyTake.src.chapter3.LinkedList import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_insert(self):
        l_list = LinkedList()
        l_list.insert("David")
        assert l_list.head.get_data() == "David"
        assert l_list.head.get_next() is None

    def test_insert_two(self):
        l_list = LinkedList()
        l_list.insert("David")
        l_list.insert("Thomas")
        self.assertEqual(l_list.head.getData(), "Thomas")
        head_next = l_list.head.get_next()
        self.assertEqual(head_next.getData(), "David")

    def test_nextNode(self):
        l_list = LinkedList()
        l_list.insert("Jacob")
        l_list.insert("Pallymay")
        l_list.insert("Rasmus")
        self.assertEqual(l_list.head.getData(), "Rasmus")
        head_next = l_list.head.get_next()
        self.assertEqual(head_next.getData(), "Pallymay")
        head_next = l_list.head.get_next()
        self.assertEqual(head_next.getData(), "Jacob")

    def test_positive_search(self):
        l_list = LinkedList()
        l_list.insert("Jacob")
        l_list.insert("Pallymay")
        l_list.insert("Rasmus")
        found = l_list.search("Rasmus")
        self.assertEqual(found.head.getData(), "Rasmus")
        found = l_list.search("Pallymay")
        self.assertEqual(found.head.getData(), "Pallymay")
        found = l_list.search("Jacob")
        self.assertEqual(found.head.getData(), "Jacob")

    def test_searchNone(self):
        l_list = LinkedList()
        l_list.insert("Jacob")
        l_list.insert("Pallymay")
        # make sure reg search works
        found = l_list.search("Jacob")
        self.assertEqual(found.getData(), "Jacob")
        # with pytest.raises(ValueError):
        #     l_list.search("Vincent")

    def test_delete(self):
        l_list = LinkedList()
        l_list.insert("Jacob")
        l_list.insert("Pallymay")
        l_list.insert("Rasmus")
        l_list.deleteValue("Rasmus")
        self.assertEqual(l_list.head.getData(), "Pallymay")
        self.assertTrue(l_list.deleteValue("Jacob"))
        l_list.printList()

    def test_delete_value_not_in_list(self):
        l_list = LinkedList()
        l_list.insert("Jacob")
        l_list.insert("Pallymay")
        l_list.insert("Rasmus")
        with self.assertRaises(ValueError):
            l_list.deleteValue("Sunny")

    def test_delete_empty_list(self):
        l_list = LinkedList()
        with self.assertRaises(ValueError):
            l_list.deleteValue("Sunny")

    def test_delete_next_reassignment(self):
        l_list = LinkedList()
        l_list.insert("Jacob")
        l_list.insert("Cid")
        l_list.insert("Pallymay")
        l_list.insert("Rasmus")
        l_list.deleteValue("Pallymay")
        l_list.deleteValue("Cid")
        self.assertEqual(l_list.head.next.getData(), "Jacob")


if __name__ == '__main__':
    unittest.main()

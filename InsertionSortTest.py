import unittest
import InsertionSort

class InsertionSortTest(unittest.TestCase): # herança
    def insertion_sort_test(self):
        numbers = [5,2,7,56,98,12,15,37,27]
        result = InsertionSort.insertion_sort(numbers)
        print(result)
        self.assertEqual(result, 31)


# if __name__ == '__main__':
unittest.main()
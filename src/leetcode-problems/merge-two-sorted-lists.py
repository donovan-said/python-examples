LT1 = [1,2,4]
LT2 = [1,3,4]

class MergeSortedLists:
    def merge_two_sorted_lists(list1, list2) -> list:
        """_summary_

        Args:
            list1 (_type_): _description_
            list2 (_type_): _description_

        Returns:
            list: _description_
        """

        list1.extend(list2)
        merged_list = sorted(list1)
        print(merged_list)



if __name__ == "__main__":
    MergeSortedLists.merge_two_sorted_lists(LT1, LT2)

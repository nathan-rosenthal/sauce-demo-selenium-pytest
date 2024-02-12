class Helpers:

    @staticmethod
    def compare_list_items_for_descending_order(list_items):
        list_is_sorted_descending = True
        i = 0
        # Iterate over list and check values are correctly sorted descending
        while i < len(list_items) - 1:
            if list_items[i] >= list_items[i + 1]:
                i += 1
            else:
                list_is_sorted_descending = False
                break
        return list_is_sorted_descending

    @staticmethod
    def compare_list_items_for_ascending_order(list_items):
        list_is_sorted_ascending = True
        i = 0
        # Iterate over list and check values are correctly sorted ascending
        while i < len(list_items) - 1:
            if list_items[i] <= list_items[i + 1]:
                i += 1
            else:
                list_is_sorted_ascending = False
                break
        return list_is_sorted_ascending

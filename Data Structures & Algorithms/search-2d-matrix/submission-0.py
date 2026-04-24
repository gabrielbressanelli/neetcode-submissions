class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outter_min = 0
        outter_max = (len(matrix) - 1)
        list_max = (len(matrix[0]) - 1)


        while outter_min <= outter_max:

            list_searcher = outter_min + (outter_max - outter_min) // 2

            list_min = 0

            if target >= matrix[list_searcher][list_min] and target <= matrix[list_searcher][list_max]:
                while list_min <= list_max:

                    list_mid = list_min + (list_max - list_min) //2
                    if matrix[list_searcher][list_mid] == target:
                        return True

                    elif matrix[list_searcher][list_mid] < target:
                        list_min = list_mid + 1
                    else:
                        list_max = list_mid - 1
                return False

            elif target > matrix[list_searcher][list_min] and target > matrix[list_searcher][list_max]:
                outter_min = list_searcher + 1
            else: 
                outter_max = list_searcher - 1
        return False




            

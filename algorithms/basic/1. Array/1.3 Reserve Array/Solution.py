class Solution:
    def rotage(array, k):
        n = len(array)
        k = k % n

        def reverse(array, start, end):
            while start < end:
                array[start], array[end] = array[end], array[start]
                start += 1
                end -=1

            # Đảo ngược các phần của mảng
        reverse(array, 0, n - 1)       # Đảo ngược toàn bộ mảng
        reverse(array, 0, k - 1)       # Đảo ngược k phần tử đầu tiên
        reverse(array, k, n - 1)       # Đảo ngược n-k phần tử còn lại
        
        return array


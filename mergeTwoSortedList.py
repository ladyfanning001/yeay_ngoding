#input [1, 2, 4] [1, 3, 4]
#output [1, 1, 2, 3, 4, 4]

def merge_two_sorted_list(arr1, arr2):
    result = []
    i, j = 0, 0  # Pointer untuk kedua list

    # Gabungkan kedua list selama masih ada elemen yang tersisa di keduanya
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Tambahkan sisa elemen dari arr1 jika ada
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    # Tambahkan sisa elemen dari arr2 jika ada
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution :
    def merge_two_sorted_list_v2(self, l1 : ListNode, l2 : ListNode) -> ListNode :
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val :
                tail.next = l1
                l1 = l1.next
            else :
                tail.next = l2
                l2 = l2.next
        
        if l1 :
            tail.next = l1
        elif l2 :
            tail.next = l2
            
        return dummy.next
            

# Contoh penggunaan
arr1 = [1, 2, 4]
arr2 = [1, 3, 4]

print(merge_two_sorted_list(arr1, arr2))  

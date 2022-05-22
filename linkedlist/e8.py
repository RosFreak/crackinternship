def multiplyTwoList(head1, head2):
    num1 = 0
    num2 = 0
 
    first_ptr = first.head
    second_ptr = second.head
     
    while first_ptr != None or second_ptr != None:
        if first_ptr != None:
            num1 = (num1 * 10) + first_ptr.data
            first_ptr = first_ptr.next
     
        if second_ptr != None:
            num2 = (num2 * 10) + second_ptr.data
            second_ptr = second_ptr.next
     
    return num1 * num2
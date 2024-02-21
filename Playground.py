def merge_sort(unsorted_list):
    if len(unsorted_list) == 1: #base case. if 1 elemente return the list
        return unsorted_list
    
    mid_point = int(len(unsorted_list)/2)   #Find the middle

    #Divide the list into halves
    first_half = unsorted_list[:mid_point]  
    second_half = unsorted_list[mid_point:]

    #Recursively pass the two sub lists
    half_a = merge_sort(first_half)
    half_b = merge_sort(second_half)

    return merge(half_a, half_b)

def merge(first_sublist, second_sublist):
    i = j = 0
    merged_list = []
    print(len(first_sublist))
    print(len(second_sublist))
    while i < len(first_sublist) and j < len(second_sublist):
        if first_sublist[i] < second_sublist[j]:
            print("[1]Added from first: " + str(first_sublist[i]))
            merged_list.append(first_sublist[i])
            i += 1
        else:
            print("[1]Added from second: " + str(second_sublist[j]))
            merged_list.append(second_sublist[j])
            j += 1
    while i < len(first_sublist):
        print("[2]Added from first: " + str(first_sublist[i]))
        merged_list.append(first_sublist[i])
        i += 1
    while j < len(second_sublist):
        print("[2]Added from second: " + str(second_sublist[j]))
        merged_list.append(second_sublist[j])
        j += 1

    return merged_list

a = [ 9, 14, 7, 42, 691, 130, 160, 124]
print(merge_sort(a))
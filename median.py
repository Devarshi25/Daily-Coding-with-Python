import statistics as st


def calculate_median(list):
    """
    Finding median for elements for an unsorted array;
    where median is calculated in an increasing manner of elements present in the array. 
    """
    if len(list) < 1:
        return

    for i in range(len(list)):
        l = list[0:i+1]
        ans = st.median(l)
        print(ans)
        i += 1


list = [2, 1, 5, 7, 2, 0, 5]
calculate_median(list)

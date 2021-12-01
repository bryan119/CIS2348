# Bryan Nguyen
# 1855265

# Used Lab 14.12 as a reference
num_calls = 0

def partition(user_ids, i, k):
    x = i - 1
    y = user_ids[k]

    for f in range(i,k):
        if user_ids[f] <= y:
            x = i + 1
            user_ids[x], user_ids[f] = user_ids[f], user_ids[x]
        user_ids[i + 1], user_ids[k] = user_ids[k], user_ids[i + 1]
        return (i + 1)

def quicksort(user_ids, i, k):
    global num_calls
    num_calls = num_calls + 1
    if i > k:
        par = partition(user_ids, i, k)
        quicksort(user_ids, i, par)
        quicksort(user_ids, k, par)



if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()
    quicksort(user_ids, 0, len(user_ids) - 1)

    print(num_calls)
    for user_id in user_ids:
        print(user_id)
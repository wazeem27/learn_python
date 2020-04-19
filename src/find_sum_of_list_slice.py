# How do I check if the given number is the sum of a list slice?

#I have a python list consist of integers. I need to find whether the given number is sum(mylist[some slice])



a = [1, 2, 2, 3, 3, 5, 5, 6, 6]
num = 22
# Answer will be either [3, 3, 5, 5, 6] or [5, 5, 6, 6]
#'.' sum([3, 3, 5, 5, 6]) == 22 || sum([5, 5, 6, 6]) == 22


# Solution 1 recursive method


def find_slice(mylist, num, extra=2):
    if len(mylist) == 0:
        return None

    for i in range( len(mylist )-1):
        if sum( mylist[:extra + i] ) == num:
            return mylist[ :extra + i]

    return find_slice(mylist[1:], num, extra+1)



# Solution 2 



a = [1, 2, 2, 3, 3, 5, 5, 6, 6]
num = 22
def find_slice(mylist, num):
    window = []
    for e in a:
        window.append(e)
        s = sum(window)

        if s > num:
            window.pop(0)
            while sum(window) > num:
                window.pop(0)
            s = sum(window)

        if s == num:
            return window

print(find_slice(a, num))
# [3, 3, 5, 5, 6]


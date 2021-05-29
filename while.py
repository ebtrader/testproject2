# def sum_to(n):
#     """ Return the sum of 1+2+3+ ...n """
#     ss = 0
#     v = 1
#     while v <= n:
#         ss = ss + v # this is the function
#         v = v + 1 # this is the counter
#
#     return ss
#
# print(sum_to(4))
# print(sum_to(1000))

# def sum_to(n):
#     """ Return the sum of 1+2+3+ ...n """
#     ss = 0
#     for v in range(n+1):
#         ss = ss + v
#     return ss
#
# print(sum_to(4))
# print(sum_to(11))


def sum_to(n):
    """ Return the sum of 1+2+3+ ...n """
    ss = 0
    for v in range(3,n+1):
        ss = ss + v
    return ss

print(sum_to(4))
print(sum_to(11))



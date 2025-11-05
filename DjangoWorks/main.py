# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# def compress(s):
#     freq = [0]*26
#     for i in range(0, len(s), 2):
#         freq[ord(s[i])-ord('a')] += int(s[i+1])
#     result = ""
#     for i in range(26):
#         if freq[i] != 0:
#             result += chr(i + ord('a')) + str(freq[i])
#     return result
#
# s = input()
# print(compress(s))

def max_subarray_sum(a):
    max_so_far = a[0]
    curr = a[0]
    for i in range(1, len(a)):
        curr = max(a[i], curr + a[i])
        max_so_far = max(max_so_far, curr)
    print(max_so_far)

a = list(map(int, input().split()))
max_subarray_sum(a)


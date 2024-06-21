odd= [1,3,5,7,9]
even= [2,4,6,8]

even.extend(odd)
print(" printing even.append {}".format(even))

even.sort()
print(" printing even.sort {}".format(even))

even.sort(reverse=True)  # rearrange
print(" printing even.sort(reverse=true) {}".format(even))

othersort= even
even.sort(reverse=False)         # rearrange
print(" printing even.sort(reverse=false) {}".format(even))
print(" printing othersort {}".format(othersort))

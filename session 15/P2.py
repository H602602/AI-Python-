def anagram(a, b):
    # c=list(a)
    # d=list(b)
    if sorted(a)==sorted(b):
        print("anagram")
    else:
        print("This is not anagram")
anagram("race","care")


def my_min(*a):
    minsayi = max(list(a))
    #print(minsayi)
    for i in list(a):
        if i < minsayi:
            minsayi = i
    return minsayi

print(my_min(-100))
 
def CountFrequency(my_list):
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    for key, value in freq.items():
        print ("% d : % d"%(key, value))
if __name__ == "__main__":
    my_list =[1, 1, 2,2,4,4,6,3,6,7,8,4,7,8,9,3,8,9,10]
 
    CountFrequency(my_list)

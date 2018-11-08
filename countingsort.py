
# coding: utf-8

# In[20]:


def countingsort(array):
    samplearr = list(range(100))
    countarr = [0] * 100
    sortedarr = list()
    
    for itr in array:
        countarr[itr] += 1
    
    for jtr in range(len(countarr)):
        if countarr[jtr] != 0:
            while countarr[jtr] != 0:
                sortedarr.append(samplearr[jtr])
                countarr[jtr] -= 1
    return sortedarr


# In[21]:


import random
array = [random.randint(0,99) for _ in range(10)]
print("Unsorted Array:",array)
print("Sorted Array:", countingsort(array))


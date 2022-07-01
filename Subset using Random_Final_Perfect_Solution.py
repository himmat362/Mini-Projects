#Subset problem where the sum of the subset is zero
import random as r


def random(subset,_final_list_):
    #chosing a new subset randomly from the given set 
    new_list=r.sample(subset, k=r.randint(3,6))
    #sorting the new_list
    new_list=sorted(new_list)
    if check_sum(new_list)==True:
        #checking whether the subset already exists in _final_list_
        if new_list in _final_list_:
            return random(subset, _final_list_)
        else:
            #appending _final_list_ with the new_list
            _final_list_.append(new_list)
            return random(subset, _final_list_)


#to check the sum of the selected subset
def check_sum(_new_list):
    if sum(_new_list)==0:
        return True
    else:
        return False


subset=[1,2,7,5,-9,-1,3,-2,-4]
final_list=[]
List=[]
#number of iterations
for i in range(10000):
    List=random(subset,final_list)
print(final_list)

#subset problem
import random as r


def random(subset,_final_list_):
    new_list=r.sample(subset, k=5)
    new_list=sorted(new_list)
    if check_sum(new_list)==True:
        if new_list in _final_list_:
            return random(subset, _final_list_)
        else:
            _final_list_.append(new_list)
            return random(subset, _final_list_)


def check_sum(_new_list):
    if sum(_new_list)==0:
        return True
    else:
        return False


subset=[1,2,7,5,-9,-1,3,-2,-4]
final_list=[]
List=[]
for i in range(10000):
    List=random(subset,final_list)
print(final_list)
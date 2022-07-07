#combo-finder problem
import random as r


def combo_finder(Listed,Lower_bound,Upper_bound,already_listed):
    #choosing random combination of values
    new_Listed=r.sample(list(Listed.keys()),k=r.randint(2, len(Listed)-1))
    #sorting of the chosen list
    list(new_Listed)
    #check the sum of list
    if check_sum(Listed,new_Listed,Lower_bound,Upper_bound)==True:
	#appending the list
        already_listed.add(tuple(new_Listed))
        return combo_finder(Listed, Lower_bound, Upper_bound, already_listed)


def check_sum(Listed,new_Listed,Lower_bound,Upper_bound):
    #sum of the values in chosen list
    sum1 = sum([ Listed[i] for i in new_Listed])
    if sum1>=Lower_bound and sum1<=Upper_bound:
        return True
    else:
        return False


Lower_bound=(290)
Upper_bound=(320)
Listed={'p1':10, 'p2':15, 'p3':20, 'p4':25, 'p5':30, 'p6':35, 'p7':50,'p8':40, 'p9':55, 'p10':60, 'p11':65, 'p12':75, 'p13':70,'p14':45}
already_listed=set()
for w in range(1000):
    List=combo_finder(Listed, Lower_bound, Upper_bound, already_listed)
for z in already_listed:
	print (z)
print(len(already_listed))

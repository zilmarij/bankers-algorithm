
#processes
#Resrcs allocated to each process
#resrc reqmts of each process
#REsrcs available

#Matrix r_allocated
#Matrix r_required
#Matrix difference
#Vector r_available
#Vector safe_sequence
import random 

def bankers_algo(r_allctd,r_reqd,r_avlbl):
    n_processes = len(r_allctd)
    n_resrcs = len(r_avlbl)
    r_diff=[[0 for i in range(n_resrcs)]for j in range(n_processes)]
    for i in range(n_processes):  #processes
        for j in range(n_resrcs):   #resources
            r_diff[i][j] = r_reqd[i][j] - r_allctd[i][j]
    print("Resources reqd. ",r_diff)
    #find safe sequence
    count=0
    sequence=[]
    while len(sequence)!=n_processes:
        for i in range(n_processes):
            if i in sequence:
                continue
            count = 0
            for j in range(n_resrcs):
                if r_avlbl[j] >= r_diff[i][j]:
                    count+=1
                    if count == n_resrcs:    
                        sequence.append(i)
                        for x in range(n_resrcs):
                            r_avlbl[x]+=r_diff[i][x]
                            r_diff[i][x]=0
            if count == n_resrcs:
                break
        if count != n_resrcs:
            return sequence
                        



    return sequence




if __name__ == '__main__':
    n_processes = 4; n_resrcs=5
    r_allocated=[[random.randrange(3) for j in range(n_resrcs)]for i in range(n_processes)]
    r_reqd=[[r_allocated[i][j]+random.randrange(3) for j in range(n_resrcs)]for i in range(n_processes)]
    r_available=[random.randrange(7) for i in range(n_resrcs)]

    print("Resources allocated ",r_allocated)
    print("Resources required total ",r_reqd)
    print("Resources available ",r_available)

    seq=bankers_algo(r_allocated,r_reqd,r_available)
    print("Safe sequence of Process_ids :", seq)
    if len(seq) < n_processes:
        print("Safe sequence could not be achieved with all the process requirements being satisfied")

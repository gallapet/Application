

def solution(A):
    ans = [0, 0, 0, 0, 0]
    dep = ["Cardiology", "Neurology", "Orthopaedics", "Gynaecology", "Oncology"]
    for word in A:
        if word in dep:
            ans[dep.index(word)] += 1
        else:
            pass
    
    return max(ans)






    '''C = A.count("Cardiology")
    N = A.count("Neurology")
    O_r = A.count("Orthopaedics")
    G = A.count("Gynaecology")
    O_n = A.count("Oncology")
    ans = [C, N, O_r, G, O_n]
    print(max(ans))'''
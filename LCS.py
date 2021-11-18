#Austin Gallup
#11/17/21
#Common subsequence


def lcs(string_one, string_two, m , n):

    if(m == 0 or n == 0):
        return 0
    elif string_one[m-1] == string_two[n-1]:
        return 1 + lcs(string_one,string_two, m-1, n-1)
    else:
        return max(lcs(string_one, string_two, m, n-1), lcs(string_one, string_two, m-1, n))

string_one = "ASDFASDGASDVGDADAS"
string_two = "ASDFASDFASDVARG"

print ("Length of LCS: " , lcs(string_one, string_two, len(string_one), len(string_two)))


def lcs_with_dynamic_prog(string_one, string_two):
    m = len(string_one)
    n = len(string_two)

    arr = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i  == 0 or j == 0:
                arr[i][j] = 0
            elif string_one[i-1] == string_two[j-1]:
                arr[i][j] = arr[i-1][j-1]+1
            else:
                arr[i][j] = max(arr[i-1][j] , arr[i][j-1])
    
    return arr[m][n]

print ("length of LCS: " ,  lcs_with_dynamic_prog(string_one, string_two))

            

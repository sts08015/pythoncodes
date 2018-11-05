def make_cipherTable(arr):
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        tmp1 = []
        tmp2 = []
        x = ' '
        tmp1 = x.join(s[:i]).split()
        tmp2 = x.join(s[i:]).split()  # tmp2 + tmp1
        for j in range(len(tmp2)):
            arr[i][j] = tmp2[j]
        for j in range(len(tmp1)):
            arr[i][j+len(tmp2)] = tmp1[j]
def make_cipherText(arr,string):
    ans = ""
    for i in range(1,len(string)+1):
        x = ord(string[i-1])-65
        ans += arr[i-1][x]

    return ans
def print_cipherTable(arr):
    for i in range(26):
        for j in range(26):
            print(arr[i][j],end=" ")
        print("")

def main():
    ct = [[' ']*26 for i in range(26)]
    make_cipherTable(ct)
    print_cipherTable(ct)
    plainText = input("plain text: ")
    cipherText = make_cipherText(ct,plainText.upper())
    print("cipher text:", cipherText)
    
main()

def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)
    
    # Inicializar uma matriz para armazenar os comprimentos das LCSs
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Preencher a matriz dp com os comprimentos das LCSs
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstruir a subsequência a partir da matriz dp
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    lcs.reverse()
    return dp[m][n], ''.join(lcs)

# Exemplo de uso
str1 = "ABCDGH"
str2 = "AEDFHR"
length, sequence = longest_common_subsequence(str1, str2)
print(f"Comprimento da LCS: {length}")
print(f"Sequência LCS: {sequence}")

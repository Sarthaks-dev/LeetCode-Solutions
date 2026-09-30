class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        m = len(matrix[0])
        total = n*m
        c = 0
        ans = []
        rowst = 0
        rowend = n-1
        colst = 0
        colend = m-1
        while c<total:
            for i in range(colst, colend+1):
                ans.append(matrix[rowst][i])
                c+=1
            rowst+=1
            if c==total:
                break
            for i in range(rowst, rowend+1):
                ans.append(matrix[i][colend])
                c+=1
            colend-=1
            if c==total:
                break
            for i in range(colend, colst-1,-1):
                ans.append(matrix[rowend][i])
                c+=1
            rowend-=1
            if c==total:
                break
            for i in range(rowend, rowst-1,-1):
                ans.append(matrix[i][colst])
                c+=1
            colst+=1
            if c==total:
                break
        return ans
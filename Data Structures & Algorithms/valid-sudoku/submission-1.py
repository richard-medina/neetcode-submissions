class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        filas = {}

        for i in range (9):
            for j in range (9):
                filas[('f'+str(i), board[i][j])] = 1 + filas.get(('f'+str(i), board[i][j]), 0)

        columns = {}

        for i in range (9):
            for j in range (9):
                columns[('c'+str(i), board[j][i])] = 1 + columns.get(('c'+str(i), board[j][i]), 0)
        
        boxes = {}

        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        boxes[('b'+str(3*i+j), board[3*i+k][3*j+l])] = 1 + boxes.get(('b'+str(3*i+j), board[3*i+k][3*j+l]), 0)


        overall_info = filas | columns | boxes
        keys_info = list(overall_info.keys())
        counter = []

        for i in range(len(overall_info)):
            if keys_info[i][1] == '.':
                continue
            else:
                counter.append(overall_info[keys_info[i]])
    
        return all(x == 1 for x in counter) 

        
# Problem Title - Find Winner on a Tic Tac Toe Game
# Date - 20251205

class Solution:
    def validate_diagonal(self, sec_prev: List[int], prev: List[int], curr: List[int]) -> bool:
        # Sort these by row and then col
        combined_list = [sec_prev, prev, curr]
        sorted_list = sorted(combined_list, key=lambda index: index[0])
        print(f"sorted_list: {sorted_list}")

        # if ((abs(sorted_list[0][0]-sorted_list[1][0]) == 1) and (abs(sorted_list[0][1]-sorted_list[1][1]) == 1)) \
        # and ((abs(sorted_list[1][0]-sorted_list[2][0]) == 1) and (abs(sorted_list[1][1]-sorted_list[2][1]) == 1)):
        if (sorted_list[1] == [1,1]) and (((sorted_list[0]==[0,2]) and (sorted_list[2]==[2,0])) or ((sorted_list[0]==[0,0]) and (sorted_list[2]==[2,2]))):
            return True
        return False

    def tictactoe(self, moves: List[List[int]]) -> str:
        # My first solution - 76/101 test case passed - does not cover un-consecutive win-moves
        """
        prev_a = None
        sec_prev_a = None
        prev_b = None
        sec_prev_b = None

        for index, move in enumerate(moves):
            if index%2 == 0:
                player = 0    # denotes 'X' (player 'A')
            else:
                player = 1    # denotes 'O' (player 'B')
            if player == 0:
                curr_a = move
                # print(f"curr_a: {curr_a}; prev_a: {prev_a}; sec_prev_a: {sec_prev_a}")
                if (sec_prev_a is None) or (prev_a is None):
                    sec_prev_a = prev_a
                    prev_a = curr_a
                    continue
                if sec_prev_a[0] == prev_a[0] == curr_a[0]:   # If all last 3 moves have same row
                    return 'A'
                if sec_prev_a[1] == prev_a[1] == curr_a[1]:   # If all last 3 moves have same col
                    return 'A'
                diagonal_flag = self.validate_diagonal(sec_prev_a, prev_a, curr_a)
                if diagonal_flag:
                    return 'A'
                sec_prev_a = prev_a
                prev_a = curr_a
            else:
                curr_b = move
                if (sec_prev_b is None) or (prev_b is None):
                    sec_prev_b = prev_b
                    prev_b = curr_b
                    continue
                if sec_prev_b[0] == prev_b[0] == curr_b[0]:   # If all last 3 moves have same row
                    print("1")
                    return 'B'
                if sec_prev_b[1] == prev_b[1] == curr_b[1]:   # If all last 3 moves have same col
                    print("2")
                    return 'B'
                diagonal_flag = self.validate_diagonal(sec_prev_b, prev_b, curr_b)
                if diagonal_flag:
                    print("3")
                    return 'B'
                sec_prev_b = prev_b
                prev_b = curr_b

        if len(moves) != 9:
            return "Pending"
        return "Draw"
        """

        board = []

        # 0 in board denotes player 'A' and 1 denotes player 'B'
        for i in range(3):
            board.append([])
            for j in range(3):
                board[i].append(-99)
        
        for ind, move in enumerate(moves):
            if ind%2 == 1:
                board[move[0]][move[1]] = 1
            else:
                board[move[0]][move[1]] = 0

        # Check for each row
        for i in range(3):
            if sum(board[i]) == 0:
                return 'A'
            if sum(board[i]) == 3:    # 1+1+1
                return 'B'
        
        # Check for each column
        for j in range(3):
            sum1 = sum([board[i][j] for i in range(3)])
            if sum1 == 0:
                return 'A'
            if sum1 == 3:
                return 'B'
        
        # Check diagonals
        if (board[1][1]+board[0][0]+board[2][2]) == 0:
            return 'A'
        elif (board[1][1]+board[0][2]+board[2][0]) == 0:
            return 'A'
        if (board[1][1]+board[0][0]+board[2][2]) == 3:
            return 'B'
        elif (board[1][1]+board[0][2]+board[2][0]) == 3:
            return 'B'

        if len(moves) != 9:
            return "Pending"
        return "Draw"
        
def max_coins(rows, cols, coins, curr_row, curr_col):
    if curr_row == rows - 1:
        if curr_col == cols - 1:
            return coins[rows-1][cols-1]
        elif curr_row < rows - 1:
            return coins[rows-1][curr_col] + max_coins(rows, cols, coins, curr_row, curr_col+1)
    elif curr_row < rows - 1:
        if curr_col == cols - 1:
            return coins[curr_row][curr_col] + max_coins(rows, cols, coins, curr_row+1, curr_col)
        elif curr_col < cols - 1:
            return coins[curr_row][curr_col] + max(max_coins(rows, cols, coins, curr_row+1, curr_col), max_coins(rows, cols, coins, curr_row, curr_col+1))


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    coins = []
    for _ in range(n):
        row = list(map(int, input().split()))
        assert len(row) == m
        coins.append(row)

    max_value = max_coins(len(coins), len(coins[0]), coins, 0, 0)
    reverted_coins = []
    for row in coins:
        reverted_coins.append([-value for value in row])

    min_value = -max_coins(len(reverted_coins), len(reverted_coins[0]), reverted_coins, 0, 0)
    
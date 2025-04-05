import streamlit as st
import numpy as np

def is_valid(board, row, col, num):
    for i in range(4):
        if board[row][i] == num or board[i][col] == num:
            return False
    return True

def solve_sudoku(board):
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                for num in range(1, 5):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def main():
    st.title("🧩 Mini Sudoku Solver 🏆")
    st.write("Enter numbers (0 for empty) and press Solve!")
    
    default_board = np.zeros((4, 4), dtype=int)
    user_input = []
    
    with st.form("sudoku_form"):
        for i in range(4):
            cols = st.text_input(f"Row {i+1} (comma-separated)",
                                 ",".join(map(str, default_board[i])))
            user_input.append([int(x) if x.isdigit() else 0 for x in cols.split(",")])
        submitted = st.form_submit_button("Solve 🏁")
    
    if submitted:
        board = np.array(user_input)
        st.write("🔍 **Input Board:**")
        st.write(board)
        
        if solve_sudoku(board):
            st.write("✅ **Solved Sudoku:** 🎉")
            st.write(board)
        else:
            st.write("❌ No solution exists! Try again.")

if __name__ == "__main__":
    main()

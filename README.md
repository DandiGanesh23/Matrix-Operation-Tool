# Matrix Operation Tool

A professional desktop application built with Python and Tkinter that performs complex linear algebra operations. This tool provides a user-friendly graphical interface to handle matrix calculations without needing to write code.

## Features
- **Interactive GUI**: A clean, windowed interface for easy matrix input and result viewing.
- **Dynamic Parsing**: Supports any matrix size. Users simply enter rows separated by newlines and elements separated by spaces.
- **Core Math Operations**: 
  - **Addition**: Adds two matrices of the same dimensions.
  - **Subtraction**: Subtracts one matrix from another.
  - **Multiplication**: Performs a matrix dot product (checks for dimension compatibility).
  - **Transpose**: Flips a matrix over its diagonal.
  - **Determinant**: Calculates the determinant for square matrices.
- **Robust Error Handling**: Integrated pop-up alerts using `messagebox` to notify users of dimension mismatches or invalid input formats.

## Technical Stack
- **Language:** Python 3.x
- **GUI Library:** Tkinter (Built-in Python library)
- **Math Library:** NumPy (Numerical Python)
- **IDE:** Visual Studio Code

##  How to Run

 1. Install Dependencies
Open your terminal and install the NumPy library:
pip install numpy

2. Launch the Application
Run the Python script using the following command:

python matrix_operation_tool.py

## How to Use
Enter Matrix A: Type your numbers in the first box.
Example:
text

1 2
3 4
Enter Matrix B: If you are performing addition, subtraction, or multiplication, enter the second matrix in the second box.
Select Operation: Click one of the operation buttons (e.g., Multiply).
View Result: The calculated matrix or value will appear instantly in the Result area at the bottom.

## Example Use Case
Scenario: Matrix Addition

Matrix A: [[1, 2], [3, 4]]
Matrix B: [[5, 6], [7, 8]]
Operation: Click "Add"
Output: [[6, 8], [10, 12]]
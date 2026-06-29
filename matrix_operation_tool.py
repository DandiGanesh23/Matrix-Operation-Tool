import tkinter as tk
from tkinter import messagebox
import numpy as np

class MatrixApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧮 Matrix Operation Tool") # Updated Name
        self.root.geometry("600x650")
        self.root.configure(bg="#f0f2f5")

        # --- Title ---
        title_label = tk.Label(root, text="Matrix Operation Tool", font=("Arial", 20, "bold"), bg="#f0f2f5", fg="#333")
        title_label.pack(pady=20)

        # --- Input Section ---
        input_frame = tk.Frame(root, bg="#f0f2f5")
        input_frame.pack(pady=10)

        # Matrix A
        tk.Label(input_frame, text="Matrix A (Rows by newline, Cols by space):", bg="#f0f2f5", font=("Arial", 10)).grid(row=0, column=0, padx=10, pady=5)
        self.text_a = tk.Text(input_frame, width=25, height=8, font=("Consolas", 11))
        self.text_a.grid(row=1, column=0, padx=10, pady=5)

        # Matrix B
        tk.Label(input_frame, text="Matrix B (Optional for Transpose/Det):", bg="#f0f2f5", font=("Arial", 10)).grid(row=0, column=1, padx=10, pady=5)
        self.text_b = tk.Text(input_frame, width=25, height=8, font=("Consolas", 11))
        self.text_b.grid(row=1, column=1, padx=10, pady=5)

        # --- Buttons Section ---
        btn_frame = tk.Frame(root, bg="#f0f2f5")
        btn_frame.pack(pady=20)

        # Define buttons
        buttons = [
            ("Add", self.add_matrices),
            ("Subtract", self.sub_matrices),
            ("Multiply", self.mul_matrices),
            ("Transpose A", self.transpose_a),
            ("Determinant A", self.det_a)
        ]

        # Create buttons in a grid
        row, col = 0, 0
        for text, cmd in buttons:
            btn = tk.Button(btn_frame, text=text, command=cmd, width=15, height=2, bg="#007bff", fg="white", font=("Arial", 10, "bold"), relief="raised")
            btn.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 2:
                col = 0
                row += 1

        # --- Result Section ---
        tk.Label(root, text="Result:", bg="#f0f2f5", font=("Arial", 12, "bold")).pack(pady=(20, 0))
        self.result_display = tk.Text(root, width=50, height=10, font=("Consolas", 12), state="disabled", bg="#e9ecef")
        self.result_display.pack(pady=10)

    # --- Helper Functions ---
    def parse_matrix(self, text_widget):
        """Convert text input into a NumPy array."""
        try:
            raw_text = text_widget.get("1.0", tk.END).strip()
            if not raw_text:
                return None
            rows = [list(map(float, line.split())) for line in raw_text.split('\n') if line.strip()]
            return np.array(rows)
        except Exception:
            raise ValueError("Invalid matrix format. Use spaces for columns and newlines for rows.")

    def show_result(self, result):
        """Display the result in the text box."""
        self.result_display.configure(state="normal")
        self.result_display.delete("1.0", tk.END)
        if isinstance(result, np.ndarray):
            res_str = "\n".join([" ".join([f"{val:8.2f}" for val in row]) for row in result])
            self.result_display.insert(tk.END, res_str)
        else:
            self.result_display.insert(tk.END, f"Result: {result:.4f}")
        self.result_display.configure(state="disabled")

    # --- Math Operations ---
    def add_matrices(self):
        try:
            A, B = self.parse_matrix(self.text_a), self.parse_matrix(self.text_b)
            if A.shape != B.shape:
                raise ValueError("Matrices must be the same size for addition!")
            self.show_result(A + B)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def sub_matrices(self):
        try:
            A, B = self.parse_matrix(self.text_a), self.parse_matrix(self.text_b)
            if A.shape != B.shape:
                raise ValueError("Matrices must be the same size for subtraction!")
            self.show_result(A - B)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mul_matrices(self):
        try:
            A, B = self.parse_matrix(self.text_a), self.parse_matrix(self.text_b)
            if A.shape[1] != B.shape[0]:
                raise ValueError("Columns of A must match Rows of B for multiplication!")
            self.show_result(np.dot(A, B))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def transpose_a(self):
        try:
            A = self.parse_matrix(self.text_a)
            if A is None: raise ValueError("Please enter Matrix A")
            self.show_result(A.T)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def det_a(self):
        try:
            A = self.parse_matrix(self.text_a)
            if A is None: raise ValueError("Please enter Matrix A")
            if A.shape[0] != A.shape[1]:
                raise ValueError("Determinant requires a square matrix!")
            self.show_result(np.linalg.det(A))
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixApp(root)
    root.mainloop()
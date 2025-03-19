import tkinter as tk
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter UI with Multiple Views")
        self.root.geometry("800x600")
        self.show_matrix_calculator()
    
    def show_matrix_calculator(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Matrix Calculator", font=("Arial", 16)).pack(pady=20)
        self.matrix_input()
        tk.Button(self.root, text="Go to 3D Square", command=self.show_3d_square).pack()
    
    def matrix_input(self):
        tk.Label(self.root, text="Enter Matrices (comma separated, rows on new line)").pack()
        self.matrix1_entry = tk.Text(self.root, height=5, width=30)
        self.matrix1_entry.pack()
        self.matrix2_entry = tk.Text(self.root, height=5, width=30)
        self.matrix2_entry.pack()
        tk.Button(self.root, text="Add", command=self.add_matrices).pack()
        tk.Button(self.root, text="Subtract", command=self.subtract_matrices).pack()
        tk.Button(self.root, text="Multiply", command=self.multiply_matrices).pack()
        self.result_label = tk.Label(self.root, text="Result:")
        self.result_label.pack()
    
    def parse_matrix(self, matrix_text):
        return np.array([[float(num) for num in row.split(',')] for row in matrix_text.strip().split('\n')])
    
    def add_matrices(self):
        try:
            m1 = self.parse_matrix(self.matrix1_entry.get("1.0", tk.END))
            m2 = self.parse_matrix(self.matrix2_entry.get("1.0", tk.END))
            result = m1 + m2
            self.result_label.config(text=f"Result:\n{result}")
        except:

            self.result_label.config(text="Error in matrix input")
    
    def subtract_matrices(self):
        try:
            m1 = self.parse_matrix(self.matrix1_entry.get("1.0", tk.END))
            m2 = self.parse_matrix(self.matrix2_entry.get("1.0", tk.END))
            result = m1 - m2
            self.result_label.config(text=f"Result:\n{result}")
        except:
            self.result_label.config(text="Error in matrix input")
    
    def multiply_matrices(self):
        try:
            m1 = self.parse_matrix(self.matrix1_entry.get("1.0", tk.END))
            m2 = self.parse_matrix(self.matrix2_entry.get("1.0", tk.END))
            result = np.dot(m1, m2)
            self.result_label.config(text=f"Result:\n{result}")
        except:
            self.result_label.config(text="Error in matrix input")
    
    def show_3d_square(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="3D Square Rotation", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.root, text="Show 3D Square", command=self.plot_3d_square).pack()
    
    def plot_3d_square(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        square = [[(0,0,0), (1,0,0), (1,1,0), (0,1,0)]]
        ax.add_collection3d(Poly3DCollection(square, facecolors='cyan', linewidths=1, edgecolors='r'))
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

import random


class Vector:
    def __init__(self, data):
        self.data = list(data)
        self.size = len(self.data)

    def __repr__(self):
        return f"Vector({self.data})"

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.data, other.data)])

    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.data, other.data)])

    def __mul__(self, scalar):
        return Vector([x * scalar for x in self.data])

    def dot(self, other):
        return sum(a * b for a, b in zip(self.data, other.data))

    def magnitude(self):
        return sum(x ** 2 for x in self.data) ** 0.5

    def normalize(self):
        mag = self.magnitude()
        return Vector([x / mag for x in self.data])


class Matrix:
    def __init__(self, data):
        self.data = [list(row) for row in data]
        self.rows = len(self.data)
        self.cols = len(self.data[0])
        self.shape = (self.rows, self.cols)

    def __repr__(self):
        col_widths = []
        for j in range(self.cols):
            width = max(len(f"{self.data[i][j]:.4f}") for i in range(self.rows))
            col_widths.append(width)
        lines = []
        for i in range(self.rows):
            row_str = "  ".join(
                f"{self.data[i][j]:{col_widths[j]}.4f}" for j in range(self.cols)
            )
            bracket_l = "|" if 0 < i < self.rows - 1 else ("/" if i == 0 else "\\")
            bracket_r = "|" if 0 < i < self.rows - 1 else ("\\" if i == 0 else "/")
            lines.append(f"  {bracket_l} {row_str} {bracket_r}")
        header = f"Matrix {self.rows}x{self.cols}:"
        return header + "\n" + "\n".join(lines)

    def __add__(self, other):
        if isinstance(other, Matrix):
            if other.shape == self.shape:
                return Matrix([
                    [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
                    for i in range(self.rows)
                ])
            if other.rows == 1 and other.cols == self.cols:
                return Matrix([
                    [self.data[i][j] + other.data[0][j] for j in range(self.cols)]
                    for i in range(self.rows)
                ])
            if other.cols == 1 and other.rows == self.rows:
                return Matrix([
                    [self.data[i][j] + other.data[i][0] for j in range(self.cols)]
                    for i in range(self.rows)
                ])
        raise ValueError(f"Cannot add shapes {self.shape} and {other.shape}")

    def __sub__(self, other):
        return Matrix([
            [self.data[i][j] - other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def scalar_multiply(self, scalar):
        return Matrix([
            [self.data[i][j] * scalar for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def element_wise_multiply(self, other):
        return Matrix([
            [self.data[i][j] * other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def matmul(self, other):
        if self.cols != other.rows:
            raise ValueError(
                f"Cannot multiply shapes {self.shape} and {other.shape}: "
                f"inner dimensions {self.cols} != {other.rows}"
            )
        return Matrix([
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows)
        ])

    def __matmul__(self, other):
        return self.matmul(other)

    def transpose(self):
        return Matrix([
            [self.data[j][i] for j in range(self.rows)]
            for i in range(self.cols)
        ])

    @property
    def T(self):
        return self.transpose()

    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("Determinant only defined for square matrices")
        if self.shape == (1, 1):
            return self.data[0][0]
        if self.shape == (2, 2):
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        det = 0
        for j in range(self.cols):
            minor = Matrix([
                [self.data[i][k] for k in range(self.cols) if k != j]
                for i in range(1, self.rows)
            ])
            det += ((-1) ** j) * self.data[0][j] * minor.determinant()
        return det

    def inverse_2x2(self):
        if self.shape != (2, 2):
            raise ValueError("This method only works for 2x2 matrices")
        det = self.determinant()
        if abs(det) < 1e-10:
            raise ValueError("Matrix is singular, no inverse exists")
        return Matrix([
            [self.data[1][1] / det, -self.data[0][1] / det],
            [-self.data[1][0] / det, self.data[0][0] / det]
        ])

    @staticmethod
    def identity(n):
        return Matrix([
            [1 if i == j else 0 for j in range(n)]
            for i in range(n)
        ])

    @staticmethod
    def zeros(rows, cols):
        return Matrix([[0] * cols for _ in range(rows)])

    @staticmethod
    def random(rows, cols, low=-1.0, high=1.0):
        return Matrix([
            [random.uniform(low, high) for _ in range(cols)]
            for _ in range(rows)
        ])


def relu_matrix(m):
    return Matrix([[max(0, val) for val in row] for row in m.data])


def demo_basic_operations():
    print("=" * 60)
    print("BASIC MATRIX OPERATIONS (OPERASI DASAR MATRIKS)")
    print("=" * 60)

    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])

    print("\n[MATRIKS AWAL]")
    print("Kita memiliki dua matriks 2x2. Matriks adalah mesin yang bisa memindahkan atau mengubah titik koordinat di dalam ruang.")
    print("A =")
    print(A)
    print("\nB =")
    print(B)

    print("\n[1] PENJUMLAHAN (A + B)")
    print("Penjelasan: Operasi 'element-wise'. Kita menjumlahkan elemen di posisi yang sama (Kiri atas + Kiri atas, dst).")
    print("Hasil A + B =")
    print(A + B)

    print("\n[2] PENGURANGAN (A - B)")
    print("Penjelasan: Sama seperti penjumlahan, kita mengurangkan elemen yang posisinya bersesuaian.")
    print("Hasil A - B =")
    print(A - B)

    print("\n[3] PERKALIAN SKALAR (A * 3)")
    print("Penjelasan: Skalar adalah angka tunggal. Di sini kita mengalikan SETIAP elemen di dalam Matriks A dengan angka 3.")
    print("Hasil A * 3 =")
    print(A.scalar_multiply(3))

    print("\n[4] PERKALIAN ELEMENT-WISE (A * B)")
    print("Penjelasan: JANGAN TERTUKAR! Ini HANYA mengalikan angka yang posisinya sama persis. Syarat mutlak: dimensi matriks harus sama.")
    print("Hasil A * B (element-wise) =")
    print(A.element_wise_multiply(B))

    print("\n[5] PERKALIAN MATRIKS / DOT PRODUCT (A @ B)")
    print("Penjelasan: Ini adalah transformasi yang sesungguhnya di dalam AI. Kita mengalikan setiap BARIS pada Matriks A dengan setiap KOLOM pada Matriks B.")
    print("Hasil A @ B (matrix multiply) =")
    print(A @ B)

    print("\n[6] TRANSPOSE (A^T)")
    print("Penjelasan: Memutar matriks. Baris mendatar diubah menjadi kolom berdiri, dan sebaliknya. Sangat penting saat AI melakukan 'belajar' (Backpropagation).")
    print("Hasil A^T =")
    print(A.T)


def demo_determinant_inverse():
    print("\n" + "=" * 60)
    print("DETERMINANT AND INVERSE (DETERMINAN & INVERS)")
    print("=" * 60)

    A = Matrix([[4, 7], [2, 6]])
    print("\nMatriks A =")
    print(A)
    
    print("\n[1] DETERMINAN")
    print("Penjelasan: Sebuah angka yang mengukur seberapa besar matriks ini mengubah skala luas area/volume. Jika nol, dimensinya hancur (kempis).")
    print(f"Hasil det(A) = {A.determinant()}")

    print("\n[2] INVERS MATRIKS (A^-1)")
    print("Penjelasan: Matriks kebalikan. Jika Matriks A memutar objek ke kanan, Invers akan memutarnya kembali ke kiri (membatalkan transformasi).")
    A_inv = A.inverse_2x2()
    print("Hasil A^-1 =")
    print(A_inv)

    print("\n[3] PEMBUKTIAN INVERS (A @ A^-1)")
    print("Penjelasan: Jika sebuah matriks dikalikan dengan inversnya, hasilnya PASTI Matriks Identitas (versi 'Angka 1' di dunia matriks).")
    print("Hasil A @ A^-1 =")
    print(A @ A_inv)


def demo_broadcasting():
    print("\n" + "=" * 60)
    print("BROADCASTING (KEAJAIBAN DIMENSI)")
    print("=" * 60)

    output = Matrix([[1, 2, 3], [4, 5, 6]])
    bias = Matrix([[10, 20, 30]])

    print("\nMatriks Output (2x3):")
    print(output)
    print("\nVektor Bias (1x3):")
    print(bias)
    
    print("\nPenjelasan: Secara matematika murni, ukuran 2x3 tidak bisa dijumlahkan dengan 1x3. Namun, komputer menggunakan 'Broadcasting'. Vektor Bias secara otomatis diduplikasi (diregangkan) ke setiap baris agar ukurannya pas sebelum dijumlahkan.")
    print("Hasil Output + Bias =")
    print(output + bias)


def demo_vectors():
    print("\n" + "=" * 60)
    print("VECTOR OPERATIONS (OPERASI VEKTOR)")
    print("=" * 60)

    v = Vector([3, 4])
    w = Vector([1, 2])

    print("\nKita memiliki Vektor v (titik koordinat 3,4) dan Vektor w (titik koordinat 1,2).")
    print(f"v = {v}")
    print(f"w = {w}")
    
    print("\n[1] MAGNITUDO (PANJANG VEKTOR)")
    print("Penjelasan: Jarak garis lurus dari titik asal (0,0) ke titik koordinat vektor (menggunakan Teorema Pythagoras).")
    print(f"Panjang |v| = {v.magnitude()}")
    
    print("\n[2] DOT PRODUCT")
    print("Penjelasan: Mengukur seberapa searah dua vektor. Semakin besar nilainya, semakin mirip arah kedua vektor tersebut.")
    print(f"Hasil v . w = {v.dot(w)}")
    
    print("\n[3] NORMALISASI")
    print("Penjelasan: Memendekkan atau memanjangkan vektor agar panjangnya tepat 1, tapi arahnya tetap sama (Unit Vector).")
    print(f"Hasil Normalisasi v = {v.normalize()}")


if __name__ == "__main__":
    demo_vectors()
    demo_basic_operations()
    demo_determinant_inverse()
    demo_broadcasting()
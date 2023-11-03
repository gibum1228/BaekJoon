import sys

IN = sys.stdin.readline


def rotation(arr, head):
    tmp = arr[0]

    if head == '+':
        arr[0] = [arr[2][0], arr[1][0], arr[0][0]]
        arr[2][0], arr[1][0], arr[0][0] = arr[2][2], arr[2][1], arr[2][0]
        arr[2][2], arr[2][1], arr[2][0] = arr[0][2], arr[1][2], arr[2][2]
        arr[0][2], arr[1][2], arr[2][2] = tmp
    elif head == '-':
        arr[0] = [arr[0][2], arr[1][2], arr[2][2]]
        arr[0][2], arr[1][2], arr[2][2] = arr[2][2], arr[2][1], arr[2][0]
        arr[2][2], arr[2][1], arr[2][0] = arr[2][0], arr[1][0], arr[0][0]
        arr[2][0], arr[1][0], arr[0][0] = tmp

    return arr


if __name__ == "__main__":
    results = ''
    for _ in range(int(IN())):
        U = [['w' for _ in range(3)] for _ in range(3)]  # top
        D = [['y' for _ in range(3)] for _ in range(3)]  # bottom
        L = [['g' for _ in range(3)] for _ in range(3)]  # left
        R = [['b' for _ in range(3)] for _ in range(3)]  # right
        B = [['o' for _ in range(3)] for _ in range(3)]  # back
        F = [['r' for _ in range(3)] for _ in range(3)]  # front
        ### input
        N = int(IN())
        orders = IN().rstrip().split()
        ### logic
        for order in orders:
            where, head = list(order)
            '''
            U[2] -> F[0]
            F[2] -> D[0]
            D[2] -> B[0]
            B[2] -> U[0]
            ============
            U[*][0] -> L[0]
            U[*][2] -> R[0]
            '''
            if where == 'U':
                tmp = B[2]

                if head == '+':
                    B[2] = [L[0][2], L[0][1], L[0][0]]
                    L[0] = F[0]
                    F[0] = R[0]
                    R[0] = tmp[::-1]
                elif head == '-':
                    B[2] = [R[0][2], R[0][1], R[0][0]]
                    R[0] = F[0]
                    F[0] = L[0]
                    L[0] = tmp[::-1]

                U = rotation(U, head)
            elif where == 'D':
                tmp = F[2]

                if head == '+':
                    F[2] = L[2]
                    L[2] = [B[0][2], B[0][1], B[0][0]]
                    B[0] = [R[2][2], R[2][1], R[2][0]]
                    R[2] = tmp
                elif head == '-':
                    F[2] = R[2]
                    R[2] = [B[0][2], B[0][1], B[0][0]]
                    B[0] = [L[2][2], L[2][1], L[2][0]]
                    L[2] = tmp

                D = rotation(D, head)
            elif where == 'L':
                tmp = [U[0][0], U[1][0], U[2][0]]

                if head == '+':
                    U[0][0], U[1][0], U[2][0] = B[0][0], B[1][0], B[2][0]
                    B[0][0], B[1][0], B[2][0] = D[0][0], D[1][0], D[2][0]
                    D[0][0], D[1][0], D[2][0] = F[0][0], F[1][0], F[2][0]
                    F[0][0], F[1][0], F[2][0] = tmp
                elif head == '-':
                    U[0][0], U[1][0], U[2][0] = F[0][0], F[1][0], F[2][0]
                    F[0][0], F[1][0], F[2][0] = D[0][0], D[1][0], D[2][0]
                    D[0][0], D[1][0], D[2][0] = B[0][0], B[1][0], B[2][0]
                    B[0][0], B[1][0], B[2][0] = tmp

                L = rotation(L, head)
            elif where == 'R':
                tmp = [U[2][2], U[1][2], U[0][2]]

                if head == '+':
                    U[2][2], U[1][2], U[0][2] = F[2][2], F[1][2], F[0][2]
                    F[2][2], F[1][2], F[0][2] = D[2][2], D[1][2], D[0][2]
                    D[2][2], D[1][2], D[0][2] = B[2][2], B[1][2], B[0][2]
                    B[2][2], B[1][2], B[0][2] = tmp
                elif head == '-':
                    U[2][2], U[1][2], U[0][2] = B[2][2], B[1][2], B[0][2]
                    B[2][2], B[1][2], B[0][2] = D[2][2], D[1][2], D[0][2]
                    D[2][2], D[1][2], D[0][2] = F[2][2], F[1][2], F[0][2]
                    F[2][2], F[1][2], F[0][2] = tmp

                R = rotation(R, head)
            elif where == 'B':
                tmp = D[2]

                if head == '+':
                    D[2] = [L[0][0], L[1][0], L[2][0]]
                    L[0][0], L[1][0], L[2][0] = U[0][2], U[0][1], U[0][0]
                    U[0] = [R[0][2], R[1][2], R[2][2]]
                    R[0][2], R[1][2], R[2][2] = tmp[::-1]
                elif head == '-':
                    D[2] = [R[2][2], R[1][2], R[0][2]]
                    R[2][2], R[1][2], R[0][2] = U[0][2], U[0][1], U[0][0]
                    U[0] = [L[2][0], L[1][0], L[0][0]]
                    L[2][0], L[1][0], L[0][0] = tmp[::-1]

                B = rotation(B, head)
            elif where == 'F':
                tmp = U[2]

                if head == '+':
                    U[2] = [L[2][2], L[1][2], L[0][2]]
                    L[0][2], L[1][2], L[2][2] = D[0]
                    D[0] = [R[2][0], R[1][0], R[0][0]]
                    R[0][0], R[1][0], R[2][0] = tmp
                elif head == '-':
                    U[2] = [R[0][0], R[1][0], R[2][0]]
                    R[2][0], R[1][0], R[0][0] = D[0]
                    D[0] = [L[0][2], L[1][2], L[2][2]]
                    L[2][2], L[1][2], L[0][2] = tmp

                F = rotation(F, head)

        ### print
        for row in U:
            results += "".join(row) + "\n"
        # results += "="*10 + "\n"

    print(results)
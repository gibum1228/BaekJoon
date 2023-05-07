import sys, itertools

IN = sys.stdin.readline

if __name__ == "__main__":
    S = [list(map(int, IN().split())) for _ in range(int(IN()))]
    max_size = len(S) // 2
    results = float('inf')

    comb = list(itertools.combinations([i for i in range(len(S))], max_size))
    for i in range(len(comb) // 2):
        start_team = comb[i]
        link_team = comb[len(comb) - 1 - i]

        start_score = sum([S[r][c] for r in start_team for c in start_team])
        link_score = sum([S[r][c] for r in link_team for c in link_team])
        results = min(results, abs(start_score - link_score))

    print(results)
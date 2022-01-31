import collections

if __name__ == '__main__':
    N = int(input())
    deck = collections.deque(range(1, N+1))

    for _ in range(len(deck) - 1):
        deck.popleft()
        deck.append(deck.popleft())
    print(deck[0])

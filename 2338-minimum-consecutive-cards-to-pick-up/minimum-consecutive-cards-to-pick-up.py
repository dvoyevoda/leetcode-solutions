class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        card_map = {}
        minimum = float("inf")
        
        for i in range(len(cards)):
            if cards[i] in card_map:
                card_map[cards[i]].append(i)
            else:
                card_map[cards[i]] = [i]
        
        for key in card_map:
            arr = card_map[key]
            for i in range(len(arr)-1):
                minimum = min(minimum, arr[i + 1] - arr[i] + 1)
        
        return minimum if minimum < float("inf") else -1
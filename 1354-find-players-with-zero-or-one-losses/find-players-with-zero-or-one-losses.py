class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        loss_map = defaultdict(int)
        no_loss = []
        one_loss = []
        
        for match in matches:
            loss_map[match[1]] += 1
            if match[0] not in loss_map:
                loss_map[match[0]] = 0
        
        for player in loss_map:
            if loss_map[player] == 0:
                no_loss.append(player)
            elif loss_map[player] == 1:
                one_loss.append(player)
        
        return([sorted(no_loss),sorted(one_loss)])
        
        
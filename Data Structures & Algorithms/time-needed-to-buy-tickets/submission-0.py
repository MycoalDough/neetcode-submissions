class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        time = 0
        index = k
        
        while True:
            tickets[0] -= 1
            time += 1

            if tickets[0] == 0:
                if index == 0:
                    return time
                tickets.pop(0)
            else:
                tickets.append(tickets[0])
                tickets.pop(0)
            
            if index == 0:
                index = len(tickets) - 1
            else:
                index -= 1

                

        
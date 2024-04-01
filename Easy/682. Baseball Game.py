class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        score = []

        for operation in operations:
            if operation == 'D':
                score.append(score[-1]*2)
            
            elif operation == 'C':
                score.pop()
            
            elif operation == '+':
                score.append(int(score[-1]) + int(score[-2]))
            
            else:
                score.append(int(operation))

            print(score)

        
        return sum(score)

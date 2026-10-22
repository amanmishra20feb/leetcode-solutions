class Solution(object):
    def bagOfTokensScore(self, tokens, power):

        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        i = 0
        j = len(tokens) - 1
        score = 0
        ans = 0

        while i <= j:
            if power >= tokens[i]:
                power -= tokens[i]
                score += 1
                i += 1
                ans = max(ans, score)

            elif score > 0 and i < j:
                power += tokens[j]
                score -= 1
                j -= 1

            else:
                break

        return ans
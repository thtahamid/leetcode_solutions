class Solution(object):
    def minOperations(self, logs):
        result = 0
        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                result = max(0, result -1)
                # if result > 0:
                #     result -= 1
                # else:
                #     result = 0
            else:
                result += 1

        return result
        
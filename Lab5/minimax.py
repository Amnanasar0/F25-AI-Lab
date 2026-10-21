scores = [3, 5, 2, 9, 3, 5, 2, 9]
depth = 3
count = [0]


def minimax(curDepth, nodeIndex, maxTurn, scores,
            targetDepth, count):

    if curDepth == targetDepth:
        count[0] += 1
        return scores[nodeIndex]

    if maxTurn:
        return max(
            minimax(curDepth + 1, nodeIndex * 2, False,
                    scores, targetDepth, count),
            minimax(curDepth + 1, nodeIndex * 2 + 1, False,
                    scores, targetDepth, count)
        )
    else:
        return min(
            minimax(curDepth + 1, nodeIndex * 2, True,
                    scores, targetDepth, count),
            minimax(curDepth + 1, nodeIndex * 2 + 1, True,
                    scores, targetDepth, count)
        )


result = minimax(0, 0, True, scores, depth, count)

print("Optimal value:", result)
print("Leaf nodes evaluated:", count[0])
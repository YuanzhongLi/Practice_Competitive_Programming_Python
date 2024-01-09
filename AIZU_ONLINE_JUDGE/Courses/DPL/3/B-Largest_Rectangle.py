from sys import stdin

input = stdin.readline


# def largest_rectangle(H, W, tiles):
#     histgram = [[0 for _ in range(W)] for _ in range(H)]
#     for i in range(H):
#         for j in range(W):
#             if tiles[i][j] == 1:
#                 histgram[i][j] = 0
#             else:
#                 histgram[i][j] = 1
#                 if i > 0:
#                     histgram[i][j] += histgram[i - 1][j]

#     ans = 0
#     for i in range(H):
#         stack = []
#         for j in range(W):
#             cur_height_tiles = histgram[i][j]
#             pos = j

#             if not stack or cur_height_tiles > stack[-1][0]:
#                 stack.append((cur_height_tiles, pos))
#             else:
#                 while stack and cur_height_tiles <= stack[-1][0]:
#                     top = stack.pop()
#                     pos = top[1]

#                     height_tiles = top[0]
#                     width_tiles = j - pos
#                     ans = max(ans, height_tiles * width_tiles)

#                 stack.append((cur_height_tiles, pos))

#         while stack:
#             top = stack.pop()
#             height_tiles = top[0]
#             width_tiles = W - top[1]
#             ans = max(ans, height_tiles * width_tiles)

#     return ans


def largest_rectangle(H, W, tiles):
    # prev_histgram[j]: 1つ前の行のj列目のタイルにおいて、上方向へ積み重なっているきれいなタイルの数
    prev_histgram = [0 for _ in range(W)]

    ans = 0
    for i in range(H):
        # cur_histgram[j]: 今見ているi行j列目のタイルにおいて、上方向へ積み重なっているきれいなタイルの数
        cur_histgram = [0 for _ in range(W)]
        for j in range(W):
            if tiles[i][j] == 1:
                cur_histgram[j] = 0
            else:
                cur_histgram[j] = prev_histgram[j] + 1

        # スタック: 高さの値とその高さが長方形として成立する最も左側の位置が格納されている
        # [(高さ, 位置)]
        stack = []
        for j in range(W):
            # i行j列目から上方向にいくつ綺麗なタイルが積み重なっているか（今見ているところ）
            cur_height_tiles = cur_histgram[j]
            pos = j

            if not stack or cur_height_tiles > stack[-1][0]:
                stack.append((cur_height_tiles, pos))
            else:
                while stack and cur_height_tiles <= stack[-1][0]:
                    top = stack.pop()
                    pos = top[1]

                    height_tiles = top[0]
                    width_tiles = j - pos
                    ans = max(ans, height_tiles * width_tiles)

                stack.append((cur_height_tiles, pos))

        while stack:
            top = stack.pop()
            height_tiles = top[0]
            width_tiles = W - top[1]
            ans = max(ans, height_tiles * width_tiles)

        # prev_histgramを更新
        prev_histgram = cur_histgram

    return ans


H, W = map(int, input().rstrip().rsplit())
tiles = []
for _ in range(H):
    tile_row = list(map(int, input().rstrip().rsplit()))
    tiles.append(tile_row)

print(largest_rectangle(H, W, tiles))

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        hash_map = dict()
        original_k = k
        for c in s:
            if c not in hash_map.keys():
                hash_map[c] = 1
            else:
                hash_map[c] += 1
        max_key = ''
        max_key_val = 0
        for key in hash_map:
            if hash_map[key] > max_key_val:
                max_key = key
                max_key_val = hash_map[key]
            if hash_map[key] <= k:
                k -= hash_map[key]
                hash_map[key] = 0
        if k == original_k:
            hash_map[max_key] -= k
        print(hash_map)
        total = 0
        for key in hash_map:
            if hash_map[key] != 0:
                if hash_map[key] == 1:
                    total += 1
                elif hash_map[key] < 10:
                    total += 2
                else:
                    total += 3
        return total
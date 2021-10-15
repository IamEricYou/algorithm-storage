# import necessary imports 
# 211015
# https://leetcode.com/problems/longest-common-prefix/
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    # first element of string list 
    # WIP - IndexError when input is empty
    try:
        target_str: List[str] = [c for c in strs[0]]
        strs = strs[1:]
        if not strs:
            return ""
    except IndexError:
        return ""
    
    common_str = []
    for s in strs:
        string_to_list: List[str] = [c for c in s]
        for c1, c2 in zip(target_str, string_to_list):
            if c1 == c2:
                common_str.append(c1)
            else:
                del common_str[-1]
                break
        target_str = common_str
    return ''.join(common_str) if common_str else ""

if __name__ == "__main__":
    ...
    
class Solution:
    def lengthOfLongesSubstring(self, s):
        # 采用滑动窗口
        # 窗口的起始位置都为0　最大长度默认为0
        num_max = cur_max = start = 0
        dict = {}
        for index, item in enumerate(s):
            # 窗口有当前值，并且在当前窗口内
            if item in dict and dict[item] >= start:
                # 窗口内元素个数是否最大
                num_max = max(num_max, cur_max)
                # 更新窗口内的元素个数
                cur_max = index - dict[item]
                # 更新窗口起始指针　移动到后一位
                start = dict[item] + 1
            else:
                # 窗口没有当前值
                cur_max += 1
            dict[item] = index
        return max(num_max, cur_max)

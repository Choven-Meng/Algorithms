"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.
Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as[1,5],[6,9].
Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as[1,2],[3,10],[12,16].
This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""

def insert(intervals, newInterval):
    intervals.append(newInterval)
    intervals.sort(key = lambda x:x[0])
    length=len(intervals)
    res=[]
    for i in range(length):
        if res==[]:
            res.append(intervals[i])
        else:
            size=len(res)
            if res[size-1][0]<=intervals[i][0]<=res[size-1][-1]:
                res[size-1][-1]=max(intervals[i][-1], res[size-1][-1])
            else:
                res.append(intervals[i])
    return res
    
    if __name__ == '__main__':
      print(insert([[1,3],[6,9]],[2,5]))
 

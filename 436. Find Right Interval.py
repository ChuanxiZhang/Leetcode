/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
class Solution {
    public int[] findRightInterval(Interval[] intervals) {
        HashMap<Interval,Integer> hash = new HashMap<>();
        int [] res = new int[intervals.length];
        for (int i = 0; i < intervals.length; i++){
            hash.put(intervals[i],i);
        }
        Arrays.sort(intervals, (a,b) -> a.start - b.start);
         for (int i = 0; i < intervals.length; i++){
            Interval ret = binarySearch(intervals, intervals[i].end, 0, intervals.length - 1);
            res[hash.get(intervals[i])] = ret == null? -1 : hash.get(ret);
        }
        return res;
    }
    public Interval binarySearch(Interval[] intervals,int target,int left ,int right){
        if (left>=right){
            if (intervals[left].start >=target){
                return intervals[left];
            }
            return null;
        }
        int mid = (left + right)/2;
        if (intervals[mid].start>=target){
            return binarySearch(intervals, target, left, mid);
        }
        else{
            return binarySearch(intervals, target, mid+1, right);
        }
    }
}

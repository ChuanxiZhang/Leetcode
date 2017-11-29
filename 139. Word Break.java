public class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        return WordTest(s, new HashSet(wordDict), 0, new Boolean [s.length()] );
    }
    public boolean WordTest(String s, Set<String> wordDict, int pos, Boolean [] memo){
        if( pos == s.length()) return true;
        if( memo[pos] != null) return memo[pos];
        for (int i = pos + 1; i <= s.length(); i++){
            if(wordDict.contains( s.substring (pos,i)) && WordTest(s, wordDict, i , memo)){
                return memo[pos] = true;
            }
        }
        return memo[pos] = false;
    }
}

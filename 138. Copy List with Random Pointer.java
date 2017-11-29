/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        RandomListNode iter = head, next;

        // Copy whole LinkedList
        // e.g. 1->2->3 to 1->1->2->2->3->3
        while (iter != null){
            RandomListNode copy = new RandomListNode(iter.label);
            next = iter.next;
            iter.next = copy;
            copy.next = next;
            iter = next;
        }

        // Add random pointer to duplicated list
        iter = head;
        while (iter != null){
            next = iter.next.next;
            if (iter.random != null){
                 iter.next.random = iter.random.next;
            }
            iter = next;
        }

        // Extract the result
        RandomListNode pseudohead = new RandomListNode(0);
        RandomListNode copy = pseudohead;
        iter = head;
        while (iter != null){
            next = iter.next.next;
            copy.next = iter.next;
            copy = iter.next;
            iter.next = next;
            iter = next;

        }
        return pseudohead.next;
    }
}

import java.util.*;

class Solution {
    ArrayList<Integer> preOrder(Node root) {
        ArrayList<Integer> result = new ArrayList<>();
        preorder(root, result);
        return result;
    }

    void preorder(Node node, ArrayList<Integer> result) {
        if (node == null) return;

        // Visit root
        result.add(node.data);

        // Left
        preorder(node.left, result);

        // Right
        preorder(node.right, result);
    }
}
import java.util.ArrayList;
import java.util.List;

// https://leetcode.com/problems/smallest-string-with-swaps/

class SmallestStringSwaps {

    public String smallestStringWithSwaps(String s, List<List<Integer>> pairs) {
        List<List<Integer>> tree = new ArrayList<List<Integer>>();
        int flag = 0;
        for (List<Integer> pair : pairs) {
            int index1 = pair.get(0);
            int index2 = pair.get(1);
            flag = 0;
            for (List<Integer> groups: tree) {
                if (groups.contains(index1) && !groups.contains(index2)) {
                    groups.add(index2);
                    flag = 1;
                    break;
                }
                if (groups.contains(index2) && !groups.contains(index1)) {
                    groups.add(index1);
                    flag = 1;
                    break;
                }
            }
            if (flag == 0) {
                List<Integer> group = new ArrayList<Integer>();
                group.add(index1);
                group.add(index2);
                tree.add(group);
            }
        }
        // for (List<Integer> group: tree) {
        //     group.sort(null);
        // }
        // print groups
        for (List<Integer> group: tree) {
            System.out.println(group);
        }
        StringBuffer sb = new StringBuffer(s);
        String[][] lines = new String[tree.size()][];

        for (int i = 0; i < tree.size(); i++) {
            List<Integer> group = tree.get(i);
            lines[i] = new String[group.size()];
            for (int j = 0; j < group.size(); j++) {
                lines[i][j] = sb.substring(group.get(j), group.get(j) + 1);
            }
            java.util.Arrays.sort(lines[i]);
        }        
        // print lines array
        // for (int i = 0; i < lines.length; i++) {
        //     for (int j = 0; j < lines[i].length; j++) {
        //         System.out.print(lines[i][j]);
        //     }
        //     System.out.println();
        // }
        for (int i = 0; i < tree.size(); i++) {
            for (int j = 0; j < lines[i].length; j++) {
                sb.setCharAt(tree.get(i).get(j), lines[i][j].charAt(0));
            }
        }

        return sb.toString();
    }

    public static void main(String[] args) {
        String s = "dcab";
        List<List<Integer>> pairs = new ArrayList<List<Integer>>();
        List<Integer> pair1 = new ArrayList<Integer>();
        pair1.add(0);
        pair1.add(3);
        pairs.add(pair1);
        List<Integer> pair2 = new ArrayList<Integer>();
        pair2.add(1);
        pair2.add(2);
        pairs.add(pair2);
        List<Integer> pair3 = new ArrayList<Integer>();
        pair3.add(0);
        pair3.add(2);
        pairs.add(pair3);
        // List<Integer> pair4 = new ArrayList<Integer>();
        // pair4.add(4);
        // pair4.add(3);
        // pairs.add(pair4);
        // List<Integer> pair5 = new ArrayList<Integer>();
        // pair5.add(6);
        // pair5.add(7);
        // pairs.add(pair5);

        SmallestStringSwaps ssw = new SmallestStringSwaps();
        
        String result = ssw.smallestStringWithSwaps(s, pairs);
        System.out.println(result);
    }
}
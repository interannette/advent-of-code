package org.interannette.day8;

import org.interannette.InputGetter;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;

public class Day8 {
    TreeNode treeRoot;

    public static void main(String[] args) throws IOException {
        Day8 day8 = new Day8(InputGetter.getInput(8).trim());
        System.out.println("Sum of metadata: " + day8.solveStar1());
        System.out.println("Value of root node: " + day8.solveStar2());
    }

    public Day8(String input) {
        List<Integer> entries = Arrays.stream(input.split(" "))
                .map(s -> Integer.valueOf(s))
                .collect(Collectors.toList());
        LinkedList<Integer> entriesQueue = new LinkedList<>(entries);

        treeRoot = buildTree(entriesQueue);
    }

    TreeNode buildTree(LinkedList<Integer> entries) {

        Integer childCount = entries.pop();
        Integer metaDataCount = entries.pop();

        List<Integer> metaData = new ArrayList<>(metaDataCount);
        List<TreeNode> children = new ArrayList<>(childCount);

        if(childCount == 0) {
            for(int i = 0; i < metaDataCount; i++) {
                metaData.add(entries.pop());
            }
        } else {
            for(int i = 0; i < childCount; i++) {
                children.add(buildTree(entries));
            }
            for(int i = 0; i < metaDataCount; i++) {
                metaData.add(entries.pop());
            }
        }
        return new TreeNode(children, metaData);

    }

    public Integer solveStar1() {
        return sumMetaData(treeRoot);
    }

    public Integer sumMetaData(TreeNode treeNode) {
        Integer sum = treeNode.metadata.stream().collect(Collectors.summingInt(Integer::intValue));
        for(TreeNode child : treeNode.children) {
            sum += sumMetaData(child);
        }
        return sum;
    }

    public Integer solveStar2() {
        return sumNodeValue(treeRoot);
    }

    public Integer sumNodeValue(TreeNode treeNode) {
        if(treeNode.children.isEmpty()) {
            return treeNode.metadata.stream().collect(Collectors.summingInt(Integer::intValue));
        } else {
            Integer sum = 0;
            for(Integer metadatum : treeNode.metadata) {
                if(metadatum > 0 && metadatum <= treeNode.children.size()) {
                    sum += sumNodeValue(treeNode.children.get(metadatum - 1));
                }
            }
            return sum;
        }
    }
}

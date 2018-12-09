package org.interannette.day8;

import lombok.AllArgsConstructor;
import lombok.Data;

import java.util.List;

@Data
@AllArgsConstructor
public class TreeNode {
    List<TreeNode> children;
    List<Integer> metadata;
}

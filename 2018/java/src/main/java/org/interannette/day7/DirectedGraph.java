package org.interannette.day7;

import lombok.Data;

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.Set;
import java.util.stream.Collectors;

@Data
public class DirectedGraph {

    // outbound edges
    private Map<String, Set<String>> fromTo = new HashMap<>();

    // inbound edges
    private Map<String, Set<String>> toFrom = new HashMap<>();

    private Set<String> all = new HashSet<>();

    public void addRelationship(String from, String to) {

        Set<String> fromSet = fromTo.get(from);
        if(fromSet == null) {
            fromSet = new HashSet<>();
            fromTo.put(from, fromSet);
        }

        fromSet.add(to);

        Set<String> toSet = toFrom.get(to);
        if(toSet == null) {
            toSet = new HashSet<>();
            toFrom.put(to, toSet);
        }

        toSet.add(from);

        all.add(to);
        all.add(from);
    }

    public List<String> nodesWithoutInbound(){
        return all.stream().filter(n -> !toFrom.containsKey(n)).collect(Collectors.toList());
    }

    public void removeNode(String completed) {

        all.remove(completed);

        Set<String> outboundFromCompleted = fromTo.remove(completed);

        if(outboundFromCompleted != null) {
            outboundFromCompleted.stream().forEach(
                    n -> {
                        Set<String> inboundToN = toFrom.get(n);
                        inboundToN.remove(completed);
                        if(inboundToN.isEmpty()) {
                            toFrom.remove(n);
                        }
                    }
            );
        }
    }
}

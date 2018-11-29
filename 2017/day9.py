def compute_score_and_garbage_count(input_string):

    in_garbage = False
    escaped = False
    group_starts = []
    current_score = 0
    total_score = 0
    garbage_count = 0;

    for i in range(len(input_string)):
        if not in_garbage:
            if input_string[i] == '{':
                group_starts.append(i)
                current_score += 1
            elif input_string[i] == '}':
                group_starts.pop()
                total_score += current_score
                current_score -= 1
            elif input_string[i] == '<':
                in_garbage = True
        else:
            if escaped:
                escaped = False
            elif input_string[i] == '>':
                in_garbage = False
            elif input_string[i] == '!':
                escaped = True
            else:
                garbage_count += 1
    return total_score, garbage_count

def undo(old_score_list, current_score_list): ## the function undos the last operation that modified the list
    current_score_list = old_score_list.copy() ## copies the old list into the current one
    return current_score_list ## return the list modified before the last operation
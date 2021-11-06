from typing import List, Tuple, Dict

from union_find import UnionFind, UnionFindInterface


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        character_index_mapping: Dict[str, int] = dict()
        for pair in equations:
            character_index_mapping.setdefault(pair[0], len(character_index_mapping))
            character_index_mapping.setdefault(pair[3], len(character_index_mapping))
        union_find_tree: UnionFindInterface = UnionFind(len(character_index_mapping))

        for pair in equations:
            first_character = pair[0]
            second_character = pair[3]
            if pair[1] == "!":
                if union_find_tree.connected(character_index_mapping[first_character],
                                             character_index_mapping[second_character]):
                    return False
            else:

                union_find_tree.union(character_index_mapping[first_character],
                                      character_index_mapping[second_character])

        for pair in equations:
            first_character = pair[0]
            second_character = pair[3]
            if pair[1] == "!":
                if union_find_tree.connected(character_index_mapping[first_character],
                                             character_index_mapping[second_character]):
                    return False
            else:
                if not union_find_tree.connected(character_index_mapping[first_character],
                                                 character_index_mapping[second_character]):
                    return False
        return True

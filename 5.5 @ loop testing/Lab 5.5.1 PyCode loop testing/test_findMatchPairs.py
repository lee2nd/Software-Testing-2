from findMatchPairs import find_matching_pairs 

def test_findMatchingPairs():
    numbers1 = [1,2,3,4,5,6]
    pairs1 = find_matching_pairs(numbers1)
    assert pairs1 == [[2,4],[2,6],[4,6]]

    numbers2 = [1,3,5,7]
    pairs2 = find_matching_pairs(numbers2)
    assert pairs2 == []

    numbers3 = [1,3,5,7,9]
    pairs3 = find_matching_pairs(numbers3)
    assert pairs3 == []

    numbers4 = [2,4,6,8,10]
    pairs4 = find_matching_pairs(numbers4)
    assert pairs4 == [[2,4],[2,6],[2,8],[2,10],[4,6],[4,8],[4,10],[6,8],[6,10],[8,10]]   
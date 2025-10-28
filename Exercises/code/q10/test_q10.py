from q10 import most_shared_interest

def test_toy():
    best_friends = most_shared_interest("toy.json")
    print(best_friends)
    
    expected_output = {
        "pair": ["John", "Ringo"],
        "societies": ["Badminton", "Hockey", "Tennis"]
    }
    
    assert best_friends["pair"] == expected_output["pair"]
    assert best_friends["societies"] == expected_output["societies"]
    

def test_pythonistas():
    best_friends = most_shared_interest("students.json")
    print(best_friends)
    
    expected_output = {
        "pair": ["Chia-Hsin", "Ludovico"],
        "societies": [
            "Archery", "Badminton", "Basketball", "Boat", "Boxing", 
            "Cheerleading", "Cricket", "Crossfit", "Cycling", "Dodgeball", 
            "Fencing", "Football", "Golf", "Lacrosse", "Rugby", "Sailing", 
            "Squash", "Synchronized Swimming", "Tennis", "Triathlon", 
            "Ultimate Frisbee", "Volleyball"
        ]
    }
    
    assert best_friends["pair"] == expected_output["pair"]
    assert best_friends["societies"] == expected_output["societies"]
    

if __name__ == "__main__":
    test_toy()
    test_pythonistas()
    

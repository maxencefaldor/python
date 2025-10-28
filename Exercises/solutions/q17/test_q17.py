from q17 import can_exit_maze

def test_4x6_exit():
    maze = [
        [0, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 0],
        [1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 0]
    ]
    result = can_exit_maze(maze)
    print(result)
    assert result == True


def test_4x6_no_exit():
    maze = [
        [0, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 0],
        [1, 1, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0]
    ]
    result = can_exit_maze(maze)
    print(result)
    assert result == False
    
    
def test_6x4_exit():
    maze = [
        [0, 1, 1, 0],
        [0, 1, 1, 1],
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 0]
    ]
    result = can_exit_maze(maze)
    print(result)
    assert result == True
    
    
def test_6x4_no_exit():
    maze = [
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 1]
    ]
    result = can_exit_maze(maze)
    print(result)
    assert result == False
    
    
def test_2x2_exit():
    maze = [
        [0, 1],
        [0, 0]
    ]
    result = can_exit_maze(maze)
    print(result)
    assert result == True
    
    
def test_2x2_no_exit():
    maze = [
        [0, 1],
        [1, 0]
    ]
    result = can_exit_maze(maze)
    print(result)
    assert result == False
    
    
if __name__ == "__main__":
    test_4x6_exit()
    test_4x6_no_exit()
    test_6x4_exit()
    test_6x4_no_exit()
    test_2x2_exit()
    test_2x2_no_exit()
    
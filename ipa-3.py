'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if from_member in social_graph and to_member in social_graph:
        if to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
            return "friends"
        elif to_member in social_graph[from_member]["following"]:
            return "follower"
        elif from_member in social_graph[to_member]["following"]:
            return "followed by"
        else:
            return "no relationship"
    elif from_member in social_graph:
        if to_member in social_graph[from_member]["following"]:
            return "follower"
        else:
            return "no relationship"
    elif to_member in social_graph:
        if from_member in social_graph[to_member]["following"]:
            return "followed by"
        else:
            return "no relationship"

def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    size = len(board)
    # establishes 3 by 3, 4 by 4, number of rows and columns are equal
    
    # Checking rows, horizontal
    for row in board:
        if len(set(row)) == 1 and row[0] != '':
        # len(set(row)) checks if there is only 1 unique element in the list for each row
        # 1 unique value notes that all the values in the row are the same, thus a win
        # necessary to check if these rows are not full of blank spaces, otherwise the winner is not clear
        # returns the symbol of the row with three of a kind
            return row[0]
        
    # Checking columns, vertical
    for column in range(size):
        if len(set(board[row][column] for row in range(size))) == 1 and board[0][column] != '':
            return board[0][column]
        
    # checking diagonal from top left to bottom right
    if len(set(board[i][i] for i in range(size))) == 1 and board[0][0] != '':
        return board[0][0]
    # tiles across this diagonal have the same index on the board
    # ex. the top left cell is in the first row first column, so its board[0][0]
    
    # checking diagonal from top right to bottom left
    if len(set(board[i][size-1-i] for i in range(size))) == 1 and board[0][size-1] != '':
        return board[0][size-1]
    # this assumes that for a player to win in a 4 by 4 game, they must have 4 in a row
    # 5 by 5 needs 5 in a row, ...
    
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    travel_time = 0
    current_stop = first_stop
    while current_stop != second_stop:
    # this counts the legs that route takes to get to the desired stop
    # when current_stop = second_stop, it means that the person arrived at the desired stop
        for leg, info in route_map.items():
            if current_stop == leg[0]:
                travel_time += info["travel_time_mins"]
                # adds the travel_time_mins until the while loop is broken
                current_stop = leg[1]
                # checks the succeeding route bc when current_stop = leg[1], it sets current_stop into the tuple of the next leg
                break
    return travel_time

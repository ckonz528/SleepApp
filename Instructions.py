def showInstructions():
    print('''Land ho! You are a pirate that has just made landfall on Sleepless Island.
    You heard that its sandy beaches are home to some of the most valuable hidden treasure-
    the Secrets of Sleep. To find these treasures you have brought with you a supply of 
    treasure detectors. 
    
    To deploy a detector you must enter the coordinates of where you want it to look for buried 
    treasure. The map of the beach will be marked with how far away the nearest chest is. 
    
    For example: You deploy a detector to the coordinate 3, 10. As you can see below, the beach
    map displays a 4 in that position because the closest chest is 4 spaces away. 
    
                                              1                   2 
                          0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
                        0 ` . * ~ ` * . * * ` ` ` ~ ~ ` ~ * ` . ` * ~ 0
                        1 * * . . ` ` ` ` ~ ~ ` ` . * ` ~ ~ * * ~ . ~ 1
                        2 * ~ * . * ` * ~ * ` . ` ` ` ~ ` ` ` . * * . 2
                        3 ~ . . * ~ . C * * . 4 * . ` ~ . . ~ C ~ ` ~ 3
                        4 ` ` ~ ` ~ ~ ` . . * . ` ` ~ . ~ ~ . * * * ~ 4
                        5 * * ~ ~ . ` . ` * * ~ ` * ~ . . ~ ~ ~ ~ ` . 5
                        6 ~ . ~ ~ * . ` ~ ` ` ` ~ ~ * . . . . . ~ * * 6
                        7 ~ ` * ` . ~ . ` . ` ` . * ` ` * ~ ` * ` ~ ~ 7
                        8 ~ . * . . ~ ~ . ~ * * * C . . . . . * . ` ~ 8
                        9 * ~ * . * * . . ` ~ ` * ` ~ * * ~ * ` ~ . ` 9
                          0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
                                              1                   2
        Note that in the actual game, chests will only be displayed as a C once they are found.''')

    input('\nPress enter to continue...')

    print('''\nWhen you drop a detector directly on a chest, you collect your treasure and the
    detectors update to show how far away the next nearest chest is. If a chest cannot be detected
    within 9 spaces, then all the treausure is out of the detecors range and and X will be displayed
    on the beach map.
    
    Try to collect all of the chests before running out of detectors. Good luck Matey!''')
    
    input('\nPress enter to start your treasure hunt!')
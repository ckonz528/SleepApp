def get_menu_selection(options):
    for i in options:
        print(f'    {i}')
    
    while True:
        menu_select = input('Please enter your selection: ')
        
        error_msg = '***ERROR: Selection must be a number between 1 and ' + str(len(options))

        if not menu_select.isdigit():
            print(error_msg)
        else:
            menu_select = int(menu_select)
            if menu_select > len(options):
                print(error_msg)
            else:
                return(menu_select)

# menu options
main_options = ['1. Log Adherance',               
                '2. Play Treasure Hunt',
                '3. Quit']

log_options = ['1. Log sleep hours', 
                '2. Clean parts',
                '3. Return']

clean_options = ['1. Wipe down the face mask', 
                '2. Replace water in reservoir',
                '3. Clean tubing with soap and water',
                '4. Clean water reservoir with soap and water',
                '5. Clean face mask with soap and water',
                '6. Return']

TH_options = ['1. View number of games earned', 
            '2. Play Treasure Hunt',
            '3. Return']
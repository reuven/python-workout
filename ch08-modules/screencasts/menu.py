def menu(**options):
    while True:
        option_string = '/'.join(sorted(options))
        choice = input(f'Enter an option ({option_string}): ')

        if choice in options:
            return options[choice]()
        else:
            print(f'{choice} is not a valid option')

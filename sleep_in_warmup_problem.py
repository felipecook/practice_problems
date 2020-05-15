# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


def sleep_in(weekday, vacation):
    if weekday is False or vacation is True:
        return True
    else:
        return False


name = "felipe"
greeting = "ciao"
# this is one way to format a string
message = '{}, {}. Welcome!'.format(greeting, name)

# this is another way to format (python 3.6 and higher)
message_2 = f'{greeting.upper}, {name}. Welcome!'


def run_program():
    print(message)
    print(message_2)


run_program()

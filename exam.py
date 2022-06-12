def calculate_score(numbers, multiplier):
    score = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == multiplier * numbers[j]\
                or numbers[j] == multiplier * numbers[i]:
                score += 1
    return score

def get_integer_input(message):
    print(message)
    while True:
        try:
            number_str = input()
            if 'stop' in number_str:
                return None
            number = int(number_str)
            return number
        except ValueError:
            print("Wrong input type, please try again")


if __name__ == "__main__":
    minimal_length = 5
    multiplier = get_integer_input("Please enter a multiplier:")
    numbers = []
    stop = False
    while not stop:
        number = get_integer_input("Please enter a number:")
        if number is None:
            if len(numbers) < minimal_length:
                print(f"Current sequence length is {len(numbers)}, minimal required is {minimal_length}.")
            else:
                stop = True
        else:
            numbers.append(number)
    score = calculate_score(numbers, multiplier)
    if score:
        print(f"Congratulation - it is a Victory with a score {score}")
    else:
        print("Sorry - it is a Defeat")


import random

VALID = {'h', 'm', 's'}


def get_random_pos():
	return random.choice("ABCDEFGHIJ")+str(random.randint(1,10))


def main():
	grid = {}
	sunk = 0
	while sunk < 10:
		pos = get_random_pos()
		if pos in grid:
			continue
		print(pos)
		answer = input().strip().lower()
		assert answer in VALID, "'{}' is not a valid answer, expected {}".format(
			answer, VALID)
		if answer == 's':
			sunk += 1
		grid[pos] = answer




if __name__ == "__main__":
	main()
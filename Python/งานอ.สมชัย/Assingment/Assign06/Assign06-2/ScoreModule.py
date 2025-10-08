def add_score(filename):
    import random
    with open(filename, 'w') as file:
        for _ in range(10):  # 10 students
            scores = [str(random.randint(0, 100)) for _ in range(5)]  # 5 subjects
            total = sum(map(int, scores))
            file.write(", ".join(scores) + f", {total}\n")

def report_score(filename):
    print(f'{"Report Score":>40}')
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())
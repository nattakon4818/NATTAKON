def add_employee(filename):
    print('Enter data employee.')
    emp_id = input('Input employee id : ')
    emp_name = input('Input employee name : ')
    emp_surname = input('Input employee surname : ')
    emp_salary = input('Input employee salary : ')
    fout = open(filename, 'a', encoding='UTF_8')
    fout.write(emp_id + ',' + emp_name + ',' + emp_surname + ',' + emp_salary + '\n')
    fout.close()
    print('Save Data Employee allready.\n')

def read_file(filename):
    with open(filename) as fin:
        for data in fin:
            print(data, end="")

def read_to_memory(filename):
    datas = []
    with open(filename) as fin:
        for data in fin:
            data = data.rstrip('\n')
            datas.append(data.split(','))
    return(datas)

def report_employee(filename):
    datas = read_to_memory(filename)
    mess = 'Report Employee'.center(50) + '\n'
    mess += ('-' * 50) + '\n'
    mess += '| No.|  Id  |  Name    | Surname    |   Salary  |\n'
    mess += ('-' * 50) + '\n'
    n = 1
    for data in datas:
        mess += f'|{n:3} |{data[0]:5} |{data[1]:10} |{data[2]:12} |'
        mess += format(float(data[3]), ',.2f').rjust(10) + '\n'
        n += 1
    mess += ('-' * 50) + '\n'
    print(mess)

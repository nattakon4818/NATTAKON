from random import randint

def random_and_save(filename, colum, day):
    file = open(filename, 'w')

    for i in range(1, colum + 1):
        # total = 0
        for j in range(1, day + 1):
            sale = randint(500, 5000)
            # total += sale
            file.write(str(sale))
            if j < day:
                file.write(",")
        # file.write("," + str(total) + "\n")
        file.write("" + "\n")

    file.close()

def report_sale(filename):
    filename = "sale.txt"

    with open(filename, 'r') as file:
        # อ่านทุกบรรทัดในไฟล์เก็บไว้ในตัวแปร lines
        lines = file.readlines()

        # อ่านบรรทัดแรกจากข้อมูลที่อ่านได้ และลบช่องว่างหน้าหลังออก
        first_line = lines[0].strip()

        # ตรวจสอบว่าข้อมูลในบรรทัดแรกเป็นแนวนอนหรือแนวตั้ง
        if ',' in first_line:
            # ถ้ามีเครื่องหมาย "," หมายถึงข้อมูลเป็นแนวนอน เช่น 1,2,3,4
            # แยกข้อมูลออกเป็นส่วน ๆ โดยใช้เครื่องหมาย "," เป็นตัวแบ่ง
            parts = first_line.split(',')

            # นับจำนวนข้อมูลในแนวนอนแล้วเก็บไว้ในตัวแปร day
            day = len(parts)

        # ถ้าไม่มีเครื่องหมาย "," หมายถึงข้อมูลเรียงในแนวตั้ง
        # สร้างลิสต์ว่างไว้เก็บข้อมูลที่ไม่ว่างเปล่า
        cleaned_lines = []

        # วนลูปอ่านทุกบรรทัดในไฟล์
        for line in lines:
            # ตัดช่องว่างและอักขระขึ้นบรรทัดใหม่ออกจากข้อความ
            stripped_line = line.strip()

            # ตรวจสอบว่าบรรทัดนี้ไม่ว่างเปล่า
            if stripped_line != "":
                # ถ้าไม่ว่าง ให้เพิ่มข้อมูลนั้นลงในลิสต์ cleaned_lines
                cleaned_lines.append(stripped_line)

        # นับจำนวนข้อมูลในแนวตั้ง แล้วเก็บไว้ในตัวแปร colum
        colum = len(cleaned_lines)

    h = "Report of Sales"
    head = ": No.:"
    day_t = ""
    colum_t = ""
    total = 0
    ttt = "Total:"

    for i in range(1, day + 1):
        day_t += f"   Day  {i}   :"
    head += day_t + "   Total    :"

    for n in range(1, colum + 1):
        colum_t += f":{n:>3} :" + "\n"
    # colum_t += open(filename, 'r').read()       ทำถึงตรงนี้


    line = "-" * len(head)
    print(f'{h:^{len(head)}}', line, head, line, sep='\n')
    print(f"{colum_t}", line, sep='')
    print(ttt, line, sep='\n')

random_and_save('sale.txt', 3, 2)
report_sale('sale.txt')
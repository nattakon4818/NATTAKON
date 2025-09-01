import time
import sys

lyrics = [
    "Mmm-mmm",
    "I remember, years ago",
    "Someone told me I should take",
    "Caution when it comes to love, I did",
    "And you were strong and I was not",
    "My illusion, my mistake",
    "I was careless, I forgot, I did",
    "And now when all is done, there is nothing to say",
    "You have won, you can go ahead, tell them",
    "Tell them all I know now",
    "Shout it from the rooftops",
    "Write it on the skyline",
    "All we had is gone now",
    "Tell them I was happy",
    "And my heart is broken",
    "All my scars are open",
    "Tell them what I hoped would be impossible",
    "Impossible Impossible Impossible"
]

def typewriter(text, delay=0.07):  # หน่วงเวลาแต่ละตัว
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')  # ขึ้นบรรทัดใหม่หลังพิมพ์เสร็จ

for line in lyrics:
    typewriter(line)
    time.sleep(1.5)  # พักก่อนขึ้นบรรทัดใหม่
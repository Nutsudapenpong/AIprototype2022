import subprocess #สำหรับ รัน terminal command

if __name__ == "__main__":
    subprocess.run(["ls", "-l"])
    for i in [2,5,6,8]:
        subprocess.run(["pyhon", "python_script_101.py", "9", "--x", "8", f"{i}", "--yval", "2"])

## use output of subprocess
pro = subprocess.Popen(["ls", "-l"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = pro.communicate()
print(out)

##HW ให้ print เฉพาะ ตัวเลขผลลัพธ์การคูณ
for i in [2,5,6,8]:
    pro = subprocess.Popen(["pyhon", "python_script_101.py", "9", "--x", "8", f"{i}", "--yval", "2"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = pro.communicate()
    print(out)


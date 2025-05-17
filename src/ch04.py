# Smart Farming project

while True:  
    try:  
        ph = float(input("ป้อนค่า pH (0-14): "))  
        if 0 <= ph <= 14:  
            break  
        else:  
            print("ค่า pH ต้องอยู่ระหว่าง 0-14")  
    except ValueError:  
        print("โปรดป้อนตัวเลขเท่านั้น!")  

print(f"ค่า pH ที่ถูกต้องคือ: {ph}") 


import pyautogui
import time
import keyboard

def auto_clicker(x, y, clicks=1000, interval=0.1):
    """
    在指定位置自动点击
    
    参数:
    x, y - 点击位置的屏幕坐标
    clicks - 点击次数 (默认1000次)
    interval - 点击间隔(秒) (默认0.1秒)
    """
    print(f"将在位置 ({x}, {y}) 自动点击 {clicks} 次，间隔 {interval} 秒")
    print("按下F6键开始，按下ESC键停止...")
    
    # 等待F6键开始
    keyboard.wait('F6')
    print("开始自动点击...")
    
    try:
        for i in range(clicks):
            if keyboard.is_pressed('esc'):
                print("检测到ESC键，停止自动点击")
                break
            pyautogui.click(x, y)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("程序被用户中断")
    
    print("自动点击完成")

if __name__ == "__main__":
    # 获取屏幕尺寸
    screen_width, screen_height = pyautogui.size()
    print(f"当前屏幕分辨率: {screen_width}x{screen_height}")
    
    # 获取鼠标当前位置
    current_x, current_y = pyautogui.position()
    print(f"当前鼠标位置: ({current_x}, {current_y})")
    
    # 用户输入点击位置
    try:
        x = int(input("请输入点击位置的X坐标(留空使用当前位置): ") or current_x)
        y = int(input("请输入点击位置的Y坐标(留空使用当前位置): ") or current_y)
        clicks = int(input("请输入点击次数(默认1000): ") or 1000)
        interval = float(input("请输入点击间隔(秒，默认0.1): ") or 0.1)
        
        auto_clicker(x, y, clicks, interval)
    except ValueError:
        print("输入错误，请输入有效的数字")

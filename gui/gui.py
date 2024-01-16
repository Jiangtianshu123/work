import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def open_order_details():
    # 创建一个新窗口
    order_details_window = tk.Toplevel(window)
    order_details_window.title("订单详情")

    # 设置新窗口的背景颜色与主窗口相同
    order_details_window.configure(bg=window.cget('bg'))

    # 设置新窗口的初始位置和大小
    x_offset = window.winfo_x() + window.winfo_width()
    y_offset = window.winfo_y()
    order_details_window.geometry(f"+{x_offset}+{y_offset}")
    order_details_window.geometry("600x700")

    # 在新窗口中添加按钮
    button_voice = tk.Button(order_details_window, text="语音启动", width=15, bg="pink", fg="yellow")
    button_voice.place(relx=0.2,rely=0.9)

    button_exit = tk.Button(order_details_window, text="系统退出", width=15, bg="pink", fg="yellow")
    button_exit.place(relx=0.7,rely=0.9)

    fruit1 = tk.StringVar(value="0")
    vegetable1 = tk.StringVar(value="0")
    clothing1 = tk.StringVar(value="0")
    snacks1 = tk.StringVar(value="0")

    fruit2 = tk.StringVar(value="0")
    vegetable2 = tk.StringVar(value="0")
    clothing2 = tk.StringVar(value="0")
    snacks2 = tk.StringVar(value="0")

    fruit3 = tk.StringVar(value="0")
    vegetable3 = tk.StringVar(value="0")
    clothing3 = tk.StringVar(value="0")
    snacks3 = tk.StringVar(value="0")

    # 创建表格
    table = ttk.Treeview(order_details_window, columns=("序号", "摊位", "水果", "蔬菜", "服装", "零食"),
                         show="headings")
    table.pack(pady=20)

    # 添加表头
    table.heading("序号", text="序号")
    table.heading("摊位", text="摊位")
    table.heading("水果", text="水果")
    table.heading("蔬菜", text="蔬菜")
    table.heading("服装", text="服装")
    table.heading("零食", text="零食")

    # 添加示例数据
    data = [
        (1, "1号摊位", fruit1.get(), vegetable1.get(), clothing1.get(), snacks1.get()),
        (2, "2号摊位", fruit2.get(), vegetable2.get(), clothing2.get(), snacks2.get()),
        (3, "3号摊位", fruit3.get(), vegetable3.get(), clothing3.get(), snacks3.get())
    ]

    for row in data:
        table.insert("", "end", values=row)

    # 设置列宽
    for column in ("序号", "摊位", "水果", "蔬菜", "服装", "零食"):
        table.column(column, width=80)

# 创建主窗口
window = tk.Tk()
window.title("越疆科技")
window.geometry("950x700")
window.configure(bg="Wheat")

# 左侧框架
left_frame = tk.Frame(window, bg="light blue", width=300, height=580)
left_frame.place(x=50, y=100)

# 左侧小框架1 - 用户信息
small_frame1 = tk.Frame(left_frame, bg="light sky blue")
small_frame1.place(x=20, y=20, width=260, height=150)

label_user_id = tk.Label(small_frame1, text="用户ID", bg="light sky blue")
label_user_id.pack()

entry_user_id = tk.Entry(small_frame1)
entry_user_id.pack()

label_user_name = tk.Label(small_frame1, text="用户姓名", bg="light sky blue")
label_user_name.pack()

entry_user_name = tk.Entry(small_frame1)
entry_user_name.pack()

button1 = tk.Button(small_frame1, text="采集", width=10, bg="pink", fg="yellow")
button1.place(x=20, y=100)

button2 = tk.Button(small_frame1, text="清除", width=10, bg="pink", fg="yellow")
button2.place(x=160, y=100)

# 左侧小框架2 - 模型信息
small_frame2 = tk.Frame(left_frame, bg="light sky blue")
small_frame2.place(x=20, y=180, width=260, height=150)

label_model_name = tk.Label(small_frame2, text="模型名称", bg="light sky blue")
label_model_name.pack()

entry_model_name = tk.Entry(small_frame2)
entry_model_name.pack()

button3 = tk.Button(small_frame2, text="训练", width=10, bg="pink", fg="yellow")
button3.place(x=20, y=100)

button4 = tk.Button(small_frame2, text="清除", width=10, bg="pink", fg="yellow")
button4.place(x=160, y=100)

# 左侧小框架3 - 图片识别
small_frame3 = tk.Frame(left_frame, bg="light sky blue")
small_frame3.place(x=20, y=340, width=260, height=220)

canvas = tk.Canvas(small_frame3, bg="light sky blue", width=260, height=80, highlightthickness=0)
canvas.pack()

image = Image.open("F:/工作资料/中高职资料/技术资料/金砖资料/培训资料/gui/peo.png")  # 加载图片
image = image.resize((50, 50))
photo = ImageTk.PhotoImage(image)

canvas.create_image(130, 40, image=photo)  # 在画布上添加图片

label_user_id = tk.Label(small_frame3, text="用户ID", bg="light sky blue")
label_user_id.pack(pady=5)  # 修改垂直间距
label_user_id.place(x=30, y=110, anchor="w")  # 将文本左对齐

label_user_name = tk.Label(small_frame3, text="用户姓名", bg="light sky blue")
label_user_name.pack(pady=5)  # 修改垂直间距
label_user_name.place(x=30, y=140, anchor="w")  # 将文本左对齐

button5 = tk.Button(small_frame3, text="识别", width=10, bg="pink", fg="yellow")
button5.place(x=20, y=180)

button6 = tk.Button(small_frame3, text="注销", width=10, bg="pink", fg="yellow")
button6.place(x=160, y=180)

# 右侧框架
right_frame = tk.Frame(window, bg="light blue")
right_frame.place(x=400, y=100, width=520, height=580)

label_distribution = tk.Label(right_frame, text="订单分布图", font=("Arial", 14))
label_distribution.pack(pady=10)

label_demand1 = tk.Label(right_frame, text="1号摊位需求量：     ", bg="light yellow", font=("Arial", 12))
label_demand1.place(x=20, y=120)

label_demand2 = tk.Label(right_frame, text="2号摊位需求量：     ", bg="light green", font=("Arial", 12))
label_demand2.place(x=20, y=220)

label_demand3 = tk.Label(right_frame, text="3号摊位需求量：     ", bg="light Coral", font=("Arial", 12))
label_demand3.place(x=20, y=320)

button_voice = tk.Button(right_frame, text="语音启动", width=15, bg="pink", fg="yellow")
button_voice.place(relx=0.2, rely=0.9, anchor=tk.CENTER)

button_exit = tk.Button(right_frame, text="订单详情", width=15, bg="pink", fg="yellow", command=open_order_details)
button_exit.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

button_order = tk.Button(right_frame, text="系统退出", width=15, bg="pink", fg="yellow")
button_order.place(relx=0.8, rely=0.9, anchor=tk.CENTER)

# 三个摊位的需求量（示例数据）
demand1 = 1
demand2 = 5
demand3 = 5

# 计算百分比
total_demand = demand1 + demand2 + demand3
percent1 = demand1 / total_demand * 100
percent2 = demand2 / total_demand * 100
percent3 = demand3 / total_demand * 100

# 扇形图数据
labels = ['摊位1', '摊位2', '摊位3']
sizes = [percent1, percent2, percent3]
colors = ['lightyellow', 'lightgreen', 'lightcoral']

# 创建扇形图
fig, ax = plt.subplots(figsize=(3, 2.5))  # 指定较小的尺寸
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # 确保饼图是圆形的
plt.title("订单分布图")

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']   # 可以尝试其他通用字体如"Microsoft YaHei"、"Arial Unicode MS"等

# 将Matplotlib绘制的图形转换为Tkinter支持的图像格式
canvas = FigureCanvasTkAgg(fig, master=right_frame)
canvas.draw()
canvas.get_tk_widget().place(relx=0.4, rely=0.18)


label = tk.Label(window, text="人工智能机器人系统集成及应用平台", font=("Arial", 18))
label.pack(pady=20)
# 运行主窗口
window.mainloop()
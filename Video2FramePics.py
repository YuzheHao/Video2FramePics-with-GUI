import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
import cv2
import os

top = tk.Tk()
top.title('Video2FramePics')
top.geometry('440x240')

fin_flag = False  # 默认初始状态为 False
name_got = False

def file_input():
    T1.delete('1.0', tk.END)
    file_path = filedialog.askopenfilename()
    T1.insert('1.0',file_path)
    print(file_path)

def path_input():
    T2.delete('1.0', tk.END)
    directory_path = filedialog.askdirectory()
    T2.insert('1.0',directory_path)
    directory_path=str(directory_path)
    print(directory_path)

def get_fore_name():
    global name_got
    fore_name = T3.get('1.0', tk.END)
    fore_name=str(fore_name)
    print(fore_name)
    name_got = True
    

def v2p():
    global fin_flag
    global name_got
    if fin_flag == True:
        tkinter.messagebox.showinfo( "提示","The program have already been run, if you need another time, please click 'Reset' button.")
    else:
        if name_got == False:
            tkinter.messagebox.showinfo( "提示","You haven't confirmed output files' fore name or haven't input the path!Please make sure there are no blank above and put the 'Confirm' button.")
        else:
            file_path = T1.get('1.0', tk.END)
            directory_path = T2.get('1.0', tk.END)
            fore_name = T3.get('1.0', tk.END)
            num=1 #初始化计数变量
                
            directory_path = directory_path[:len(directory_path)-1]
            fore_name = fore_name[:len(fore_name)-1]
            # 去掉text内文本最后的换行符
            
            if len(directory_path)==3:
                directory_path = directory_path[:len(directory_path)-1]
                # 判断是否是根目录，若是的话，还要把多出来的一个斜杠删掉
            
            loaded_video=cv2.VideoCapture(str(file_path)) # change the folder
            if loaded_video.isOpened():
                rval,frame_video=loaded_video.read()
                print("Open successfully.")
            else:
                rval=False
                print("Open Errors，Please check the folder and the name of loaded_video.")
            while rval:
                rval,frame_video=loaded_video.read()
                cv2.imwrite(directory_path+'/'+fore_name+'_'+str(num)+'.jpg',frame_video) # naming the frame pics
                # 【WATCH OUT】: The output file path is divided by the last "/", on the left is the path to save the frame image, on the right is the name of saved image.
                print("The No.",num,"frame picture has been generated")
                num=num+1
                cv2.waitKey(10) # The time interval between creation of frame images, only can the speed of image's generating be changed, sampling rate of video is unchanged. 
            tkinter.messagebox.showinfo( "提示", "The video has been cut into frame pictures.")
            fin_flag = True
    
def fin():
    global fin_flag
    directory_path = T2.get('1.0', tk.END)    
    directory_path = directory_path[:len(directory_path)-1]
    if fin_flag == False:
        tkinter.messagebox.showinfo( "提示", "The program haven't been run yet.")
    else: 
        os.startfile(directory_path)

def reset():
    global fin_flag
    global name_got
    fin_flag = False
    name_got = False
    T1.delete('1.0', tk.END)
    T2.delete('1.0', tk.END)
    T3.delete('1.0', tk.END)
        
# # # # # #

L1 = tk.Label(top, text='选择输入文件：')
L1.place(x=23, y=25)

T1 = tk.Text(top, width=30, height=2)
T1.place(x=120, y=20)

B1 = tk.Button(top, text =" ... ", command = file_input)
B1.place(x=350, y=20)

# # # # # #

L2 = tk.Label(top, text='选择输出路径：')
L2.place(x=23, y=75)

T2 = tk.Text(top, width=30, height=2)
T2.place(x=120, y=70)

B2 = tk.Button(top, text =" ... ", command = path_input)
B2.place(x=350, y=70)

# # # # # #

L3 = tk.Label(top, text='输出文件前缀：')
L3.place(x=23, y=125)

T3 = tk.Text(top, width=30,height=2)
T3.place(x=120, y=120)

B3 = tk.Button(top, text =" 确定 ", command = get_fore_name)
B3.place(x=350, y=120)

# # # # # #

B5 = tk.Button(top, text =" 重置 ", command =  reset)
B5.place(x=180, y=175)

B3 = tk.Button(top, text =" 运行 ", command = v2p)
B3.place(x=240, y=175)

B4 = tk.Button(top, text =" 打开输出文件夹 ", command =  fin)
B4.place(x=300, y=175)

# # # # # #
          
top.mainloop()

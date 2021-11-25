import csv
import getpass
import os

path = 'C:/Users/user.name/' #csvファイルが保存されているディレクトリ
password = '12345678'

#ファイルの存在確認
def file_exists(file_name):
    return os.path.exists(path+file_name+'.csv')

#本システムのパスワード入力
def security():
    while True:
        p = getpass.getpass()
        if p.lower() == password:
            print("\033[32m"+"Right. Off you go."+"\033[0m")
            break
        else:
            print("\033[31m"+"ERROR : wrong passwords. you're not makoto."+"\033[0m")
            pass

#モード選択
def select_mode():
    while True:
        mode = input("craete file-> 2, input-> 1, reference-> 0, close-> 10: ")
        if(mode=='2' or mode=='1' or mode=='0' or mode=='10'):
            break
        else:
            print("\033[31m"+"ERROR : no mode. re-enter."+"\033[0m")
            pass
    return mode

#csvファイルの新規作成
def create_field():
    print("<create mode>")
    file_name = input("csv file name : ")
    with open(path+file_name+'.csv', 'w', newline="") as f:
        attribute = ['name', 'id', 'passwords']
        w = csv.writer(f)
        w.writerow(attribute)
        f.close()
    print("complete"+"\n")

#データ追加（プラットフォーム等の名前、ID、パスワード）
def input_data():
    print("<input mode>")
    #ファイル名入力
    while True:
        file_name = input("input file name : ")
        if file_exists(file_name):
            break
        else:
            print("\033[31m"+"No such a file"+"\033[0m")
            pass
    
    #データ入力
    while True:
        data = []
        data.append(input("input name : "))
        data.append(input("input id   : "))
        while True:
            pas0 = getpass.getpass("input pass : ")
            pas1 = getpass.getpass("re-input pass : ")
            if(pas0==pas1):
                data.append(pas0)
                break
            else:
                print("\033[31m"+"ERROR : passwords don't match !"+"\033[0m")
            pass

        if("" in data):
            print("\033[31m"+"ERROR : data include blank. re-enter data."+"\033[0m")
            pass
        else:
            break
    
    #csvファイルに書き込み
    with open(path+file_name+'.csv', 'a', newline='') as f:
        w = csv.writer(f)
        w.writerow(data)
        f.close()
    print("complete"+"\n")

    

#保存データの参照
def refer_data():
    print("<reference mode>")
    while True:
        file_name = input("input file name : ")
        try:
            with open(path+file_name+'.csv') as f:
                data_lsit = [line.strip() for line in f.readlines()]
                f.close()
            break
        except FileNotFoundError as e:
            print(e)

    cnt = 0
    data_name = input("input data name : ")
    data_some = [line for line in data_lsit if data_name in line]
    for data in data_some:
        print(data)
        cnt += 1
    print("complete"+"\n")

    if cnt == 0:
        print("\033[31m"+"No such a data"+"\033[0m"+"\n")
        


if __name__=='__main__':
    security() #パスワード入力
    while True:
        mode = select_mode() #モード選択
        if mode=='1':
            input_data()

        
        elif mode=='0':
            refer_data()
        
        elif mode=='2':
            create_field()
        
        else:
            print("bye ノシ")
            break
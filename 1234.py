list_nm=input("輸入n,m:").split(',')
list_time=input("輸入每位客人時間:").split(',')
list_revenue=input("輸入收入:").split(',')

for i in range(len(list_nm)):
    list_nm[i] = int(list_nm[i])
for j in range(len(list_time)):
    list_time[j] = int(list_time[j])
for k in range(len(list_revenue)):
    list_revenue[k] = int(list_revenue[k])
    
loads = [0]*list_nm[1]
profit =0
served_number=0

for l in range(len(list_time)): #l為客人編號
    serve_number=0 #決定要安排的按摩師編號
    switch = 0 #決定此客人最後有沒有人接 如果接了則SWITCH變成1，如果到最後都是0則代表沒人可以接
    for m in range(len(loads)-1):
        if loads[m+1] < loads[m] and loads[m+1] + list_time[l]<360:
            serve_number=m+1
    if serve_number != 0:
        loads[serve_number] += list_time[l]
        profit += list_revenue[l]
        switch=1
        served_number+=1
    if serve_number == 0 and loads[serve_number] + list_time[l]<360:
        loads[serve_number] += list_time[l]
        profit += list_revenue[l]
        switch=1
        served_number+=1

print(str(served_number)+','+str(profit))
        
    

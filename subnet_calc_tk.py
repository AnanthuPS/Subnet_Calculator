import re
from tkinter import *

win= Tk()
win.geometry("750x250")


#Function definition for calculations
def sub_calc():

    ipr = ip.get()
    subnet=int(subnet_add.get())
    lst = []
    one = str(1)
    for i in range(subnet):
        lst.append(one)

    zero = str(0)
    rem = 32 - subnet
    for j in range(rem):
        lst.append(zero)
        
    sub_net_str = ''.join(lst)
    temp = re.findall('........',sub_net_str)
    final_subnet_ip_binary = ".".join(temp)
    #print(f"subnet mask binary : {final_subnet_ip_binary}")
    subnet_lst = final_subnet_ip_binary.split(".")
    count = 0
    temp_list = []
    for i in subnet_lst:
        b_num = list(subnet_lst[count])
        value = 0
        for i in range(len(b_num)):            
            digit = b_num.pop()
            if digit == '1':       
                value = value + pow(2, i)
        count+=1
        temp_list.append(value)
    subnet_mask_ipv4 =".".join(map(str, temp_list))
    #print(f"subnet mask ipv4 : {subnet_mask_ipv4}")
    ###########################################################

    #####################################################
    #Calculating Network address
    network_lst = []
    new = list(ipr.split("."))

    for i in range(len(new)):
        network_lst.append(int(new[i]) & temp_list[i])

    network_address = ".".join(map(str, network_lst))
    #print(network_address)
    ####################################################

    ########################################################################################
    network_address_b = '.'.join([bin(int(x)+256)[3:] for x in network_address.split('.')])
    string_subnet = "".join(final_subnet_ip_binary.split("."))

    def swap(string_subnet):
        replac = {'1':'0', '0':'1'}
        translateble = string_subnet.maketrans(replac)
        res = string_subnet.translate(translateble)
        return res

    str_inverted_subnet= swap(string_subnet)
    inverted= re.findall('........',str_inverted_subnet)
    finalstr_inverted_subnet = ".".join(inverted)
    subnetinvert_lst = finalstr_inverted_subnet.split(".")
    count3 = 0
    inver_lst = []

    for i in subnet_lst:
        b_num = list(subnetinvert_lst[count3])
        value = 0
        for i in range(len(b_num)):           
            digit = b_num.pop()
            if digit == '1':      
                value = value + pow(2, i)
        count3+=1
        inver_lst.append(value)

    subnet_inverted_mask_ipv4 =".".join(map(str, inver_lst))
    brodcast_lst = []
    new1 = list(network_address.split("."))

    for i in range(len(new)):
        brodcast_lst.append(int(new1[i]) | inver_lst[i])
    brodacast_address = ".".join(map(str, brodcast_lst))
    #######################################################################################

    ####################################################
    No_of_available_IP_address= pow(2, rem)
    useable_ip_address = No_of_available_IP_address - 2
    #print(useable_ip_address)
    ####################################################

    #############################################################
    network_lst_for_range = list(network_address.split("."))
    network_lst_for_range[3] = int(network_lst_for_range[3]) + 1
    s_range = ".".join(map(str, network_lst_for_range))
    brodcast_lst[3] = int(brodcast_lst[3]) - 1
    e_range = ".".join(map(str, brodcast_lst))
    iprange = ""
    iprange = s_range + " - " + e_range
    ##############################################################

    ##########################
    #Destroying inner window
    def close_win():
        inner.destroy()
    ##########################    
    
    #######################################################################################
    inner= Toplevel(win)
    inner.geometry("500x400")
    inner.title("Final")
    inner.config(bg='grey')
    Label(inner, text="IP ADDRESS : ", font=('Cooper Std Black',10)).place(x=10,y=40)
    Label(inner, text=ipr, font=('Cooper Std Black',10)).place(x=300,y=40)
    Label(inner, text="SUBNET MASK : ", font=('Cooper Std Black',10)).place(x=10,y=70)
    Label(inner, text=subnet_mask_ipv4, font=('Cooper Std Black',10)).place(x=300,y=70)
    Label(inner, text="NETWORK ADDRESS : ", font=('Cooper Std Black',10)).place(x=10,y=100)
    Label(inner, text=network_address, font=('Cooper Std Black',10)).place(x=300,y=100)
    Label(inner, text="BROADCAST ADDRESS : ", font=('Cooper Std Black',10)).place(x=10,y=130)
    Label(inner, text=brodacast_address, font=('Cooper Std Black',10)).place(x=300,y=130)
    Label(inner, text="AVAILABLE IPs:", font=('Cooper Std Black',10)).place(x=10,y=160)
    Label(inner, text=useable_ip_address, font=('Cooper Std Black',10)).place(x=320,y=160)
    Label(inner, text="AVAILABLE RANGE : ", font=('Cooper Std Black',10)).place(x=10,y=190)
    Label(inner, text=iprange, font=('Cooper Std Black',10)).place(x=300,y=190)
    button2 = Button(inner,text="EXIT",bg='red',command=close_win).place(x=240,y=250)
    ############################################################################################

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Main
win.title('SUBNET CALCULATOR')
win.geometry('400x300')
ip = StringVar(win)
subnet_add=StringVar(win)
label1 = Label(win, text="enter the ip address : ").place(x=10,y=40)
label2 = Label(win, text="enter the subnetmask : ").place(x=10,y=80)
ip_addr = Entry(win, bd =5,textvariable=ip).place(x=190,y=40)
sub_net_mask = Entry(win, bd =5,textvariable=subnet_add).place(x=190,y=80)
button1 = Button(win,text="Calculate",bg='light green',command=sub_calc).place(x=140,y=150)
win.mainloop()
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
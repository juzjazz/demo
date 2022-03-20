import time

all_role=[]
while True:
    choice = input('请选择功能：\n 1.添加角色\n 2.删除角色\n 3.修改角色\n 4.查询角色\n 5.显示所有角色\n 6.退出系统\n')
    if choice=='1':
        name=input('角色名：')
        sex=input('性别：')
        job=input('职业：')
        role=[name,sex,job]
        all_role.append(role)
        print('\t成功添加{}到王者荣耀系统！\n'.format(name))
    elif choice=='2':
        pass
    elif choice=='3':
        pass
    elif choice=='4':
        pass
    elif choice=='5':
        print('显示所有角色')
        print('{}{}{}'.format('名称'.center(10),'性别'.center(10),'职业'.center(10)))
        for role in all_role:
            print(role[0].center(10),end='')
            print(role[1].center(10), end='')
            print(role[2].center(10), end='')
            print()
    elif choice=='6':
        print('正在退出')
        time.sleep(3)
        print('成功退出啦')
        break
    else:
        print('输入错误')



'''
枪类
士兵类
'''


class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count<=0:
            print("%s没有子弹了..."%self.model)
            return
        self.bullet_count -= 1
        print("tututu,子弹剩余%s" % self.bullet_count)

class Solider:
    def __init__(self,name):
        self.name=name
        self.gun=None

qiang=Gun("98K")
qiang.add(30)
qiang.shoot()


#创建士兵
bingbing=Solider("兵兵")
bingbing.gun=qiang
print(bingbing.gun)

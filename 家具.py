class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s]占地面积 %.2f" % (self.name, self.area)


class House:
    def __init__(self, kind, area):
        self.kind = kind
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return "户型：%s\n总面积：%.2f\n剩余面积：%s\n家具：%s" % (self.kind, self.area, self.free_area, self.item_list)

    def add_item(self, item):
        print("要添加%s" % item)
        if item.area > self.free_area:
            print("%s的面积太大了，无法添加" % item.name)
            return
        self.item_list.append(item.name)
        self.free_area-=item.area


# 创建家具

bed = HouseItem("床",40)
chest = HouseItem("衣柜", 20)
table = HouseItem("桌子", 3)
print(bed)
print(chest)
print(table)

my_home = House("两室一厅", 60)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)

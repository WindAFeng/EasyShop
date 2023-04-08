# 配置常量
import yaml
from tinydb import *

config: dict = yaml.load(open('Setting/config.yml', encoding='utf-8'), Loader=yaml.FullLoader)


class EasyShop:
    def __init__(self):
        self.tinydb_path = config['Tiny']['path']
        self.shop_name = config['shop_name']

    def init(self):
        shop = TinyDB(f"{self.tinydb_path}/{self.shop_name}.json")
        shop.close()

    def Add(self, good_name: str, good_price: int, good_quantity: int) -> None:
        shop = TinyDB(f"{self.tinydb_path}/{self.shop_name}.json")
        shop_all = EasyShop().All()
        if len(shop_all) == 0:
            shop.insert({"good_name": good_name,
                         "good_price": good_price,
                         "good_number": "0001",
                         "good_quantity": good_quantity})
        else:
            shop_last = shop_all[-1]
            if int(shop_last['good_number']) == 9999:
                print('到达上限')
            else:
                good_number = shop_last['good_number']
                shop.insert({"good_name": good_name,
                             "good_price": good_price,
                             "good_number": good_number,
                             "good_quantity": good_quantity})

        shop.close()

    def Delete(self, good_number: str) -> None:
        shop = TinyDB(f"{self.tinydb_path}/{self.shop_name}.json")
        shop_search = Query()
        shop.remove(shop_search['good_number'] == good_number)
        good_all = EasyShop().All()
        for i in range(1, len(good_all)):
            if int(good_all[i - 1]['good_number']) + 1 == int(good_all[i]['good_number']):
                pass
            else:
                num = str(int(good_all[i - 1]['good_number']))
                add = 4 - len(num)
                end = '0' * add + str(int(num) + 1)
                EasyShop().Update('good_number', end, good_all[i]['good_number'])
        shop.close()

    def Search(self, good_number: str) -> dict:
        shop = TinyDB(f"{self.tinydb_path}/{self.shop_name}.json")
        shop_search = Query()
        shop_goods = shop.search(shop_search['good_number'] == good_number)
        shop.close()
        if len(shop_goods) == 0:
            return {}
        else:
            return shop_goods[0]

    def All(self) -> list[dict]:
        shop = TinyDB(f"{self.tinydb_path}/{self.shop_name}.json")
        return shop.all()

    def Update(self, good_key: str, good_value, good_number: str):
        shop = TinyDB(f"{self.tinydb_path}/{self.shop_name}.json")
        shop_search = Query()
        shop.update({good_key: good_value}, shop_search['good_number'] == good_number)
        shop.close()

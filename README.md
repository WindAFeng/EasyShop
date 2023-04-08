# EasyShop---python

可用于KOOK机器人的轮子（使用了本地数据库Tinydb开发）
使用教程：

## 0. 使用

克隆本仓库到你项目文件夹下,在EasyShop文件夹下的EasyShop文件夹中添加Database文件夹作为数据库文件夹,并在Setting文件夹下修改配置文件

在文件使用

```python
from EasyShop import EasyShop
shop = EasyShop() # 链接模块
```

## 1. 添加商品

```python
shop.Add('测试',10,10)
```

参数：
商品名称
商品价格
商品数量

## 2. 删除商品

```python
shop.DeleteGoods('0001')
```

参数：
商品编号

## 3. 搜索商品

```python
shop.Search(number='0001')
```

参数:
商品编号

## 4. 更新商品

```python
shop.UpdateGoods("商品价格/数量/名称", "值（请根据数据类型填入）", "商品编号")
```

参数:
商品键
商品值
商品编号

## 5.  所有商品

```python
shop.All()
```

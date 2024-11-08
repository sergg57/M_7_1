from itertools import product
from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name} {self.weight} {self.category}'

    def __repr__(self):
        return f'{self.name} {self.weight} {self.category}'

class Shop:
    __file_name = 'product.txt'

    def get_product(self):
        product_list = []
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            for line in file:
                product_list.append(Product(*line.strip().split()))
                pprint(line)
        return product_list

    def add(self, *product):
        with open(self.__file_name, 'a', encoding='utf-8') as file:
            product_list = self.get_product()
            for prod in product:
                count = 0
                if len(product_list) == 0:
                    file.write(f'{prod.name} {prod.weight} {prod.category}\n')
                else:
                    for item in product_list:
                        if prod.name == item.name:
                            print(f'Продукт {prod.name} уже есть в магазине')
                            break
                        else:
                            count += 1
                            if count == len(product_list):
                                file.write(f'{prod.name} {prod.weight} {prod.category}\n')




s1 = Shop()
p1 = Product('Potato',50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)
print(s1.get_product())

p3 = Product('Apple', 10.8, 'Fruits')
s1.add(p3)
print(s1.get_product())

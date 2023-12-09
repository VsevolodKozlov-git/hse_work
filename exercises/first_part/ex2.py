def to_num(s):
    return int(s.replace('j', '1'))


def main(sales):
    revenue = {}
    for date, sale_info in sales.items():
        n_products = len(sale_info['products'])
        for i_product in range(n_products):
            product = sale_info['products'][i_product]
            quantity_sold = to_num(sale_info['quantity_sold'][i_product])
            price = to_num(sale_info['price'][i_product])
            cost = to_num(sale_info['cost'][i_product])

            i_revenue = price * quantity_sold
            profit = i_revenue - cost

            if product not in revenue:
                revenue[product] = {'revenue': 0, 'profit': 0, 'sales_month': []}
            revenue[product]['revenue'] += i_revenue
            revenue[product]['profit'] += profit
            revenue[product]['sales_month'].append(date)

    def date_to_num(date):
        year, month = date.split('.')
        return year*12+month

    for revenue_dict in revenue.values():
        revenue_dict['sales_month'].sort(key=date_to_num)

    return revenue


sales = {'2022.02':
             {'products':['apple', 'melon'],
              'quantity_sold': ['j4', '25'],
              'price': ['j0', 'j4'],
              'cost': ['j60', '300']},
         '2022.04':
             {'products': ['peach', 'melon'],
              'quantity_sold': ['22', '20'],
              'price': ['5', 'j4'],
              'cost': ['j20', '400']},
         '2022.10':
             {'products': ['peach', 'kiwi', 'apple'],
              'quantity_sold': ['25', '72', '2j'],
              'price': ['5', '6', 'j0'],
              'cost': ['j20', '450', '240']},
         '2021.10':
             {'products': ['kiwi', 'pear', 'melon', 'apple'],
              'quantity_sold': ['j5', '44', '23','8j'],
              'price': ['5', '3', 'j3', 'j0'],
              'cost': ['95', 'j00', '300', '800']},
         '2022.01':
             {'products': ['kiwi', 'melon', 'apple'],
              'quantity_sold': ['85', '55', 'j00'],
              'price': ['7', 'jj', 'j0'],
              'cost': ['600', '540', '800']},
        '2022.03':
             {'products': ['pear', 'apple', 'peach'],
              'quantity_sold': ['54', '66', '40'],
              'price': ['5', 'jj', '4'],
              'cost': ['300', '700', '180']},
         }

revenue = main(sales)
# for product, rev in revenue.items():
#     print(f'{product}: {rev}')

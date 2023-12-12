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
                revenue[product] = {'revenue': 0, 'profit': 0, 'sales_months': []}
            revenue[product]['revenue'] += i_revenue
            revenue[product]['profit'] += profit
            revenue[product]['sales_months'].append(date)

    def date_to_num(date):
        year, month = date.split('.')
        return year*12+month

    for revenue_dict in revenue.values():
        revenue_dict['sales_months'].sort(key=date_to_num)

    return revenue

# u ncomment line below
# revenue = main(sales)

from app.database.order import all_carriers


def select_carrier(order_data):
    suitable_carriers = []
    carriers = all_carriers()
    for carrier in carriers:
        if carrier['capacity'] >= order_data['weight'] and carrier['volume'] >= order_data['volume']:
            suitable_carriers.append(carrier)
    suitable_carriers.sort(key=lambda x: x['cost'])
    return suitable_carriers

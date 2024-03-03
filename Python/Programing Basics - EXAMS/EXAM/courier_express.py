shipment_weight = float(input())
shipment_type = input()
distance_km = int(input())

price_per_km = 0
overprice_kg = 0

if shipment_type == "standard":
    if shipment_weight < 1:
        price_per_km = 0.03
    elif 1 <= shipment_weight < 10:
        price_per_km = 0.05
    elif 10 <= shipment_weight < 40:
        price_per_km = 0.10
    elif 40 <= shipment_weight < 90:
        price_per_km = 0.15
    elif 90 <= shipment_weight <= 150:
        price_per_km = 0.20

if shipment_type == "express":
    if shipment_weight < 1:
        price_per_km = 0.03
        overprice_kg = 0.03 * 0.8
    elif 1 <= shipment_weight < 10:
        price_per_km = 0.05
        overprice_kg = 0.05 * 0.4
    elif 10 <= shipment_weight < 40:
        price_per_km = 0.10
        overprice_kg = 0.1 * 0.05
    elif 40 <= shipment_weight < 90:
        price_per_km = 0.15
        overprice_kg = 0.15 * 0.02
    elif 90 <= shipment_weight <= 150:
        price_per_km = 0.20
        overprice_kg = 0.2 * 0.01

overprice_km = shipment_weight * overprice_kg
total_overprice = distance_km * overprice_km
total_price_km = distance_km * price_per_km + overprice_kg + total_overprice

print(f"The delivery of your shipment with weight of {shipment_weight:.3f} kg. would cost {total_price_km:.2f} lv.")

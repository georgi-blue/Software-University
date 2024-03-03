skumriq_price_kg = float(input())
caca_price_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

palamud_price = skumriq_price_kg + (skumriq_price_kg * 0.6)
palamud_price_kg = palamud_price * palamud_kg
safrid_price = caca_price_kg + (caca_price_kg * 0.8)
safrid_kg_price = safrid_kg * safrid_price
midi_price = 7.5
midi_kg_price = midi_kg * midi_price

total_price = palamud_price_kg + safrid_kg_price + midi_kg_price

print(f"{total_price:.2f}")

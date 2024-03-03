chicken_menus = int(input())
fish_menus = int(input())
vegeterian_menus = int(input())

CHICKEN_MENUS_PRICE = 10.35
FISH_MENUS_PRICE = 12.4
VEGETERIAN_MENUS_PRICE = 8.15
DELIVERY = 2.5

summary_without_desert_and_delivery = (chicken_menus * CHICKEN_MENUS_PRICE)\
                                    + (fish_menus * FISH_MENUS_PRICE)\
                                    + (vegeterian_menus * VEGETERIAN_MENUS_PRICE)
desert = summary_without_desert_and_delivery * 0.2
total_summary = summary_without_desert_and_delivery + desert + DELIVERY

print(total_summary)

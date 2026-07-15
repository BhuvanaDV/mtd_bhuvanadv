total_land = 80
segments = 5
area = total_land / segments

tomato_yield = (area * 0.30 * 10) + (area * 0.70 * 12)
tomato_sales = tomato_yield * 1000 * 7

potato_yield = area * 10
potato_sales = potato_yield * 1000 * 20

cabbage_yield = area * 14
cabbage_sales = cabbage_yield * 1000 * 24

sunflower_yield = area * 0.7
sunflower_sales = sunflower_yield * 1000 * 200

sugarcane_yield = area * 45
sugarcane_sales = sugarcane_yield * 4000

overall_sales = (
    tomato_sales
    + potato_sales
    + cabbage_sales
    + sunflower_sales
    + sugarcane_sales
)

chemical_free_sales = (
    tomato_sales
    + potato_sales
    + cabbage_sales
    + sunflower_sales
)

print("Tomato Sales      :", tomato_sales)
print("Potato Sales      :", potato_sales)
print("Cabbage Sales     :", cabbage_sales)
print("Sunflower Sales   :", sunflower_sales)
print("Sugarcane Sales   :", sugarcane_sales)
print()
print("Overall Sales     :", overall_sales)
print("Chemical-Free Sales after 11 months :", chemical_free_sales)

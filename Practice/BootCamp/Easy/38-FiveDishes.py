from math import ceil
def main():
    dish_list = []
    for _ in range(5):
        dish_list.append(int(input()))

    mod_last_dish = min([(i-1)%10 for i in dish_list])

    cnt = 0
    had_last_meal = False

    for i in range(5):
        if (dish_list[i]-1)%10 == mod_last_dish and not had_last_meal:
            cnt += dish_list[i]
            had_last_meal = True
        else:
            cnt += ceil(dish_list[i]/10)*10
    
    print(cnt)

main()
        

#This is a program to find the net profit for MallowSquishDesigns
import math
#All costs are by per item/piece
#two pieces of stabilizer are used for tshirts and sweatshirts

def clothing_cost():
    cost = (stabilizer_cost * 2) + backing_cost + adhesive_cost + thread_cost
    return cost

def check(x):
    a = False
    while a != True:
        try:
            x = float(x)
            a = True
        except:
            x = input('That is a not a number, please try again.')
            a = False
    return x

def check_int(x):
    a = False
    while a != True:
        try:
            x = int(x)
            a = True
        except:
            x = input('This is not a whole number, please enter a whole number.')
            a = False
    return x

tshirt_cost = 5.00
sweatshirt_cost = 15.00
beanies_cost = 5.00
croc_charms_cost = 0.12
adhesive_cost = 0.45
thread_cost = 0.20
backing_cost = 0.30
stabilizer_cost = 0.14
small_packaging_cost = 0.20
big_packaging_cost = 0.30
envelope_cost = 0.16
croc_bags = 0.07
label_paper_cost = 0.10
laminate_paper_cost = 0.40
cardstock_cost = 0.10
thank_you_cards = 0.06
shipping_cost = check(input('How much is shipping?'))

num_charms = check_int(input('How many croc charms did you sell?'))
num_tshirts = check_int(input('How many t shirts did you sell?'))
num_sweatshirt = check_int(input('How many sweaters did you sell?'))
num_tags = check_int(input('How many tags did you sell?'))
num_beanies = check_int(input('How many beanies did you sell?'))
num_orders = check_int(input('How many orders do you have?'))
num_envelopes = check_int(input('How many envelopes will you use?'))
num_big_orders = check_int(input('How many big bag orders do you have?'))
num_small_orders = check_int(input('How many small bag orders do you have?'))
gross_sales = check(input('How much did you make in gross sales?'))



#Each sheet of laminate paper does 1 and a half tags
total_tag_cost = (math.ceil((num_tags / 1.5)) * laminate_paper_cost) + (num_tags * cardstock_cost)
total_tshirt_cost = (tshirt_cost + clothing_cost()) * num_tshirts
total_sweatshirt_cost = (sweatshirt_cost + clothing_cost() - stabilizer_cost) * num_sweatshirt
total_beanie_cost = (beanies_cost + clothing_cost() - stabilizer_cost) * num_beanies
total_charm_cost = (croc_bags + croc_charms_cost) * num_charms
total_packaging_cost = (num_small_orders * small_packaging_cost) + (num_big_orders * big_packaging_cost) + (num_orders * thank_you_cards) + shipping_cost + (num_envelopes * envelope_cost)
total_cost = total_charm_cost + total_beanie_cost + total_sweatshirt_cost + total_tshirt_cost + total_tag_cost + total_packaging_cost
net_revenue = gross_sales - (total_cost)

print('Your total tag cost is:', end=' $')
print('%.2f'%total_tag_cost)
print('Your total tshirt cost is:', end= ' $')
print('%.2f'%total_tshirt_cost)
print('Your total sweatshirt cost is:', end= ' $')
print('%.2f'%total_sweatshirt_cost)
print('Your total beanie cost is:', end= ' $')
print('%.2f'%total_beanie_cost)
print('Your total charm cost is:', end= ' $')
print('%.2f'%total_charm_cost)
print('Your total packaging cost is:', end= ' $')
print('%.2f'%total_packaging_cost)
print('Your total cost is:', end= ' $')
print('%.2f'%total_cost)
print('Your revenue is:', end= ' $')
print('%.2f'%net_revenue)







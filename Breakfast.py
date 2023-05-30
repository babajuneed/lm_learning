#Breakfast Code
#Author Juneed Baba
#Date 30-05-2023

def args_func(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I want {} in {}\t Breakfast'.format(arg[0],kwargs['fruit']))
    
    
args_func(1,2,3,drink:'Milk',food:'egg',fruit:'banana')

#coding:gbk
"""
程序:RPSLS游戏.
作者:范茗越
"""

def name_to_number(name):
	if name=="石头":
		player_choice_number=0		
	if name=="史波克":
		player_choice_number=1			
	if name=="布":
		player_choice_number=2		
	if name=="蜥蜴":
		player_choice_number=3	
	if name=="剪刀":
		player_choice_number=4
	if name!="石头" and name!="史波克" and name!="布" and name!="蜥蜴" and name!="剪刀":
		player_choice_number=-1					
	return(player_choice_number)
							
def number_to_name(number):
	if number==0:
		a="石头"
	if number==1:
		a="史波克"
	if number==2:
		a="布"
	if number==3:
		a="蜥蜴"
	if number==4:
		a="剪刀"
	return(a)
	
import random						
comp_number=random.randrange(0,5)
						
def rpsls(player_choice):
	a=name_to_number(player_choice)
	c=a-comp_number
	if a==-1:
		return("Error: No Correct Name")	
	if c in range(-4,-2) or c in range(1,3):
		return("您赢了")	
	if c in range(-2,0) or c in range(3,5):
		return("机器赢了")
	if a==comp_number: 
		return("您和机器出的一样呢")
		
							
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
print("您的选择为:",choice_name)
print("机器的选择为:",number_to_name(comp_number))
c=rpsls(choice_name)
print(c)



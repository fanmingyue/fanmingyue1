#coding:gbk
"""
����:RPSLS��Ϸ.
����:����Խ
"""

def name_to_number(name):
	if name=="ʯͷ":
		player_choice_number=0		
	if name=="ʷ����":
		player_choice_number=1			
	if name=="��":
		player_choice_number=2		
	if name=="����":
		player_choice_number=3	
	if name=="����":
		player_choice_number=4
	if name!="ʯͷ" and name!="ʷ����" and name!="��" and name!="����" and name!="����":
		player_choice_number=-1					
	return(player_choice_number)
							
def number_to_name(number):
	if number==0:
		a="ʯͷ"
	if number==1:
		a="ʷ����"
	if number==2:
		a="��"
	if number==3:
		a="����"
	if number==4:
		a="����"
	return(a)
	
import random						
comp_number=random.randrange(0,5)
						
def rpsls(player_choice):
	a=name_to_number(player_choice)
	c=a-comp_number
	if a==-1:
		return("Error: No Correct Name")	
	if c in range(-4,-2) or c in range(1,3):
		return("��Ӯ��")	
	if c in range(-2,0) or c in range(3,5):
		return("����Ӯ��")
	if a==comp_number: 
		return("���ͻ�������һ����")
		
							
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
print("����ѡ��Ϊ:",choice_name)
print("������ѡ��Ϊ:",number_to_name(comp_number))
c=rpsls(choice_name)
print(c)



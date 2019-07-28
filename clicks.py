#!/usr/bin/python/
import sys
#Function to get Number of Digits
def Digits(num):
	count=0;
	while(num>0):
		count=count+1
		num=num/10
	return count
#Function to get min clicks
def reverse(low,high,num1,num2,skip_array):
	skip_no=0
	high_skip=0
	low_skip=0
	tmp_click=0
	high_click=0
	low_click=0
	min_click=0
	#Removing duplicate values from array
	tmp_array=list(set(skip_array))
	#Excluding skipped channels from clicks
	if(num1 < num2):
			r=range(int(num1),int(num2)+1)
	else:
			r=range(int(num2),int(num1)+1)
	for j in range(len(tmp_array)):
		if int(tmp_array[j]) in r:
				skip_no+=1
	r1=range(int(num2),int(high))
	r2=range(int(low),int(num1))
	j=0
	for j in range(len(tmp_array)):
    		if int(tmp_array[j]) in r1:
        		high_skip+=1
	j=0
	for j in range(len(tmp_array)):
        	if int(tmp_array[j]) in r2:
            		low_skip+=1
    #Finding all possible clicks and considering minimum clicks
	tmp_click=int(num1)-int(num2)-int(skip_no);
	if(tmp_click < 0):
		tmp_click=abs(abs(int(num1)-int(num2))-int(skip_no));
	"""nod=Digits(total_channel[i])"""
	high_click=abs(abs(int(high)-int(num1))+abs(int(low)-int(num2))-high_skip-low_skip+1)
	low_click=abs(abs(int(low)-int(num1))+abs(int(high)-int(num2))-high_skip-low_skip+1)
	min_click=min(tmp_click,high_click,low_click)
	return min_click

#Low and High value
low,high=raw_input().split(' ')
if int(low) < 0 or int(low) > 10000 or int(high) < int(low) or int(high) > 10000:
	print "Please enter low value less than high or please maintain low or high within the range 0-10000"
	sys.exit(0)
skip_array=[]
#List of skipped channels
skip=raw_input().split(' ')
if (int(skip[0]) == (len(skip) - 1)):
	for i in range(int(skip[0])):
		if (int(skip[i+1]) <= int(high) and int(skip[i+1])>=int(low)):
			skip_array.append(int(skip[i+1]));
		else:
			print "please enter within channel limit"
			sys.exit(0);
else:
	print "please enter correct number of terms"
	sys.exit(0);
if int(skip[0]) > 40:
	print "Blocked list can be only maximum of 40 channels"
	sys.exit(0);
total=raw_input().split(' ')
total_channel=[]
#Channels to be visited
if(int(total[0]) == (len(total)-1)):
	for i in range(int(total[0])):
		if(int(total[i+1]) <= int(high) and int(total[i+1])>=int(low)):
			if int(total[i+1]) in skip_array:
				print "Element is present in skipped channel list"
				sys.exit(0)
			total_channel.append(int(total[i+1]));
		else:
			print "please enter within channel limit"
			sys.exit(0);
else:
	print "please enter correct no of terms"
if int(total[0]) < 1 or int(total[0]) > 50:
	print "Please enter number of elements between 1 - 50"
	sys.exit(0);
click=0
reverse_click=100001
nod=6
min_click=0
back_click=100001
new_click=100001
temp=100001
for i in range(int(total[0])):
	if(i==0):
		click+=Digits(total_channel[i])
	elif(int(total_channel[i])==int(total_channel[i-2])):
		click+=1
	else:
		if(i>1):
			#Number clicks from back
			back_click=int(reverse(low,high,total_channel[i],total_channel[i-2],skip_array))+1
		#Number of click while moving forward or backward
		new_click=int(reverse(low,high,total_channel[i],total_channel[i-1],skip_array))
		#Clicks as number of digits
		nod=Digits(total_channel[i])
		#Minimum number of clicks
		min_click=min(new_click,back_click,nod)
		click+=int(min_click)
		"""print tmp_click,nod,high_click,low_click,reverse_click,back_click"""
#Total number of clicks
print click

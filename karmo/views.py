from django.shortcuts import render
import subprocess
from .models import Contest,Question,Testcase,Submit_Question
from datetime import datetime
from .forms import NewTopicForm,NewTopicForm2,NewTopicForm3
from django.http import HttpResponse, HttpResponseNotFound
import os
from django.views.decorators.csrf import csrf_exempt
from .models import Code_Snippet
from src.settings import *

from django.core.files.base import ContentFile


from django.core.files.storage import default_storage

import random, string

from django.contrib.auth.decorators import login_required


#g++ -o output_file input_file

import os 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)


@login_required(login_url='/users/login/')
#Compiling,Running file and taking input as a file and generating output in file result.txt
#C++
def hii(request):
	
	#compilation
	cmd = 'g++ working_input.cpp -o a.out' #compiling c++ program
	p = subprocess.call(cmd, shell=True)
	#print(subprocess.check_output(cmd, shell=True))
	if p==0:
		print("Successfully running")
	else:
		print(subprocess.check_output(cmd, shell=True))
		print("Error")
	generate_input()
	return HttpResponse("ok")
	


def generate_input():
	startTime = datetime.now()
	cmd = './a.out < /home/paras/Desktop/coding/my-project/Judge/input.txt > result.txt' #running a c++ program(name of file)

	#command to run code with input file ./test.exe input.txt
	
	p = subprocess.call(cmd, shell=True)
	if p==0:
		print("Successfully running")
	else:
		print(subprocess.check_output(cmd, shell=True))
		print("Error")

	print("Time taken in Judging")
	print(datetime.now() - startTime)
	#running
#C++
#Compiling,Running file and taking input as a file and generating output in file result.txt



@login_required(login_url='/users/login/')
#checking difference of ouptput file of two files
def match_testcase(request):
	cmd = "diff -w result.txt true_result.txt"
	p = subprocess.call(cmd,shell=True)
	if p==0:
		return HttpResponse("Successfully running")
	else:
		print("Error")
		return HttpResponse("WA")
	
#checking difference of ouptput file of two files



#Python

@login_required(login_url='/users/login/')
def hi(request):
	
	#compilation
	cmd = 'python Compile_error.py' 
	p = subprocess.call(cmd, shell=True)
	prin
	#print(subprocess.check_output(cmd, shell=True))
	if p==0:
		print("Successfully running")
	else:
		print(subprocess.check_output(cmd, shell=True))
		print("Error")


#Python


@login_required(login_url='/users/login/')
#GIves compilation result for a code
@csrf_exempt
def take_input(request):
	if request.method == 'POST':
		form = NewTopicForm3(request.POST)
		if form.is_valid():
			new = form.save(commit=False)
			new.save()
			p = new.id
			code = Code_Snippet.objects.get(id = p)
			print(code.code)
			dir_path = BASE_DIR + '/code_compile'
			if not os.path.exists(dir_path):
				os.makedirs(dir_path, 0o777)
			file2write=open(BASE_DIR + '/code_compile/%s.cpp'%p,'w')
			file2write.write(code.code)
			file2write.close()
			file_path = BASE_DIR + '/code_compile/%s.cpp'%p
			if code.language=='c++' or code.language=='C++':
				cmd = 'g++ %s'%file_path
				status = subprocess.call(cmd, shell=True)
				if(status==1):
					print("Compilation Error")
					return HttpResponse("Compilation Error")
				else:
					print("Running Successfully")	
					return HttpResponse("Running Successfully")
	else:
		form = NewTopicForm3()
	return render(request, 'code_snippet.html', {'form' : form})
#GIves compilation result for a code


@login_required(login_url='/users/login/')
@csrf_exempt
def create_contest(request):
	if request.method == 'POST':
		form = NewTopicForm(request.POST)
		if form.is_valid():
			new = form.save(commit=False)
			print(request.user)
			new.created_by = request.user
			cmd = 'mkdir %s'%BASE_DIR + '/Contest'+ '/%s'%new.Name#create folder for contest Name
			print(cmd)
			subprocess.call(cmd, shell=True)

			new.save()
			return HttpResponse("Contest created Successfully")
	else:
		form = NewTopicForm()
	return render(request, 'create_contest.html', {'form' : form})


@login_required(login_url='/users/login/')
@csrf_exempt
def create_question(request):
	if request.method == 'POST':
		form = NewTopicForm2(request.POST)
		if form.is_valid():
			new = form.save(commit=False)
			print(request.user)
			
			cmd = 'mkdir %s/'%BASE_DIR + '/Contest'+ '/%s'%new.contest  +'/%s'%new.Name #create folder for question name in contest
			subprocess.call(cmd, shell=True)
			

			cmd = 'mkdir %s/'%BASE_DIR + '/Contest'+ '/%s'%new.contest  +'/%s'%new.Name + '/code_compile' #create folder code_compile for question in a contest
			subprocess.call(cmd, shell=True)


			cmd = 'mkdir %s/'%BASE_DIR + '/Contest'+ '/%s'%new.contest  +'/%s'%new.Name + '/testcases' #create folder testcases for question in a contest
			subprocess.call(cmd, shell=True)

			cmd = 'mkdir %s/'%BASE_DIR + '/Contest'+ '/%s'%new.contest  +'/%s'%new.Name + '/testcases/Input' #create folder testcases for question in a contest
			subprocess.call(cmd, shell=True)

			cmd = 'mkdir %s/'%BASE_DIR + '/Contest'+ '/%s'%new.contest  +'/%s'%new.Name + '/testcases/Output' #create folder testcases for question in a contest
			subprocess.call(cmd, shell=True)			


			cmd = 'mkdir %s/'%BASE_DIR + '/Contest'+ '/%s'%new.contest  +'/%s'%new.Name + '/question' #create folder question for question in a contest
			subprocess.call(cmd, shell=True)


			cmd = 'mkdir %s/'%BASE_DIR + '/Contest'+ '/%s'%new.contest  +'/%s'%new.Name + '/solution' #create folder solution for question in a contest 
			subprocess.call(cmd, shell=True)

			cmd = 'mkdir %s/'%BASE_DIR + '/Contest'+ '/%s'%new.contest  +'/%s'%new.Name + '/coreoperations' #create folder coreoperations for operations 
			subprocess.call(cmd, shell=True)


			#write question to a file in local
			file2write=open('%s'%BASE_DIR + '/Contest'+ '/%s'%new.contest  +'/%s'%new.Name + '/question' + '/Question.txt','w')
			file2write.write(new.Prob_statement)
			file2write.close()
			#write question to a file in local

			#write question to a file in local
			file2write=open('%s'%BASE_DIR + '/Contest'+ '/%s'%new.contest  +'/%s'%new.Name + '/solution' + '/Solution.cpp','w')
			file2write.write(new.solution)
			file2write.close()
			#write question to a file in local

			new.created_by = request.user

			new.save()
			return HttpResponse("Question Created")
	else:
		form = NewTopicForm2()
	return render(request, 'create_question.html', {'form' : form})


@login_required(login_url='/users/login/')
#Upload Input,Output Testcase for a question in a particular contest
def testcase(request,pk,pkk):
	question = Question.objects.get(pk=pkk)
	contest = Contest.objects.get(pk =pk)
	return render(request, 'upload_testcase.html',{'question':question,'contest':contest})

def testcase_main(request,pk,pkk):
	question = Question.objects.get(pk=pkk)
	contest = Contest.objects.get(pk =pk)	
	print(question)
	print(contest)
	if request.method == 'POST':
		files = request.FILES.getlist("file")
		folder = BASE_DIR + '/Contest/' + '%s/'%contest + '%s'%question +'/testcases'
		folder2 = '/Contest/' + '%s/'%contest + '%s'%question +'/testcases'
		print(folder)
		f=0
		test = Testcase.objects.create(contest=contest,question=question)
		#Added x for randomness in input output file name
		#x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(4))
		for files in files:
			ext = files.name.split('.')[-1]
			if ext=='txt' or ext=='Txt':
				if f==0:#input file
					default_storage.save(folder + '/Input' + '/i' + '%s'%str(test.id)  +".txt", ContentFile(files.read()))
					print(test.id)
					print(Testcase.objects.filter(id = test.id))
					Testcase.objects.filter(id = test.id).update(inpt =(folder2 + '/Input' + '/i' + '%s'%str(test.id)  +".txt") )
				else:
					default_storage.save(folder + '/Output'+'/o' + '%s'%str(test.id) + ".txt", ContentFile(files.read()))
					Testcase.objects.filter(id = test.id).update(outp =(folder2 + '/Output' + '/o' + '%s'%str(test.id)  +".txt") )
				f = f+1	
	return HttpResponse("Uploaded Successfully")	
#Upload Input,Output Testcase for a question in a particular contest


@login_required(login_url='/users/login/')
#For single question
def question(request,pk,cont):
	question = Question.objects.get(pk=pk)
	contest = Contest.objects.get(pk =cont)
	print(contest)
	print(question)
	return render(request,'single_question.html',{'question':question,'contest':contest})
#For single question


@login_required(login_url='/users/login/')
#See all exsisting contests
def exsisting_contest(request):
	print(request.META['HTTP_HOST'])
	contest = Contest.objects.all()
	print(contest)
	return render(request,'exsisting_contest.html',{'contest':contest})
#See all exsisting contests


#To display all questions
'''
logic to display solved question using flag of verdict =1 and for unsolved question taking all question in a set and removing solved question from set.
'''
@login_required(login_url='/users/login/')
def problem(request,pk):
	contest = Contest.objects.filter(pk=pk)
	question = Question.objects.filter(contest=pk)
	user = request.user
	
	solved_question = Submit_Question.objects.filter(user=user,contest=contest,question=question,verdict=1)
	
	my_set = set()
	for solved_question in solved_question:
		my_set.add(solved_question.question)
	
	print(my_set)

	for contest in contest:
		contests = contest
	return render(request,'problem.html',{'contest':contests,'question':question,'my_set':my_set})



@login_required(login_url='/users/login/')
#submit solution in contest
#file saving in code_compile folder for contest with name of user +id
def submit_problem_contest(request,pk,pkk):
	startTime = datetime.now()
	contest = Contest.objects.get(pk=pk)
	question = Question.objects.get(pk=pkk)
	if request.method == 'POST':
		form = NewTopicForm3(request.POST)
		if form.is_valid():
			new = form.save(commit=False)
			new.save()
			p = new.id
			code = Code_Snippet.objects.get(id = p)
			print(code.code)
			dir_path = BASE_DIR + '/Contest/%s'%contest.Name + '/%s'%question.Name +'/code_compile'

			path_to_question = BASE_DIR + '/Contest/%s'%contest.Name + '/%s'%question.Name

			if not os.path.exists(dir_path):
				os.makedirs(dir_path, 0o777)
			nam = request.user
			compile_folder_path = BASE_DIR + '/Contest/%s'%contest.Name + '/%s'%question.Name +'/code_compile/%s'%nam + '%s'%p
			if not os.path.exists(compile_folder_path):
				os.makedirs(compile_folder_path, 0o777)
			file2write=open(compile_folder_path + '/%s'%nam + '%s'%p + '.cpp','w')
			file2write.write(code.code)
			file2write.close()
			file_path = compile_folder_path +'/%s'%nam + '%s'%p + '.cpp'
			if code.language=='c++' or code.language=='C++':
				cmd = 'g++ %s'%file_path +" -o "+ compile_folder_path +'/%s'%nam + '%s'%p + '.out'
				path_to_send = compile_folder_path +'/%s'%nam + '%s'%p + '.out'
				status = subprocess.call(cmd, shell=True)

				compile_folder_path_input = compile_folder_path + '/Input'
				if not os.path.exists(compile_folder_path_input):
					os.makedirs(compile_folder_path_input, 0o777)

				compile_folder_path_output = compile_folder_path + '/Output'
				if not os.path.exists(compile_folder_path_output):
					os.makedirs(compile_folder_path_output, 0o777)

				if(status==1):
					print("Compilation Error")
					return HttpResponse("Compilation Error")
				else:
					print("Running Successfully")
					ans =0	
					ans =	generate_input_contest(path_to_send,contest,question,path_to_question,compile_folder_path)
					if ans==0:
						return HttpResponse("WA")
					else:
						print(datetime.now() - startTime)
						user = request.user
						Submit_Question.objects.create(user=user,contest=contest,question=question,verdict=1)
						return HttpResponse("AC",datetime.now() - startTime)


	else:
		form = NewTopicForm3()
	return render(request, 'code_snippet.html', {'form' : form})	#submit solution in contest

def generate_input_contest(path_to_send,contest,question,path_to_question,compile_folder_path):
	startTime = datetime.now()
	testcase = Testcase.objects.filter(contest=contest,question=question)
	
	#path_to_send = /home/paras/Desktop/coding/my-project/Judge/Contest/Algofuzz18.1/Divisor4/code_compile/demo70/demo70.out
	ans =0
	for testcase in testcase:
		print(testcase.inpt)
		name_out = testcase.outp.split('/')[-1]
		#cmd = '/home/paras/Desktop/coding/my-project/Judge/Contest/Algofuzz18.1/Divisor4/code_compile/demo78/demo78.out < /home/paras/Desktop/coding/my-project/Judge/Contest/Algofuzz18.1/Divisor4/testcases/Input/i18.txt > result.txt'
		cmd = '%s'%path_to_send + ' < ' '%s'%BASE_DIR + '%s'%testcase.inpt + ' > ' + '%s'%compile_folder_path + '/Output/%s'%name_out #running a c++ program(name of file)
		out_testcase = '%s'%BASE_DIR + '%s'%testcase.outp 
		compile_testcase = '%s'%compile_folder_path + '/Output/%s'%name_out
		print("this",out_testcase,compile_testcase)
		p = subprocess.call(cmd, shell=True)
		if p==0:
			ans = match_testcase_contest(out_testcase,compile_testcase,ans)
			if ans==0:
				break
	if ans==0:
		return ans
	else:
		return ans	


def match_testcase_contest(output_path,compile_path,ans):
	cmd = "diff -w %s"%output_path + " %s"%compile_path
	p = subprocess.call(cmd,shell=True)
	if p==0:
		ans=1
		return ans
	else:
		ans=0
		print("Error")
		return ans


@login_required(login_url='/users/login/')
#Function to run file
def run_file():
	#running	
	print("hi")
	startTime = datetime.now()
	cmd = './a.out' #running a c++ program(name of file)

	#command to run code with input file ./test.exe input.txt
	
	p = subprocess.call(cmd, shell=True)
	if p==0:
		print("Successfully running")
	else:
		print(subprocess.check_output(cmd, shell=True))
		print("Error")

	print("Time taken in Judging")
	print(datetime.now() - startTime)
	#running

#Function to run file

def ranking(request,pk):
	submission = Submit_Question.objects.filter(contest=pk,verdict=1).order_by('time')
	print(submission)
	return render(request,'ranking.html',{'submission':submission})




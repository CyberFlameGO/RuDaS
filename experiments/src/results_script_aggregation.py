'''
 Copyright IBM Corp. 1992, 1993 All Rights Reserved
SPDX-License-Identifier: Apache-2.0
'''

import os


DATASETS_EXP_2 = ['CHAIN-XS-2', 'CHAIN-XS-2-0', 'CHAIN-XS-2-1', 'CHAIN-XS-2-2', 'CHAIN-XS-2-3', 'CHAIN-XS-2-4', 'CHAIN-XS-2-5', 'CHAIN-XS-2-6', 'CHAIN-XS-2-7', 'CHAIN-XS-2-8', 'CHAIN-XS-3', 'CHAIN-XS-3-0', 'CHAIN-XS-3-1', 'CHAIN-XS-3-2', 'CHAIN-XS-3-3', 'CHAIN-XS-3-4', 'CHAIN-XS-3-5', 'CHAIN-XS-3-6', 'CHAIN-XS-3-7', 'CHAIN-XS-3-8', 'CHAIN-S-2', 'CHAIN-S-2-0', 'CHAIN-S-2-1', 'CHAIN-S-2-2', 'CHAIN-S-2-3', 'CHAIN-S-2-4', 'CHAIN-S-2-5', 'CHAIN-S-2-6', 'CHAIN-S-2-7', 'CHAIN-S-2-8', 'CHAIN-S-3', 'CHAIN-S-3-0', 'CHAIN-S-3-1', 'CHAIN-S-3-2', 'CHAIN-S-3-3', 'CHAIN-S-3-4', 'CHAIN-S-3-5', 'CHAIN-S-3-6', 'CHAIN-S-3-7', 'CHAIN-S-3-8', 'RDG-XS-2', 'RDG-XS-2-0', 'RDG-XS-2-1', 'RDG-XS-2-2', 'RDG-XS-2-3', 'RDG-XS-2-4', 'RDG-XS-2-5', 'RDG-XS-2-6', 'RDG-XS-2-7', 'RDG-XS-2-8', 'RDG-XS-3', 'RDG-XS-3-0', 'RDG-XS-3-1', 'RDG-XS-3-2', 'RDG-XS-3-3', 'RDG-XS-3-4', 'RDG-XS-3-5', 'RDG-XS-3-6', 'RDG-XS-3-7', 'RDG-XS-3-8', 'RDG-S-2', 'RDG-S-2-0', 'RDG-S-2-1', 'RDG-S-2-2', 'RDG-S-2-3', 'RDG-S-2-4', 'RDG-S-2-5', 'RDG-S-2-6', 'RDG-S-2-7', 'RDG-S-2-8', 'RDG-S-3', 'RDG-S-3-0', 'RDG-S-3-1', 'RDG-S-3-2', 'RDG-S-3-3', 'RDG-S-3-4', 'RDG-S-3-5', 'RDG-S-3-6', 'RDG-S-3-7', 'RDG-S-3-8', 'DRDG-XS-2', 'DRDG-XS-2-0', 'DRDG-XS-2-1', 'DRDG-XS-2-2', 'DRDG-XS-2-3', 'DRDG-XS-2-4', 'DRDG-XS-2-5', 'DRDG-XS-2-6', 'DRDG-XS-2-7', 'DRDG-XS-2-8', 'DRDG-XS-3', 'DRDG-XS-3-0', 'DRDG-XS-3-1', 'DRDG-XS-3-2', 'DRDG-XS-3-3', 'DRDG-XS-3-4', 'DRDG-XS-3-5', 'DRDG-XS-3-6', 'DRDG-XS-3-7', 'DRDG-XS-3-8', 'DRDG-S-2', 'DRDG-S-2-0', 'DRDG-S-2-1', 'DRDG-S-2-2', 'DRDG-S-2-3', 'DRDG-S-2-4', 'DRDG-S-2-5', 'DRDG-S-2-6', 'DRDG-S-2-7', 'DRDG-S-2-8', 'DRDG-S-3', 'DRDG-S-3-0', 'DRDG-S-3-1', 'DRDG-S-3-2', 'DRDG-S-3-3', 'DRDG-S-3-4', 'DRDG-S-3-5', 'DRDG-S-3-6', 'DRDG-S-3-7', 'DRDG-S-3-8']
DATASETS_EXP_1 = ['DRDG-XS-2', 'DRDG-XS-2-0', 'DRDG-XS-2-1',  'DRDG-XS-2-2', 'DRDG-XS-2-3', 'DRDG-XS-2-4', 'DRDG-XS-3', 'DRDG-XS-3-0', 'DRDG-XS-3-1', 'DRDG-XS-3-2', 'DRDG-XS-3-3', 'DRDG-XS-3-4','DRDG-S-2', 'DRDG-S-2-0', 'DRDG-S-2-1',  'DRDG-S-2-2', 'DRDG-S-2-3', 'DRDG-S-2-4', 'DRDG-S-3', 'DRDG-S-3-0', 'DRDG-S-3-1',  'DRDG-S-3-2', 'DRDG-S-3-3', 'DRDG-S-3-4', 'RDG-XS-2', 'RDG-XS-2-0', 'RDG-XS-2-1',  'RDG-XS-2-2', 'RDG-XS-2-3', 'RDG-XS-2-4','RDG-XS-3', 'RDG-XS-3-0', 'RDG-XS-3-1', 'RDG-XS-3-2', 'RDG-XS-3-3', 'RDG-XS-3-4', 'RDG-S-2', 'RDG-S-2-0', 'RDG-S-2-1',  'RDG-S-2-2', 'RDG-S-2-3', 'RDG-S-2-4', 'RDG-S-3', 'RDG-S-3-0', 'RDG-S-3-1',  'RDG-S-3-2', 'RDG-S-3-3', 'RDG-S-3-4']



def print_measures2(file_name,FOIL,NTP,NEURAL_LP,AMIE):
	file = open(file_name, "w+")
	file.write("\n FOIL \n")
	count=0
	for i in FOIL:
		count = count+1
		file.write(i)
		if count in [40,80]:
			file.write("\n")
	file.write("\n NTP \n")
	count = 0
	for i in NTP:
		count = count + 1
		file.write(i)
		if count in [40,80]:
			file.write("\n")
	file.write("\n NEURAL_LP \n")
	count = 0
	for i in NEURAL_LP:
		count = count + 1
		file.write(i)
		if count in [40,80]:
			file.write("\n")
	file.write("\n AMIE \n")
	count = 0
	for i in AMIE:
		count = count + 1
		i=i.replace("\t","").replace(" ",'')
		file.write(i)
		if count in [40,80]:
			file.write("\n")


	averageFOIL=0
	no_eval_count=0
	for i in FOIL:
		if "no_eval" not in i:
			averageFOIL+=float(i)
		else:
			no_eval_count+=1
	if averageFOIL >0:
		averageFOIL /= len(FOIL) - no_eval_count

	averageNTP = 0
	no_eval_count = 0
	for i in NTP:
		if "no_eval" not in i:
			averageNTP += float(i)
		else:
			no_eval_count += 1
	if averageNTP > 0:
		averageNTP /= len(NTP) - no_eval_count

	averageNEURAL_LP = 0
	no_eval_count = 0
	for i in NEURAL_LP:
		if "no_eval" not in i:
			averageNEURAL_LP += float(i)
		else:
			no_eval_count += 1
	if averageNEURAL_LP>0:
		averageNEURAL_LP /= len(NEURAL_LP) - no_eval_count

	averageAMIE = 0
	no_eval_count = 0
	for i in AMIE:
		if "no_eval" not in i:
			averageAMIE += float(i)
		else:
			no_eval_count += 1
	if averageAMIE>0:
		averageAMIE /= len(AMIE) - no_eval_count
	print(averageFOIL,averageNTP,averageNEURAL_LP,averageAMIE)


def print_measures1(file_name,FOIL,NTP,NEURAL_LP,AMIE):
	file = open(file_name, "w+")
	file.write("\n FOIL \n")
	count=0
	for i in FOIL:
		count = count+1
		file.write(i)
		if count in [24]:
			file.write("\n")
	file.write("\n NTP \n")
	count = 0
	for i in NTP:
		count = count + 1
		file.write(i)
		if count in [24]:
			file.write("\n")
	file.write("\n NEURAL_LP \n")
	count = 0
	for i in NEURAL_LP:
		count = count + 1
		file.write(i)
		if count in [24]:
			file.write("\n")
	file.write("\n AMIE \n")
	count = 0
	for i in AMIE:
		count = count + 1
		i=i.replace("\t","").replace(" ",'')
		file.write(i)
		if count in [24]:
			file.write("\n")

def read_measures(file_name):
	no_eval = False
	measures =["no_eval\n","no_eval\n","no_eval\n","no_eval\n","no_eval\n","no_eval\n","no_eval\n"]
	Herbrant_accuracy = "no_eval"
	Hscore = "no_eval"
	Accuracy = "no_eval"
	Precision = "no_eval"
	Recall = "no_eval"
	F1score = "no_eval"
	RuleScore = "no_eval"
	try:
		file = open(file_name, "r")
	except:
		no_eval=True
	if no_eval:
		return measures
	else:
		line = file.readline()
		while line:
			if "Herbrant accuracy" in line:
				Herbrant_accuracy=line.split("\t")[1]
			if "Hscore" in line:
				Hscore=line.split("\t")[1]
			if "Accuracy" in line:
				Accuracy=line.split("\t")[1]
			if "Precision" in line:
				Precision=line.split("\t")[1]
			if "Recall" in line:
				Recall=line.split("\t")[1]
			if "F1score" in line:
				F1score=line.split("\t")[1]
			if "Rule-score" in line:
				RuleScore = line.split("\t")[1]
			line = file.readline()
		measures = [Herbrant_accuracy,Hscore,Accuracy,Precision,Recall,F1score,RuleScore]
	file.close()
	return measures


def read_exp_2(path):
	
	datasets = DATASETS_EXP_2
	# FOIL
	FOIL_Herbrant_accuracy=[]
	FOIL_Hscore=[]
	FOIL_Accuracy=[]
	FOIL_Precision=[]
	FOIL_Recall=[]
	FOIL_F1score=[]
	FOIL_RuleScore=[]
	# NTP
	NTP_Herbrant_accuracy=[]
	NTP_Hscore=[]
	NTP_Accuracy=[]
	NTP_Precision=[]
	NTP_Recall=[]
	NTP_F1score=[]
	NTP_RuleScore=[]
	# NEURAL_LP
	NEURAL_LP_Herbrant_accuracy=[]
	NEURAL_LP_Hscore=[]
	NEURAL_LP_Accuracy=[]
	NEURAL_LP_Precision=[]
	NEURAL_LP_Recall=[]
	NEURAL_LP_F1score=[]
	NEURAL_LP_RuleScore=[]
	# AMIE
	AMIE_Herbrant_accuracy=[]
	AMIE_Hscore=[]
	AMIE_Accuracy=[]
	AMIE_Precision=[]
	AMIE_Recall=[]
	AMIE_F1score=[]
	AMIE_RuleScore=[]
	# FOIL
	for dataset in datasets:
		mes=read_measures(path+"FOIL/"+dataset+"/INCOMPLETE_NOISE2/evaluation.txt")
		FOIL_Herbrant_accuracy.append(mes[0])
		FOIL_Hscore.append(mes[1])
		FOIL_Accuracy.append(mes[2])
		FOIL_Precision.append(mes[3])
		FOIL_Recall.append(mes[4])
		FOIL_F1score.append(mes[5])
		FOIL_RuleScore.append(mes[6])
	# NTP
	for dataset in datasets:
		mes=read_measures(path+"ntp/"+dataset+"/INCOMPLETE_NOISE2/evaluation.txt")
		# NTP
		NTP_Herbrant_accuracy.append(mes[0])
		NTP_Hscore.append(mes[1])
		NTP_Accuracy.append(mes[2])
		NTP_Precision.append(mes[3])
		NTP_Recall.append(mes[4])
		NTP_F1score.append(mes[5])
		NTP_RuleScore.append(mes[6])
	# NEURAL_LP
	for dataset in datasets:
		mes=read_measures(path+"Neural-LP/"+dataset+"/INCOMPLETE_NOISE2/evaluation.txt")
		NEURAL_LP_Herbrant_accuracy.append(mes[0])
		NEURAL_LP_Hscore.append(mes[1])
		NEURAL_LP_Accuracy.append(mes[2])
		NEURAL_LP_Precision.append(mes[3])
		NEURAL_LP_Recall.append(mes[4])
		NEURAL_LP_F1score.append(mes[5])
		NEURAL_LP_RuleScore.append(mes[6])
	# AMIE
	for dataset in datasets:
		mes=read_measures(path+"amiep/"+dataset+"/INCOMPLETE_NOISE2/evaluation.txt")
		AMIE_Herbrant_accuracy.append(mes[0])
		AMIE_Hscore.append(mes[1])
		AMIE_Accuracy.append(mes[2])
		AMIE_Precision.append(mes[3])
		AMIE_Recall.append(mes[4])
		AMIE_F1score.append(mes[5])
		AMIE_RuleScore.append(mes[6])
	print_measures2(os.getcwd()+"/Herbrant_accuracy.txt",FOIL_Herbrant_accuracy,NTP_Herbrant_accuracy,NEURAL_LP_Herbrant_accuracy,AMIE_Herbrant_accuracy)
	print_measures2(os.getcwd()+"/Hscore.txt",FOIL_Hscore,NTP_Hscore,NEURAL_LP_Hscore,AMIE_Hscore)
	print_measures2(os.getcwd()+"/Accuracy.txt",FOIL_Accuracy,NTP_Accuracy,NEURAL_LP_Accuracy,AMIE_Accuracy)
	print_measures2(os.getcwd()+"/Precision.txt",FOIL_Precision,NTP_Precision,NEURAL_LP_Precision,AMIE_Precision)
	print_measures2(os.getcwd()+"/Recall.txt",FOIL_Recall,NTP_Recall,NEURAL_LP_Recall,AMIE_Recall)
	print_measures2(os.getcwd()+"/F1score.txt",FOIL_F1score,NTP_F1score,NEURAL_LP_F1score,AMIE_F1score)
	print_measures2(os.getcwd()+"/RuleScore.txt",FOIL_RuleScore,NTP_RuleScore,NEURAL_LP_RuleScore,AMIE_RuleScore)



def read_mode(mode, path):
	
	datasets = DATASETS_EXP_1
	# FOIL
	FOIL_Herbrant_accuracy=[]
	FOIL_Hscore=[]
	FOIL_Accuracy=[]
	FOIL_Precision=[]
	FOIL_Recall=[]
	FOIL_F1score=[]
	# NTP
	NTP_Herbrant_accuracy=[]
	NTP_Hscore=[]
	NTP_Accuracy=[]
	NTP_Precision=[]
	NTP_Recall=[]
	NTP_F1score=[]
	# NEURAL_LP
	NEURAL_LP_Herbrant_accuracy=[]
	NEURAL_LP_Hscore=[]
	NEURAL_LP_Accuracy=[]
	NEURAL_LP_Precision=[]
	NEURAL_LP_Recall=[]
	NEURAL_LP_F1score=[]
	# AMIE
	AMIE_Herbrant_accuracy=[]
	AMIE_Hscore=[]
	AMIE_Accuracy=[]
	AMIE_Precision=[]
	AMIE_Recall=[]
	AMIE_F1score=[]
	# FOIL
	for dataset in datasets:
		mes=read_measures(path+"FOIL/"+dataset+"/"+mode+"/evaluation.txt")
		FOIL_Herbrant_accuracy.append(mes[0])
		FOIL_Hscore.append(mes[1])
		FOIL_Accuracy.append(mes[2])
		FOIL_Precision.append(mes[3])
		FOIL_Recall.append(mes[4])
		FOIL_F1score.append(mes[5])
		#if mes[1]==None:
		#	print(dataset)
	# NTP
	for dataset in datasets:
		mes=read_measures(path+"ntp/"+dataset+"/"+mode+"/evaluation.txt")
		# NTP
		NTP_Herbrant_accuracy.append(mes[0])
		NTP_Hscore.append(mes[1])
		NTP_Accuracy.append(mes[2])
		NTP_Precision.append(mes[3])
		NTP_Recall.append(mes[4])
		NTP_F1score.append(mes[5])
	# NEURAL_LP
	for dataset in datasets:
		mes=read_measures(path+"Neural-LP/"+dataset+"/"+mode+"/evaluation.txt")
		NEURAL_LP_Herbrant_accuracy.append(mes[0])
		NEURAL_LP_Hscore.append(mes[1])
		NEURAL_LP_Accuracy.append(mes[2])
		NEURAL_LP_Precision.append(mes[3])
		NEURAL_LP_Recall.append(mes[4])
		NEURAL_LP_F1score.append(mes[5])
	# AMIE
	for dataset in datasets:
		mes=read_measures(path+"amiep/"+dataset+"/"+mode+"/evaluation.txt")
		AMIE_Herbrant_accuracy.append(mes[0])
		AMIE_Hscore.append(mes[1])
		AMIE_Accuracy.append(mes[2])
		AMIE_Precision.append(mes[3])
		AMIE_Recall.append(mes[4])
		AMIE_F1score.append(mes[5])
	print_measures1(os.getcwd()+"../results/"+mode+"_Hscore.txt",FOIL_Hscore,NTP_Hscore,NEURAL_LP_Hscore,AMIE_Hscore)

def read_exp_1(path):
	read_mode("COMPLETE1",path)
	read_mode("INCOMPLETE1",path)
	read_mode("INCOMPLETE_NOISE1",path)



path = os.getcwd()+"/../output/exp2/"
read_exp_2(path)
path = os.getcwd()+"/../output/exp1/"
read_exp_1(path)

#rule score
#path = "../output/test/"
#read_exp_2(path)
import pickle
name = ["MJ","Rich","AN"]
skill = ["Java","Raj","Python"]
pickle_file = open("emp1.txt","ab")
pickle.dump(name,pickle_file)
pickle.dump(skill,pickle_file)
pickle_file.close()
pickle_file_read = open("emp1.txt",'rb')
name_list = pickle.load(pickle_file_read)
skill_list = pickle.load(pickle_file_read)

print(name_list, "and ", skill_list)

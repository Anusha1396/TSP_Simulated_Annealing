import argparse
from sa import *
from util import *

parser = argparse.ArgumentParser(description='NISO')

# Instance file argument
parser.add_argument('-inst', type=str, help='Instance File')

# Algorithm argument
parser.add_argument('-alg', type=str, help='Algorithm')

# cutoff time
parser.add_argument('-time', type=str, help='Cutoff Time')

# Seed
parser.add_argument('-seed', type=int, help='Random Seed')


args = parser.parse_args()

input_file = args.inst
alg = args.alg
Cutoff_Time = args.time
seed = args.seed

instance = input_file.split("/")[-1].split(".")[0]
output_path = "./output/"

if alg == "SA":
	distance = read_file(input_file)
	start_time = time.time()
	print("Seed is:", seed)
	random.seed(seed)
	sa = Simulated_annealing(distance, limited_time = int(Cutoff_Time))
	sa.batch_anneal(times = 100)
	outfile_name = "solution" +".csv"
	outfolder = output_path
	if not os.path.exists(outfolder):
			os.mkdir(outfolder)
	solution(os.path.join(output_path, outfile_name), sa.best_dis, sa.best_tour)


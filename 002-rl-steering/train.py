'''
This is a train module for full step-by-step RL tutorial
You need to run this to start training a new RL model/policy
Pre-requisite: Carla Sim should be running before you start training
You must use use the same versions of Carla, e.g. 9.15 of the sim and Carla Python module 9.15

Terminology:
	Episode: one go of the car trying to "live" in the simulation and earn max rewards.
				Episode start from spawning a new car and ends with either car crashing or episode duration limit running out

	Timestep: one frame through simulation: the car gets a camera image, reward from prior step and then it makes a decision on control input and sends it to simulation

	Reward logic: each timestep a logic is applied to calculate a reward from latest step. 
				This logic represents you describing the desired behaviour the car needs to learn.

	Policy/model: our objective, what we need learn as part of RL. This is the latest set of rules on what to do at a given camera image.

	Iterations: RL training sessions (multiple episodes and timesteps) when a policy/model is saved. So the policy is changed throughout one iteration
				but then saved in a new file at the end of iteration. This allows to test all models later at different stages of training  
'''

from stable_baselines3 import PPO #PPO
import os
from environment import CarEnv
import time


print('This is the start of training script')

print('setting folders for logs and models')
training_name = "with_shufflenet_1_0x_ft_ex_-1"

workspace_root = os.environ["SELF_DRIVE_CARLA_WORKSPACE"]
project_workspace = os.path.join(workspace_root, "02-rl-steering", training_name)
models_root_dir = os.path.join(project_workspace, "models")
models_dir = os.path.join(project_workspace, f"models/{int(time.time())}/")
logdir = os.path.join(project_workspace,f"logs/{int(time.time())}/")

if not os.path.exists(models_dir):
	os.makedirs(models_dir)

if not os.path.exists(logdir):
	os.makedirs(logdir)

print('connecting to env..')

env = CarEnv()

env.reset()
print('Env has been reset as part of launch')

# Load the latest model if it exists
model_files = [os.path.join(dirpath, file) for dirpath, dirnames, files in os.walk(models_root_dir) for file in files]
model_files.sort(key=lambda x: os.path.getmtime(os.path.join(models_root_dir, x)), reverse=True)

if model_files:
    print(f"Loading model from {model_files[0]}")
    model = PPO.load(os.path.join(models_dir, model_files[0]), env=env)
    model.tensorboard_log = logdir
else:
    print("No previous model found, starting from scratch")
    model = PPO('MlpPolicy', env, verbose=1,learning_rate=0.001, tensorboard_log=logdir)


TIMESTEPS = 400 # how long is each training iteration - individual steps
iters = 0
while iters<400:  # how many training iterations you want
	iters += 1
	print('Iteration ', iters,' is to commence...')
	model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=f"PPO" )
	print('Iteration ', iters,' has been trained')
	model.save(f"{models_dir}/{TIMESTEPS*iters}")
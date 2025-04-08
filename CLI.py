'''
Author : Zhongke Sun
Date : 2023/10/12

ATTENTION: If you need to run this entire project, please replace all 'shiyumao' with your Docker account username, otherwise you will get an error when build/push your container and image.
ATTENTION: Otherwise, if you just want to run our model, you can just 'pull' my Docker image from Docker Hub and run it. (I have already pushed my Docker image to Docker Hub)
'''



import argparse
import os

# This function is to build the Docker image
def build_image():
    os.system("docker build -t ml_iris_model .")

# This function is to run the Docker container
def run_container():
    os.system("docker run ml_iris_model")
    
# This function is to push my Docker image to Docker Hub
def push_image():
    os.system("docker login")
    # You have to replace 'shiyumao' with your Docker Hub username
    os.system("docker tag ml_iris_model shiyumao/ml_iris_model")
    os.system("docker push shiyumao/ml_iris_model")

# This function is to pull my Docker image from Docker Hub
def pull_image():
    os.system("docker pull shiyumao/ml_iris_model")

# This function is to run my Docker image, my iris machine learning model
def run_model():
    os.system("docker run shiyumao/ml_iris_model")
    
# This function is to stop my Docker container
def stop_container():
    os.system("docker stop $(docker ps -q --filter ancestor=shiyumao/ml_iris_model)")
    
# This function is to delete my Docker container
def delete_container():
    os.system("docker rm $(docker ps -aq --filter ancestor=shiyumao/ml_iris_model)")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MLOPS CLI for Docker")
    parser.add_argument('command', choices=['build', 'run_container', 'push', 'pull', 'run_model', 'stop', 'delete'], help="Command to execute: 'build', 'run_container', 'push', 'pull', 'run_model', 'stop', 'delete'")
    
    args = parser.parse_args()
    
    if args.command == 'build':
        build_image()
    elif args.command == 'run_container':
        run_container()
    elif args.command == 'push':
        push_image()
    elif args.command == 'pull':
        pull_image()
    elif args.command == 'run_model':
        run_model()
    elif args.command == 'stop':
        stop_container()
    elif args.command == 'delete':
        delete_container()
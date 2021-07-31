#sudo docker run -d -v $(pwd)/pymesh_examples:/pymesh_examples -it --rm pymesh/pymesh bash -c 'python /pymesh_examples/pymesh_example_04.py '$1 | tee docker_id.txt
sudo docker run -v $(pwd)/pymesh_examples:/pymesh_examples -it --rm pymesh/pymesh bash -c 'python /pymesh_examples/pymesh_example_04.py '$1 | tee log.txt
#sudo docker stop $(cat docker_id.txt)
#sudo docker rm $(cat docker_id.txt)

sudo docker run -d -v $(pwd)/pymesh_examples:/pymesh_examples -it pymesh/pymesh python /pymesh_examples/pymesh_example_01.py | tee docker_id.txt
sudo docker stop $(cat docker_id.txt)
sudo docker rm $(cat docker_id.txt)

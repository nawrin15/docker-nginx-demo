sudo docker build -t webserver .
sudo docker run -it 
sudo docker run -it --rm -d -p 8001:80 --name web webserver
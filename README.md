# cicdassignment

# Jenkins Installation Steps

#Prerequisites
# A Linux based os from AWS ec2 should be created 
![image](https://github.com/Akhilbmsb/cicdassignment/assets/54345937/5f6996c3-79c7-47dd-992b-d65625fdcaa4)
# After Launching open 8080 port
![image](https://github.com/Akhilbmsb/cicdassignment/assets/54345937/e6c8cf56-9cd1-4218-8444-b30f89e3f200)
# After that ssh into the server by connecting and run the follwing commands,which includes the updating server,installing JDK and installation of Jenkins

# sudo apt-get -y update 
# sudo apt-get -y upgrade 
# sudo apt install -y openjdk-11-jdk 
# java -version
# wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | apt-key add -
# sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ >  /etc/apt/sources.list.d/jenkins.list'
# sudo apt-get -y update 
# sudo wget -O /usr/share/keyrings/jenkins-keyring.asc   https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
# echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]   https://pkg.jenkins.io/debian-stable binary/ | sudo tee   /etc/apt/sources.list.d/jenkins.list > /dev/null
# sudo apt-get update
# sudo apt install -y jenkins 
# sudo apt update
# sudo systemctl status Jenkins
# sudo apt install -y python3-pip
# sudo pip install streamlit

# open browser and naviogate to the 
http://<instanceIPaddress>:8080

# To retrieve Admin password run the following command

cat /var/lib/jenkins/secrets/initialAdminPassword

![image](https://github.com/Akhilbmsb/cicdassignment/assets/54345937/b20be95f-a7eb-4466-a9bb-568f34aa6f7d)

Now you can Access the Jenkins and build the Automation framework setup by logging in to it

# Screenshots of github Actions
![Screenshot (2472)](https://github.com/Akhilbmsb/cicdassignment/assets/54345937/86473b03-d0be-43b9-9ac2-db4bb8574a20)
![Screenshot (2471)](https://github.com/Akhilbmsb/cicdassignment/assets/54345937/c527e9b7-4668-469c-a95c-43a711bf4237)
![Screenshot (2470)](https://github.com/Akhilbmsb/cicdassignment/assets/54345937/5661f4e7-7d3a-4b91-ac2d-1f45195371b4)
![Screenshot (2469)](https://github.com/Akhilbmsb/cicdassignment/assets/54345937/9d3d9d12-1d87-43c4-9368-022a1d65f903)
![Screenshot (2468)](https://github.com/Akhilbmsb/cicdassignment/assets/54345937/41d4e4ac-8d90-4c9a-a857-dce7ea88ba95)
![Screenshot (2467)](https://github.com/Akhilbmsb/cicdassignment/assets/54345937/2af12cca-9279-4a01-84c1-a1e10564bfb7)
![Screenshot (2466)](https://github.com/Akhilbmsb/cicdassignment/assets/54345937/f7b01e88-5afd-4111-963d-909412579c18)






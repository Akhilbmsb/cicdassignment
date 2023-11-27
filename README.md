# cicdassignment

# Jenkins Installation Steps

#Prerequisites
# A Linux based os from AWS ec2 should be created 
![image](https://github.com/Akhilbmsb/cicdassignment/assets/54345937/5f6996c3-79c7-47dd-992b-d65625fdcaa4)
# After Launching open 8080 port
![image](https://github.com/Akhilbmsb/cicdassignment/assets/54345937/e6c8cf56-9cd1-4218-8444-b30f89e3f200)
# After that ssh into the server by connecting and run the follwing commands,which includes the updating server,installing JDK and installation of Jenkins

sudo apt-get -y update 
sudo apt-get -y upgrade 
sudo apt install -y openjdk-11-jdk 
java -version
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ >  /etc/apt/sources.list.d/jenkins.list'
sudo apt-get -y update 
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc   https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]   https://pkg.jenkins.io/debian-stable binary/ | sudo tee   /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt install -y jenkins 
sudo apt update
sudo systemctl status Jenkins
sudo apt install -y python3-pip
sudo pip install streamlit

# open browser and naviogate to the 
http://<instanceIPaddress>:8080

# To retrieve Admin password run the following command

cat /var/lib/jenkins/secrets/initialAdminPassword

![image](https://github.com/Akhilbmsb/cicdassignment/assets/54345937/b20be95f-a7eb-4466-a9bb-568f34aa6f7d)

Now you can Access the Jenkins and build the Automation framework setup by logging in to it



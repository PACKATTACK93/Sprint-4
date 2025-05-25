# Creating car sales Ads with some visualization using the streamlit service with the following modlues, pandas, plotly, altair and matplotlib. The App will Deployed by using the Render web app service.

## Setup Instructions
 1.) Clone the local GitHub Repository:
https://github.com/PACKATTACK93/Sprint-4.git

 2.) You will need to register and Create a Streamlit user profile as well as a Render account, This can be accomplished via email and or you're local GitHub account assuming you already have one. 
 Once you're signed into streamlit Click on "Create App" and it will guide you from there.  Here are the URL's if you unfamilar. and some get started info. (posted below)
https://render.com/platform
https://docs.streamlit.io/get-started
https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github
 
 3.) Make sure the streamlit configuration matches in your local configuration yaml file via port service.The streamlit default for the server port is usually (10000) with the server address of (0.0.0.0)
Once you name your app.py file (under settings) on the secrets tab option you can insert the port keys via (SECRETS) which is where you'll insert the yaml file as discussed above.

4.) Please doublecheck to make sure: if the service does not allow you to run it it then it wont deploy. (IMPORTANT) check you're local firewall settings and or setup a port foward service to allow it to run properly.

** IF IT STILL DOES NOT ALLOW YOU TO RUN IT LOCALLY OR VIA THE STREAMLIT SERVICE YOU MAY HAVE TO DISABLE THE FIREWALL ENTIRELY.** (WARNING)** ONLY DO IT TEMPORARILY TO SEE IF IT FIXES THE ISSUE.(NOT RECOMMENDED!) (documentation below)
https://docs.streamlit.io/knowledge-base/deploy/remote-start
https://discuss.streamlit.io/t/permission-denied-in-ec2-port-80/798/3
https://discuss.streamlit.io/t/how-to-use-streamlit-with-nginx/378/7
https://github.com/streamlit/streamlit/issues/443
https://support.microsoft.com/en-us/windows/firewall-and-network-protection-in-the-windows-security-app-ec0844f7-aebd-0583-67fe-601ecf5d774f
https://cloudzy.com/blog/disable-firewall-using-group-policy/

5.) In you're Render Dashboard the app.py should be named what you created it to be in your Git Repo in my case Car_Sales_app.py, and under the build and deploy section, the repository should also match you're main local repository. 
example: Github.com/MYREPOSITORY/123 etc. Set the branch that you're deploying from. Typically the "Main branch"

6.) Under you're dashboard there will be a setting called the (BUILD Command) which will be simular to the requirements file that you created previously in VS. it should look something like. $ pip install streamlit & pip install -r requirements.txt

7.) Make sure to setup and create the requirements.txt with the following dependency/packages this will be required to run the app successfully:
https://python.land/virtual-environments/installing-packages-with-pip#Pip_install_requirementstxt_file

8.) Launch the bash terminal via command prompt shell: Then insert the (package) 
that you're installing below via the pip install command: $ ~ pip install scipy etc.
https://python.land/virtual-environments/installing-packages-with-pip
https://packaging.python.org/en/latest/tutorials/managing-dependencies/
scipy == 1.11.4
numpy == 1.23.5
seaborn == 0.12.2
pandas==2.0.3
streamlit==1.25.0
altair==5.0.1
plotly==5.15.0
plotly-express==0.4.1
pyarrow==12.0.1
matplotlib == 3.10.0

 9.) You will need to create a juypter notebook which can be achieved in VS code with an extension and or through the conda enviroment locally. See (documentation below:)
https://github.com/jupyter/notebook
https://jupyter-notebook.readthedocs.io/en/stable/
https://code.visualstudio.com/docs/datascience/jupyter-notebooks

 10.) In VS/Jupyter import you're python libraries include you're local csv file. pd=read.csv(') etc optionally you can visualize it first by using a live playground to see what it will look like before you pull or push it to you're main repository. 
https://jupyter.org/try-jupyter/notebooks/?path=notebooks/Intro.ipynb

Here is my Personal streamlit profile:
https://share.streamlit.io/user/packattack93
https://car-dataset.onrender.com/
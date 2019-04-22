# Reddit-Mood-Analyzer
<h2> How to install </h2>

<ol>
  <li> git clone git@github.com:CamWeston/Reddit-Mood-Analyzer.git </li>
  <li> cd Reddit-Mood-Analyzer </li>
  <li> Make sure you are running on at least python 3.4 upgrade if not </li>
  <li> now activate your virtual environment: </li>
  <li> python3 -m venv venv </li>
  <li> . venv/bin/activate </li> 
  <li> now while in the venv install your dependencies </li>
  <li> pip install flask </li> 
  <li> pip install praw </li>
  <li> pip install --upgrade "watson-developer-cloud>=2.8.0" </li>
  <li> pip install --upgrade IPython </li>
  <li> pip install requests </li>
  <li> if you are getting an error from pip saying "Could not find any downloads that satisfy the requirement your package   No distributions at all found for your package" do the following: </li>
  <ol>
    <li> pip uninstall pip </li>
    <li> curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py </li>
    <li> python get-pip.py </li>
    <li> now you can do all your pip installs </li>
  </ol>
  <li> we now have to init the database </li> 
  <li> flask init-db </li>
  <li> now you can run your program: </li>
  <li> export FLASK_APP=RMA_APP </li>
  <li> export FLASK_ENVIRONMENT=dev  </li>
  <li> flask run </li>
 </ol>

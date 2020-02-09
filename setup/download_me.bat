REM clone the repo
git clone https://github.com/kevindiclemente/did-i-beat-becklyin did-i-beat-becklyin
cd did-i-beat-becklyin

REM run the setup script
call setup\env_setup.bat

REM Run whatever script is passed in as an argument 
py -3 %1
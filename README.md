[![Python 3.7](https://img.shields.io/badge/Python->=3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![SWI-Prolog](https://img.shields.io/badge/Prolog-SWIProlog-red.svg)](https://www.swi-prolog.org/Download.html)
[![Unity](https://img.shields.io/badge/Unity-2019.4.15f1-green.svg)](https://unity.com/)

# German shepherd simulation with Unity using Prolog
Project for exam Intelligent Systems and Robotics Lab.

In this project we have created a Unity scene that simulating a german sheperd catching the sheeps. The dog logic was created in Prolog using pyswip library in Python, that read a .pl file.
In Python we do some heuristic logic based on choices that coming from Prolog computation and then we try to choose the best.
In Unity we just send the perception of the world based on sensors, created by the colliders as a triggers, and execute the action coming from Python.

Thanks to Youssef Elashry for the Two-way communication between Python 3 and Unity (C#) that we used to send message from Unity to Python and viceversa.
You can find his project at this link: <br>
https://github.com/Siliconifier/Python-Unity-Socket-Communication

<h1>Dependencies</h1>

Install Swi-Prolog, you can find at this link: <br>
https://www.swi-prolog.org/Download.html

I used Swi-Prolog with 64 bit architecture version, but if you have Python 32 bit, you have to install Swi-Prolog 32 bit.

Then configure your python enviroment with the file \__main__.py as main script for running in your IDE.

After you need to install pyswip, use the command:

```markdown
pip3 install pyswip
```
<h1>Starting the simulation</h1>

For launch the simulation, keep open Unity ad Python project (I used pycharm, but i have tried on vs code and works fine on there too), then start the main.py
After start on Unity clicking play on editor. Is very important to start always **FIRST** Python and **AFTER** Unity. The simulation start when both program are running.

![alt text](https://github.com/LorisNanni91/ProgettoRobotica/blob/master/python.gif?raw=true)
![alt text](https://github.com/LorisNanni91/ProgettoRobotica/blob/master/unity.gif?raw=true)

# LoL-Winrate-Analysis
Analyze the winrate of players as a function of division.
# abstract
This program was made in an attempt to prove that players with high win rates are paired with players with  
low win rates in order to balance out games. This hypothesis could be proven correct if a players team members  
win rates decrease as a players personal win rate increases. The results show that a players team mates win rate  
increase as their win rate increases, disproving the hypothesis.
# technical details
lol_wr_analysis.py crawls through players profile pages on op.gg and gathers information about their win rates, and their team mates win rates.  
That information is saved as a dictionary in a pickle file. Those pickle files are read in by lol_wr_plots.py.  
Plots are made of a players win rate vs. their team mates win rates. A line is plotted using linear regression to represent the average trend.
# Plots
![python_J3lVR3DZem](https://user-images.githubusercontent.com/23323883/129270028-0ac90383-1226-4490-8f25-2f2683820783.png)
![python_UNvnHiswqr](https://user-images.githubusercontent.com/23323883/129270038-1f065102-ef6b-4420-b8be-69f4771e92df.png)
![python_Z928RGKOaO](https://user-images.githubusercontent.com/23323883/129270048-55fc00ed-ebf4-4f5c-9684-9c90dfd6223f.png)
![python_Y6HGGz6xfo](https://user-images.githubusercontent.com/23323883/129270074-b8a95a6d-8958-4484-aa90-531547dc258d.png)
![python_DORBYPTUZj](https://user-images.githubusercontent.com/23323883/129270078-f5cd3a4b-f9c5-4442-8360-894437126394.png)
![python_e9PA7UezKx](https://user-images.githubusercontent.com/23323883/129270081-0573d690-9189-4b8a-9002-b3f13d9ceae5.png)
![python_2I91ssSacB](https://user-images.githubusercontent.com/23323883/129270082-c076814b-5ec7-482b-b17f-c3585252d1a7.png)
![python_T5S9x39u4j](https://user-images.githubusercontent.com/23323883/129270084-13bc6063-8081-4c44-823b-cfb4700c3cd3.png)

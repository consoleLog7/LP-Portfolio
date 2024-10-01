tmux new-session -d -s Logan-Portfolio
tmux send-keys -t Logan-Portfolio 'cd /home/ec2-user/LP-Portfolio' C-m
tmux send-keys -t Logan-Portfolio 'python -m streamlit run main.py' C-m
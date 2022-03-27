FROM ubuntu 
RUN apt update 
RUN apt install python3 -y
RUN apt install ncat -y 
RUN apt install netcat -y


WORKDIR home/
COPY python_shell_level_5.py .
COPY run_ncat_level5.sh .
COPY here_is_maybe_a_flag .

RUN chmod +x run_ncat_level5.sh 
RUN chmod +x python_shell_level_5.py 

CMD ./run_ncat_level5.sh

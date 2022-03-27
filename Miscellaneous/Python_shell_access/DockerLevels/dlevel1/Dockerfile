FROM ubuntu 
RUN apt update 
RUN apt install python3 -y
RUN apt install ncat -y 
RUN apt install netcat -y


WORKDIR home/
COPY python_shell_level_1.py .
COPY run_ncat_level1.sh .
RUN chmod +x run_ncat_level1.sh 
RUN chmod +x python_shell_level_1.py 

CMD ./run_ncat_level1.sh
FROM ubuntu 
RUN apt update 
RUN apt install python3 -y
RUN apt install ncat -y 
RUN apt install netcat -y
RUN apt install net-tools -y



WORKDIR home/
COPY no_response.py .
COPY run_ncat_no_response.sh . 
COPY genericflagnamefile.txt .
RUN chmod +x run_ncat_no_response.sh
RUN chmod +x no_response.py
CMD ./run_ncat_no_response.sh

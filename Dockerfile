FROM hypriot/rpi-python

COPY myServer.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

VOLUME [ "/opt/vc/lib" , "/etc/ld.so.conf.d" ]
COPY files/lib /opt/vc/lib
COPY files/conf /etc/ld.so.conf.d

RUN ldconfig

EXPOSE 8082

CMD [ "python", "./myServer.py" ]

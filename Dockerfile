# Using Python Slim-Buster
FROM xluxz/geezproject:buster
# RAM-UBOT
# Geez-UserBot
#yaudah iya

RUN git clone -b JOO-USERBOT https://github.com/jookalem/SANJO-USERBOT /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/jookalem/SANJO-USERBOT/JOO-USERBOT/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]

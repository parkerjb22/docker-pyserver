```
chmod u+x dockerinstall.sh
./dockerinstall.sh
docker build -t pyserver .
docker run -d -p 8082:8082 --name pysever --privileged pyserver
```

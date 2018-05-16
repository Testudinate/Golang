1/ sudo service mongod start

2/ mongo --host 127.0.0.1:27017

3/ scp -v *@*:/storage/backup/mongo/dump_2018_05_15/dump/*.tar /home/*/

4/ tar -xf ***.tar.gz

5/ $ mongorestore -d *** /home/***/storage/backup/mongo/dump_2018_05_15/dump/***/

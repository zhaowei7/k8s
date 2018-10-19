# cat /opt/init_public.sh 
#!/bin/bash
cat /dev/null > /tmp/${4}jenkins
echo name:$1 > /tmp/${4}jenkins
echo version:$2 >> /tmp/${4}jenkins
echo replicas_num:$3 >> /tmp/${4}jenkins
echo namespace:$4 >> /tmp/${4}jenkins

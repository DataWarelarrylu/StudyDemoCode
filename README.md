# StudyDemoCode

docker build -t mysql .
docker images |grep mysql
docker run -p 3306:3306 --name mymysql -v $PWD/conf:/etc/mysql/conf.d -v $PWD/logs:/logs -v $PWD/data:/mysql_data -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.6
安装完成
docker run -it mysql:5.6  /bin/bash   新建一个container

docker exec -it e09e37b39016  /bin/bash  进入mysql的docker
/etc/init.d/mysql start

--wordpress
docker run --name some-wordpress --link some-mysql:mysql -p 8080:80 -d wordpress

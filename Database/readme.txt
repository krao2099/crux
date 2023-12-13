docker run --name pgsql-dev -e POSTGRES_PASSWORD=test1234 -p 5432:5432 -v ./init_scripts:/docker-entrypoint-initdb.d postgres

docker run --name pgsql-dev -e POSTGRES_PASSWORD=test1234 -p 5432:5432 -v ./init_scripts:/docker-entrypoint-initdb.d -v ${PWD}/postgres-docker:/var/lib/postgresql/data postgres



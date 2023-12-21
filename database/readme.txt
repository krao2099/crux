WINDOWS:
docker run --name pgsql-dev --rm -e POSTGRES_PASSWORD=test1234 -e POSTGRES_DB=crux_db -p 5432:5432 -v .\init_scripts:/docker-entrypoint-initdb.d postgres

docker run --name pgsql-dev -e POSTGRES_PASSWORD=test1234 -e POSTGRES_DB=crux_db -p 5432:5432 -v .\init_scripts:/docker-entrypoint-initdb.d -v ${PWD}/postgres-docker:/var/lib/postgresql/data postgres


LINUX:
docker run --name pgsql-dev --rm -e POSTGRES_PASSWORD=test1234 -e POSTGRES_DB=crux_db -p 5432:5432 -v ./init_scripts:/docker-entrypoint-initdb.d postgres

docker run --name pgsql-dev -e POSTGRES_PASSWORD=test1234 -e POSTGRES_DB=crux_db -p 5432:5432 -v ./init_scripts:/docker-entrypoint-initdb.d -v ${PWD}/postgres-docker:/var/lib/postgresql/data postgres


docker exec -it pgsql-dev bash

psql -h localhost -U postgres

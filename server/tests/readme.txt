curl -c cookies.txt -X POST -H "Content-Type: application/json; charset=utf-8" -d @sample_user.json "http://127.0.0.1:5000/user"
curl -b cookies.txt -X POST -H "Content-Type: application/json; charset=utf-8" -d @sample_user.json "http://127.0.0.1:5000/login"
curl -C cookies.txt -X POST -H "Content-Type: application/json; charset=utf-8" -d @sample_user.json "http://127.0.0.1:5000/login"

curl -X GET "http://127.0.0.1:5000/test"
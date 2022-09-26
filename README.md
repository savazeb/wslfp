# PORTPROXY FOR WSL2
When this app under development assigning static ip for wsl2 wasn't possible. This app will help this shortage by utilizing netsh, forwarding selected port from wsl to windows machine.

## Listed PORT
| NAME                      | PORT |
| ------------------------- | ---- |
| SSH                       | 22   |
| HTTP                      | 80   |
| HTTPS                     | 443  |
| MQTT                      | 1883 |
| CRA                       | 3000 |
| MYSQL                     | 3306 |
| PostgreSQL                | 5432 |
| HTTP Development Server   | 8000 |
| Alternative port for HTTP | 8080 |
| InfluxDB                  | 8086 |
| MQTTS                     | 8883 |

For adding new port go to `$HOME/wslfp/wslfp.db` location and add the new port into `port` table.

## Instalation
**prerequisite** bash shell and python installed

1. clone this repository
2. from `bash` run `setup.sh` to install the app

## Usage
to run installed app, execute `wslfp` from `bash`

## License
[MIT](https://choosealicense.com/licenses/mit/)

Copyright ? Sava Zeb, 2022

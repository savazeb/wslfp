pip install -r requirements.txt

pyinstaller --onefile python/main.py -n wslfp

mkdir /usr/lib/wslfp
mkdir $HOME/wslfp

cp ./dist/wslfp /usr/lib/wslfp
cp ./python/database/wslfp.db $HOME/wslfp

if ! which wslfp > /dev/null; then 
    echo 'export PATH="/usr/lib/wslfp:$PATH"' >> ~/.bashrc
    source ~/.bashrc
fi

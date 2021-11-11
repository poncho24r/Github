GNU nano 5.4                                                                                                    checkmail.bash *                                                                                                           

if (( "$#" == 0 ))      #<1>
then
        printf 'Enter API KEY: ''\n '
        read -s apik

        printf 'Enter email address: '
        read emailin

else
        apik="$1" 
        emailin="$2"
fi

pwned=$(curl -s 'https://haveibeenpwned.com/api/v3/breachedaccount/'$emailin''  -H 'hibp-api-key: '$apik ) #<2>

if [ "$pwned" == "" ]
then
        exit 1
else
        echo 'Account pwned in the following breaches:'
        echo "$pwned" | grep -Po '"Name":".*?"' | cut -d':' -f2 | tr -d '\"'    #<3>
        exit 0
fi
